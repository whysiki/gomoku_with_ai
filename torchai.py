import torch
import numpy as np
from torchrl.data.tensor_specs import (
    Categorical,
    Composite,
    Unbounded,
    Binary,
)
from gomoku_rl.policy import Policy
from omegaconf import DictConfig
from torchrl.data.tensor_specs import TensorSpec
from tensordict import TensorDict
from typing import Dict


class TorchGomokuAI:
    def __init__(self, cfg: Dict = None):
        self.cfg = (
            DictConfig(cfg)
            if cfg is not None
            else DictConfig(
                {
                    "algo": {
                        "name": "ppo",
                        "ppo_epochs": 3,
                        "clip_param": 0.2,
                        "entropy_coef": 0.01,
                        "gae_lambda": 0.95,
                        "gamma": 0.99,
                        "max_grad_norm": 0.5,
                        "batch_size": 4096,
                        "normalize_advantage": True,
                        "average_gae": False,
                        "share_network": True,
                        "optimizer": {"name": "adam", "kwargs": {"lr": 0.0001}},
                        "num_channels": 64,
                        "num_residual_blocks": 4,
                    },
                    "board_size": 15,
                    "checkpoint": "model/0.pt",
                    "device": "cpu",
                    "human_black": True,
                    "grid_size": 56,
                    "piece_radius": 24,
                }
            )
        )
        self.board_size = self.cfg.board_size
        self.device = self.cfg.device
        self.model = self._make_model(self.cfg)
        self.model_ckpt_path = self.cfg.checkpoint
        self.model.load_state_dict(
            torch.load(
                self.model_ckpt_path, map_location=self.cfg.device, weights_only=True
            )
        )
        self.model.eval()

    def _make_model(self, cfg: DictConfig) -> Policy:
        def get_policy(
            name: str,
            cfg: DictConfig,
            action_spec: Categorical,
            observation_spec: TensorSpec,
            device="cuda",
        ) -> Policy:
            cls = Policy.REGISTRY[name.lower()]
            return cls(
                cfg=cfg,
                action_spec=action_spec,
                observation_spec=observation_spec,
                device=device,
            )

        action_spec = Categorical(
            self.board_size * self.board_size,
            shape=[1],
            device=self.device,
        )
        observation_spec = Composite(
            {
                "observation": Unbounded(
                    device=self.device,
                    shape=[2, 3, self.board_size, self.board_size],
                ),
                "action_mask": Binary(
                    n=self.board_size * self.board_size,
                    device=self.device,
                    shape=[2, self.board_size * self.board_size],
                    dtype=torch.bool,
                ),
            },
            shape=[2],
            device=self.device,
        )
        model = get_policy(
            name="ppo",
            cfg=cfg.algo,
            action_spec=action_spec,
            observation_spec=observation_spec,
            device=self.device,
        )
        return model

    def _generate_observation_and_action_mask(
        self, board_state: np.ndarray, turn: int
    ) -> tuple[torch.Tensor, torch.Tensor]:
        board_size = board_state.shape[0]
        device = torch.device("cpu")
        board = torch.tensor(board_state, dtype=torch.long, device=device).unsqueeze(0)
        action_mask = (board == 0).flatten(start_dim=1)
        piece = (
            torch.tensor(1 if turn == 0 else -1, device=device)
            .unsqueeze(0)
            .unsqueeze(-1)
            .unsqueeze(-1)
        )
        layer1 = (board == piece).float()
        layer2 = (board == -piece).float()
        layer3 = torch.zeros((1, board_size, board_size), device=device)
        observation = torch.stack([layer1, layer2, layer3], dim=1)
        return observation, action_mask

    def get_best_action(self, board_state: np.ndarray, play_value: int = -1) -> tuple:
        turn = 0 if play_value == 1 else -1
        observation, action_mask = self._generate_observation_and_action_mask(
            board_state, turn
        )
        tensordict = TensorDict(
            {
                "observation": observation,
                "action_mask": action_mask,
            },
            batch_size=1,
        )
        with torch.no_grad():
            tensordict = self.model(tensordict).cpu()
        action: int = tensordict["action"].item()
        x = action // self.board_size
        y = action % self.board_size
        return x, y

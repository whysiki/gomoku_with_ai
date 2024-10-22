import numpy as np
import gymnasium as gym
from gymnasium import spaces
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.logger import configure


class GomokuEnv(gym.Env):
    def __init__(self, board_size=15):
        super(GomokuEnv, self).__init__()
        self.board_size = board_size
        self.action_space = spaces.Discrete(board_size * board_size)
        self.observation_space = spaces.Box(
            low=-1, high=1, shape=(board_size, board_size), dtype=np.int8
        )
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.status_matrix = np.zeros((self.board_size, self.board_size), dtype=np.int8)
        return self.status_matrix, {}

    def step(self, action):
        x, y = divmod(action, self.board_size)
        if self.status_matrix[y][x] != 0:
            return self.status_matrix, -1, True, False, {}  # Invalid move

        self.status_matrix[y][x] = 1  # AI always plays as black
        reward = self.get_reward(x, y)
        done = reward != 0 or np.all(self.status_matrix != 0)
        return self.status_matrix, reward, done, False, {}

    def get_reward(self, x, y):
        if self.check_win(x, y):
            return 1
        return 0

    def check_win(self, x, y):
        # Simplified win check logic
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                nx, ny = x + i * dx, y + i * dy
                if (
                    0 <= nx < self.board_size
                    and 0 <= ny < self.board_size
                    and self.status_matrix[ny][nx] == 1
                ):
                    count += 1
                else:
                    break
            for i in range(1, 5):
                nx, ny = x - i * dx, y - i * dy
                if (
                    0 <= nx < self.board_size
                    and 0 <= ny < self.board_size
                    and self.status_matrix[ny][nx] == 1
                ):
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False


# 创建环境
env = GomokuEnv()

# 检查环境是否符合Gymnasium的要求
check_env(env)

# 配置Tensorboard日志记录器
log_dir = "./log/"
new_logger = configure(log_dir, ["stdout"])

# 创建模型
model = PPO("MlpPolicy", env, verbose=1)
model.set_logger(new_logger)

# 创建回调以保存检查点
checkpoint_callback = CheckpointCallback(
    save_freq=1000, save_path="./models/", name_prefix="gomoku_model"
)

# 训练模型
model.learn(total_timesteps=10000, callback=checkpoint_callback)

# 保存模型
model.save("gomoku_ppo_model")

# 加载模型
model = PPO.load("gomoku_ppo_model")

# 测试模型
obs, _ = env.reset()
for _ in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info, _ = env.step(action)
    if dones:
        obs, _ = env.reset()

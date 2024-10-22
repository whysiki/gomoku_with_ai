from dataclasses import dataclass
import random
from ai_actions import BaseGomokuAI
import numpy as np


@dataclass
class PlayerColor:
    BLACK = "black"
    WHITE = "white"
    COLOR_NUM_DICT = {"black": -1, "white": 1}


@dataclass
class PlayerType:
    AI = "ai"
    HUMAN = "human"


@dataclass
class Player:
    name: str
    color: str
    type: str

    def __init__(self, name: str, color: str, type: str):
        if color.strip() not in (PlayerColor.BLACK, PlayerColor.WHITE):
            raise ValueError("Invalid color: {}, must be black or white".format(color))
        self.name = name
        self.color = color
        if type.strip() not in (PlayerType.AI, PlayerType.HUMAN):
            raise ValueError("Invalid type: {}, must be ai or human".format(type))
        self.type = type

    def test_ai_get_action(self, status_matrix: np.ndarray) -> tuple[int, int]:
        # default ai color is black
        color = self.color
        value = PlayerColor.COLOR_NUM_DICT[color]
        # if self.type == PlayerType.AI:
        #     return random.choice(np.argwhere(status_matrix == 0))
        baseai = BaseGomokuAI(color)
        return baseai.get_best_action(status_matrix)
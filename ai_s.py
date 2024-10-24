import numpy as np
import random
from tools import (
    create_pattern_dict,
    evaluate_board,
    is_gameover,
    get_near_actions,
)
import sys
from loguru import logger
from rich import print
import diskcache as dc

sys.setrecursionlimit(1500)
# 创建缓存实例
cache = dc.Cache("./cache")


class AlphaBetaGomokuAI:
    def __init__(self, aivalue: int, depth=3):
        self.value = aivalue
        self.enemy_value = -self.value
        self.depth = depth
        self.patternDict = create_pattern_dict(self.value)
        self.move_history = []
        self.base_move = None
        self.cache = {}  # Add a cache dictionary
        logger.info("Current AI: AlphaBetaGomokuAI")

    def board_to_tuple(self, board: np.ndarray) -> tuple:
        return tuple(map(tuple, board))

    def alphabeta(
        self,
        board_state: np.ndarray,
        depth: int,
        alpha: int,
        beta: int,
        is_max_player: bool,
    ):
        board_tuple = self.board_to_tuple(board_state)
        if board_tuple in self.cache:
            return self.cache[board_tuple]

        if depth == 0 or is_gameover(board_state):
            eval_ = evaluate_board(board_state, self.patternDict)
            self.cache[board_tuple] = eval_
            return eval_

        if is_max_player:
            max_val = -np.inf
            for action in get_near_actions(
                board_state, self.move_history[-1] if self.move_history else None
            ):
                if action in self.move_history:
                    continue
                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.value
                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, False)
                board_state[action[0]][action[1]] = temp
                if eval_ > max_val:
                    max_val = eval_
                    if depth == self.depth:
                        self.base_move = action
                alpha = max(alpha, max_val)
                if beta <= alpha:
                    break
            self.cache[board_tuple] = max_val
            return max_val
        else:
            min_val = np.inf
            for action in get_near_actions(
                board_state, self.move_history[-1] if self.move_history else None
            ):
                if action in self.move_history:
                    continue
                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.enemy_value
                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, True)
                board_state[action[0]][action[1]] = temp
                if eval_ < min_val:
                    min_val = eval_
                    if depth == self.depth:
                        self.base_move = action
                beta = min(beta, min_val)
                if beta <= alpha:
                    break
            self.cache[board_tuple] = min_val
            return min_val

    def get_best_action(self, board_state: np.ndarray):
        if is_gameover(board_state):
            logger.warning("Game over")
            return (-1, -1)
        self.base_move = None
        self.alphabeta(board_state, self.depth, -np.inf, np.inf, self.value == 1)
        best_action = self.base_move

        if best_action is None:
            logger.error("No best action found")
            random_position = random.choice(np.argwhere(board_state == 0))
            best_action = (np.int64(random_position[0]), np.int64(random_position[1]))

        if self.move_history:
            assert len(self.move_history) == len(
                set(self.move_history)
            ), "AI move error: duplicate move"
            assert best_action not in self.move_history, "AI move error: duplicate move"
        assert (
            board_state[best_action[0]][best_action[1]] == 0
        ), "AI move error: invalid move"
        self.move_history.append(best_action)
        logger.success(f"AI move: {best_action}")
        return best_action


if __name__ == "__main__":
    test_state = np.zeros((15, 15), dtype=int)
    # a = random.choice(np.argwhere(test_state == 0))
    # print(a)
    test_state[7, 7] = 1  # ai
    test_state[8, 8] = -1  # player
    test_state[9, 9] = 1  # ai
    test_state[10, 10] = -1  # player
    ai = AlphaBetaGomokuAI(1, depth=3)
    aimove = ai.get_best_action(test_state)
    test_state[aimove[0], aimove[1]] = 1  # ai
    print(aimove)

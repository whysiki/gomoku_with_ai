import numpy as np
import random
import numpy as np


class FoolishGomokuAI:
    def __init__(self, aivalue: int):
        self.value = aivalue
        self.enemy_value = -self.value
        self.pattern_scores = {
            (1, 0): 1,
            (2, 0): 10,
            (3, 0): 100,
            (4, 0): 1000,
            (5, 0): 10000,
            (0, 1): -1,
            (0, 2): -10,
            (0, 3): -100,
            (0, 4): -1000,
        }

    def evaluate_board(self, board: np.ndarray) -> int:
        score = 0
        for row in board:
            score += self._evaluate_line(row, self.value, self.enemy_value)
        for col in board.T:
            score += self._evaluate_line(col, self.value, self.enemy_value)
        score += self._evaluate_intersectLines(board, self.value, self.enemy_value)

        return score

    def _evaluate_intersectLines(
        self, board: np.ndarray, color_value: int, enemy_value: int
    ) -> int:
        score = 0
        for i in range(-10, 11):
            line = board.diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        for i in range(-10, 11):
            line = np.fliplr(board).diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        return score

    def _evaluate_line(
        self, line: np.ndarray, color_value: int, enemy_value: int
    ) -> int:
        score = 0
        max_len = len(line)
        for i in range(max_len):
            if line[i] == color_value:
                count = 1
                for j in range(i + 1, min(i + 5, max_len)):
                    if line[j] == color_value:
                        count += 1
                    else:
                        break
                score += self.pattern_scores.get((count, 0), 0)
        for i in range(max_len):
            if line[i] == enemy_value:
                count = 1
                for j in range(i + 1, min(i + 5, max_len)):
                    if line[j] == enemy_value:
                        count += 1
                    else:
                        break
                score += self.pattern_scores.get((0, count), 0)

        return score

    def get_best_action(self, board: np.ndarray) -> tuple[int, int]:
        best_score = -float("inf")
        best_move = None
        for x in range(board.shape[0]):
            for y in range(board.shape[1]):
                if board[y, x] == 0:
                    board[y, x] = self.value
                    score = self.evaluate_board(board)
                    board[y, x] = self.enemy_value
                    enemy_score = self.evaluate_board(board)
                    board[y, x] = 0
                    if enemy_score >= 1000:
                        return (x, y)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
        return best_move if best_move else random.choice(np.argwhere(board == 0))

import numpy as np
from game_object import PlayerColor


class BaseGomokuAI:
    def __init__(self, color: str):
        self.color = color
        self.enemy_color = (
            PlayerColor.WHITE if color == PlayerColor.BLACK else PlayerColor.BLACK
        )

    def evaluate_board(self, board: np.ndarray) -> int:
        color_value = PlayerColor.COLOR_NUM_DICT[self.color]
        enemy_value = PlayerColor.COLOR_NUM_DICT[self.enemy_color]
        score = 0
        # 遍历棋盘，简单计分
        for row in board:
            score += self._evaluate_line(row, color_value, enemy_value)
        for col in board.T:
            score += self._evaluate_line(col, color_value, enemy_value)
        score += self._evaluate_intersectLines(board, color_value, enemy_value)

        return score

    def _evaluate_intersectLines(
        self, board: np.ndarray, color_value: int, enemy_value: int
    ) -> int:
        score = 0
        # 从左上到右下
        for i in range(-10, 11):
            line = board.diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        # 从右上到左下
        for i in range(-10, 11):
            line = np.fliplr(board).diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        return score

    def _evaluate_line(
        self, line: np.ndarray, color_value: int, enemy_value: int
    ) -> int:
        score = 0
        return score

    def get_best_action(self, board: np.ndarray) -> tuple[int, int]:
        best_score = -float("inf")
        best_move = None
        for x in range(board.shape[0]):
            for y in range(board.shape[1]):
                if board[y, x] == 0:
                    board[y, x] = PlayerColor.COLOR_NUM_DICT[self.color]
                    score = self.evaluate_board(board)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
                    board[y, x] = 0
        return best_move


if __name__ == "__main__":
    test_status_matrix = np.zeros((15, 15), dtype=int)
    test_ai = BaseGomokuAI(PlayerColor.BLACK)
    print(test_ai.get_best_action(test_status_matrix))

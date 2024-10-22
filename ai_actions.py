import numpy as np

class FoolishGomokuAI:
    def __init__(self, color: str, PlayerColor):
        self.PlayerColor = PlayerColor
        self.color = color
        self.enemy_color = (
            PlayerColor.WHITE if color == PlayerColor.BLACK else PlayerColor.BLACK
        )
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
        color_value = self.PlayerColor.COLOR_NUM_DICT[self.color]
        enemy_value = self.PlayerColor.COLOR_NUM_DICT[self.enemy_color]
        score = 0
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
        for i in range(-10, 11):
            line = board.diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        for i in range(-10, 11):
            line = np.fliplr(board).diagonal(i)
            score += self._evaluate_line(line, color_value, enemy_value)
        return score

    def _evaluate_line(self, line: np.ndarray, color_value: int, enemy_value: int) -> int:
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
            elif line[i] == enemy_value: 
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
                    board[y, x] = self.PlayerColor.COLOR_NUM_DICT[self.color] 
                    score = self.evaluate_board(board)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
                    board[y, x] = 0 
        return best_move

if __name__ == "__main__":
    pass
    # from game_object import PlayerColor
    # test_status_matrix = np.zeros((15, 15), dtype=int)
    # test_ai = FoolishGomokuAI("black", PlayerColor)
    # print(test_ai.get_best_action(test_status_matrix))

import numpy as np
import random
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
                    board[y, x] = self.PlayerColor.COLOR_NUM_DICT[self.color]
                    score = self.evaluate_board(board)
                    board[y, x] = self.PlayerColor.COLOR_NUM_DICT[self.enemy_color]
                    enemy_score = self.evaluate_board(board)
                    board[y, x] = 0
                    if enemy_score >= 1000:
                        return (x, y)
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
        return best_move if best_move else random.choice(np.argwhere(board == 0))


# import os
# import requests
# import re
# from rich import print

# class WorkerAI:

#     def __init__(self, color: str, PlayerColor) -> None:
#         self.ACCOUNT_ID =
#         self.AUTH_TOKEN = 🤣

#         self.PlayerColor = PlayerColor
#         self.color = color
#         self.enemy_color = (
#             PlayerColor.WHITE if color == PlayerColor.BLACK else PlayerColor.BLACK
#         )
#         self.color_value = self.PlayerColor.COLOR_NUM_DICT[self.color]
#         self.enemy_value = self.PlayerColor.COLOR_NUM_DICT[self.enemy_color]

#     def get_best_action(self, board: np.ndarray) -> tuple[int, int]:
#         ACCOUNT_ID = self.ACCOUNT_ID
#         print(board.tolist())
#         prompt = f"Find the best move in this Gomoku board: {board.tolist()}, The value you represent is:{self.color_value},the enemy'value is {self.enemy_value}, and the zero is the empty place.You only have to answer with one tuple, like (1, 2), the first number is the x coordinate, the second number is the y coordinate.the indices start in 0. Don't tell me the updated board and other information, just give me a tuple."
#         response = requests.post(
#         # f"https://api.cloudflare.com/client/v4/accounts/{self.ACCOUNT_ID}/ai/run/@cf/deepseek-ai/deepseek-math-7b-instruct",
#         # f"https://api.cloudflare.com/client/v4/accounts/{self.ACCOUNT_ID}/ai/run/@cf/openchat/openchat-3.5-0106",
#         f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@hf/thebloke/llama-2-13b-chat-awq",
#             headers={"Authorization": f"Bearer {self.AUTH_TOKEN}"},
#             json={
#             "messages": [
#                 {"role": "system", "content": "You are playing Gomoku with DeepSeek AI. Please answer the following question to make your move."},
#                 {"role": "user", "content": prompt}
#             ]
#             },
#             proxies={"https": "http://127.0.0.1:62333", "http": "http://localhost:62333"}
#         )
#         result = response.json()
#         print(result)
#         if result["success"]:
#             # x, y = map(int, re.findall(r"\d+", result["result"]["response"]))
#             # print(x, y)
#             # 匹配第一个括号内的数字(int, int)
#             fs = re.findall(r"\d+", result["result"]["response"])
#             if len(fs) >= 2:
#                 x, y = int(fs[0]), int(fs[1])
#                 return (x, y) if self.check_answer_is_valid(board, x, y) else random.choice(np.argwhere(board == 0))
#             else:
#                 return random.choice(np.argwhere(board == 0))
#     def check_answer_is_valid(self, board: np.ndarray, x: int, y: int) -> bool:
#         return board[y, x] == 0 and 0 <= x < board.shape[1] and 0 <= y < board.shape[0]


# if __name__ == "__main__":
# # #     # pass
#     from game_object import PlayerColor
#     test_status_matrix = np.zeros((15, 15), dtype=int)
#     test_status_matrix[7, 7] = 1
#     test_status_matrix[7, 8] = -1
# #     # test_ai = FoolishGomokuAI("black", PlayerColor)
# #     # print(test_ai.get_best_action(test_status_matrix))
#     test_ai = WorkerAI("black", PlayerColor)
#     print(test_ai.get_best_action(test_status_matrix))

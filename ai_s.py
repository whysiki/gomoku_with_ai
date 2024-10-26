import numpy as np
import random
from tools import (
    create_pattern_dict,
    evaluate_board,
    is_gameover,
    get_near_actions,
    get_near_actions_with_noempty,
    get_near_actions_with_noempty_generator,
    is_gameover_with_state,
)
import sys
from loguru import logger
from rich import print
from functools import lru_cache
import hashlib

sys.setrecursionlimit(1500)


@lru_cache(maxsize=None)
def hash_tuple_md5(tup: tuple) -> str:
    hasher = hashlib.md5()
    hasher.update(str(tup).encode("utf-8"))
    return hasher.hexdigest()


class AlphaBetaGomokuAI:
    def __init__(self, aivalue: int, depth=2):
        self.value = aivalue
        self.enemy_value = -self.value
        self.maxvalue = max(self.value, self.enemy_value)
        self.minvalue = min(self.value, self.enemy_value)
        self.is_max_player = self.value > self.enemy_value
        self.depth = depth
        self.patternDict = create_pattern_dict()
        self.move_history = []
        self.enemy_history = []
        self.best_move = None
        self.cache = {}
        # self.last_board_state: np.ndarray = np.zeros((15, 15), dtype=int)  # 默认新局面
        logger.info("Current AI: AlphaBetaGomokuAI")

    @lru_cache(maxsize=None)
    def heuristic(self, board_state: tuple, action: tuple, is_max_player: bool) -> int:
        """模拟落子后的局势评估"""
        board_state_copy = np.array(board_state)  # 复制棋盘
        board_state_copy[action[0]][action[1]] = (
            self.maxvalue if is_max_player else self.minvalue
        )  # 落子
        return evaluate_board(board_state_copy, self.patternDict)

    def board_to_tuple(self, board: np.ndarray) -> tuple:
        return tuple(map(tuple, board))

    # def check_boradis_maxplayer_Win(self, board_state: np.ndarray) -> bool:
    # return is_gameover(self.board_to_tuple(board_state)) and self.is_max_player

    def alphabeta(
        self,
        board_state: np.ndarray,
        depth: int,
        alpha: int,
        beta: int,
        is_max_player: bool,
    ):
        board_tuple = self.board_to_tuple(board_state)  # 转换为元组
        hash_key = hash_tuple_md5(board_tuple)  # 计算哈希值
        if hash_key in self.cache and depth != self.depth:  # 非根节点直接返回缓存的分数
            # print(
            #     f"[bold red]Cache hit eval_ {self.cache[hash_key]},depth:{depth}[/bold red]"
            # )
            return self.cache[hash_key]
        # 终止条件：到达最大深度或游戏结束
        if depth <= 0 or is_gameover(board_tuple):
            eval_ = evaluate_board(board_state, self.patternDict)
            self.cache[hash_key] = eval_  # 缓存结果
            return eval_  # 返回评估分数

        if is_max_player:
            max_val = -np.inf
            for action in get_near_actions_with_noempty_generator(board_tuple, 2):

                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.maxvalue  # 极大玩家落子
                check_over_tuple = is_gameover_with_state(
                    self.board_to_tuple(board_state)
                )
                if (
                    check_over_tuple[0] and check_over_tuple[1] > 0
                ):  # 如果下了之后就赢了，直接返回最大值, 极大玩家赢
                    print(
                        f"[bold red]极大玩家赢,action: {action},depth :{depth}[/bold red]"
                    )
                    eval_ = np.inf  # 如果下了之后就赢了，直接返回最大值
                else:
                    eval_ = self.alphabeta(
                        board_state, depth - 1, alpha, beta, False
                    )  # 下了之后评估分数
                board_state[action[0]][action[1]] = temp  # 撤销落子
                if eval_ > max_val:
                    max_val = eval_
                    if depth == self.depth:  # 只在最外层记录最佳落子
                        # print(f"Update best move: {action}, max_val: {max_val}")
                        self.best_move = action
                alpha = max(alpha, max_val)
                if beta <= alpha:
                    break
            self.cache[hash_key] = max_val  # 缓存结果
            return max_val
        else:
            min_val = np.inf
            for action in get_near_actions_with_noempty_generator(board_tuple, 2):

                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.minvalue  # 极小玩家落子
                check_over_tuple = is_gameover_with_state(
                    self.board_to_tuple(board_state)
                )
                if check_over_tuple[0] and check_over_tuple[1] < 0:  # 极小玩家赢
                    print(
                        f"[bold red]极小玩家赢,action: {action},depth :{depth}[/bold red]"
                    )
                    eval_ = -np.inf  # 如果下了之后就输了，直接返回最小值
                else:
                    eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, True)
                board_state[action[0]][action[1]] = temp  # 撤销落子
                if eval_ <= min_val:
                    min_val = eval_
                    if depth == self.depth:  # 只在最外层记录最佳落子
                        # print(f"Update best move: {action}, min_val: {min_val}")
                        self.best_move = action
                beta = min(beta, min_val)
                if beta <= alpha:
                    break
            self.cache[hash_key] = min_val  # 缓存结果
            return min_val

    def diff_board_state(
        self, new_board_state: np.ndarray, old_board_state: np.ndarray
    ) -> tuple:
        diff = []
        for i in range(15):
            for j in range(15):
                if new_board_state[i][j] != old_board_state[i][j]:
                    diff.append((i, j))
        return diff  # 返回差异的位置

    def get_best_action(self, board_state: np.ndarray) -> tuple:
        if is_gameover(self.board_to_tuple(board_state)):
            logger.warning("Game over")
            return (-1, -1)

        self.best_move = None
        num_pieces = np.count_nonzero(board_state)
        enemy_num_pieces = np.count_nonzero(board_state == self.enemy_value)
        if num_pieces == 0:
            logger.debug("No pieces , AI will choose center")
            best_action = (board_state.shape[0] // 2, board_state.shape[1] // 2)

        elif enemy_num_pieces < 2:
            # 在敌方棋子少于2个时，优先选择中心位置,距离中心位置2以内的位置
            logger.debug("Enemy pieces less than 3, will choose center randomly")
            center_position = (board_state.shape[0] // 2, board_state.shape[1] // 2)
            near_center_positions = []
            for i in range(center_position[0] - 2, center_position[0] + 3):
                for j in range(center_position[1] - 2, center_position[1] + 3):
                    if (
                        i >= 0
                        and i < 15
                        and j >= 0
                        and j < 15
                        and board_state[i][j] == 0  # 位置为空
                        # and (i, j) not in self.move_history  # 位置不在历史记录中
                    ):
                        near_center_positions.append((i, j))
            best_action = (
                random.choice(near_center_positions)
                if len(near_center_positions) > 0
                else None
            )

        else:
            if self.maxvalue == self.value:
                logger.debug("AI is thinking ... AI is max player")
                self.alphabeta(
                    board_state, self.depth, -np.inf, np.inf, True  # 最大化玩家
                )
            else:
                logger.debug("AI is thinking ... AI is min player")
                self.alphabeta(
                    board_state, self.depth, -np.inf, np.inf, False  # 最小化玩家
                )
            best_action = self.best_move

        # 后续处理
        if best_action is None:
            logger.warning(
                "No best action found in AlphaBeta , will use heuristic get a move"
                + f"| Current Player is {"MaxPlayer" if self.is_max_player else "MinPlayer"}"
            )
            available_actions = get_near_actions(
                self.board_to_tuple(board_state),
                self.move_history[-1] if self.move_history else None,
                3,
            )
            available_actions.sort(
                key=lambda action: self.heuristic(
                    self.board_to_tuple(board_state),
                    action,
                    self.is_max_player,
                ),
                reverse=self.is_max_player,
            )
            best_action = available_actions[0]

        assert board_state[best_action[0]][best_action[1]] == 0, (
            "AI move error: invalid move"
            + f"{board_state[best_action[0]][best_action[1]]}"
        )
        self.move_history.append(best_action)
        logger.success(f"AI move: {best_action}")
        return best_action


def get_best_action_multiprocess(ai, board_state):
    return ai.get_best_action(board_state)


# if __name__ == "__main__" and True:

#     import numpy as np
#     import random

#     def generate_board_with_four_in_a_row(
#         ai_value: int, enemy_value: int
#     ) -> np.ndarray:
#         # 创建一个 15x15 的空棋盘
#         board = np.zeros((15, 15), dtype=int)

#         # 在棋盘上放置 AI 的四子
#         row = random.randint(0, 14)
#         col = random.randint(0, 10)  # 确保可以放下四个子
#         for i in range(4):
#             board[row][col + i] = ai_value

#         # 在棋盘上放置一个空位
#         empty_col = col + 4  # 确保下一个位置是空的
#         board[row][empty_col] = 0

#         return board

#     def generate_board_with_three_in_a_row(
#         ai_value: int, enemy_value: int
#     ) -> np.ndarray:
#         # 创建一个 15x15 的空棋盘
#         board = np.zeros((15, 15), dtype=int)

#         # 在棋盘上放置敌人的三子
#         row = random.randint(0, 14)
#         col = random.randint(0, 10)  # 确保可以放下三个子
#         for i in range(3):
#             board[row][col + i] = enemy_value

#         # 在棋盘的两边放置空位
#         board[row][col - 1] = 0  # 左边空位
#         board[row][col + 3] = 0  # 右边空位

#         return board

#     def test_ai_on_generated_boards(
#         ai: AlphaBetaGomokuAI, ai_value: int, enemy_value: int
#     ):
#         # 测试 AI 让自己形成五子
#         board_four = generate_board_with_four_in_a_row(ai_value, enemy_value)
#         print("Testing board with AI's four in a row:")
#         print(board_four)
#         action = ai.get_best_action(board_four)
#         print(f"AI's action to win: {action}")
#         try:
#             board_four[action[0]][action[1]] = ai_value
#             # 检查 AI 是否落子在合适的位置
#             assert is_gameover(ai.board_to_tuple(board_four)), "AI failed to win."

#         except AssertionError as e:

#             raise e
#         finally:
#             print(board_four)

#         # 测试 AI 拦截对手的三子
#         board_three = generate_board_with_three_in_a_row(ai_value, enemy_value)
#         print("Testing board with enemy's three in a row:")
#         print(f"Test this board score: {evaluate_board(board_three, ai.patternDict)}")
#         print(board_three)
#         action = ai.get_best_action(board_three)
#         print(f"AI's action to intercept: {action}")

#         try:
#             board_three[action[0]][action[1]] = ai_value
#             # 检查 AI 是否落子在合适的位置
#             # assert np.count_nonzero(board_three == ai_value) == 2, "AI failed to intercept the enemy's three in a row."
#         except AssertionError as e:

#             raise e
#         finally:
#             print(board_three)

#     # 测试连续对局的性能
#     def test_ai_on_generated_boards_continuously(
#         ai: AlphaBetaGomokuAI, ai_value: int, enemy_value: int, first_turn: str = "AI"
#     ):
#         init_board = np.zeros((15, 15), dtype=int)
#         player_move_history = set()
#         ai_move_history = set()
#         # print(init_board)

#         for i in range(225):
#             print(f"Round {i} with {first_turn}'s first turn")

#             # 控制先后手
#             if (first_turn == "AI" and i % 2 == 0) or (
#                 first_turn == "Player" and i % 2 == 1
#             ):
#                 print("AI's turn")
#                 action = ai.get_best_action(init_board)
#                 assert (
#                     init_board[action[0]][action[1]] == 0
#                 ), "AI move error: invalid move"
#                 assert action not in ai_move_history, "AI move error: duplicate move"
#                 assert (
#                     action not in ai_move_history | player_move_history
#                 ), "Invalid move"
#                 init_board[action[0]][action[1]] = ai_value  # 更新棋盘
#                 ai_move_history.add(action)
#                 print(f"AI's action: {tuple(map(int, action))}")
#                 if is_gameover(ai.board_to_tuple(init_board)):
#                     print("AI wins")
#                     break
#             else:
#                 print("Player's turn")
#                 avi_actions = get_near_actions(ai.board_to_tuple(init_board), None)
#                 avi_actions.sort(
#                     key=lambda action: ai.heuristic(
#                         ai.board_to_tuple(init_board), action, enemy_value > ai_value
#                     ),
#                     reverse=True if enemy_value > ai_value else False,
#                 )  # 对玩家的动作进行启发式排序
#                 playaction = avi_actions[0]
#                 row, col = playaction
#                 assert init_board[row][col] == 0, "Player move error: invalid move"
#                 assert (
#                     playaction not in player_move_history
#                 ), "Player move error: duplicate move"
#                 assert (
#                     playaction not in ai_move_history | player_move_history
#                 ), "Invalid move"
#                 print(f"Player's action: {tuple(map(int, (row, col)))}")
#                 init_board[row][col] = enemy_value
#                 player_move_history.add(playaction)
#                 if is_gameover(ai.board_to_tuple(init_board)):
#                     print("Player wins")
#                     break

#         print(init_board)

#     #
#     def test_ai_vs_ai(
#         ai1: AlphaBetaGomokuAI, ai2: AlphaBetaGomokuAI, ai1_value: int, ai2_value: int
#     ):
#         init_board = np.zeros((15, 15), dtype=int)
#         ai1_move_history = set()
#         ai2_move_history = set()

#         for i in range(225):
#             print(f"Round {i}")

#             if i % 2 == 0:
#                 print("AI1's turn")
#                 action = ai1.get_best_action(
#                     init_board.copy()
#                 )  # 传入副本,因为AI内部会修改棋盘
#                 assert (
#                     init_board[action[0]][action[1]] == 0
#                 ), "AI1 move error: invalid move"
#                 assert action not in ai1_move_history, "AI1 move error: duplicate move"
#                 assert action not in ai1_move_history | ai2_move_history, "Invalid move"
#                 init_board[action[0]][action[1]] = ai1_value
#                 ai1_move_history.add(action)
#                 print(f"AI1's action: {tuple(map(int, action))}")
#                 if is_gameover(ai1.board_to_tuple(init_board)):
#                     print("AI1 wins")
#                     break
#             else:
#                 print("AI2's turn")
#                 action = ai2.get_best_action(init_board.copy())
#                 assert (
#                     init_board[action[0]][action[1]] == 0
#                 ), "AI2 move error: invalid move"
#                 assert action not in ai2_move_history, "AI2 move error: duplicate move"
#                 assert action not in ai1_move_history | ai2_move_history, "Invalid move"
#                 init_board[action[0]][action[1]] = ai2_value
#                 ai2_move_history.add(action)
#                 print(f"AI2's action: {tuple(map(int, action))}")
#                 if is_gameover(ai2.board_to_tuple(init_board)):
#                     print("AI2 wins")
#                     break
#             print(f"Current board score: {evaluate_board(init_board, ai1.patternDict)}")
#         print(init_board)

#     ai1, ai2 = [AlphaBetaGomokuAI(1, depth=3), AlphaBetaGomokuAI(-1, depth=2)]
#     test_ai_vs_ai(ai1, ai2, ai1.value, ai2.value)

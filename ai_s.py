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

# import diskcache as dc
# 创建缓存实例
# cache = dc.Cache("./cache")

sys.setrecursionlimit(1500)


class AlphaBetaGomokuAI:
    def __init__(self, aivalue: int, depth=3):
        self.value = aivalue
        self.enemy_value = -self.value
        self.depth = depth
        self.patternDict = create_pattern_dict(self.value)
        self.move_history = []
        self.base_move = None
        self.MaxPlayeralphabetaMoveHistory = set()
        self.MinPlayeralphabetaMoveHistory = set()
        # Zobrist Hashing
        self.zobristTable = self.create_zobrist_table()  # 生成 Zobrist 表
        self.rollingHash = 0  # 当前棋盘状态的 Zobrist 哈希值
        self.TTable = {}  # 这里存储的是当前局面的哈希值对应的最优值和深度
        logger.info("Current AI: AlphaBetaGomokuAI")

    def create_zobrist_table(self):
        # 生成随机的 Zobrist 哈希表
        return np.random.randint(1, 2**64, (15, 15, 2), dtype=np.uint64)

    def update_hash(self, row: int, col: int, player_value: int):
        # 更新 Zobrist 哈希值
        self.rollingHash ^= self.zobristTable[row][col][player_value]

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

        if depth <= 0 or is_gameover(board_state):
            return evaluate_board(board_state, self.patternDict)

        if is_max_player:
            max_val = -np.inf
            for action in get_near_actions(self.board_to_tuple(board_state), None):
                if action in self.move_history:
                    continue
                temp = board_state[action[0]][action[1]]  # 保存当前位置的值
                board_state[action[0]][action[1]] = self.value  # 模拟AI落子
                self.update_hash(action[0], action[1], 1)  # 更新哈希

                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, False)
                board_state[action[0]][action[1]] = temp  # 撤销棋盘
                self.update_hash(action[0], action[1], 0)  # 撤销哈希

                if eval_ > max_val:
                    max_val = eval_
                    if depth == self.depth:
                        print(f"Update base_move: {action}, max_val: {max_val}")
                        self.base_move = action
                alpha = max(alpha, max_val)

                self.rollingHash ^= self.zobristTable[action[0]][action[1]][1]

                if beta <= alpha:
                    # print("AlphaBeta Pruning ........ ")
                    break

            self.TTable[self.rollingHash] = [max_val, depth]
            return max_val
        else:
            min_val = np.inf
            for action in get_near_actions(self.board_to_tuple(board_state), None):
                if action in self.move_history:
                    continue

                temp = board_state[action[0]][action[1]]  # 保存当前位置的值
                board_state[action[0]][action[1]] = self.enemy_value  # 模拟对手落子
                self.update_hash(action[0], action[1], 0)  # 更新哈希

                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, True)

                board_state[action[0]][action[1]] = temp  # 撤销棋盘
                self.update_hash(action[0], action[1], 1)  # 撤销哈希

                if eval_ < min_val:
                    min_val = eval_
                    if depth == self.depth:
                        self.base_move = action
                beta = min(beta, min_val)
                if beta <= alpha:
                    # print("AlphaBeta Pruning ........ ")
                    break

            self.TTable[self.rollingHash] = [min_val, depth]
            return min_val

    def get_best_action(self, board_state: np.ndarray) -> tuple:
        # 纠正方向 互换xy
        board_state = board_state.T
        if is_gameover(board_state):
            logger.warning("Game over")
            return (-1, -1)
        self.base_move = None
        # self.MaxPlayeralphabetaMoveHistory.clear()
        # self.MinPlayeralphabetaMoveHistory.clear()

        # 计算当前棋盘上的棋子数量
        num_pieces = np.count_nonzero(board_state)
        # 如果没有棋子，选择中间位置
        if num_pieces == 0:
            print("No pieces will choose center")
            # best_action = (board_state.shape[0] // 2, board_state.shape[1] // 2)
            best_action = (3, 7)
        else:
            print("AI is thinking ...")
            self.alphabeta(
                board_state, self.depth, -np.inf, np.inf, self.value > self.enemy_value
            )
            best_action = self.base_move

        # 后续检查
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
        board_state_copy = board_state.copy()
        board_state_copy[best_action[0]][best_action[1]] = self.value
        print(f"AI moved:\n {board_state_copy.T}")
        logger.success(f"AI move: {best_action}")
        return best_action


if __name__ == "__main__":
    # test_state = np.zeros((15, 15), dtype=int)
    # # a = random.choice(np.argwhere(test_state == 0))
    # # print(a)
    # test_state[7, 7] = 1  # ai
    # test_state[8, 8] = -1  # player
    # test_state[9, 9] = 1  # ai
    # test_state[10, 10] = -1  # player
    # ai = AlphaBetaGomokuAI(1, depth=2)
    # aimove = ai.get_best_action(test_state)
    # test_state[aimove[0], aimove[1]] = 1  # ai
    # print(aimove)

    import numpy as np
    import random

    def generate_board_with_four_in_a_row(
        ai_value: int, enemy_value: int
    ) -> np.ndarray:
        # 创建一个 15x15 的空棋盘
        board = np.zeros((15, 15), dtype=int)

        # 在棋盘上放置 AI 的四子
        row = random.randint(0, 14)
        col = random.randint(0, 10)  # 确保可以放下四个子
        for i in range(4):
            board[row][col + i] = ai_value

        # 在棋盘上放置一个空位
        empty_col = col + 4  # 确保下一个位置是空的
        board[row][empty_col] = 0

        return board

    def generate_board_with_three_in_a_row(
        ai_value: int, enemy_value: int
    ) -> np.ndarray:
        # 创建一个 15x15 的空棋盘
        board = np.zeros((15, 15), dtype=int)

        # 在棋盘上放置敌人的三子
        row = random.randint(0, 14)
        col = random.randint(0, 10)  # 确保可以放下三个子
        for i in range(3):
            board[row][col + i] = enemy_value

        # 在棋盘的两边放置空位
        board[row][col - 1] = 0  # 左边空位
        board[row][col + 3] = 0  # 右边空位

        return board

    def test_ai_on_generated_boards(
        ai: AlphaBetaGomokuAI, ai_value: int, enemy_value: int
    ):
        # 测试 AI 让自己形成五子
        board_four = generate_board_with_four_in_a_row(ai_value, enemy_value)
        print("Testing board with AI's four in a row:")
        print(board_four)
        action = ai.get_best_action(board_four)
        print(f"AI's action to win: {action}")
        try:
            board_four[action[0]][action[1]] = ai_value
            # 检查 AI 是否落子在合适的位置
            assert is_gameover(board_four), "AI failed to win the game."

        except AssertionError as e:

            raise e
        finally:
            print(board_four)

        # 测试 AI 拦截对手的三子
        board_three = generate_board_with_three_in_a_row(ai_value, enemy_value)
        print("Testing board with enemy's three in a row:")
        print(board_three)
        action = ai.get_best_action(board_three)
        print(f"AI's action to intercept: {action}")

        try:
            board_three[action[0]][action[1]] = ai_value
            # 检查 AI 是否落子在合适的位置
            # assert np.count_nonzero(board_three == ai_value) == 2, "AI failed to intercept the enemy's three in a row."
        except AssertionError as e:

            raise e
        finally:
            print(board_three)

    ai = AlphaBetaGomokuAI(1, depth=2)
    test_ai_on_generated_boards(ai, 1, -1)

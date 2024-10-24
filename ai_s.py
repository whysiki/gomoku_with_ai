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
import uuid

sys.setrecursionlimit(1500)


class AlphaBetaGomokuAI:
    def __init__(self, aivalue: int, depth=3):
        self.value = aivalue
        self.enemy_value = -self.value
        self.maxvalue = max(self.value, self.enemy_value)
        self.minvalue = min(self.value, self.enemy_value)
        self.is_max_player = self.value > self.enemy_value
        self.depth = depth
        self.patternDict = create_pattern_dict(self.value)
        self.move_history = []
        self.base_move = None
        self.MaxPlayeralphabetaMoveHistory: list = list()
        self.MinPlayeralphabetaMoveHistory: list = list()
        self.TTable = {}  # [score, depth, best_move]
        self.zobristTable = self.init_zobrist()
        self.last_board_state: np.ndarray = np.zeros((15, 15), dtype=int)  # 默认新局面
        self.rollingHash = 0
        logger.info("Current AI: AlphaBetaGomokuAI")

    def init_zobrist(self):
        # 用随机整数替代 UUID，范围控制在 int32 内
        zTable = [
            [[np.random.randint(0, 2**31) for _ in range(2)] for j in range(15)]
            for i in range(15)
        ]
        return zTable

    def update_rolling_hash(self, row: int, col: int, player: int):
        self.rollingHash ^= self.zobristTable[row][col][player]

    def update_TTable(
        self, table: dict, hash: int, score: int, depth: int, best_move: tuple = None
    ):
        if hash not in table or depth >= table[hash][1]:
            table[hash] = [score, depth, best_move]  # 存储最佳下法
        # print(f"TTable updated: {hash}, score: {score}, depth: {depth}, best move: {best_move}")

    def board_to_tuple(self, board: np.ndarray) -> tuple:
        return tuple(map(tuple, board))

    def heuristic(
        self, board_state: np.ndarray, action: tuple, is_max_player: bool
    ) -> int:
        temp = board_state[action[0]][action[1]]  # 保存当前位置的值
        board_state[action[0]][action[1]] = (
            self.maxvalue if is_max_player else self.minvalue
        )  # 模拟落子
        score = evaluate_board(board_state, self.patternDict)  # 评估落子后的局势
        board_state[action[0]][action[1]] = temp  # 撤销落子
        # print(f"Action: {action}, score: {score}")
        return score  # 返回评估值

    def alphabeta(
        self,
        board_state: np.ndarray,
        depth: int,
        alpha: int,
        beta: int,
        is_max_player: bool,
    ):
        board_tuple = self.board_to_tuple(board_state)
        # print(f"TTable size: {len(self.TTable)}")

        # 检查置换表
        if (
            self.rollingHash in self.TTable
            and self.TTable[self.rollingHash][1] >= depth
        ):
            print(f"rollingHash: {self.rollingHash}")
            print(f"TTable value: {self.TTable[self.rollingHash]}")
            return self.TTable[self.rollingHash][0]

        # 终止条件：到达最大深度或游戏结束
        if depth <= 0 or is_gameover(board_tuple):
            eval_ = evaluate_board(board_state, self.patternDict)
            self.update_TTable(self.TTable, self.rollingHash, eval_, depth)
            return eval_

        if is_max_player:
            max_val = -np.inf
            father_node_action = (
                self.MaxPlayeralphabetaMoveHistory[-1]
                if self.MaxPlayeralphabetaMoveHistory
                else None
            )
            actions = get_near_actions(board_tuple, father_node_action, 3)

            # 对可能的动作进行启发式排序，提升剪枝效果
            actions.sort(
                key=lambda action: self.heuristic(board_state, action, is_max_player),
                reverse=True,
            )

            for action in actions:
                if action in self.move_history:
                    continue
                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.maxvalue  # 极大玩家落子
                self.update_rolling_hash(action[0], action[1], 0)  # 更新当前哈希值
                self.MaxPlayeralphabetaMoveHistory.append(action)
                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, False)
                board_state[action[0]][action[1]] = temp  # 撤销落子
                self.update_rolling_hash(action[0], action[1], 0)  # 撤销当前哈希值
                self.MaxPlayeralphabetaMoveHistory.remove(action)

                if eval_ > max_val:
                    max_val = eval_
                    if depth == self.depth:
                        print(f"Update best move: {action}, score: {max_val}")
                        self.base_move = action
                alpha = max(alpha, max_val)
                if beta <= alpha:
                    break

            self.update_TTable(
                self.TTable, self.rollingHash, max_val, depth, self.base_move
            )  # 更新置换表
            return max_val
        else:
            min_val = np.inf
            father_node_action = (
                self.MinPlayeralphabetaMoveHistory[-1]
                if self.MinPlayeralphabetaMoveHistory
                else None
            )
            actions = get_near_actions(board_tuple, father_node_action, 3)

            # 对极小玩家的动作进行启发式排序
            actions.sort(
                key=lambda action: self.heuristic(
                    board_state, action, not is_max_player
                ),
                reverse=False,
            )

            for action in actions:
                if action in self.move_history:
                    continue
                temp = board_state[action[0]][action[1]]
                board_state[action[0]][action[1]] = self.minvalue  # 极小玩家落子
                self.update_rolling_hash(action[0], action[1], 1)  # 更新当前哈希值
                eval_ = self.alphabeta(board_state, depth - 1, alpha, beta, True)
                board_state[action[0]][action[1]] = temp  # 撤销落子
                self.update_rolling_hash(action[0], action[1], 1)  # 撤销当前哈希值

                if eval_ < min_val:
                    min_val = eval_
                    if depth == self.depth:
                        print(f"Update best move: {action}, score: {min_val}")
                        self.base_move = action
                beta = min(beta, min_val)
                if beta <= alpha:
                    break

            self.update_TTable(
                self.TTable, self.rollingHash, min_val, depth, self.base_move
            )  # 更新置换表
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

        diff_actions = self.diff_board_state(board_state, self.last_board_state)

        if len(diff_actions) == 1:
            # 对手落了一子
            diff_action = diff_actions[0]
            assert (
                board_state[diff_action[0]][diff_action[1]] == self.enemy_value
            ), "AI detected invalid move by opponent"
            self.update_rolling_hash(diff_action[0], diff_action[1], 1)
        elif len(diff_actions) > 1:
            print("A sequence of chess moves by the opponent")
        else:
            print("AI is first")

        self.base_move = None
        num_pieces = np.count_nonzero(board_state)
        if num_pieces == 0:
            print("No pieces , AI will choose center")
            best_action = (board_state.shape[0] // 2, board_state.shape[1] // 2)
        else:
            print("AI is thinking ...")
            if self.maxvalue == self.value:
                print("AI is max player")
                self.alphabeta(
                    board_state,
                    self.depth,
                    -np.inf,
                    np.inf,
                    self.value > self.enemy_value,
                )
            else:
                print("AI is min player")
                self.alphabeta(
                    board_state,
                    self.depth,
                    -np.inf,
                    np.inf,
                    self.value < self.enemy_value,
                )
            best_action = self.base_move

        if best_action is None:
            if self.rollingHash in self.TTable:
                _, _, best_action = self.TTable[self.rollingHash]
            if best_action is not None:
                print(f"Using cached best move: {best_action}")
            else:
                logger.warning(
                    "No best action found in AlphaBeta , will use heuristic get a move"
                )
                available_actions = get_near_actions(
                    self.board_to_tuple(board_state),
                    self.move_history[-1] if self.move_history else None,
                    3,
                )
                available_actions.sort(
                    key=lambda action: self.heuristic(
                        board_state, action, self.value > self.enemy_value
                    ),
                    reverse=self.is_max_player,
                )
                best_action = available_actions[0]

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
        self.last_board_state = board_state_copy
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
            assert is_gameover(ai.board_to_tuple(board_four)), "AI failed to win."

        except AssertionError as e:

            raise e
        finally:
            print(board_four)

        # 测试 AI 拦截对手的三子
        board_three = generate_board_with_three_in_a_row(ai_value, enemy_value)
        print("Testing board with enemy's three in a row:")
        print(f"Test this board score: {evaluate_board(board_three, ai.patternDict)}")
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

    # 测试连续对局的性能
    def test_ai_on_generated_boards_continuously(
        ai: AlphaBetaGomokuAI, ai_value: int, enemy_value: int, first_turn: str = "AI"
    ):
        init_board = np.zeros((15, 15), dtype=int)
        player_move_history = set()
        ai_move_history = set()
        # print(init_board)

        while True:
            print(f"Round {i} with {first_turn}'s first turn")

            # 控制先后手
            if (first_turn == "AI" and i % 2 == 0) or (
                first_turn == "Player" and i % 2 == 1
            ):
                print("AI's turn")
                action = ai.get_best_action(init_board)
                assert (
                    init_board[action[0]][action[1]] == 0
                ), "AI move error: invalid move"
                assert action not in ai_move_history, "AI move error: duplicate move"
                assert (
                    action not in ai_move_history | player_move_history
                ), "Invalid move"
                init_board[action[0]][action[1]] = ai_value  # 更新棋盘
                ai_move_history.add(action)
                print(f"AI's action: {tuple(map(int, action))}")
                if is_gameover(ai.board_to_tuple(init_board)):
                    print("AI wins")
                    break
            else:
                print("Player's turn")
                avi_actions = get_near_actions(ai.board_to_tuple(init_board), None)
                avi_actions.sort(
                    key=lambda action: ai.heuristic(
                        init_board, action, enemy_value > ai_value
                    ),
                    reverse=True if enemy_value > ai_value else False,
                )  # 对玩家的动作进行启发式排序
                playaction = avi_actions[0]
                row, col = playaction
                assert init_board[row][col] == 0, "Player move error: invalid move"
                assert (
                    playaction not in player_move_history
                ), "Player move error: duplicate move"
                assert (
                    playaction not in ai_move_history | player_move_history
                ), "Invalid move"
                print(f"Player's action: {tuple(map(int, (row, col)))}")
                init_board[row][col] = enemy_value
                player_move_history.add(playaction)
                if is_gameover(ai.board_to_tuple(init_board)):
                    print("Player wins")
                    break

            print(init_board)

    ai = AlphaBetaGomokuAI(1, depth=1)
    test_ai_on_generated_boards_continuously(ai, 1, -1, first_turn="AI")
    test_ai_on_generated_boards_continuously(ai, 1, -1, first_turn="Player")
    # ai = AlphaBetaGomokuAI(1, depth=2)
    # test_ai_on_generated_boards(ai, 1, -1)

    # best_action = (3, 7)
    # elif enemy_num_pieces < 3:
    #     # 在敌方棋子少于3个时，优先选择中心位置,距离中心位置3以内的位置
    #     print("Enemy pieces less than 3, will choose center")
    #     center_position = (board_state.shape[0] // 2, board_state.shape[1] // 2)
    #     near_center_positions = []
    #     for i in range(center_position[0] - 3, center_position[0] + 4):
    #         for j in range(center_position[1] - 3, center_position[1] + 4):
    #             if (
    #                 i >= 0
    #                 and i < 15
    #                 and j >= 0
    #                 and j < 15
    #                 and board_state[i][j] == 0
    #             ):
    #                 near_center_positions.append((i, j))
    #     best_action = random.choice(near_center_positions)

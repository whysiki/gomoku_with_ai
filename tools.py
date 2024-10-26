import numpy as np
from functools import lru_cache


def create_pattern_dict(isto_normalization: bool = False) -> dict:
    # 初始化模式分数字典
    patternDict = {}
    # x 为 -1 表示对手，x 为 1 表示己方
    for x in [-1, 1]:
        y = -x  # y为对手棋子的表示
        # patternDict[(x, x, x, x, x)] = 100000 * 99999 * x  # 连五
        # patternDict[(0, x, x, x, x, 0)] = 100 * 100000 * x  # 活四
        patternDict[(x, x, x, x, x)] = 100000 * 100 * x  # 连五
        patternDict[(0, x, x, x, x, 0)] = 10 * 100000 * x  # 活四
        patternDict[(0, x, x, x, 0, x, 0)] = 100000 * x  # 跳四
        patternDict[(0, x, 0, x, x, x, 0)] = 100000 * x  # 跳四
        patternDict[(0, x, x, 0, x, x, 0)] = 100000 * x  # 跳四

        patternDict[(0, x, x, x, x, y)] = 10000 * x  # 冲四，左边有堵
        patternDict[(y, x, x, x, x, 0)] = 10000 * x  # 冲四，右边有堵
        patternDict[(y, x, x, x, x, y)] = 100 * x  # 死四，封堵两边

        patternDict[(0, x, x, x, 0)] = 1000 * x  # 活三
        patternDict[(0, x, 0, x, x, 0)] = 1000 * x  # 跳三
        patternDict[(0, x, x, 0, x, 0)] = 1000 * x  # 跳三

        patternDict[(0, 0, x, x, x, y)] = 100 * x  # 冲三
        patternDict[(y, x, x, x, 0, 0)] = 100 * x  # 冲三
        patternDict[(0, x, 0, x, x, y)] = 100 * x  # 跳冲三
        patternDict[(y, x, x, 0, x, 0)] = 100 * x  # 跳冲三
        patternDict[(0, x, x, 0, x, y)] = 100 * x  # 跳冲三
        patternDict[(y, x, 0, x, x, 0)] = 100 * x  # 跳冲三

        patternDict[(x, 0, 0, x, x)] = 100 * x  # 冲二
        patternDict[(x, x, 0, 0, x)] = 100 * x  # 冲二
        patternDict[(x, 0, x, 0, x)] = 100 * x  # 跳冲二

        patternDict[(0, 0, x, x, 0)] = 10 * x  # 活二
        patternDict[(0, x, x, 0, 0)] = 10 * x  # 活二
        patternDict[(0, x, 0, x, 0)] = 10 * x  # 跳二
        patternDict[(0, x, 0, 0, x, 0)] = 10 * x  # 跳二

        patternDict[(y, 0, x, 0, x, 0, y)] = 10 * x  # 封堵跳二
        patternDict[(y, 0, x, x, 0, 0, y)] = 10 * x  # 封堵冲二
        patternDict[(y, 0, 0, x, x, 0, y)] = 10 * x  # 封堵冲二

        patternDict[(y, x, x, x, y)] = 1 * x  # 死三
        patternDict[(y, x, 0, x, x, y)] = 1 * x  # 封堵跳三

        patternDict[(0, x, x, 0, x, 0, x, 0)] = 500 * x  # 跳四
        patternDict[(0, x, 0, x, 0, x, 0, x, 0)] = 500 * x  # 跳四
        patternDict[(0, x, x, x, 0, 0)] = 500 * x  # 活三
        patternDict[(0, 0, x, x, x, 0)] = 500 * x  # 活三
        patternDict[(0, x, 0, x, 0, x, 0)] = 500 * x  # 跳三
        patternDict[(0, x, 0, 0, x, 0, x, 0)] = 500 * x  # 跳三

    if isto_normalization:
        # 计算最大值和最小值
        max_value = max(patternDict.values())
        min_value = min(patternDict.values())
        # 归一化
        # -1到1的归一化
        for key in patternDict.keys():
            patternDict[key] = (patternDict[key] - min_value) / (
                max_value - min_value
            ) * 2 - 1

    return patternDict


def evaluate_board(board: np.ndarray, patternDict: dict) -> int:

    @lru_cache(maxsize=None)
    def evaluate_line(line: tuple) -> int:
        # patternDict_items = patternDict.items()
        score = 0

        # 如果行全是0，直接返回0
        if not any(line):
            return 0

        line_str = "".join(map(str, line))  # 将数组转换为字符串进行模式匹配

        # 遍历每个模式
        for pattern, pattern_score in patternDict.items():
            if len(pattern) > len(line):
                continue  # 跳过不可能匹配的模式
            pattern_str = "".join(map(str, pattern))
            # 直接查找子字符串的位置
            if pattern_str in line_str:
                score += pattern_score
        return score

    @lru_cache(maxsize=None)
    def evaluate_intersectLines(board: tuple) -> int:
        board = np.array(board)
        score = 0
        # 正对角线
        for i in range(-board.shape[0] + 5, board.shape[0] - 4):
            diag = board.diagonal(i)
            score += evaluate_line(tuple(diag))

        # 反对角线
        flipped_board = np.fliplr(board)  # 提前计算一次反转的棋盘
        for i in range(-flipped_board.shape[0] + 5, flipped_board.shape[0] - 4):
            diag = flipped_board.diagonal(i)
            score += evaluate_line(tuple(diag))

        return score

    score = 0
    # 评估行和列
    for i in range(board.shape[0]):
        score += evaluate_line(tuple(board[i, :]))  # 行
        score += evaluate_line(tuple(board[:, i]))  # 列

    # 评估对角线
    score += evaluate_intersectLines(tuple(map(tuple, board)))
    return score


@lru_cache(maxsize=None)
def is_gameover(board: tuple) -> bool:

    board = np.array(board)
    # 检查行、列是否有赢家
    for i in range(board.shape[0]):
        if check_winning_line(board[i, :]) or check_winning_line(board[:, i]):
            return True

    # 检查对角线
    for i in range(-board.shape[0] + 5, board.shape[0] - 4):
        if check_winning_line(board.diagonal(i)) or check_winning_line(
            np.fliplr(board).diagonal(i)
        ):
            return True

    # 检查是否无空位
    return not np.any(board == 0)


def check_winning_line(line: np.ndarray) -> bool:
    count = 1
    if len(line) < 5:
        return False
    for i in range(1, len(line)):
        if line[i] == line[i - 1] and line[i] != 0:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False


@lru_cache(maxsize=None)
def is_gameover_with_state(board: tuple) -> tuple[bool, int]:
    "检查游戏是否结束，并返回胜利方或者平局， 0 为平局, 1 为极大方，-1 为极小方"
    board = np.array(board)

    # 检查行、列是否有赢家
    for i in range(board.shape[0]):
        if check_winning_line(board[i, :]):
            return True, board[i, 0]  # 返回行的赢家
        if check_winning_line(board[:, i]):
            return True, board[0, i]  # 返回列的赢家

    ## 检查对角线
    for i in range(-board.shape[0] + 1, board.shape[0]):  # 注意范围调整
        if check_winning_line(board.diagonal(i)):
            return True, board[0, 0]  # 返回对角线的赢家
        if check_winning_line(np.fliplr(board).diagonal(i)):
            return True, board[0, board.shape[0] - 1]  # 返回反对角线的赢家

    # 检查是否无空位
    if not np.any(board == 0):
        return True, 0  # 平局
    return False, None  # 游戏未结束


def get_actions(board: np.ndarray) -> list[tuple]:
    return list(map(tuple, np.argwhere(board == 0)))


@lru_cache(maxsize=None)
def get_near_actions(
    board: tuple, last_move: tuple, search_radius: int = 2
) -> list[tuple]:
    board = np.array(board)
    if last_move is None:
        return list(map(tuple, np.argwhere(board == 0)))
    available_actions = []
    last_x, last_y = last_move
    min_x = max(0, last_x - search_radius)
    max_x = min(board.shape[0], last_x + search_radius + 1)
    min_y = max(0, last_y - search_radius)
    max_y = min(board.shape[1], last_y + search_radius + 1)

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            if board[x, y] == 0 and (x, y) != last_move:
                available_actions.append((x, y))

    return available_actions


@lru_cache(maxsize=None)
def get_near_actions_with_noempty(board: tuple, search_radius: int = 2) -> list[tuple]:
    board = np.array(board)
    available_actions = set()
    # 找所有有棋子的点，扩展周围的搜索
    # 找到所有棋子的坐标
    all_moves = np.argwhere(board != 0)
    for move in all_moves:
        last_x, last_y = move
        # 搜索每个棋子周围的点
        min_x = max(0, last_x - search_radius)
        max_x = min(board.shape[0], last_x + search_radius + 1)
        min_y = max(0, last_y - search_radius)
        max_y = min(board.shape[1], last_y + search_radius + 1)

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if board[x, y] == 0:
                    available_actions.add((x, y))
    return available_actions


@lru_cache(maxsize=None)
def get_near_actions_with_noempty_generator(board: tuple, search_radius: int = 2):
    board = np.array(board)
    seen_actions = set()

    # 找到所有棋子的坐标
    all_moves = np.argwhere(board != 0)
    for move in all_moves:
        last_x, last_y = move
        # 搜索每个棋子周围的点
        min_x = max(0, last_x - search_radius)
        max_x = min(board.shape[0], last_x + search_radius + 1)
        min_y = max(0, last_y - search_radius)
        max_y = min(board.shape[1], last_y + search_radius + 1)

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if board[x, y] == 0 and (x, y) not in seen_actions:
                    seen_actions.add((x, y))
                    yield (x, y)


if __name__ == "__main__" and False:

    def test_():

        test_board = np.zeros((15, 15), dtype=int)
        test_board[0:5, 0] = 1
        print(is_gameover_with_state(tuple(map(tuple, test_board))))

        test_board2 = np.zeros((15, 15), dtype=int)
        test_board2[0:5, 0] = -1
        print(is_gameover_with_state(tuple(map(tuple, test_board2))))

        test_board3 = np.ones((15, 15), dtype=int)
        # 全-1数组
        test_board4 = -1 * np.ones((15, 15), dtype=int)
        print(is_gameover_with_state(tuple(map(tuple, test_board3))))
        print(is_gameover_with_state(tuple(map(tuple, test_board4))))

    # test_()

    def is_gameover(board: np.ndarray) -> bool:
        # 检查行、列是否有赢家
        for i in range(board.shape[0]):
            if check_winning_line(board[i, :]) or check_winning_line(board[:, i]):
                return True

        # 检查对角线
        for i in range(-board.shape[0] + 5, board.shape[0] - 4):
            if check_winning_line(board.diagonal(i)) or check_winning_line(
                np.fliplr(board).diagonal(i)
            ):
                return True

        # 检查是否无空位
        return not np.any(board == 0)

    def generate_disadvantage_board(
        direction: str, board_size=15, player_value=1, opponent_value=-1
    ) -> np.ndarray:
        """
        "horizontal", "vertical", "diagonal"
        """

        # 初始化棋盘
        board = np.zeros((board_size, board_size), dtype=int)

        # 放置随机的对手四连子，制造劣势
        for _ in range(3):  # 放置3组对手连子
            while True:
                # 随机选择一个方向（水平、垂直、对角线）
                # direction = np.random.choice(["horizontal", "vertical", "diagonal"])
                if direction == "horizontal":
                    row = np.random.randint(0, board_size)
                    col = np.random.randint(0, board_size - 4)
                    if np.all(board[row, col : col + 4] == 0):
                        board[row, col : col + 4] = opponent_value
                        break
                elif direction == "vertical":
                    row = np.random.randint(0, board_size - 4)
                    col = np.random.randint(0, board_size)
                    if np.all(board[row : row + 4, col] == 0):
                        board[row : row + 4, col] = opponent_value
                        break
                elif direction == "diagonal":
                    row = np.random.randint(0, board_size - 4)
                    col = np.random.randint(0, board_size - 4)
                    if np.all([board[row + i, col + i] == 0 for i in range(4)]):
                        for i in range(4):
                            board[row + i, col + i] = opponent_value
                        break
                else:
                    raise ValueError("Invalid direction")

        # 随机放置AI的棋子，构建防守局面
        for _ in range(8):
            x, y = np.random.randint(0, board_size, size=2)
            if board[x, y] == 0:
                board[x, y] = player_value

        return board

    def generate_advantage_board(
        direction: str, board_size=15, player_value=1, opponent_value=-1
    ) -> np.ndarray:
        """
        "horizontal", "vertical", "diagonal"
        """
        # 初始化棋盘
        board = np.zeros((board_size, board_size), dtype=int)

        # 放置AI即将五连子的情况
        for _ in range(3):  # 放置3组AI四连子
            while True:
                direction = np.random.choice(["horizontal", "vertical", "diagonal"])
                if direction == "horizontal":
                    row = np.random.randint(0, board_size)
                    col = np.random.randint(0, board_size - 4)
                    if np.all(board[row, col : col + 4] == 0):
                        board[row, col : col + 4] = player_value
                        break
                elif direction == "vertical":
                    row = np.random.randint(0, board_size - 4)
                    col = np.random.randint(0, board_size)
                    if np.all(board[row : row + 4, col] == 0):
                        board[row : row + 4, col] = player_value
                        break
                elif direction == "diagonal":
                    row = np.random.randint(0, board_size - 4)
                    col = np.random.randint(0, board_size - 4)
                    if np.all([board[row + i, col + i] == 0 for i in range(4)]):
                        for i in range(4):
                            board[row + i, col + i] = player_value
                        break
                else:
                    raise ValueError("Invalid direction")

        # 放置随机的对手棋子，构建防守局面
        for _ in range(8):
            x, y = np.random.randint(0, board_size, size=2)
            if board[x, y] == 0:
                board[x, y] = opponent_value

        return board

    def test_win():
        board = np.zeros((15, 15), dtype=int)
        board[0, 0] = 1
        board[1, 1] = 1
        board[2, 2] = 1
        board[3, 3] = 1
        board[4, 4] = 1
        assert is_gameover(board)
        board[0, 0] = 0
        board[1, 1] = 0
        board[2, 2] = 0
        board[3, 3] = 0
        board[4, 4] = 0
        assert not is_gameover(board)
        print("胜利测试通过")
        del board

    def test_actions():
        board = np.zeros((15, 15), dtype=int)
        board[0, 0] = 1
        board[1, 1] = 1
        board[2, 2] = 1
        board[3, 3] = 1
        board[4, 4] = 1
        assert len(get_actions(board)) == 225 - 5
        await_actions = get_near_actions(tuple(map(tuple, board)), (0, 0))
        # print(await_actions)
        assert (
            len(await_actions) == 8 - 2
            and (1, 1) not in await_actions
            and (2, 2) not in await_actions
        )
        del board
        # print("行动测试通过")

    def test_score():
        board1 = np.zeros((15, 15), dtype=int)
        predictDict = create_pattern_dict(1)
        board1[0, 0] = 1
        board1[1, 1] = 1
        board1[2, 2] = 1
        board1[3, 3] = 1
        board1[4, 4] = 1
        print(evaluate_board(board1, predictDict))
        board2 = np.zeros((15, 15), dtype=int)
        # 测试死局
        board2[0, 0] = -1
        board2[1, 1] = -1
        board2[2, 2] = -1
        board2[3, 3] = -1
        board2[4, 4] = -1
        print(evaluate_board(board2, predictDict))
        # 测试活三
        board3 = np.zeros((15, 15), dtype=int)
        board3[0, 0] = 1
        board3[1, 1] = 1
        board3[2, 2] = 1
        board3[3, 3] = 0
        board3[4, 4] = 1
        print(evaluate_board(board3, predictDict))
        del board1, board2, board3

    # 测试平局
    def test_both_win():
        board = np.random.randint(-1, 2, (15, 15))
        # print(board)
        assert is_gameover(board), "平局测试未通过"
        print("平局测试通过")
        print(evaluate_board(board, create_pattern_dict(1)))
        del board

    def test_advantage_board():
        for _ in range(100):
            board = generate_advantage_board("horizontal")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score > 0, "优势局面测试未通过"
            except AssertionError as e:

                print(board)
                raise e
        for _ in range(100):
            board = generate_advantage_board("vertical")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score > 0, "优势局面测试未通过"
            except AssertionError as e:

                print(board)
                raise e
        for _ in range(100):
            board = generate_advantage_board("diagonal")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score > 0, "优势局面测试未通过"
            except AssertionError as e:

                print(board)
                raise e
        print("优势局面测试通过")

    def test_disadvantage_board():
        for _ in range(100):
            board = generate_disadvantage_board("horizontal")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score < 0, "劣势局面测试通过"
            except AssertionError as e:

                print(board)
                raise e
        for _ in range(100):
            board = generate_disadvantage_board("vertical")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score < 0, "劣势局面测试通过"
            except AssertionError as e:

                print(board)
                raise e
        for _ in range(100):
            board = generate_disadvantage_board("diagonal")
            score = evaluate_board(board, create_pattern_dict(1))
            print(f"Test advantage board: {score}")
            try:
                assert score < 0, "劣势局面测试通过"
            except AssertionError as e:

                print(board)
                raise e
        print("劣势局面测试通过")

    def test_get_near_actions():
        # 测试用例 1: 空棋盘
        board = np.zeros((15, 15), dtype=int)
        actions = get_near_actions(tuple(map(tuple, board)), None)
        try:
            assert (
                len(actions) == 15 * 15
            ), "Test 1 failed: Should return all empty positions"
        except AssertionError as e:
            print(actions, len(actions))
            raise e

        # 测试用例 2: 有最后一步的情况下
        last_move = (7, 7)
        actions = get_near_actions(tuple(map(tuple, board)), last_move, search_radius=2)
        expected_actions_count = (5 * 5) - 1  # 5x5 grid minus the last move position
        try:
            assert (
                len(actions) == expected_actions_count
            ), "Test 2 failed: Should return 24 near positions"
        except AssertionError as e:
            print(actions, len(actions))
            raise e

        # 测试用例 3: 边缘情况
        last_move = (0, 0)
        actions = get_near_actions(tuple(map(tuple, board)), last_move, search_radius=1)
        assert len(actions) == 3, "Test 3 failed: Should return 3 near positions"

        last_move = (14, 14)
        actions = get_near_actions(tuple(map(tuple, board)), last_move, search_radius=1)
        assert len(actions) == 3, "Test 4 failed: Should return 3 near positions"

        # 测试用例 4: 棋盘上有棋子
        board = np.zeros((15, 15), dtype=int)
        board[6, 6] = 1
        board[7, 6] = -1
        board[7, 8] = 1
        last_move = (7, 7)
        actions = get_near_actions(tuple(map(tuple, board)), last_move, search_radius=2)
        expected_actions_count = 21  # 25 - 4 occupied positions
        try:
            assert (
                len(actions) == expected_actions_count
            ), "Test 5 failed: Should return available positions correctly"
        except AssertionError as e:
            print(actions, len(actions))
            raise e

        # 测试用例 5: 没有最后一步
        actions = get_near_actions(tuple(map(tuple, board)), None)
        assert (
            len(actions) == 15 * 15 - 3
        ), "Test 6 failed: Should return all empty positions minus occupied ones"

        print("All tests passed!")

    def test_get_near_actions_with_noempty():
        board = np.zeros((15, 15), dtype=int)
        board[0, 0] = 1
        board[1, 1] = 1
        board[2, 2] = 1
        board[3, 3] = 1
        board[4, 4] = 1
        print("Empty positions:")
        print(len(np.argwhere(board == 0)))
        # print(board)
        actions = get_near_actions_with_noempty(tuple(map(tuple, board)), 1)
        assert any(
            [board[x, y] == 0 for x, y in actions]
        ), "Test 1 failed: Should return 24 near positions"
        print(actions, len(actions))
        # print(board)
        # print([tuple(x) for x in np.argwhere(board != 0)])
        # assert len(actions) == 24, "Test 1 failed: Should return 24 near positions"
        del board

    test_win()
    test_actions()
    test_score()
    test_both_win()
    test_advantage_board()
    test_disadvantage_board()
    # test_get_near_actions()
    # print(init_board)
    test_get_near_actions_with_noempty()

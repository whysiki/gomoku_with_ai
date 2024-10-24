import numpy as np
from functools import wraps, lru_cache
import diskcache as dc

# 创建缓存实例
cache = dc.Cache("./cache")


def create_pattern_dict(your_value: int) -> dict:
    x = -1
    patternDict = {}
    while x < 2:
        y = -x
        patternDict[(x, x, x, x, x)] = 1000000 * x
        patternDict[(0, x, x, x, x, 0)] = 100000 * x
        patternDict[(0, x, x, x, 0, x, 0)] = 100000 * x
        patternDict[(0, x, 0, x, x, x, 0)] = 100000 * x
        patternDict[(0, x, x, 0, x, x, 0)] = 100000 * x
        patternDict[(0, x, x, x, x, y)] = 10000 * x
        patternDict[(y, x, x, x, x, 0)] = 10000 * x
        patternDict[(y, x, x, x, x, y)] = -10 * x
        patternDict[(0, x, x, x, 0)] = 1000 * x
        patternDict[(0, x, 0, x, x, 0)] = 1000 * x
        patternDict[(0, x, x, 0, x, 0)] = 1000 * x
        patternDict[(0, 0, x, x, x, y)] = 100 * x
        patternDict[(y, x, x, x, 0, 0)] = 100 * x
        patternDict[(0, x, 0, x, x, y)] = 100 * x
        patternDict[(y, x, x, 0, x, 0)] = 100 * x
        patternDict[(0, x, x, 0, x, y)] = 100 * x
        patternDict[(y, x, 0, x, x, 0)] = 100 * x
        patternDict[(x, 0, 0, x, x)] = 100 * x
        patternDict[(x, x, 0, 0, x)] = 100 * x
        patternDict[(x, 0, x, 0, x)] = 100 * x
        patternDict[(y, 0, x, x, x, 0, y)] = 100 * x
        patternDict[(y, x, x, x, y)] = -10 * x
        patternDict[(0, 0, x, x, 0)] = 100 * x
        patternDict[(0, x, x, 0, 0)] = 100 * x
        patternDict[(0, x, 0, x, 0)] = 100 * x
        patternDict[(0, x, 0, 0, x, 0)] = 100 * x
        patternDict[(0, 0, 0, x, x, y)] = 10 * x
        patternDict[(y, x, x, 0, 0, 0)] = 10 * x
        patternDict[(0, 0, x, 0, x, y)] = 10 * x
        patternDict[(y, x, 0, x, 0, 0)] = 10 * x
        patternDict[(0, x, 0, 0, x, y)] = 10 * x
        patternDict[(y, x, 0, 0, x, 0)] = 10 * x
        patternDict[(x, 0, 0, 0, x)] = 10 * x
        patternDict[(y, 0, x, 0, x, 0, y)] = 10 * x
        patternDict[(y, 0, x, x, 0, 0, y)] = 10 * x
        patternDict[(y, 0, 0, x, x, 0, y)] = 10 * x
        patternDict[(y, x, x, y)] = -10 * x
        x += 2
    return patternDict if your_value == 1 else {k: -v for k, v in patternDict.items()}


def evaluate_board(board: np.ndarray, patternDict: dict) -> int:
    def evaluate_intersectLines(board: np.ndarray) -> int:
        score = 0
        for i in range(-board.shape[0] + 5, board.shape[0] - 4):
            score += evaluate_line(board.diagonal(i))
            score += evaluate_line(np.fliplr(board).diagonal(i))
        return score

    def evaluate_line(line: np.ndarray) -> int:
        score = 0
        for i in range(len(line) - 4):
            score += patternDict.get(tuple(int(k) for k in line[i : i + 5]), 0)
        return score

    score = 0
    for row, col in zip(board, board.T):
        score += evaluate_line(row)
        score += evaluate_line(col)
    score += evaluate_intersectLines(board)
    return score


def is_gameover(board: np.ndarray) -> bool:
    for i in range(board.shape[0]):
        if check_winning_line(board[i, :]) or check_winning_line(board[:, i]):
            return True
    for i in range(-board.shape[0] + 5, board.shape[0] - 4):
        if check_winning_line(board.diagonal(i)) or check_winning_line(
            np.fliplr(board).diagonal(i)
        ):
            return True
    if not np.any(board == 0):
        return True
    return False


def get_actions(board: np.ndarray) -> list[tuple]:
    return list(zip(*np.where(board == 0)))


def get_near_actions(
    board: np.ndarray, last_move: tuple, search_radius: int = 2
) -> list[tuple]:
    if last_move is None:
        return list(zip(*np.where(board == 0)))

    available_actions = []
    last_x, last_y = last_move
    for dx in range(-search_radius, search_radius + 1):
        for dy in range(-search_radius, search_radius + 1):
            x, y = last_x + dx, last_y + dy
            if 0 <= x < board.shape[0] and 0 <= y < board.shape[1] and board[x, y] == 0:
                available_actions.append((x, y))
    return available_actions


def check_winning_line(line: np.ndarray) -> bool:
    count = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1] and line[i] != 0:
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

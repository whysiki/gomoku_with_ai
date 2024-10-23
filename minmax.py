import math
import uuid
import sys
from typing import Tuple, List

sys.setrecursionlimit(1500)


def create_pattern_dict():
    patternDict = {}
    for x in [-1, 1]:
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
    return patternDict


def init_zobrist(N: int):
    return [[[uuid.uuid4().int for _ in range(2)] for j in range(N)] for i in range(N)]


def update_TTable(table, hash, score, depth):
    table[hash] = [score, depth]


class GomokuAI:
    def __init__(self, depth=3, N: int = 15):
        self.board_size: int = N
        self.depth: int = depth
        self.boardMap: List[List[int]] = [[0 for j in range(N)] for i in range(N)]
        self.currentI: int = -1
        self.currentJ: int = -1
        self.nextBound: dict = {}
        self.boardValue: int = 0
        self.turn: int = 0
        self.lastPlayed: int = 0
        self.emptyCells: int = N * N
        self.patternDict: dict = create_pattern_dict()
        self.zobristTable = init_zobrist(self.board_size)
        self.rollingHash = 0
        self.TTable = {}

    def isValid(self, i, j, state=True):
        if i < 0 or i >= self.board_size or j < 0 or j >= self.board_size:
            return False
        if state:
            return self.boardMap[i][j] == 0
        return True

    def countDirection(self, i, j, xdir, ydir, state):
        count = 0
        for step in range(1, 5):
            if xdir != 0 and (
                j + xdir * step < 0 or j + xdir * step >= self.board_size
            ):
                break
            if ydir != 0 and (
                i + ydir * step < 0 or i + ydir * step >= self.board_size
            ):
                break
            if self.boardMap[i + ydir * step][j + xdir * step] == state:
                count += 1
            else:
                break
        return count

    def isFive(self, i, j, state):
        directions = [
            [(-1, 0), (1, 0)],
            [(0, -1), (0, 1)],
            [(-1, 1), (1, -1)],
            [(-1, -1), (1, 1)],
        ]
        for axis in directions:
            axis_count = 1
            for xdir, ydir in axis:
                axis_count += self.countDirection(i, j, xdir, ydir, state)
                if axis_count >= 5:
                    return True
        return False

    def childNodes(self, bound):
        for pos in sorted(bound.items(), key=lambda el: el[1], reverse=True):
            yield pos[0]

    def updateBound(self, new_i, new_j, bound):
        played = (new_i, new_j)
        if played in bound:
            bound.pop(played)
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
            (1, 1),
        ]
        for dir in directions:
            new_col = new_j + dir[0]
            new_row = new_i + dir[1]
            if self.isValid(new_row, new_col) and (new_row, new_col) not in bound:
                bound[(new_row, new_col)] = 0

    def countPattern(self, i_0, j_0, pattern, score, bound, flag):
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1)]
        length = len(pattern)
        count = 0
        for dir in directions:
            if dir[0] * dir[1] == 0:
                steps_back = dir[0] * min(5, j_0) + dir[1] * min(5, i_0)
            elif dir[0] == 1:
                steps_back = min(5, j_0, i_0)
            else:
                steps_back = min(5, self.board_size - 1 - j_0, i_0)
            i_start = i_0 - steps_back * dir[1]
            j_start = j_0 - steps_back * dir[0]
            z = 0
            while z <= steps_back:
                i_new = i_start + z * dir[1]
                j_new = j_start + z * dir[0]
                index = 0
                remember = []
                while (
                    index < length
                    and self.isValid(i_new, j_new, state=False)
                    and self.boardMap[i_new][j_new] == pattern[index]
                ):
                    if self.isValid(i_new, j_new):
                        remember.append((i_new, j_new))
                    i_new = i_new + dir[1]
                    j_new = j_new + dir[0]
                    index += 1
                if index == length:
                    count += 1
                    for pos in remember:
                        if pos not in bound:
                            bound[pos] = 0
                        bound[pos] += flag * score
                    z += index
                else:
                    z += 1
        return count

    def evaluate(self, new_i, new_j, board_value, turn, bound):
        value_before = 0
        value_after = 0
        for pattern in self.patternDict:
            score = self.patternDict[pattern]
            value_before += (
                self.countPattern(new_i, new_j, pattern, abs(score), bound, -1) * score
            )
            self.boardMap[new_i][new_j] = turn
            value_after += (
                self.countPattern(new_i, new_j, pattern, abs(score), bound, 1) * score
            )
            self.boardMap[new_i][new_j] = 0
        return board_value + value_after - value_before

    def alphaBetaPruning(
        self, depth, board_value, bound, alpha, beta, maximizingPlayer
    ):
        if depth <= 0 or (self.checkResult() is not None):
            return board_value
        if (
            self.rollingHash in self.TTable
            and self.TTable[self.rollingHash][1] >= depth
        ):
            return self.TTable[self.rollingHash][0]
        if maximizingPlayer:
            max_val = -math.inf
            for child in self.childNodes(bound):
                i, j = child[0], child[1]
                new_bound = dict(bound)
                new_val = self.evaluate(i, j, board_value, 1, new_bound)
                self.boardMap[i][j] = 1
                self.rollingHash ^= self.zobristTable[i][j][0]
                self.updateBound(i, j, new_bound)
                eval = self.alphaBetaPruning(
                    depth - 1, new_val, new_bound, alpha, beta, False
                )
                if eval > max_val:
                    max_val = eval
                    if depth == self.depth:
                        self.currentI = i
                        self.currentJ = j
                        self.boardValue = eval
                        self.nextBound = new_bound
                alpha = max(alpha, eval)
                self.boardMap[i][j] = 0
                self.rollingHash ^= self.zobristTable[i][j][0]
                del new_bound
                if beta <= alpha:
                    break
            update_TTable(self.TTable, self.rollingHash, max_val, depth)
            return max_val
        else:
            min_val = math.inf
            for child in self.childNodes(bound):
                i, j = child[0], child[1]
                new_bound = dict(bound)
                new_val = self.evaluate(i, j, board_value, -1, new_bound)
                self.boardMap[i][j] = -1
                self.rollingHash ^= self.zobristTable[i][j][1]
                self.updateBound(i, j, new_bound)
                eval = self.alphaBetaPruning(
                    depth - 1, new_val, new_bound, alpha, beta, True
                )
                if eval < min_val:
                    min_val = eval
                    if depth == self.depth:
                        self.currentI = i
                        self.currentJ = j
                        self.boardValue = eval
                        self.nextBound = new_bound
                beta = min(beta, eval)
                self.boardMap[i][j] = 0
                self.rollingHash ^= self.zobristTable[i][j][1]
                del new_bound
                if beta <= alpha:
                    break
            update_TTable(self.TTable, self.rollingHash, min_val, depth)
            return min_val

    def checkResult(self):
        if self.isFive(
            self.currentI, self.currentJ, self.lastPlayed
        ) and self.lastPlayed in (-1, 1):
            return self.lastPlayed
        elif self.emptyCells <= 0:
            return 0
        else:
            return None


def get_best_move(board, player):
    ai = GomokuAI(depth=3)
    ai.boardMap = board
    ai.turn = player
    bound = {}
    for i in range(ai.board_size):
        for j in range(ai.board_size):
            if board[i][j] == 0:
                bound[(i, j)] = 0
    board_value = 0
    for i in range(ai.board_size):
        for j in range(ai.board_size):
            if board[i][j] != 0:
                board_value = ai.evaluate(i, j, board_value, board[i][j], bound)
    print(f"Initial board value: {board_value}")
    ai.alphaBetaPruning(ai.depth, board_value, bound, -math.inf, math.inf, player == 1)
    return ai.currentI, ai.currentJ


if __name__ == "__main__":
    test_board = [[0 for j in range(15)] for i in range(15)]
    test_board[7][7] = 1
    test_board[7][8] = -1

    print(get_best_move(test_board, 1))

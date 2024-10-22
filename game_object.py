from dataclasses import dataclass
import numpy as np
from loguru import logger
import random


@dataclass
class PlayerColor:
    BLACK = "black"
    WHITE = "white"


@dataclass
class PlayerType:
    AI = "ai"
    HUMAN = "human"


@dataclass
class Player:
    name: str
    color: str
    type: str

    def __init__(self, name: str, color: str, type: str):
        if color.strip() not in (PlayerColor.BLACK, PlayerColor.WHITE):
            raise ValueError("Invalid color: {}, must be black or white".format(color))
        self.name = name
        self.color = color
        if type.strip() not in (PlayerType.AI, PlayerType.HUMAN):
            raise ValueError("Invalid type: {}, must be ai or human".format(type))
        self.type = type

    def test_ai_get_action(self, status_matrix: np.ndarray) -> tuple[int, int]:
        # return random.choice(np.argwhere(status_matrix == 0))
        # assert status_matrix.shape == (15, 15)
        if self.type == PlayerType.AI:
            return random.choice(np.argwhere(status_matrix == 0))


class GomokuBoard:
    def __init__(self, canvas):
        self.__canvas = canvas
        self.__canvas__width = self.__canvas.winfo_width()
        self.__canvas__height = self.__canvas.winfo_height()
        self.board_size = 15
        assert (
            self.__canvas__width == self.__canvas__height == 640
        ), "当前棋盘canvas大小必须为 640x640"
        self.__canvas.configure(bg="burlywood")
        self.__canvas.pack()
        self.draw_board()
        self.__status_matrix = np.zeros(
            (self.board_size, self.board_size), dtype=int
        )  # 0: empty, 1: white, -1: black
        self.winner: Player = None
        self.current_player: Player = None
        self.last_player: Player = None
        self.action_done = False
        logger.info("初始化棋盘完成, 接下来请设置当前玩家")

    @property
    def canvas(self):
        return self.__canvas

    @property
    def status_matrix(self):
        return self.__status_matrix

    @property
    def grid_size(self):
        return self.__canvas__width // (self.board_size + 1)
        # return 40

    @property
    def offset(self):
        # return self.grid_size // 2
        # return 40
        return self.grid_size

    def set_current_player(self, curent_player: Player):
        if curent_player != self.last_player:  # 防止重复设置当前玩家
            self.current_player = curent_player
            self.action_done = False
            if self.current_player.type == PlayerType.AI:
                logger.info(
                    f"当前玩家: {self.current_player}" + "AI 玩家, 请等待AI下棋"
                )
            elif self.current_player.type == PlayerType.HUMAN:
                logger.info(
                    f"当前玩家: {self.current_player}" + "人类玩家, 请点击棋盘下棋"
                )
                self.__canvas.bind("<Button-1>", self.__place_a_piece)
            self.last_player = self.current_player

    def clear_board(self):
        self.__canvas.delete("all")
        self.draw_board()
        self.reset_status_matrix()
        self.winner = None
        self.action_done = False
        self.current_player = None
        self.last_player = None
        logger.info("棋盘已清空")

    def reset_status_matrix(self):
        self.__status_matrix = np.zeros((self.board_size, self.board_size), dtype=int)

    def update_status_matrix(self, x: int, y: int, color: str):
        """0: empty, 1: white, -1: black"""
        if color.strip() == PlayerColor.WHITE:
            self.__status_matrix[y][x] = 1
        elif color.strip() == PlayerColor.BLACK:
            self.__status_matrix[y][x] = -1
        else:
            raise ValueError("Invalid color: {}".format(color))

    def draw_board(self):
        for i in range(self.board_size):
            self.__canvas.create_line(
                self.offset,
                self.offset + i * self.grid_size,
                self.offset + (self.board_size - 1) * self.grid_size,
                self.offset + i * self.grid_size,
                fill="black",
            )
            self.__canvas.create_line(
                self.offset + i * self.grid_size,
                self.offset,
                self.offset + i * self.grid_size,
                self.offset + (self.board_size - 1) * self.grid_size,
                fill="black",
            )
            self.__canvas.create_text(
                self.offset - 20,
                self.offset + i * self.grid_size,
                text=str(i + 1),
                anchor="e",
                font=("Arial", 12),
            )
            self.__canvas.create_text(
                self.offset + (self.board_size - 1) * self.grid_size + 20,
                self.offset + i * self.grid_size,
                text=str(i + 1),
                anchor="w",
                font=("Arial", 12),
            )
            self.__canvas.create_text(
                self.offset + i * self.grid_size,
                self.offset - 20,
                text=chr(ord("A") + i),
                anchor="s",
                font=("Arial", 12),
            )
            self.__canvas.create_text(
                self.offset + i * self.grid_size,
                self.offset + (self.board_size - 1) * self.grid_size + 20,
                text=chr(ord("A") + i),
                anchor="n",
                font=("Arial", 12),
            )

    def get_coordinate_text_for_index(
        self, index_x: int, index_y: int
    ) -> tuple[str, str]:
        return chr(ord("A") + index_x), str(index_y + 1)

    def __caculate_place_oval_coordinate(
        self, index_x: int, index_y: int
    ) -> tuple[int, int]:
        """从棋盘坐标转换为画布坐标"""
        x = index_x * self.grid_size + self.offset
        y = index_y * self.grid_size + self.offset
        return x, y

    def __place_oval(self, index_x: int, index_y: int):
        """
        由棋盘坐标放置棋子
        """
        text_x, text_y = self.get_coordinate_text_for_index(index_x, index_y)
        fill: str = self.current_player.color
        # 如果当前棋盘位置已经有棋子，则不再绘制
        if self.__status_matrix[index_y][index_x] != 0:
            logger.debug(
                "当前位置: {}={} 已经有棋子, 颜色: {}".format(
                    (index_x, index_y), (text_x, text_y), fill
                )
            )
            return
        else:
            x, y = self.__caculate_place_oval_coordinate(index_x, index_y)
            self.__canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=fill)
            logger.debug(
                "当前位置: {}={} 绘制棋子完成, 颜色: {}".format(
                    (index_x, index_y),
                    (text_x, text_y),
                    fill,
                )
            )
            self.update_status_matrix(index_x, index_y, fill)

        if self.__check_win(index_x, index_y):
            logger.info(f"{self.current_player} 胜利")
            self.winner = self.current_player

    def action(self, index_x: int, index_y: int):
        """执行下棋操作"""
        if self.winner:
            logger.info(f"{self.winner} 已经胜利, 请重新开始游戏")
            return
        self.__place_oval(index_x, index_y)
        self.action_done = True

    def __place_a_piece(self, event):
        """点击棋盘下棋"""
        if self.winner:
            logger.info(f"{self.winner} 已经胜利, 请重新开始游戏")
            return
        if self.current_player:
            if self.current_player.type == PlayerType.HUMAN:
                x = (
                    round((event.x - self.offset) / self.grid_size) * self.grid_size
                    + self.offset
                )
                y = (
                    round((event.y - self.offset) / self.grid_size) * self.grid_size
                    + self.offset
                )

                index_x = round((x - self.offset) / self.grid_size)
                index_y = round((y - self.offset) / self.grid_size)

                self.action(index_x, index_y)

            else:
                logger.warning("当前玩家不是人类玩家, 请等待AI下棋")
        else:
            logger.warning("请先设置当前玩家")

    def __check_win(self, index_x, index_y):
        x, y = index_x, index_y
        color = self.__status_matrix[y][x]
        directions = [
            (1, 0),  # 水平
            (0, 1),  # 垂直
            (1, 1),  # 主对角线
            (1, -1),  # 副对角线
        ]

        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                if (
                    0 <= x + i * dx < self.board_size
                    and 0 <= y + i * dy < self.board_size
                    and self.__status_matrix[y + i * dy][x + i * dx] == color
                ):
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if (
                    0 <= x - i * dx < self.board_size
                    and 0 <= y - i * dy < self.board_size
                    and self.__status_matrix[y - i * dy][x - i * dx] == color
                ):
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

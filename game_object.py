from dataclasses import dataclass
import numpy as np
from loguru import logger


@dataclass
class Player:
    name: str
    color: str

    def __init__(self, name: str, color: str):
        if color.strip() not in ["black", "white"]:
            raise ValueError("Invalid color: {}, must be black or white".format(color))
        self.name = name
        self.color = color


class GomokuBoard:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.configure(bg="burlywood")
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.place_white_piece)
        self.status_matrix = np.zeros(
            (15, 15), dtype=int
        )  # 0: empty, 1: white, -1: black
        self.winner: Player = None
        logger.info("初始化棋盘完成, 接下来请设置当前玩家")

    def set_current_player(self, curent_player: Player):
        self.current_player = curent_player
        logger.info(f"当前玩家: {self.current_player}")

    def reset_status_matrix(self):
        self.status_matrix = np.zeros((15, 15), dtype=int)

    def clear_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.reset_status_matrix()
        self.winner = None
        logger.info("棋盘已清空")

    def update_status_matrix(self, x: int, y: int, color: str):
        if color.strip() == "white".strip():
            self.status_matrix[y][x] = 1
        elif color.strip() == "black".strip():
            self.status_matrix[y][x] = -1
        else:
            raise ValueError("Invalid color: {}".format(color))

    def draw_board(self):
        self.grid_size = 40
        self.offset = 40
        self.board_size = 15
        for i in range(self.board_size):
            self.canvas.create_line(
                self.offset,
                self.offset + i * self.grid_size,
                self.offset + (self.board_size - 1) * self.grid_size,
                self.offset + i * self.grid_size,
                fill="black",
            )
            self.canvas.create_line(
                self.offset + i * self.grid_size,
                self.offset,
                self.offset + i * self.grid_size,
                self.offset + (self.board_size - 1) * self.grid_size,
                fill="black",
            )
            self.canvas.create_text(
                self.offset - 20,
                self.offset + i * self.grid_size,
                text=str(i + 1),
                anchor="e",
                font=("Arial", 12),
            )
            self.canvas.create_text(
                self.offset + (self.board_size - 1) * self.grid_size + 20,
                self.offset + i * self.grid_size,
                text=str(i + 1),
                anchor="w",
                font=("Arial", 12),
            )
            self.canvas.create_text(
                self.offset + i * self.grid_size,
                self.offset - 20,
                text=chr(ord("A") + i),
                anchor="s",
                font=("Arial", 12),
            )
            self.canvas.create_text(
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

    def place_white_piece(self, event):
        if self.winner:
            logger.info(f"{self.winner} 已经胜利, 请重新开始游戏")
            return
        fill: str = self.current_player.color
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

        text_x, text_y = self.get_coordinate_text_for_index(index_x, index_y)

        # 如果当前棋盘位置已经有棋子，则不再绘制
        if self.status_matrix[index_y][index_x] != 0:
            logger.debug(
                "当前位置: {}={} 已经有棋子, 颜色: {}".format(
                    (index_x, index_y), (text_x, text_y), fill
                )
            )
            return
        else:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=fill)
            logger.debug(
                "当前位置: {}={} 绘制棋子完成, 颜色: {}".format(
                    (index_x, index_y),
                    (text_x, text_y),
                    fill,
                )
            )
            self.update_status_matrix(index_x, index_y, fill)

        if self.check_win(index_x, index_y):
            logger.info(f"{self.current_player} 胜利")
            self.winner = self.current_player

    def check_win(self, x, y):
        color = self.status_matrix[y][x]
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
                    and self.status_matrix[y + i * dy][x + i * dx] == color
                ):
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if (
                    0 <= x - i * dx < self.board_size
                    and 0 <= y - i * dy < self.board_size
                    and self.status_matrix[y - i * dy][x - i * dx] == color
                ):
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

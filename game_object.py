from dataclasses import dataclass
import numpy as np
from loguru import logger
from ai_actions import *
from ai_s import AlphaBetaGomokuAI


@dataclass
class PlayerColor:
    BLACK = "black"
    WHITE = "white"
    COLOR_NUM_DICT = {"black": -1, "white": 1}


@dataclass
class PlayerType:
    AI = "ai"
    HUMAN = "human"
    NONE = "none"


@dataclass
class Player:
    name: str
    color: str
    type: str

    def __init__(self, name: str, color: str, type: str, airank: int = 0):
        if color.strip() not in (PlayerColor.BLACK, PlayerColor.WHITE):
            raise ValueError("Invalid color: {}, must be black or white".format(color))
        self.name = name
        self.color = color
        if type.strip() not in (PlayerType.AI, PlayerType.HUMAN):
            raise ValueError("Invalid type: {}, must be ai or human".format(type))
        self.type = type
        self.ai = None
        if self.type == PlayerType.AI:
            if airank == 0:
                self.ai = FoolishGomokuAI(PlayerColor.COLOR_NUM_DICT[self.color])
            elif airank == 1:
                self.ai = AlphaBetaGomokuAI(
                    PlayerColor.COLOR_NUM_DICT[self.color], depth=2
                )
            else:
                raise ValueError("Invalid airank: {}, must be 0 or 1".format(airank))

    def test_ai_get_action(self, status_matrix: np.ndarray) -> tuple[int, int]:
        if self.type == PlayerType.AI:
            return self.ai.get_best_action(status_matrix)
        else:
            raise ValueError("当前玩家不是AI玩家")


class GomokuBoard:
    def __init__(self, canvas):
        self.__canvas = canvas
        self.__canvas__width = self.__canvas.winfo_width()
        self.__canvas__height = self.__canvas.winfo_height()
        self.board_size = 15
        assert self.__canvas__width == self.__canvas__height, "棋盘canvas必须是正方形"
        self.__canvas.configure(bg="burlywood")
        self.__canvas.pack()
        self.draw_board()
        self.__status_matrix = np.zeros((self.board_size, self.board_size), dtype=int)
        self.winner: Player | str = None
        self.current_player: Player = None
        self.last_player: Player = None
        self.action_done = False
        self.last_piece_color = None
        logger.info("初始化棋盘完成, 接下来请设置当前玩家")

    @property
    def isfullzero(self):
        return not np.any(self.__status_matrix != 0)  # 没有非0元素

    @property
    def canvas(self):
        return self.__canvas

    @property
    def status_matrix(self):
        return self.__status_matrix

    @property
    def grid_size(self):
        return self.__canvas__width // (self.board_size + 1)

    @property
    def offset(self):
        return self.grid_size

    def set_current_player(self, curent_player: Player):
        assert curent_player and isinstance(curent_player, Player), "设置的玩家非法"
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
                self.__canvas.bind("<Button-1>", self.__human_place_a_piece)
            self.last_player = self.current_player
        else:
            # logger.warning("玩家不能连续下棋")
            pass

    def clear_board(self):
        self.__canvas.delete("all")
        self.draw_board()
        self.reset_status_matrix()
        self.winner = None
        self.action_done = False
        self.current_player = None
        self.last_player = None
        self.last_piece_color = None
        logger.info("棋盘已清空")

    def reset_status_matrix(self):
        self.__status_matrix = np.zeros((self.board_size, self.board_size), dtype=int)

    def update_status_matrix(self, x: int, y: int, color: str):
        """0: empty, 1: white, -1: black"""
        if color in PlayerColor.COLOR_NUM_DICT.keys():
            self.__status_matrix[y][x] = PlayerColor.COLOR_NUM_DICT[color]
        else:
            raise ValueError("Invalid color: {}, must be black or white".format(color))
        if not np.any(self.__status_matrix == 0):
            logger.warning("棋盘已满, 平局")
            self.winner = "平局".strip()

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
        # 检查是否越界
        if not (0 <= index_x < self.board_size and 0 <= index_y < self.board_size):
            logger.error("当前位置: {}={} 超出棋盘范围".format((index_x, index_y)))
            return
        text_x, text_y = self.get_coordinate_text_for_index(index_x, index_y)
        fill: str = self.current_player.color
        # 如果当前棋盘位置已经有棋子，则不再绘制
        if self.__status_matrix[index_y][index_x] != 0:
            logger.warning(
                "当前位置: {}={} 已经有棋子, 颜色: {}".format(
                    (index_x, index_y), (text_x, text_y), fill
                )
            )
            return
        else:
            x, y = self.__caculate_place_oval_coordinate(index_x, index_y)
            self.__canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=fill)

            # Remove previous AI markers
            if self.current_player.type == PlayerType.AI:
                self.__canvas.delete("ai_marker")

            if self.current_player.type == PlayerType.AI:
                self.__canvas.create_oval(
                    x - 10,
                    y - 10,
                    x + 10,
                    y + 10,
                    outline="red",
                    width=2,
                    tags="ai_marker",
                )

            logger.debug(
                "当前位置: {}={} 绘制棋子完成, 颜色: {}".format(
                    (index_x, index_y),
                    (text_x, text_y),
                    fill,
                )
            )
            self.last_piece_color = fill
            self.update_status_matrix(index_x, index_y, fill)
            self.action_done = True

        if self.__check_win(index_x, index_y):
            logger.info(f"{self.current_player} 胜利")
            self.winner = self.current_player

    def action(self, index_x: int, index_y: int):
        """执行下棋操作"""
        if self.winner:
            logger.info(f"{self.winner} 已经胜利, 请重新开始游戏")
            return
        if (not self.last_piece_color) or (
            self.last_piece_color != self.current_player.color
        ):
            self.__place_oval(index_x, index_y)
        else:
            logger.warning(
                f"玩家{self.current_player}不能连续下棋, 你的颜色是: {self.current_player.color}, 上一步棋子颜色是: {self.last_piece_color}"
            )

    def __human_place_a_piece(self, event):
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
        """检查下的这一步是否赢"""
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

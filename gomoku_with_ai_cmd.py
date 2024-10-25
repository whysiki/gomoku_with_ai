# coding=utf-8
import sys
import os
from os.path import abspath, dirname
from tkinter import messagebox, simpledialog

sys.path.insert(0, abspath(dirname(__file__)))
import tkinter
from tkinter import *
import Fun
from rich import print
from loguru import logger
from game_object import Player, GomokuBoard, PlayerColor, PlayerType
import threading
import os
import winsound
import time

uiName = "gomoku_with_ai"
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}


logger.add(
    f"{Fun.G_ExeDir}/log/gomoku_with_ai.log",
    rotation="10 MB",
    mode="a",
    encoding="utf-8",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
)

# 清除日志
# logger.remove()

gbd = None
is_priority = True


class TimeCounter:

    def __init__(self):
        self.total_time_start = None
        self.player_time_start = None
        self.ai_time_start = None

    @property
    def player_time_elapsed(self):
        if self.player_time_start:
            return time.time() - self.player_time_start
        else:
            return 0

    @property
    def ai_time_elapsed(self):
        if self.ai_time_start:
            return time.time() - self.ai_time_start
        else:
            return 0

    @property
    def total_time_elapsed(self):
        if self.total_time_start:
            return time.time() - self.total_time_start
        else:
            return 0

    def start_total_time(self):
        self.total_time_start = time.time()

    def start_player_time(self):
        self.player_time_start = time.time()

    def start_ai_time(self):
        self.ai_time_start = time.time()

    def get_total_time(self):
        # 当前总用时 - 总开始用时
        return int(self.total_time_elapsed)

    def get_player_time(self):
        # 当前玩家用时 - 玩家开始用时
        return int(self.player_time_elapsed)

    def get_ai_time(self):
        # 当前AI用时 - AI开始用时
        return int(self.ai_time_elapsed)

    def reset(self):
        self.total_time_start = None
        self.player_time_start = None
        self.ai_time_start = None

    def print(self):
        print(f"total_time_start: {self.total_time_start}")
        print(f"player_time_start: {self.player_time_start}")
        print(f"ai_time_start: {self.ai_time_start}")
        print(f"total_time_elapsed: {self.total_time_elapsed}")
        print(f"player_time_elapsed: {self.player_time_elapsed}")
        print(f"ai_time_elapsed: {self.ai_time_elapsed}")


time_counter = TimeCounter()


def Form_1_onLoad(uiName, threadings=0):
    global gbd
    if gbd and isinstance(gbd, GomokuBoard):
        gbd.clear_board()
    canvas = Fun.GetElement(uiName, "Canvas_1")
    gbd = GomokuBoard(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    Fun.SetCurrentValue(uiName, "SwitchButton_1", True)
    Fun.SetVisible(uiName, "Button_1", False)
    Fun.SetVisible(uiName, "Label_2", Visible=True)
    Fun.SetText(uiName, "Label_5", "0")  # 总用时
    Fun.SetText(uiName, "Label_6", "0")  # AI用时
    Fun.SetText(uiName, "Label_7", "0")  # 玩家用时
    gbd.canvas.create_text(
        width // 2,
        height // 2,
        text="请点击开始游戏",
        font=("Segoe UI", 30, "bold"),
        fill="red",
        tag="start_tip_text",
    )
    print(f"GomokuBoard , width: {width}, height: {height}")  # 640, 640
    # Start the timer update loop
    threading.Thread(target=update_time_labels_loop, daemon=True).start()


def update_time_labels():
    total_time = time_counter.get_total_time()
    ai_time = time_counter.get_ai_time()
    player_time = time_counter.get_player_time()
    # print(f"total_time: {total_time}, ai_time: {ai_time}, player_time: {player_time}")
    Fun.SetText(uiName, "Label_5", f"{total_time}s")  # 总用时
    Fun.SetText(uiName, "Label_6", f"{ai_time}s")  # AI用时
    Fun.SetText(uiName, "Label_7", f"{player_time}s")  # 玩家用时


def reset_time_labels():
    Fun.SetText(uiName, "Label_5", "0")  # 总用时
    Fun.SetText(uiName, "Label_6", "0")  # AI用时
    Fun.SetText(uiName, "Label_7", "0")  # 玩家用时


def update_time_labels_loop():
    last_player_type = None
    while True:
        if gbd:
            if last_player_type != (
                gbd.current_player.type if gbd.current_player else None
            ):
                # 切换玩家
                if gbd.current_player and gbd.current_player.type == PlayerType.AI:
                    time_counter.player_time_start = None  # 玩家计时清零
                    time_counter.start_ai_time()  # 开始AI计时
                    # print("AI开始计时")
                elif gbd.current_player and gbd.current_player.type == PlayerType.HUMAN:
                    time_counter.ai_time_start = None  # AI计时清零
                    time_counter.start_player_time()  # 开始玩家计时
                    # print("玩家开始计时")
                last_player_type = (
                    gbd.current_player.type if gbd.current_player else None
                )

            # if gbd.isfullzero and not gbd.winner and gbd.current_player:
            # time_counter.start_total_time()
            # print("总时间开始计时")

            if gbd.current_player and not gbd.winner:
                update_time_labels()  # 更新时间标签
                # time_counter.print()
            time.sleep(0.5)  # 增加UI更新频率


def process_winner():
    Fun.SetVisible(uiName, "Button_1", True)  # 设置重新开始按钮可见
    if gbd.winner:
        if gbd.winner.type == PlayerType.HUMAN:
            Fun.MessageBox(f"恭喜{gbd.winner.name}获胜", type="info")
        elif gbd.winner.type == PlayerType.AI:
            Fun.MessageBox("再接再力", type="error")
        elif gbd.winner == "平局".strip():
            Fun.MessageBox("平局", type="info")
        time_counter.reset()
        # reset_time_labels()


def play_click_sound():
    pass
    threading.Thread(
        target=winsound.PlaySound,
        args=(f"{Fun.G_ExeDir}/static/sounds/rclick-13693.wav", winsound.SND_ASYNC),
    ).start()


def run_gbd(is_priority):
    gbd.current_player = None
    player = Player(
        name="Player",
        color=PlayerColor.BLACK,
        type=PlayerType.HUMAN,
    )
    ai_player = Player(
        name="AI",
        color=PlayerColor.WHITE,
        type=PlayerType.AI,
        airank=1,
    )

    def player_turn():
        if gbd.winner:
            process_winner()
            return
        gbd.set_current_player(player)
        if not gbd.action_done:
            gbd.canvas.after(100, player_turn)  # 继续等待玩家动作
        else:
            play_click_sound()
            threading.Thread(target=ai_turn).start()

    def ai_turn():
        if gbd.winner:
            process_winner()
            return
        gbd.set_current_player(ai_player)
        if not gbd.action_done:
            ai_action = ai_player.test_ai_get_action(gbd.status_matrix.T)
            gbd.action(*ai_action)
            gbd.canvas.after(100, player_turn)  # 切换到玩家动作

    if is_priority:
        player_turn()
    else:
        threading.Thread(target=ai_turn).start()


# 开始游戏
def Button_2_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None:
        gbd.clear_board()
        is_priority_work = is_priority
        time_counter.reset()
        reset_time_labels()
        time_counter.start_total_time()
        threading.Thread(target=run_gbd, args=(is_priority_work,)).start()


# 重新开始
def Button_1_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None:
        gbd.clear_board()
        is_priority_work = is_priority
        time_counter.reset()
        reset_time_labels()
        time_counter.start_total_time()
        threading.Thread(target=run_gbd, args=(is_priority_work,)).start()
    Fun.SetVisible(uiName, "Button_1", False)


# 是否先手
def SwitchButton_1_onSwitch(uiName, widgetName, value, threadings=0):
    global is_priority
    is_priority = value
    if gbd is not None:
        gbd.clear_board()
        time_counter.reset()
        reset_time_labels()
        Fun.MessageBox("请重新点击开始游戏", type="info")
    Fun.SetVisible(uiName, "Button_1", False)

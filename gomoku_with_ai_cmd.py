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
import queue
from time_count_ import TimeCounter

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
gbd_global = None
is_priority_global = True
time_counter_global = TimeCounter()
turn_queue_global = queue.Queue()
turn_last_name_global = None
is_continue_queue_global = False


class Competitors:

    def __init__(self):
        self.player1 = Player(
            name="Player",
            color=PlayerColor.WHITE,
            type=PlayerType.HUMAN,
        )

        self.player2 = Player(
            name="AI",
            color=PlayerColor.BLACK,
            type=PlayerType.AI,
            airank=2,
        )


CompetitorsGlobal = Competitors()


def update_time_labels():
    total_time = time_counter_global.get_total_time()
    ai_time = time_counter_global.get_ai_time()
    player_time = time_counter_global.get_player_time()
    Fun.SetText(uiName, "Label_5", f"{total_time}s")  # 总用时
    Fun.SetText(uiName, "Label_6", f"{ai_time}s")  # AI用时
    Fun.SetText(uiName, "Label_7", f"{player_time}s")  # 玩家用时


def reset_time_labels():
    Fun.SetText(uiName, "Label_5", "0")  # 总用时
    Fun.SetText(uiName, "Label_6", "0")  # AI用时
    Fun.SetText(uiName, "Label_7", "0")  # 玩家用时


def update_time_labels_main_loop():
    last_player_type = None

    def update():
        nonlocal last_player_type
        if gbd_global:
            current_player_type = (
                gbd_global.current_player.type if gbd_global.current_player else None
            )

            if last_player_type != current_player_type:
                # 切换玩家
                if (
                    gbd_global.current_player
                    and gbd_global.current_player.type == PlayerType.AI
                ):
                    time_counter_global.player_time_start = None  # 玩家计时清零
                    time_counter_global.start_ai_time()  # 开始AI计时
                elif (
                    gbd_global.current_player
                    and gbd_global.current_player.type == PlayerType.HUMAN
                ):
                    time_counter_global.ai_time_start = None  # AI计时清零
                    time_counter_global.start_player_time()  # 开始玩家计时

                last_player_type = current_player_type

            if gbd_global.current_player and not gbd_global.winner:
                update_time_labels()  # 更新时间标签

        gbd_global.canvas.after(500, update)

    update()


def process_turn_queue_main_loop():

    global is_continue_queue_global
    print("process_turn_queue start")
    process_winner_task_executed = False

    def process_turn_queue():
        global turn_last_name_global
        nonlocal process_winner_task_executed
        if gbd_global and not gbd_global.winner and is_continue_queue_global:
            if not turn_queue_global.empty():
                turn = turn_queue_global.get()
                if turn.__name__ != turn_last_name_global:
                    print(f"process_turn_queue {turn.__name__}")
                    turn()
                    turn_last_name_global = turn.__name__
            process_winner_task_executed = False  # 任务未执行
        if gbd_global.winner and not process_winner_task_executed:
            process_winner()
            process_winner_task_executed = True  # 任务已执行

        gbd_global.canvas.after(500, process_turn_queue)

    process_turn_queue()


def process_winner():
    Fun.SetVisible(uiName, "Button_1", True)  # 设置重新开始按钮可见
    if gbd_global.winner:
        if gbd_global.winner.type == PlayerType.HUMAN:
            Fun.MessageBox(f"恭喜{gbd_global.winner.name}获胜", type="info")
        elif gbd_global.winner.type == PlayerType.AI:
            Fun.MessageBox("再接再力", type="error")
        elif gbd_global.winner == "平局".strip():
            Fun.MessageBox("平局", type="info")
        time_counter_global.reset()  # 重置时间


def play_click_sound():
    threading.Thread(
        target=winsound.PlaySound,
        args=(f"{Fun.G_ExeDir}/static/sounds/rclick-13693.wav", winsound.SND_ASYNC),
    ).start()


def run_gbd(is_priority):
    gbd_global.current_player = None

    def player_turn():
        gbd_global.set_current_player(CompetitorsGlobal.player1)
        if not gbd_global.action_done:
            gbd_global.canvas.after(100, player_turn)
        else:
            play_click_sound()
            turn_queue_global.put(ai_turn)

    def ai_turn():
        gbd_global.set_current_player(CompetitorsGlobal.player2)
        if not gbd_global.action_done:
            if (
                CompetitorsGlobal.player2.airank == 1
                or CompetitorsGlobal.player2.airank == 2
            ):
                ai_action = CompetitorsGlobal.player2.test_ai_get_action(
                    gbd_global.status_matrix.T
                )
            if CompetitorsGlobal.player2.airank == 0:
                ai_action = CompetitorsGlobal.player2.test_ai_get_action(
                    gbd_global.status_matrix
                )
            gbd_global.action(*ai_action)
            gbd_global.canvas.after(100, lambda: turn_queue_global.put(player_turn))

    if is_priority:
        turn_queue_global.put(player_turn)
    else:
        turn_queue_global.put(ai_turn)


def free_run_gbd_queue():
    global turn_last_name_global
    global turn_queue_global
    global is_continue_queue_global
    while not turn_queue_global.empty():  # 清空队列
        turn_queue_global.get()
    turn_last_name_global = None  # 重置上一次的函数名
    is_continue_queue_global = False  # 重置是否继续队列


def start_game_handler(is_run_gbd=True):
    global is_continue_queue_global
    if gbd_global is not None:
        gbd_global.clear_board()  # 清空棋盘
        is_priority_work = is_priority_global  # 是否先手
        time_counter_global.reset()  # 重置时间
        reset_time_labels()  # 重置时间标签
        time_counter_global.start_total_time()  # 开始总时间计时
        free_run_gbd_queue()  # 清空队列
        gbd_global.clear_board()  # 清空棋盘
        if is_run_gbd:
            is_continue_queue_global = True
            run_gbd(is_priority_work)  # 开始交互队列


def refresh_gime(tip: str, type="info"):
    if gbd_global is not None:
        gbd_global.clear_board()
        time_counter_global.reset()
        reset_time_labels()
        free_run_gbd_queue()
        gbd_global.clear_board()  # 清空棋盘
        Fun.MessageBox(tip, type=type)
    Fun.SetVisible(uiName, "Button_1", False)


# 开始游戏加载事件
def Form_1_onLoad(uiName, threadings=0):
    global gbd_global
    if gbd_global and isinstance(gbd_global, GomokuBoard):
        gbd_global.clear_board()
    canvas = Fun.GetElement(uiName, "Canvas_1")
    gbd_global = GomokuBoard(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    Fun.SetCurrentValue(uiName, "SwitchButton_1", True)
    Fun.SetVisible(uiName, "Button_1", False)
    Fun.SetVisible(uiName, "Label_2", Visible=True)
    Fun.SetText(uiName, "Label_5", "0")  # 总用时
    Fun.SetText(uiName, "Label_6", "0")  # AI用时
    Fun.SetText(uiName, "Label_7", "0")  # 玩家用时
    Fun.SetBGColor(uiName, "Label_11", "#5D9CEC")  # TorchDeep
    gbd_global.canvas.create_text(
        width // 2,
        height // 2,
        text="请点击开始游戏",
        font=("Segoe UI", 30, "bold"),
        fill="red",
        tag="start_tip_text",
    )
    print(f"GomokuBoard , width: {width}, height: {height}")  # 640, 640
    threading.Thread(
        target=update_time_labels_main_loop, daemon=True
    ).start()  # 时间更新线程
    threading.Thread(
        target=process_turn_queue_main_loop, daemon=True
    ).start()  # 下子线程


# 开始游戏按钮
def Button_2_onCommand(uiName, widgetName, threadings=0):
    start_game_handler()


# 重新开始按钮
def Button_1_onCommand(uiName, widgetName, threadings=0):
    start_game_handler()
    Fun.SetVisible(uiName, "Button_1", False)


# 是否先手开关
def SwitchButton_1_onSwitch(uiName, widgetName, value, threadings=0):
    global is_priority_global
    is_priority_global = value
    refresh_gime("请重新点击开始游戏")


# 是否换色
def SwitchButton_2_onSwitch(uiName, widgetName, value, threadings=0):
    refresh_gime("请重新点击开始游戏")
    temp_color = CompetitorsGlobal.player1.color
    CompetitorsGlobal.player1.color = CompetitorsGlobal.player2.color
    CompetitorsGlobal.player2.color = temp_color


# 选择AI等级
def switch_ai_level(player, level):
    if level == 0:
        Fun.SetBGColor(uiName, "Label_9", "#5D9CEC")  # FoolishAI
        Fun.SetBGColor(uiName, "Label_10", "#EC87C0")  # AlphaBeta
        Fun.SetBGColor(uiName, "Label_11", "#EC87C0")  # TorchDeep
    elif level == 1:
        Fun.SetBGColor(uiName, "Label_9", "#EC87C0")  # FoolishAI
        Fun.SetBGColor(uiName, "Label_10", "#5D9CEC")  # AlphaBeta
        Fun.SetBGColor(uiName, "Label_11", "#EC87C0")  # TorchDeep
    elif level == 2:
        Fun.SetBGColor(uiName, "Label_9", "#EC87C0")  # FoolishAI
        Fun.SetBGColor(uiName, "Label_10", "#EC87C0")  # AlphaBeta
        Fun.SetBGColor(uiName, "Label_11", "#5D9CEC")  # TorchDeep
    player.airank = level


# FoolishAI按钮
def Label_9_onButton1(event, uiName, widgetName, threadings=0):
    switch_ai_level(CompetitorsGlobal.player2, 0)
    refresh_gime("已切换到FoolishAI,请重新点击开始游戏")


# AlphaBeta按钮
def Label_10_onButton1(event, uiName, widgetName, threadings=0):
    switch_ai_level(CompetitorsGlobal.player2, 1)
    refresh_gime("已切换到AlphaBeta,请重新点击开始游戏")


# TorchDeep按钮
def Label_11_onButton1(event, uiName, widgetName, threadings=0):
    switch_ai_level(CompetitorsGlobal.player2, 2)
    refresh_gime("已切换到TorchDeep,请重新点击开始游戏")

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

uiName = "gomoku_with_ai"
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}


logger.add(
    "log/gomoku_with_ai.log",
    rotation="10 MB",
    mode="a",
    encoding="utf-8",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}",
)

gbd = None
is_priority = True


# Form 'Form_1's Load Event :
def Form_1_onLoad(uiName, threadings=0):
    global gbd
    if not gbd:
        Fun.MessageBox("点击开始进行游戏")
    if gbd and isinstance(gbd, GomokuBoard):
        gbd.clear_board()
    canvas = Fun.GetElement(uiName, "Canvas_1")
    gbd = GomokuBoard(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    # hide restart button
    Fun.SetCurrentValue(uiName, "SwitchButton_1", True)
    Fun.SetVisible(uiName, "Button_1", False)
    print(f"GomokuBoard , width: {width}, height: {height}")  # 640, 640


def process_winner():
    if gbd.winner:
        if gbd.winner.type == PlayerType.HUMAN:
            Fun.MessageBox("你赢了", type="info")
        else:
            Fun.MessageBox("再接再力", type="error")


def run_gbd(is_priority):
    gbd.current_player = None
    player = Player(
        name="Player",
        color=PlayerColor.WHITE,
        type=PlayerType.HUMAN,
    )
    ai_player = Player(
        name="AI",
        color=PlayerColor.BLACK,
        type=PlayerType.AI,
    )

    def player_turn():
        if gbd.winner:
            Fun.SetVisible(uiName, "Button_1", True)
            process_winner()
            return

        gbd.set_current_player(player)
        if not gbd.action_done:
            gbd.canvas.after(100, player_turn)  # 继续等待玩家动作
        else:
            ai_turn()

    def ai_turn():
        if gbd.winner:
            Fun.SetVisible(uiName, "Button_1", True)
            process_winner()
            return
        gbd.set_current_player(ai_player)
        if not gbd.action_done:
            status_matrix = gbd.status_matrix
            ai_action = ai_player.test_ai_get_action(status_matrix, rank=1)
            gbd.action(*ai_action)
            gbd.canvas.after(100, player_turn)  # 切换到玩家动作

    if is_priority:
        player_turn()
    else:
        ai_turn()


# Start Game
def Button_2_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None and gbd.current_player is None:
        # 开启线程
        is_priority_work = is_priority
        threading.Thread(target=run_gbd, args=(is_priority_work,)).start()


# restart
def Button_1_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None:
        gbd.clear_board()
        is_priority_work = is_priority

        threading.Thread(target=run_gbd, args=(is_priority_work,)).start()
    Fun.SetVisible(uiName, "Button_1", False)


# isis_priority
def SwitchButton_1_onSwitch(uiName, widgetName, value, threadings=0):
    global is_priority
    is_priority = value
    if gbd is not None:
        gbd.clear_board()
        is_priority_work = is_priority
        threading.Thread(target=run_gbd, args=(is_priority_work,)).start()
    Fun.SetVisible(uiName, "Button_1", False)

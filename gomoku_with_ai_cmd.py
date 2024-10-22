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
    canvas = Fun.GetElement(uiName, "Canvas_1")
    gbd = GomokuBoard(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    print(f"GomokuBoard , width: {width}, height: {height}")  # 640, 640


# Button 'Button_1' 's Command Event :
# Restart Game
def Button_1_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None:
        gbd.clear_board()
        threading.Thread(target=run_gbd, args=(is_priority,)).start()


def run_gbd(is_priority):
    player = Player(
        name="Player",
        color=PlayerColor.WHITE if is_priority else PlayerColor.BLACK,
        type=PlayerType.HUMAN,
    )
    ai_player = Player(
        name="AI",
        color=PlayerColor.BLACK if is_priority else PlayerColor.WHITE,
        type=PlayerType.AI,
    )

    def player_turn():
        if gbd.winner:
            return

        gbd.set_current_player(player)
        if not gbd.action_done:
            gbd.canvas.after(100, player_turn)  # 继续等待玩家动作
        else:
            ai_turn()

    def ai_turn():
        if gbd.winner:
            return
        gbd.set_current_player(ai_player)
        if not gbd.action_done:
            status_matrix = gbd.status_matrix
            ai_action = ai_player.test_ai_get_action(status_matrix)
            gbd.action(*ai_action)
            gbd.canvas.after(100, player_turn)  # 切换到玩家动作

    if is_priority:
        player_turn()
    else:
        ai_turn()


# Button 'Button_2' 's Command Event :
# Start Game
def Button_2_onCommand(uiName, widgetName, threadings=0):
    if gbd is not None:
        # 选择先手
        response = messagebox.askquestion(
            "选择先手",
            "是否选择先手？\n是 (Yes) 代表先手\n否 (No) 代表后手",
            icon="question",
            type="yesno",
            default="yes",
        )
        is_priority = response == "yes"

        # 开启线程
        threading.Thread(target=run_gbd, args=(is_priority,)).start()

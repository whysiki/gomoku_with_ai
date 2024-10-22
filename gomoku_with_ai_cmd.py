# coding=utf-8
import sys
import os
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(__file__)))
import tkinter
from tkinter import *
import Fun
from rich import print
from loguru import logger
from game_object import Player, GomokuBoard

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


# Form 'Form_1's Load Event :
def Form_1_onLoad(uiName, threadings=0):
    global gbd
    canvas = Fun.GetElement(uiName, "Canvas_1")
    gbd = GomokuBoard(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    print(f"GomokuBoard , width: {width}, height: {height}")  # 640, 640
    player1 = Player("player1", "white")
    AI = Player("AI", "black")
    gbd.set_current_player(player1)


# Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName, widgetName, threadings=0):
    gbd.clear_board()

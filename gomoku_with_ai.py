# coding=utf-8
# import libs
import sys
import os
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(__file__)))
import gomoku_with_ai_cmd
import gomoku_with_ai_sty
import Fun
import tkinter
from tkinter import *
import tkinter.ttk
import tkinter.font
from PIL import Image, ImageTk


# Add your Varial Here: (Keep This Line of comments)
# Define UI Class
class gomoku_with_ai:
    def __init__(self, root, isTKroot=True, params=None):
        uiName = Fun.GetUIName(root, self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName, "UIClass", self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName] = params
        Fun.G_UICommandDictionary[uiName] = gomoku_with_ai_cmd
        Fun.Register(uiName, "root", root)
        style = gomoku_with_ai_sty.SetupStyle(isTKroot)
        self.UIJsonString = '{"Version": "1.0.0", "UIName": "gomoku_with_ai", "Description": "", "WindowSize": [960, 717], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": true, "WindowTitle": "五子棋AI对战", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": true, "MinSize": [0, 0], "TransparentColor": null, "RootTransparency": 255, "ICOFile": null, "WinState": 1, "WinTopMost": false, "BGColor": "#EFEFEF", "GroupList": {}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#EFEFEF", "Size": [960, 717], "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Canvas", "Index": 2, "AliasName": "Canvas_1", "ParentName": "Form_1", "PlaceInfo": [160, 40, 640, 640, "nw", true, true], "Visible": true, "Size": [640, 640], "BGColor": "#EFEFEF", "Relief": "flat", "BorderWidth": 1, "BorderColor": "#FC6E51", "ScrollRegion": null}, {"Type": "Button", "Index": 3, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [840, 120, 80, 48, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "重新开始", "FGColor": "#000000", "Font": ["Segoe UI", 11, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "Button", "Index": 5, "AliasName": "Button_2", "ParentName": "Form_1", "PlaceInfo": [840, 40, 80, 48, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "开始游戏", "FGColor": "#000000", "Font": ["Segoe UI", 11, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_2_onCommand"}}, {"Type": "SwitchButton", "Index": 6, "AliasName": "SwitchButton_1", "ParentName": "Form_1", "PlaceInfo": [840, 240, 80, 40, "nw", true, false], "Visible": true, "Size": [80, 40], "Shape": "circular", "BGColor_Off": "#333333", "Text_Off": "", "FGColor_Off": "#FFFFFF", "BtnColor_Off": "#FFFFFF", "BGColor_On": "#2F9F00", "Text_On": "", "FGColor_On": "#FFFFFF", "BtnColor_On": "#FFFFFF", "Font": ["Segoe UI", 9, "normal", "roman", 0, 0], "Value": false, "SwitchMode": "0", "EventList": {"Switch": "SwitchButton_1_onSwitch"}}, {"Type": "Label", "Index": 7, "AliasName": "Label_1", "ParentName": "Form_1", "PlaceInfo": [840, 200, 80, 40, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#EFEFEF", "Text": "是否先手", "FGColor": "#000000", "Font": ["Segoe UI", 11, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 12, "AliasName": "Label_2", "ParentName": "Form_1", "PlaceInfo": [0, 40, 160, 48, "nw", true, false], "Visible": true, "Size": [160, 48], "BGColor": "#EFEFEF", "Text": "总用时", "FGColor": "#000000", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 13, "AliasName": "Label_3", "ParentName": "Form_1", "PlaceInfo": [0, 160, 160, 48, "nw", true, false], "Visible": true, "Size": [160, 48], "BGColor": "#EFEFEF", "Text": "AI", "FGColor": "#000000", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 14, "AliasName": "Label_4", "ParentName": "Form_1", "PlaceInfo": [0, 280, 160, 48, "nw", true, false], "Visible": true, "Size": [160, 48], "BGColor": "#EFEFEF", "Text": "Player", "FGColor": "#000000", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 16, "AliasName": "Label_5", "ParentName": "Form_1", "PlaceInfo": [0, 80, 160, 88, "nw", true, false], "Visible": true, "Size": [160, 88], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#48CFAD", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 17, "AliasName": "Label_6", "ParentName": "Form_1", "PlaceInfo": [0, 200, 160, 88, "nw", true, false], "Visible": true, "Size": [160, 88], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#ED5565", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 18, "AliasName": "Label_7", "ParentName": "Form_1", "PlaceInfo": [0, 320, 160, 88, "nw", true, false], "Visible": true, "Size": [160, 88], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#5D9CEC", "Font": ["Segoe UI", 13, "bold", "roman", 0, 0]}]}'
        Form_1 = Fun.CreateUIFormJson(uiName, root, isTKroot, style, self.UIJsonString)
        # Inital all element's Data
        Fun.InitElementData(uiName)
        # Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName, "Load", gomoku_with_ai_cmd.Form_1_onLoad)
        # Add Some Logic Code Here: (Keep This Line of comments)

        # Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName, "root"):
            self.root.protocol("WM_DELETE_WINDOW", self.Exit)
            self.root.bind("<Configure>", self.Configure)

    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)

    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]

    def Escape(self, event):
        if Fun.AskBox("提示", "确定退出程序？") == True:
            self.Exit()

    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName, 0, "")

    def Configure(self, event):
        Form_1 = Fun.GetElement(self.uiName, "Form_1")
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget and (
            self.configure_event is None
            or self.configure_event[2] != event.width
            or self.configure_event[3] != event.height
        ):
            uiName = self.uiName
            self.configure_event = [event.x, event.y, event.width, event.height]
            Fun.ResizeRoot(self.uiName, self.root, event)
            Fun.ResizeAllChart(self.uiName)
            pass


# Create the root of tkinter
if __name__ == "__main__":
    Fun.RunApplication(gomoku_with_ai)

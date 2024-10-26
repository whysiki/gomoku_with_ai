#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
ElementBGArray = {}
ElementBGArray_Resize = {}
ElementBGArray_IM = {}
import gomoku_with_ai_sty
import Fun
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  gomoku_with_ai:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.Register(uiName,'root',root)
        style = gomoku_with_ai_sty.SetupStyle(isTKroot)
        self.UIJsonString ='{"Version": "1.0.0", "UIName": "gomoku_with_ai", "Description": "", "WindowSize": [960, 719], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": false, "WindowTitle": "五子棋AI对战", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": true, "MinSize": [0, 0], "TransparentColor": null, "RootTransparency": 255, "ICOFile": null, "WinState": 1, "WinTopMost": false, "BGColor": "#FFFFFF", "GroupList": {}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#FFFFFF", "Size": [960, 719], "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Canvas", "Index": 2, "AliasName": "Canvas_1", "ParentName": "Form_1", "PlaceInfo": [66, 33, 266, 266, "nw", true, true], "Visible": true, "Size": [640, 640], "BGColor": "#EFEFEF", "Relief": "flat", "ScrollRegion": null}, {"Type": "Button", "Index": 3, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [350, 83, 33, 20, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "重新开始", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "Button", "Index": 5, "AliasName": "Button_2", "ParentName": "Form_1", "PlaceInfo": [350, 33, 33, 20, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "开始游戏", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_2_onCommand"}}, {"Type": "SwitchButton", "Index": 6, "AliasName": "SwitchButton_1", "ParentName": "Form_1", "PlaceInfo": [350, 150, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "Shape": "circular", "BGColor_Off": "#333333", "Text_Off": "", "FGColor_Off": "#FFFFFF", "BtnColor_Off": "#FFFFFF", "BGColor_On": "#2F9F00", "Text_On": "", "FGColor_On": "#FFFFFF", "BtnColor_On": "#FFFFFF", "Font": ["Segoe UI", 3, "normal", "roman", 0, 0], "Value": false, "SwitchMode": "0", "EventList": {"Switch": "SwitchButton_1_onSwitch"}}, {"Type": "SwitchButton", "Index": 21, "AliasName": "SwitchButton_2", "ParentName": "Form_1", "PlaceInfo": [350, 200, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "Shape": "circular", "BGColor_Off": "#333333", "Text_Off": "", "FGColor_Off": "#FFFFFF", "BtnColor_Off": "#FFFFFF", "BGColor_On": "#2F9F00", "Text_On": "", "FGColor_On": "#FFFFFF", "BtnColor_On": "#FFFFFF", "Font": ["Segoe UI", 3, "normal", "roman", 0, 0], "Value": false, "SwitchMode": "0", "EventList": {"Switch": "SwitchButton_2_onSwitch"}}, {"Type": "Label", "Index": 7, "AliasName": "Label_1", "ParentName": "Form_1", "PlaceInfo": [350, 133, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#EFEFEF", "Text": "是否先手", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 12, "AliasName": "Label_2", "ParentName": "Form_1", "PlaceInfo": [66, 16, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#48CFAD", "Text": "总用时", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 13, "AliasName": "Label_3", "ParentName": "Form_1", "PlaceInfo": [150, 16, 66, 16, "nw", true, false], "Visible": true, "Size": [160, 40], "BGColor": "#EC87C0", "Text": "AI", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 14, "AliasName": "Label_4", "ParentName": "Form_1", "Layer": "lift", "PlaceInfo": [266, 16, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#5D9CEC", "Text": "Player", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 16, "AliasName": "Label_5", "ParentName": "Form_1", "Layer": "lift", "PlaceInfo": [100, 16, 50, 16, "nw", true, false], "Visible": true, "Size": [120, 40], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#48CFAD", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 17, "AliasName": "Label_6", "ParentName": "Form_1", "PlaceInfo": [216, 16, 50, 16, "nw", true, false], "Visible": true, "Size": [120, 40], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#ED5565", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 18, "AliasName": "Label_7", "ParentName": "Form_1", "PlaceInfo": [300, 16, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#EFEFEF", "Text": "0", "FGColor": "#5D9CEC", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 22, "AliasName": "Label_8", "ParentName": "Form_1", "PlaceInfo": [350, 183, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#EFEFEF", "Text": "是否换色", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 24, "AliasName": "Label_9", "ParentName": "Form_1", "PlaceInfo": [0, 62, 50, 16, "nw", true, false], "Visible": true, "Size": [120, 40], "BGColor": "#EC87C0", "Text": "FoolishAI", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0], "EventList": {"Button-1": "Label_9_onButton1"}}, {"Type": "Label", "Index": 25, "AliasName": "Label_10", "ParentName": "Form_1", "PlaceInfo": [0, 137, 50, 16, "nw", true, false], "Visible": true, "Size": [120, 40], "BGColor": "#EC87C0", "Text": "AlphaBeta", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0], "EventList": {"Button-1": "Label_10_onButton1"}}, {"Type": "Label", "Index": 26, "AliasName": "Label_11", "ParentName": "Form_1", "PlaceInfo": [0, 212, 50, 16, "nw", true, false], "Visible": true, "Size": [120, 40], "BGColor": "#EC87C0", "Text": "TorchDeep", "FGColor": "#000000", "Font": ["Segoe UI", 5, "bold", "roman", 0, 0], "EventList": {"Button-1": "Label_11_onButton1"}}, {"Type": "Label", "Index": 28, "AliasName": "Label_13", "ParentName": "Form_1", "PlaceInfo": [0, 37, 50, 25, "nw", true, false], "Visible": true, "Size": [120, 60], "BGColor": "#EFEFEF", "Text": "选择一个AI等级", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0]}, {"Type": "Label", "Index": 30, "AliasName": "Label_14", "ParentName": "Form_1", "PlaceInfo": [0, 87, 54, 50, "nw", true, false], "Visible": true, "Size": [130, 120], "BGColor": "#FFFFFF", "Text": "基于简单实现的决策算法", "FGColor": "#000000", "Font": ["Segoe UI", 4, "normal", "roman", 0, 0], "AutoWrap": true}, {"Type": "Label", "Index": 31, "AliasName": "Label_15", "ParentName": "Form_1", "PlaceInfo": [0, 162, 50, 50, "nw", true, false], "Visible": true, "Size": [120, 120], "BGColor": "#FFFFFF", "Text": "利用极大极小和Alphabeta优化决策算法", "FGColor": "#000000", "Font": ["Segoe UI", 4, "normal", "roman", 0, 0], "AutoWrap": true}, {"Type": "Label", "Index": 32, "AliasName": "Label_16", "ParentName": "Form_1", "PlaceInfo": [0, 237, 50, 37, "nw", true, false], "Visible": true, "Size": [120, 90], "BGColor": "#FFFFFF", "Text": "深度强化学习", "FGColor": "#000000", "Font": ["Segoe UI", 4, "normal", "roman", 0, 0], "AutoWrap": true}]}'
        Form_1 = Fun.CreateUIFormJson(uiName,root,isTKroot,style,self.UIJsonString,False)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName,0,'')

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
        if self.root == event.widget and (self.configure_event is None or self.configure_event[2]!= event.width or self.configure_event[3]!= event.height):
            uiName = self.uiName
            self.configure_event = [event.x,event.y,event.width,event.height]
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            pass
#Create the root of tkinter 

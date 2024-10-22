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
        self.UIJsonString ='{"Version": "1.0.0", "UIName": "gomoku_with_ai", "Description": "", "WindowSize": [960, 720], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": true, "WindowTitle": "gomoku_with_ai", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": true, "MinSize": [0, 0], "TransparentColor": null, "RootTransparency": 255, "ICOFile": null, "WinState": 1, "WinTopMost": false, "BGColor": "#EFEFEF", "GroupList": {}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#EFEFEF", "Size": [960, 720], "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Canvas", "Index": 2, "AliasName": "Canvas_1", "ParentName": "Form_1", "PlaceInfo": [66, 16, 266, 266, "nw", true, true], "Visible": true, "Size": [640, 640], "BGColor": "#ffffff", "Relief": "flat", "BorderWidth": 1, "BorderColor": "#FC6E51", "ScrollRegion": null}, {"Type": "Button", "Index": 3, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [350, 50, 33, 20, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "重新开始", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "Button", "Index": 5, "AliasName": "Button_2", "ParentName": "Form_1", "PlaceInfo": [350, 16, 33, 20, "nw", true, false], "Visible": true, "Size": [80, 48], "BGColor": "#48CFAD", "Text": "开始游戏", "FGColor": "#000000", "Font": ["Segoe UI", 4, "bold", "roman", 0, 0], "Relief": "raised", "EventList": {"Command": "Button_2_onCommand"}}, {"Type": "SwitchButton", "Index": 6, "AliasName": "SwitchButton_1", "ParentName": "Form_1", "PlaceInfo": [350, 100, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "Shape": "circular", "BGColor_Off": "#333333", "Text_Off": "", "FGColor_Off": "#FFFFFF", "BtnColor_Off": "#FFFFFF", "BGColor_On": "#2F9F00", "Text_On": "", "FGColor_On": "#FFFFFF", "BtnColor_On": "#FFFFFF", "Font": ["Segoe UI", 3, "normal", "roman", 0, 0], "Value": false, "SwitchMode": "0", "EventList": {"Switch": "SwitchButton_1_onSwitch"}}, {"Type": "Label", "Index": 7, "AliasName": "Label_1", "ParentName": "Form_1", "PlaceInfo": [350, 83, 33, 16, "nw", true, false], "Visible": true, "Size": [80, 40], "BGColor": "#EFEFEF", "Text": "是否先手", "FGColor": "#000000", "Font": ["Segoe UI", 3, "bold", "roman", 0, 0]}]}'
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

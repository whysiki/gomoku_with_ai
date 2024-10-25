# 版权声明：日历控件参考CSDN博主「我的眼_001」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原作者出处链接及声明
# 原文链接：https://blog.csdn.net/wodeyan001/article/details/86703034
# -*- coding: utf-8 -*- 
import os
import tkinter
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk
from   functools import partial
import win32gui
import inspect
import threading
G_ExeDir = None
G_ResDir = None
FunLib = None
SCALE_FACTOR = 1.5
def EventFunction_Adaptor(fun,  **params):
    """重新定义消息映射函数,自定义参数。"""
    return lambda event, fun=fun, params=params: fun(event, **params)
#判读是否多线程调用
def onThreadingCallFunction(fun,FunctionThreadDict,uiName,widgetName,value=None):
    threadingvalue = 0
    argspec = inspect.getfullargspec(fun)
    if "threadings" in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue > 0:
            EventFunctionNameKey = fun.__module__+'.'+fun.__name__
            if EventFunctionNameKey in FunctionThreadDict:
                for thread in FunctionThreadDict[EventFunctionNameKey]:
                    if not thread.is_alive():
                        FunctionThreadDict[EventFunctionNameKey].remove(thread)
                if len(FunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:
                    return
            function_args = [uiName,widgetName]
            if value != None:
                function_args.append(value)
            run_thread = threading.Thread(target=fun, args=function_args)
            run_thread.Daemon = True
            run_thread.start()
            if threadingvalue > 0:
                if EventFunctionNameKey not in FunctionThreadDict:
                    FunctionThreadDict[EventFunctionNameKey] = [run_thread]
                else:
                    FunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return
    if value:
        fun(uiName,widgetName,value)
    else:
        fun(uiName,widgetName)
class SwitchButton:
    def __init__(self, widget):
        self.ParentWidget = widget
        self.Shape = 'circular'
        self.CurrValue = False
        self.OnText = ""
        self.OnTextColor = '#FFFFFF'
        self.OffText = ""
        self.OffTextColor = '#FFFFFF'
        self.TextFont = tkinter.font.Font(font='TkDefaultFont')
        self.SwitchMode = 1 #立即和动画模式
        self.FrameDelay = 1
        self.BGColor = '#EFEFEF'
        self.OffBGColor = '#333333'
        self.OnBGColor = '#2F9F00'
        self.OnButtonColor = '#FFFFFF'
        self.OffButtonColor = '#FFFFFF'
        self.ButtonX = 0
        self.StopMove = False
        self.Canvas_width = 60
        self.Canvas_height = 20
        self.Canvas_radius = int(self.Canvas_height / 2)
        self.Canvas = tkinter.Canvas(self.ParentWidget,width=self.Canvas_width,height=self.Canvas_height,bg = self.BGColor,highlightthickness=0,bd=0)
        self.Canvas.create_oval(0, 0, self.Canvas_height, self.Canvas_height-1,fill=self.OffBGColor,width=0, tag='bg')
        self.Canvas.create_rectangle(self.Canvas_radius,0,(self.Canvas_width-self.Canvas_radius),self.Canvas_height,fill=self.OffBGColor,width=0, tag='bg')
        self.Canvas.create_oval((self.Canvas_width-self.Canvas_height), 0, self.Canvas_width, self.Canvas_height-1,fill=self.OffBGColor,width=0, tag='bg')
        self.Canvas.create_text(self.Canvas_height+2, 2, fill=self.OffTextColor,text=self.OffText,font = self.TextFont,anchor='nw',tag='text')
        self.Canvas.create_oval(2, 2, (self.Canvas_height-3), (self.Canvas_height-3),fill=self.OffButtonColor,width=0,tag='button')
        self.Canvas.bind("<ButtonRelease-1>",self.onSwitch)
        self.Canvas.bind('<Configure>',self.Configure)
        self.Canvas.place(x=0, y=0,width=40,height=20)
        self.SwitchCallBackFunction = None
        self.SwitchUIName = None
        self.SwitchName =  None
        self.State = True
    #设置形状
    def SetShape(self,shape):
        self.Shape = shape
    #取得形状
    def GetShape(self):
        return self.Shape
    #取得当前值
    def GetCurrValue(self):
        return self.CurrValue
    #设置当前值
    def SetCurrValue(self,value):
        if value == True:
            self.SwithOn()
        else:
            self.SwitchOff()
    #取得所属窗体
    def GetWidget(self):
        return self.Canvas
    #窗口大小变化
    def Configure(self,event):
        self.Canvas_width = event.width
        self.Canvas_height = event.height
        self.Canvas_radius = int(self.Canvas_height / 2)
        if self.Shape == 'circular':
            import win32gui
            if event.width > 1 and event.height > 1:
                HRGN = win32gui.CreateRoundRectRgn(0,0,event.width,event.height,event.height,event.height)
                win32gui.SetWindowRgn(self.Canvas.winfo_id(),HRGN,1)
        self.Redraw()
    #取得边框样式
    def Hide(self,layout="place"):
        if layout == "pack":
            self.Canvas.pack_forget()
        elif layout == "grid":
            self.Canvas.grid_forget()
        else:
            self.Canvas.place_forget()
    #传递绑定事件
    def bind(self,EventName,callBack):
        if self.Canvas:
            self.Canvas.bind(EventName,callBack)
    #传递pack_forget事件
    def pack_forget(self):
        if self.Canvas:
            self.Canvas.pack_forget()
    #传递grid_forget事件
    def grid_forget(self):
        if self.Canvas:
            self.Canvas.grid_forget()
    #传递place_forget事件
    def place_forget(self):
        if self.Canvas:
            self.Canvas.place_forget()
    #设置切换事件回调函数
    def SetSwitchCallBackFunction(self,callBack,uiName,widgetName):
        self.SwitchCallBackFunction = callBack 
        self.SwitchUIName = uiName
        self.SwitchName = widgetName
    #设置透明色
    def SetBGColor(self,color):
        self.BGColor = color
    #设置打开时背景色
    def SetOnStateBGColor(self,color):
        self.OnBGColor = color
        self.MoveTo(self.CurrValue)
    #设置OFF时背景色
    def SetOffStateBGColor(self,color):
        self.OffBGColor = color
        self.MoveTo(self.CurrValue)
    #设置打开时按钮色
    def SetOnStateButtonColor(self,color):
        self.OnButtonColor = color
        self.MoveTo(self.CurrValue)
    #设置关闭时按钮色
    def SetOffStateButtonColor(self,color):
        self.OffButtonColor = color
        self.MoveTo(self.CurrValue)
    #设置打开时显示文字
    def SetOnStateText(self,text):
        self.OnText = text
    #取得文字宽度
    def GetOnStateTextWidth(self):
        return self.TextFont.measure(self.OnText)
    #设置打开时文字颜色
    def SetOnStateTextColor(self,color='#FFFFFF'):
        self.OnTextColor = color
        self.MoveTo(self.CurrValue)
    #设置关闭时显示文字
    def SetOffStateText(self,text):
        self.OffText = text
        self.MoveTo(self.CurrValue)
    #取得文字宽度
    def GetOffStateTextWidth(self):
        return self.TextFont.measure(self.OffText)
    #设置关闭时文字颜色
    def SetOffStateTextColor(self,color='#FFFFFF'):
        self.OffTextColor = color
        self.MoveTo(self.CurrValue)
    #设置当前是否可用
    def SetState(self,state):
        self.State = state
    #取得是否可用
    def GetState(self):
        return self.State
    #设置文字字体
    def SetFont(self,font):
        self.TextFont = font
    #移动动画
    #mode:0:"immediate",1:"animation"
    #framedelay:帧切换的时间间隔
    def SetSwitchMode(self,mode=0,framedelay=1):
        self.SwitchMode = mode
        self.FrameDelay = framedelay
        self.StopMove = False
    def GetSwitchMode(self):
        return self.SwitchMode
    #切换开关
    def onSwitch(self,event):
        if self.State == True:
            if self.CurrValue == False:
                self.SwithOn()
                if self.SwitchCallBackFunction:
                    self.SwitchCallBackFunction(self.SwitchUIName,self.SwitchName,True)
            else:
                self.SwitchOff()
                if self.SwitchCallBackFunction:
                    self.SwitchCallBackFunction(self.SwitchUIName,self.SwitchName,False)
    #设置切换到打开
    def SwithOn(self):
        if self.CurrValue == False:
            self.CurrValue = True
            self.StopMove = False
            #如果是动画模式
            if self.SwitchMode == 1:
                self.Canvas.after(4, lambda: self.MoveTo(self.CurrValue))
            else:
                self.ButtonX = (self.Canvas_width-self.Canvas_height)
                self.MoveTo(self.CurrValue)
    #切换到关
    def SwitchOff(self):
        if self.CurrValue == True:
            self.CurrValue = False
            self.StopMove = False
            #如果是动画模式
            if self.SwitchMode == 1:
                self.Canvas.after(4, lambda: self.MoveTo(self.CurrValue))
            else:
                self.ButtonX = 2
                self.MoveTo(self.CurrValue)
    #动画
    def MoveTo(self,currValue):
        if self.StopMove == False:
            if currValue == True:
                self.Canvas.delete('bg')
                self.Canvas.delete('text')
                self.Canvas.delete('button')
                radius = int(self.Canvas_height/2)
                border = int(self.Canvas_height * 0.1)
                if border < 2:
                    border = 2
                if self.ButtonX <= (self.Canvas_width - self.Canvas_height):
                    self.ButtonX = self.ButtonX + 1
                if self.ButtonX >= (self.Canvas_width - self.Canvas_height):
                    self.ButtonX = (self.Canvas_width - self.Canvas_height)
                    self.StopMove = True
                if self.Shape == 'circular':
                    self.Canvas.create_oval(0, 0, self.Canvas_height, self.Canvas_height,fill=self.OnBGColor,width=0, tag='bg')
                    self.Canvas.create_rectangle(radius,0,self.Canvas_width-radius,self.Canvas_height+1,fill=self.OnBGColor,width=0, tag='bg')
                    self.Canvas.create_oval(self.Canvas_width-self.Canvas_height, 0, self.Canvas_width, self.Canvas_height,fill=self.OnBGColor,width=0, tag='bg')
                    self.Canvas.create_oval(self.ButtonX, border, self.ButtonX + (self.Canvas_height - border), self.Canvas_height - border,fill=self.OnButtonColor, tag='button')    
                    self.Canvas.create_text(self.ButtonX-border-self.GetOnStateTextWidth(), self.Canvas_radius, fill=self.OnTextColor,text=self.OnText,font = self.TextFont,anchor='w',tag='text')
                    self.Canvas.create_text(self.ButtonX+self.Canvas_height+border, self.Canvas_radius, fill=self.OffTextColor,text=self.OffText,font = self.TextFont,anchor='w',tag='text')
                else:
                    self.Canvas.create_rectangle(0,0,self.Canvas_width,self.Canvas_height,fill=self.OnBGColor,width=0, tag='bg')
                    self.Canvas.create_rectangle(self.ButtonX, border, self.ButtonX + (self.Canvas_height - border), self.Canvas_height - border,fill=self.OnButtonColor, tag='button')    
                    self.Canvas.create_text(self.ButtonX-border-self.GetOnStateTextWidth(), self.Canvas_radius, fill=self.OnTextColor,text=self.OnText,font = self.TextFont,anchor='w',tag='text')
                    self.Canvas.create_text(self.ButtonX+self.Canvas_height+border, self.Canvas_radius, fill=self.OffTextColor,text=self.OffText,font = self.TextFont,anchor='w',tag='text')
                if self.StopMove == False:
                    self.Canvas.after(self.FrameDelay, lambda: self.MoveTo(currValue))
                else:
                    self.Canvas.after_cancel(self.MoveTo)
            else:
                self.Canvas.delete('bg')
                self.Canvas.delete('text')
                self.Canvas.delete('button')
                radius = int(self.Canvas_height/2)
                border = int(self.Canvas_height * 0.1)
                if border < 2:
                    border = 2
                if self.ButtonX >= border:
                    self.ButtonX = self.ButtonX - 1
                if self.ButtonX < border:
                    self.ButtonX = border
                    self.StopMove = True
                if self.Shape == 'circular':
                    self.Canvas.create_oval(0, 0, self.Canvas_height, self.Canvas_height,fill=self.OffBGColor,width=0, tag='bg')
                    self.Canvas.create_rectangle(radius,0,self.Canvas_width-radius,self.Canvas_height+1,fill=self.OffBGColor,width=0, tag='bg')
                    self.Canvas.create_oval(self.Canvas_width-self.Canvas_height, 0, self.Canvas_width, self.Canvas_height,fill=self.OffBGColor,width=0, tag='bg')
                    self.Canvas.create_oval(self.ButtonX, border, self.ButtonX + (self.Canvas_height - border), self.Canvas_height - border,fill=self.OffButtonColor, tag='button')    
                    self.Canvas.create_text(self.ButtonX-border-self.GetOnStateTextWidth(), self.Canvas_radius, fill=self.OnTextColor,text=self.OnText,font = self.TextFont,anchor='w',tag='text')
                    self.Canvas.create_text(self.ButtonX+self.Canvas_height+border, self.Canvas_radius, fill=self.OffTextColor,text=self.OffText,font = self.TextFont,anchor='w',tag='text')
                else:
                    self.Canvas.create_rectangle(0,0,self.Canvas_width,self.Canvas_height,fill=self.OffBGColor,width=0, tag='bg')
                    self.Canvas.create_rectangle(self.ButtonX, border, self.ButtonX + (self.Canvas_height - border), self.Canvas_height - border,fill=self.OffButtonColor, tag='button')    
                    self.Canvas.create_text(self.ButtonX-border-self.GetOnStateTextWidth(), self.Canvas_radius, fill=self.OnTextColor,text=self.OnText,font = self.TextFont,anchor='w',tag='text')
                    self.Canvas.create_text(self.ButtonX+self.Canvas_height+border, self.Canvas_radius, fill=self.OffTextColor,text=self.OffText,font = self.TextFont,anchor='w',tag='text')
                if self.StopMove == False:
                    self.Canvas.after(self.FrameDelay, lambda: self.MoveTo(currValue))
                else:
                    self.Canvas.after_cancel(self.MoveTo)
    #重新绘制
    def Redraw(self):
        self.MoveTo(self.CurrValue)

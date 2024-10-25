#!/usr/bin/env python
#coding=utf-8
#Project:gomoku_with_ai
#此文件由PyMe自动生成，如需要手动编写，请鼠标右键点击左边锁定标记，在弹出菜单中取消锁定。
g_TKScaling_Init=1.33
g_TKScaling=1.33
import sys
import io
import os
from   os.path import abspath, dirname
import shutil
import tkinter
import time
import requests
import threading
from   pathlib import Path
from urllib.request import urlopen
from   tkinter import *
import tkinter.ttk
import tkinter.font
import tkinter.simpledialog
from PIL import Image,ImageTk
from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
import zipfile
import inspect
import math
import json
import re
import copy
from  functools import partial
import aggdraw
import windnd
import ctypes
from  ctypes import windll
import win32gui
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
G_ExeDir = os.getcwd()
G_ResDir =  os.path.join(G_ExeDir,"Resources")
if os.path.exists(G_ResDir) == True:
    sys.path.insert(0,G_ResDir)
ModulesDir =  os.path.join(G_ExeDir,"Modules")
if os.path.exists(ModulesDir) == True:
    sys.path.insert(0,ModulesDir)
import EXUIControl
EXUIControl.FunLib = sys.modules[__name__]
EXUIControl.G_ExeDir = G_ExeDir
EXUIControl.G_ResDir = G_ResDir
G_UIRootIDDictionary={}
G_UIRootSizeDictionary={}
G_UIRootStateDictionary={}
G_UIElementDictionary={}
G_UIGlobalElementDictionary={}
G_UIElementLayerDictionary={}
G_UIActiveDictionary={}
G_UIParamsDictionary={}
G_UICommandDictionary={}
G_UIElementPlaceDictionary={}
G_UILoadPageDictionary={}
G_UIElementRoundRectangleDictionary={}
G_UIElementUserDataArray={}
G_UIElementVariableArray={}
G_UIElementIconDictionary={}
G_UIInputDataArray={} 
G_UIElementAliasDictionary={}
G_UIGroupDictionary={}
G_UIStyleDictionary={}
G_UIRadioButtonGroupArray={}
G_CanvasSizeDictionary={}
G_CanvasShapeDictionary={}
G_CanvasParamDictionary={}
G_CanvasFontDictionary={}
G_CanvasImageDictionary={}
G_CanvasPointDictionary={}
G_CanvasEventDictionary={}
G_ListViewTagDictionary={}
G_ListViewCommandDictionary={}
G_TKRoot=None
G_TKKey=[]
G_TKKey.append('F1')
G_TKKey.append('F2')
G_TKKey.append('F3')
G_TKKey.append('F4')
G_TKKey.append('F5')
G_TKKey.append('F6')
G_TKKey.append('F7')
G_TKKey.append('F8')
G_TKKey.append('F9')
G_TKKey.append('F10')
G_TKKey.append('F11')
G_TKKey.append('F12')
G_TKKey.append('Control-a')
G_TKKey.append('Control-b')
G_TKKey.append('Control-c')
G_TKKey.append('Control-d')
G_TKKey.append('Control-e')
G_TKKey.append('Control-f')
G_TKKey.append('Control-g')
G_TKKey.append('Control-h')
G_TKKey.append('Control-i')
G_TKKey.append('Control-j')
G_TKKey.append('Control-k')
G_TKKey.append('Control-l')
G_TKKey.append('Control-m')
G_TKKey.append('Control-n')
G_TKKey.append('Control-o')
G_TKKey.append('Control-p')
G_TKKey.append('Control-q')
G_TKKey.append('Control-r')
G_TKKey.append('Control-s')
G_TKKey.append('Control-t')
G_TKKey.append('Control-u')
G_TKKey.append('Control-v')
G_TKKey.append('Control-w')
G_TKKey.append('Control-x')
G_TKKey.append('Control-y')
G_TKKey.append('Control-z')
#暂时保留G_RootSize
G_RootSize=None
G_UIScale=1.0
G_UserVarDict={}
G_TopDialog = None
G_LaunchDlg = None
G_ResourcesFileList={}
G_EventFunctionThreadDict={}
G_CutContent=None
G_FlaskReturnContent=None
G_UrlParamMessageBox=None
G_TargetUIName=None
G_WindowDraggable=None
G_PrintFunctionMode=False

def GetPKGResources(ResourcePathName):
    #获取打包后的配置文件路径  
    import pkg_resources
    if getattr(sys, 'frozen', False):
        # 在打包后的程序中运行
        filePath, fileName = os.path.split(ResourcePathName)  
        return pkg_resources.resource_filename(__name__,fileName)
    # 在源代码环境中运行
    return ResourcePathName

def PrintFunctionInfo(TargetFunction,args=[]):
    #函数调用打印  
    global G_PrintFunctionMode
    if G_PrintFunctionMode == True:
        argspec = inspect.getfullargspec(TargetFunction)
        ParamText = ""
        ParamIndex = 0
        for ParamName in argspec.args:
            ParamText = ParamText + ParamName + "=" + str(args[ParamIndex]) + ","
            ParamIndex = ParamIndex + 1
        if ParamText != "":
            ParamText = ParamText[0:-1]
        if ParamText != "":
            print('函数调用打印'+TargetFunction.__name__+"("+ParamText+")")
        else:
            print('函数调用打印'+TargetFunction.__name__+"()")
def IsInt(text):    
    #是否是整数字符串  
    if (text.startswith('-') and text[1:] or text).isdigit():
        return True    
    return False    
def IsFloat(text):    
    #是否是浮点字符中  
    if text.count('.') == 1:    
        left = text.split('.')[0]    
        right = text.split('.')[1]    
        lright = ''    
        if left.count('-') == 1 and left[0] == '-':    
            lright = left.split('-')[1]    
        elif left.count('-') == 0:    
            lright = left    
        if right.isdigit() and lright.isdigit():    
            return True    
    return False    
def IsNumeric(text):    
    #是否是数字字符串  
    if IsInt(text) == True or IsFloat(text) == True:    
        return True    
    return False    
def IsAlphanumeric(text):    
    #字母或数字  
    pattern = r'[a-zA-Z0-9]+'   
    if bool(re.fullmatch(pattern, text)):
        return True
    return False  
def CheckSpecialChar(text):    
    #是否包含特殊字符  
    string = '~!@#$%^&*()+-*/<>,.[]、‘’\'"{}/^'    
    for i in string:    
        if i in text:    
            return True    
    return False    
def IsMobilePhone(text):    
    #是否是手机号  
    ret = re.match(r"^1[35789]\d{9}$", text)
    if ret:    
        return True    
    return False    
def IsEmail(text):    
    #是否是Email  
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'    
    return re.match(pattern, text) is not None    
def RandNumber(begin=0,end=100):    
    #获取一个0~100的随机数字  
    import random    
    return random.randint(begin,end)
def GetCurrTime(splitChar=':'):    
    #获取当前时间  
    import datetime    
    nowDateTime = datetime.datetime.now()
    currTime = str("%d%s%d%s%d"%(nowDateTime.hour,splitChar,nowDateTime.minute,splitChar,nowDateTime.second))
    return currTime    
def GetCurrDate(splitChar=':'):    
    #获取当前日期  
    import datetime    
    nowDateTime = datetime.datetime.now()
    currDate = str("%d%s%d%s%d"%(nowDateTime.year,splitChar,nowDateTime.month,splitChar,nowDateTime.day))
    return currDate    
def Sleep(second=1):    
    #Sleep等待  
    import time    
    time.sleep(second)
def OutputProcessToText(cmdText,uiName,elementName):    
    #运行命令并输出  
    DelAllLines(uiName,elementName)
    try:    
        import subprocess    
        process = subprocess.Popen(cmdText,shell=True, bufsize=0, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,stdin=subprocess.PIPE,encoding='utf-8')
        outputString = process.stdout.readline()
        Result = 0    
        while outputString:    
            AddLineText(uiName,elementName,outputString)
            outputString = process.stdout.readline()
        process.stdout.close()
    except Exception as ex:    
        if uiName and elementName:    
            AddLineText(uiName,elementName,str(ex))
        else:    
            print(str(ex))
  
def EventFunction_Adaptor(fun,  **params):  
    #重新定义消息映射函数,自定义参数。 
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun)
    if G_PrintFunctionMode == True:
        ParamText = ""
        ParamIndex = 0
        for ParamName in argspec.args:
            if ParamName == "event":
                ParamText = ParamText + "event = event ,"
            else:
                if ParamName in params.keys():
                    ParamText = ParamText + ParamName + "=" + str(params[ParamName]) + ","
                else:
                    ParamText = ParamText + ParamName + "= None,"
            ParamIndex = ParamIndex + 1
        if ParamText != "":
            ParamText = ParamText[0:-1]
        if ParamText != "":
            print('函数调用打印'+fun.__name__+"("+ParamText+")")
        else:
            print('函数调用打印'+fun.__name__+"()")


    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            def fun_threading(event, **params):    
                if threadingvalue > 0:
                    EventFunctionNameKey = fun.__module__+"."+fun.__name__
                    if EventFunctionNameKey in G_EventFunctionThreadDict:    
                        for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                            if not thread.is_alive():    
                                G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                        if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                            return
                paramslist = [event]
                for key in params:    
                    paramslist.append(params[key])
                run_thread = threading.Thread(target=fun, args=paramslist)
                run_thread.Daemon = True    
                run_thread.start()
                if threadingvalue > 0:
                    if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                        G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                    else:
                        G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return lambda event, fun=fun_threading, params=params: fun(event, **params)  
    return lambda event, fun=fun, params=params: fun(event, **params)  
def EventTwoFunction_Adaptor(fun1,fun2, **params):    
    #重新定义消息映射函数,自定义参数。
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun2)
    if G_PrintFunctionMode == True:
        ParamText = ""
        ParamIndex = 0
        for ParamName in argspec.args:
            ParamText = ParamText + ParamName + "=" + str(params[ParamIndex]) + ","
            ParamIndex = ParamIndex + 1
        if ParamText != "":
            ParamText = ParamText[0:-1]
        if ParamText != "":
            print('函数调用打印'+fun2.__name__+"("+ParamText+")")
        else:
            print('函数调用打印'+fun2.__name__+"()")

    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            def call_fun1_fun2(event, **params):
                fun1(event, **params)
                fun2(event, **params)

            def fun_threading(event, **params):
                if threadingvalue > 0:
                    EventFunctionNameKey = fun1.__module__+"."+fun1.__name__+"."+fun2.__module__+"."+fun2.__name__
                    if EventFunctionNameKey in G_EventFunctionThreadDict:    
                        for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                            if not thread.is_alive():    
                                G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                        if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                            return
                paramslist = [event]
                for key in params:    
                    paramslist.append(params[key])
                run_thread = threading.Thread(target=call_fun1_fun2, args=paramslist)
                run_thread.Daemon = True    
                run_thread.start()
                if threadingvalue > 0:
                    if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                        G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                    else:
                        G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return lambda event, fun=fun_threading, params=params: fun(event, **params)
    return lambda event, fun1=fun1,fun2=fun2, params=params: (fun1(event, **params),fun2(event, **params))

def CommandFunction_Adaptor(fun,uiName,widgetName):    
    #重新定义消息映射函数,自定义参数。  
    button = GetElement(uiName,widgetName)
    if button:    
        button.focus_set()   
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun)
    if G_PrintFunctionMode == True:
        ParamText = "uiName =" + str(uiName) + "," + "widgetName =" + str(widgetName)
        print('函数调用打印'+fun.__name__+"("+ParamText+")")

    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            if threadingvalue > 0:
                EventFunctionNameKey = fun.__module__+"."+fun.__name__
                if EventFunctionNameKey in G_EventFunctionThreadDict:    
                    for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                        if not thread.is_alive():    
                            G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                    if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                        return
            run_thread = threading.Thread(target=fun, args=[uiName,widgetName])
            run_thread.Daemon = True    
            run_thread.start()
            if threadingvalue > 0:
                if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                    G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                else:
                    G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return 
    fun(uiName=uiName,widgetName=widgetName)

def SetValueChangedFunction(fun, uiName,widgetName):    
    #重新定义消息映射函数,自定义参数。 
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun)
    if G_PrintFunctionMode == True:
        ParamText = ParamText + "uiName =" + str(uiName) + "," + "widgetName =" + str(widgetName)
        print('函数调用打印'+fun.__name__+"("+ParamText+")")

    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            if threadingvalue > 0:
                EventFunctionNameKey = fun.__module__+"."+fun.__name__
                if EventFunctionNameKey in G_EventFunctionThreadDict:    
                    for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                        if not thread.is_alive():    
                            G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                    if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                        return
            run_thread = threading.Thread(target=fun, args=[uiName,widgetName,value])
            run_thread.Daemon = True    
            run_thread.start()
            if threadingvalue > 0:
                if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                    G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                else:
                    G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return 
    return lambda value,fun=fun: fun(uiName=uiName,widgetName=widgetName,value=value)

def ListViewHeadingFunction_Adaptor(fun,uiName,widgetName,columnname):    
    #重新定义消息映射函数,自定义参数。 
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun)
    if G_PrintFunctionMode == True:
        ParamText = ParamText + "uiName =" + str(uiName) + "," + "widgetName =" + str(widgetName) + "," + "columnname =" + str(columnname)
        print('函数调用打印'+fun.__name__+"("+ParamText+")")

    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            if threadingvalue > 0:
                EventFunctionNameKey = fun.__module__+"."+fun.__name__
                if EventFunctionNameKey in G_EventFunctionThreadDict:    
                    for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                        if not thread.is_alive():    
                            G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                    if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                        return
            run_thread = threading.Thread(target=fun, args=[uiName,widgetName,columnname])
            run_thread.Daemon = True    
            run_thread.start()
            if threadingvalue > 0:
                if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                    G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                else:
                    G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return 
    fun(uiName = uiName , widgetName = widgetName,columnname = columnname)
def MenuFunction_Adaptor(fun,  **params):  
    #重新定义消息映射函数,自定义参数。  
    global G_EventFunctionThreadDict  
    global G_PrintFunctionMode
    argspec = inspect.getfullargspec(fun)
    if G_PrintFunctionMode == True:
        ParamText = ""
        ParamIndex = 0
        for ParamName in argspec.args:
            ParamText = ParamText + ParamName + "=" + str(params[ParamIndex]) + ","
            ParamIndex = ParamIndex + 1
        if ParamText != "":
            ParamText = ParamText[0:-1]
        if ParamText != "":
            print('函数调用打印'+fun.__name__+"("+ParamText+")")
        else:
            print('函数调用打印'+fun.__name__+"()")
    if 'threadings' in argspec.args:
        threadingindex = argspec.args.index('threadings')
        threadingvalue = argspec[threadingindex+1]
        if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
            if len(threadingvalue) == 0:    
                threadingvalue = 0
            else:
                threadingvalue = threadingvalue[0]
        if threadingvalue != 0:
            def fun_threading(**params):   
                if threadingvalue > 0:
                    EventFunctionNameKey = fun.__module__+"."+fun.__name__
                    if EventFunctionNameKey in G_EventFunctionThreadDict:    
                        for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:    
                            if not thread.is_alive():    
                                G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                        if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:    
                            return
                paramslist = []
                for key in params:    
                    paramslist.append(params[key])
                run_thread = threading.Thread(target=fun, args=paramslist)
                run_thread.Daemon = True    
                run_thread.start()
                if threadingvalue > 0:
                    if EventFunctionNameKey not in G_EventFunctionThreadDict:    
                        G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                    else:
                        G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
            return lambda event, fun=fun_threading, params=params: fun(**params)  
    return lambda event, fun=fun, params=params: fun(**params)
class   PyMeEvent():    
    def __init__(self,x,y,tag=None):    
        self.x = x    
        self.y = y    
        self.tag = tag    
class   ChartEvent():    
    def __init__(self,width,height,widget):    
        self.width = width    
        self.x = 0    
        self.y = 0
        self.height = height    
        self.widget = widget    
class   ResetPrintClass():    
    #定义一个打印输出目标  
    def __init__(self):    
        self.str = ""    
    def write(self,s):    
        self.str += s    
    def clear(self):    
        self.str = ""    
    def getString(self):    
        return self.str    
def GetParentCallFunc():    
    #获取堆栈中上层调用函数的名称和参数  
    stackFunctionInfo = inspect.currentframe().f_back    
    while stackFunctionInfo is not None and '__name__' in stackFunctionInfo.f_globals:    
        if stackFunctionInfo.f_code.co_filename != __file__:     
            parent_func = stackFunctionInfo.f_globals['__name__'] + "." + stackFunctionInfo.f_code.co_name    
            return [parent_func,list(stackFunctionInfo.f_locals.values())]    
        stackFunctionInfo = stackFunctionInfo.f_back    
    return [None,None]
  
def DropFileFunction_Callback(fun,files, **params):    
    fileList = []    
    for fileName in files:    
        fileList.append(fileName.decode('gbk'))
    threading.Thread(target=fun,args=(fileList,params['uiName'],params['widgetName'])).start()
#f.write("    fun(**params,files=fileList)
def DropFileFunction_Adaptor(fun,  **params):    
    return lambda files, fun=fun, params=params: DropFileFunction_Callback(fun,files, **params)
def SetControlAcceptDrop(uiName,elementName,functionCallback):    
    #设置控件接受拖拽文件  
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return     
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    import windnd    
    windnd.hook_dropfiles(Control,func=DropFileFunction_Adaptor(functionCallback,uiName=uiName,widgetName=elementName))

def GetUIName(root,className): 
    #取得界面名称  
    uiName = className    
    if className in G_UIRootIDDictionary and G_UIRootIDDictionary[className] == root:    
        return uiName    
    if G_UIElementDictionary:    
        classIndex = 0    
        while uiName in G_UIElementDictionary:    
            classIndex = classIndex + 1    
            uiName = className + "_" + str(classIndex)
    G_UIRootIDDictionary[className] = root    
    return uiName       
def HScrollBar_Config(event,scrollBar):    
    parentinfo = event.widget.winfo_parent()
    parentWidget = event.widget._nametowidget(parentinfo)
    top = parentWidget.winfo_height()-20    
    width = parentWidget.winfo_width()
    if top >= 0 and width >= 0:    
        scrollBar.place(x = 0,y = top,width = width ,height = 20)
def VScrollBar_Config(event,scrollBar):    
    parentinfo = event.widget.winfo_parent()
    parentWidget = event.widget._nametowidget(parentinfo)
    left = parentWidget.winfo_width()-20    
    height = parentWidget.winfo_height()
    if left >= 0 and height >= 0:    
        scrollBar.place(x = left,y = 0,width = 20,height = height)
def GetUIParams(uiName):    
    #取得界面参数  
    global G_UIParamsDictionary    
    if uiName in G_UIParamsDictionary:    
        return G_UIParamsDictionary[uiName]    
    else:    
        G_UIParamsDictionary[uiName] = uiName    
    return uiName 
def Register(uiName,elementName,element,alias=None,groupName=None,styleName=None):    
    #注册一个控件,用于记录它:参数1 :界面类名, 参数2:控件名称,参数3 :控件。  
    if uiName not in G_UIElementDictionary:    
        G_UIElementDictionary[uiName]={}   
        G_UIGlobalElementDictionary[uiName]={}
        G_UIElementLayerDictionary[uiName]={}
        G_UIRootSizeDictionary[uiName]={}
        G_UICommandDictionary[uiName]={}
        G_UIActiveDictionary[uiName]={}
        G_UIElementVariableArray[uiName]={}    
        G_UIElementAliasDictionary[uiName]={}
        G_UIElementPlaceDictionary[uiName]={}
        G_UILoadPageDictionary[uiName]={}
        G_UIElementRoundRectangleDictionary[uiName]={}
        G_UIGroupDictionary[uiName]={}
        G_UIStyleDictionary[uiName]={} 
        G_UIRadioButtonGroupArray[uiName]={}
        G_CanvasSizeDictionary[uiName]={}
        G_CanvasShapeDictionary[uiName]={}
        G_CanvasParamDictionary[uiName]={}
        G_CanvasFontDictionary[uiName]={}
        G_CanvasImageDictionary[uiName]={}
        G_CanvasEventDictionary[uiName]={}
        G_CanvasPointDictionary[uiName]={}
        G_ListViewTagDictionary[uiName]={}
        G_ListViewCommandDictionary[uiName]={}
        G_UIElementIconDictionary[uiName]={}
        G_UIElementIconDictionary[uiName]['MainMenu'] = {}
        G_UIElementIconDictionary[uiName]['SysTray'] = {}
    G_UIElementDictionary[uiName][elementName]=element     
    if elementName == 'UIClass':     
        G_UIElementAliasDictionary[uiName].clear() 
    if alias:     
        G_UIElementAliasDictionary[uiName][alias]=elementName     
    if groupName:     
        G_UIGroupDictionary[uiName][elementName]=groupName     
    if styleName:     
        G_UIStyleDictionary[uiName][elementName]=styleName     
    if elementName.find('TreeView_') >= 0:    
        G_UIElementIconDictionary[uiName][elementName]={}    
    if elementName.find('ListView_') >= 0:    
        G_ListViewTagDictionary[uiName][elementName]=[]   
    if elementName.find('_HScrollbar') >= 0:    
        FrameName = elementName.replace('_HScrollbar','')
        if FrameName:    
            FrameWidget = G_UIElementDictionary[uiName][FrameName]    
            FrameWidget.bind('<Configure>',EventFunction_Adaptor(HScrollBar_Config,scrollBar = element))
    if elementName.find('_VScrollbar') >= 0:    
        FrameName = elementName.replace('_VScrollbar','')
        if FrameName:    
            FrameWidget = G_UIElementDictionary[uiName][FrameName]    
            FrameWidget.bind('<Configure>',EventFunction_Adaptor(VScrollBar_Config,scrollBar = element))   

def SetTitleBar(root,titleText='',isDarkMode=False,isDropTitle=False):    
    #设置标题文字及暗色  
    PrintFunctionInfo(SetTitleBar,[root,titleText,isDarkMode,isDropTitle])
    try :    
        root.update()
        root.title(titleText)
        if isDarkMode == True and isDropTitle == False:    
            DARK_MODE = 20    
            DwmSetWindowAttribute = ctypes.windll.dwmapi.DwmSetWindowAttribute    
            WindowHandle = ctypes.windll.user32.GetParent(root.winfo_id())
            value = ctypes.c_int(2)
            DwmSetWindowAttribute(WindowHandle, DARK_MODE, ctypes.byref(value), ctypes.sizeof(value))
            root.update()
        if isDropTitle == True:   
            root.overrideredirect(True)
            from win32gui import GetParent, SetWindowPos, UpdateWindow, SetWindowLong, GetWindowLong, ReleaseCapture, SendMessage, PostMessage  
            from win32con import NULL, SWP_NOSIZE, SWP_NOMOVE, SWP_NOZORDER, SWP_DRAWFRAME, GWL_STYLE, WS_CAPTION, WM_SYSCOMMAND, SC_MOVE, HTCAPTION, WS_THICKFRAME    
            WindowHandle = ctypes.windll.user32.GetParent(root.winfo_id())    
            # if isinstance(root,tkinter.Tk) == True:
            #     SetWindowLong(WindowHandle, GWL_STYLE, GetWindowLong(WindowHandle, GWL_STYLE) & ~WS_CAPTION & ~WS_THICKFRAME)
            SetWindowPos(WindowHandle, NULL, 0, 0, 0, 0, SWP_DRAWFRAME)

            #下面是为了让窗口在任务栏显示
            GWL_EXSTYLE=-20
            WS_EX_APPWINDOW=0x00040000
            WS_EX_TOOLWINDOW=0x00000080
            style = ctypes.windll.user32.GetWindowLongPtrW(WindowHandle, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res = ctypes.windll.user32.SetWindowLongPtrW(WindowHandle, GWL_EXSTYLE, style)

            #UpdateWindow有时会导致界面卡住
            #UpdateWindow(WindowHandle)  
            WM_PAINT = 0x000F
            PostMessage(WindowHandle,WM_PAINT,0,0)  
    except Exception:    
        root.title(titleText)

def PlayDestroyDialogAction(uiName,result,topLevel,animation='zoomout'):  
    PrintFunctionInfo(PlayDestroyDialogAction,[uiName,result,topLevel,animation])
    def FadeOut(topLevel,alpha):    
        try :    
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32    
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000    
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha - 1    
        except ImportError:    
            pass    
        if alpha > 0:    
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = alpha))
        else:    
            DestroyUI(uiName,result)
            print("结束")
    def ZoomOut(topLevel,zoom,win_x,win_y,win_width,win_height):    
        try :    
            center_x = win_x + int(win_width/2)
            center_y = win_y + int(win_height/2)
            zw = int(win_width * zoom)
            zh = int(win_height * zoom)
            zx = center_x - int(zw/2)
            zy = center_y - int(zh/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom - 0.01    
        except ImportError:    
            pass    
        if zoom > 0.0:    
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = zoom ,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        else:    
            DestroyUI(uiName,result)
            print("结束")
    if animation == "fadeout":    
        try :    
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32    
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000    
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeOut(topLevel = topLevel,alpha = 255))
        except ImportError:    
            pass    
    elif animation == "zoomout":    
        try :    
            win_x = topLevel.winfo_x()
            win_y = topLevel.winfo_y()
            win_width = topLevel.winfo_width()
            win_height = topLevel.winfo_height()
            topLevel.after(1,lambda:ZoomOut(topLevel = topLevel,zoom = 1.0,win_x = win_x,win_y = win_y,win_width=win_width,win_height=win_height))
        except ImportError:    
            pass    
def DestroyUI(uiName,result=0,animation=''): 
    PrintFunctionInfo(DestroyUI,[uiName,result,animation])
    #销毁一个界面:参数1 :界面类名,参数2:CallUIDialog返回值  
    global G_TopDialog
    global G_TKRoot
    if uiName in G_UIElementDictionary:    
        root = GetElement(uiName,"root")
        if root is not None:    
            if G_TopDialog is root:    
                G_TopDialog = None    
            animation = animation.lower()
            if animation != '':    
                PlayDestroyDialogAction(uiName,result,root,animation)
                return    
            if root.master:    
                try:    
                    GetUIDataDictionary(uiName)
                except:    
                    pass    
            try:    
                if root.master != None or result == 0:    
                    root.withdraw()
                    for childName in root.children.keys():    
                        child = root.children[childName]    
                        try:    
                            child.pack_forget()
                        except:    
                            pass    
                        try:    
                            child.grid_forget()
                        except:    
                            pass    
                        try:    
                            child.place_forget()
                        except:    
                            pass    
                    if G_TKRoot is root:
                        G_TKRoot = None
                    root.destroy()
            except:    
                pass    
        G_UIElementDictionary.pop(uiName)
        G_UIElementLayerDictionary.pop(uiName)
        G_UIRootSizeDictionary.pop(uiName)
        G_UICommandDictionary.pop(uiName)
        G_UIElementAliasDictionary.pop(uiName)
        G_UIElementPlaceDictionary.pop(uiName)
        G_UILoadPageDictionary.pop(uiName)
        G_UIElementRoundRectangleDictionary.pop(uiName)
        G_UIGroupDictionary.pop(uiName)
        G_UIStyleDictionary.pop(uiName)
        G_UIRadioButtonGroupArray.pop(uiName)
        G_CanvasSizeDictionary.pop(uiName)
        G_CanvasShapeDictionary.pop(uiName)
        G_CanvasParamDictionary.pop(uiName)
        G_CanvasFontDictionary.pop(uiName)
        G_CanvasImageDictionary.pop(uiName)
        G_CanvasEventDictionary.pop(uiName)
        G_CanvasPointDictionary.pop(uiName)
        G_ListViewTagDictionary.pop(uiName)
        G_ListViewCommandDictionary.pop(uiName)
        G_UIElementIconDictionary.pop(uiName)
        G_UIInputDataArray['PFunc'] = GetParentCallFunc()
        G_UIInputDataArray['result'] = result    
  
def SetCursor(uiName,elementName,cursor='hand2'):   
    PrintFunctionInfo(SetCursor,[uiName,elementName,cursor])  
    #设置控件光标  
    if uiName in G_UIElementDictionary:    
        Control = GetElement(uiName,elementName)
        if Control is not None:    
            if hasattr(Control,"GetEntry") == True:    
                Control = Control.GetEntry()
            elif hasattr(Control,"GetWidget") == True:    
                Control = Control.GetWidget()
            try:    
                Control.config(cursor=cursor)
            except:    
                pass    
def HideCursor(uiName):  
    PrintFunctionInfo(HideCursor,[uiName])  
    #隐藏控件光标  
    if uiName in G_UIElementDictionary:    
        root = GetElement(uiName,"root")
        if root is not None:    
            root.config(cursor="none")
def GetCursorPosition(uiName='',elementName='root'):  
    PrintFunctionInfo(GetCursorPosition,[uiName,elementName])  
    #取得当前光标位置  
    if uiName in G_UIElementDictionary:    
        Control = GetElement(uiName,elementName)
        if Control:    
            return Control.winfo_pointerxy()
        else:    
            Form_1 = GetElement(uiName,"Form_1")
            if Form_1 is not None:    
                return Form_1.winfo_pointerxy()
    return G_TKRoot.winfo_pointerxy()
  
def GetElement(uiName,elementName):    
    #取得控件:参数1 :界面类名, 参数2:控件名称。  
    if uiName and elementName:
        if uiName in G_UIElementAliasDictionary:    
            if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
                elementName = G_UIElementAliasDictionary[uiName][elementName]    
        if uiName in G_UIElementDictionary:    
            if elementName in G_UIElementDictionary[uiName]:    
                return G_UIElementDictionary[uiName][elementName]    
            if elementName.find("TreeView") >= 0:    
                elementName = elementName.replace("TreeView","ListView")
                if elementName in G_UIElementDictionary[uiName]:    
                    return G_UIElementDictionary[uiName][elementName]  
        if uiName in G_UIGlobalElementDictionary:
            if elementName in G_UIGlobalElementDictionary[uiName]:
                return G_UIGlobalElementDictionary[uiName][elementName]
    return None    
def GetElementName(element,isAliasName=True):    
    #取得控件的界面类名与控件名称:参数1 :控件  
    for uiName in G_UIElementDictionary:    
        for elementName in G_UIElementDictionary[uiName]:    
            Control = G_UIElementDictionary[uiName][elementName]    
            if Control == element:    
                if isAliasName == True:    
                    for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                        if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                            return uiName,aliasName    
                return uiName,elementName    
            if hasattr(Control,"GetEntry") == True:    
                ChildWidget = Control.GetEntry()
                if ChildWidget is element:    
                    if isAliasName == True:    
                        for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                            if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                                return uiName,aliasName    
                    return uiName,elementName    
            if hasattr(Control,"GetWidget") == True:    
                ChildWidget = Control.GetWidget()
                if ChildWidget is element:    
                    if isAliasName == True:    
                        for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                            if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                                return uiName,aliasName    
                    return uiName,elementName    
    return None,None    
#注册Form_1的回调函数:    
def SetForm1_CallBack(uiName,eventType,onLoadCallBack=None):    
    pass    
#运行Form_1的回调函数:    
def RunForm1_CallBack(uiName,eventType,onLoadCallBack=None): 
    PrintFunctionInfo(RunForm1_CallBack,[uiName,eventType,onLoadCallBack])
    global G_EventFunctionThreadDict  
    if onLoadCallBack:    
        threadingvalue = 0
        argspec = inspect.getfullargspec(onLoadCallBack)
        if "threadings" in argspec.args:
            threadingindex = argspec.args.index('threadings')
            threadingvalue = argspec[threadingindex+2]
            if type(threadingvalue) == type(()) or type(threadingvalue) == type([]):
                if len(threadingvalue) == 0:
                    threadingvalue = 0
                else:
                    threadingvalue = threadingvalue[0]
            if threadingvalue > 0:
                EventFunctionNameKey = onLoadCallBack.__module__+'.'+onLoadCallBack.__name__
                if EventFunctionNameKey in G_EventFunctionThreadDict:
                    for thread in G_EventFunctionThreadDict[EventFunctionNameKey]:
                        if not thread.is_alive():
                            G_EventFunctionThreadDict[EventFunctionNameKey].remove(thread)
                    if len(G_EventFunctionThreadDict[EventFunctionNameKey]) >= threadingvalue:
                        return
                run_thread = threading.Thread(target=onLoadCallBack, args=[uiName])
                run_thread.Daemon = True
                run_thread.start()
                if threadingvalue > 0:
                    if EventFunctionNameKey not in G_EventFunctionThreadDict:
                        G_EventFunctionThreadDict[EventFunctionNameKey] = [run_thread]
                    else:
                        G_EventFunctionThreadDict[EventFunctionNameKey].append(run_thread)
                return
        return onLoadCallBack(uiName)
def PrepareDisplayUI(uiName,form1,onLoadCallBack=None): 
    PrintFunctionInfo(PrepareDisplayUI,[uiName,form1,onLoadCallBack])
    children = form1.winfo_children()
    for child in children:    
        uiName,elementName = GetElementName(child)
        if elementName and uiName in G_UIActiveDictionary.keys():    
            G_UIActiveDictionary[uiName][elementName] = child    
    if uiName in G_UIActiveDictionary.keys():    
        G_UIActiveDictionary[uiName]['onLoad'] = onLoadCallBack    
def ActiveElement(uiName,element):    
    PrintFunctionInfo(ActiveElement,[uiName,element])
    if uiName in G_UIActiveDictionary:    
        for elementName in G_UIActiveDictionary[uiName].keys():    
            if G_UIActiveDictionary[uiName][elementName] == element:    
                G_UIActiveDictionary[uiName].pop(elementName)
                break    
    if uiName in G_UIElementDictionary.keys():
        if uiName in G_UIElementRoundRectangleDictionary:
            for elementName in G_UIElementRoundRectangleDictionary[uiName]:
                if elementName in G_UIElementDictionary[uiName].keys():
                    Control = G_UIElementDictionary[uiName][elementName]
                    if hasattr(Control,"GetEntry") == True:
                        Control = Control.GetEntry()
                    elif hasattr(Control,"GetWidget") == True:
                        Control = Control.GetWidget()
                    if Control == element:
                        RRInfo = G_UIElementRoundRectangleDictionary[uiName][elementName]
                        ShowRoundedRectangle(Control,RRInfo[0],RRInfo[1])
        Form_1 = GetElement(uiName,"Form_1")
        if Form_1 == element:    
            return    
        if uiName in G_UIElementPlaceDictionary.keys():    
            for elementName in G_UIElementPlaceDictionary[uiName]:    
                if elementName in G_UIElementDictionary[uiName].keys():    
                    Control = G_UIElementDictionary[uiName][elementName]    
                    if hasattr(Control,"GetEntry") == True:
                        Control = Control.GetEntry()
                    elif hasattr(Control,"GetWidget") == True:
                        Control = Control.GetWidget()
                    if Control == element:
                        UpdateElementPlace(uiName,elementName)
                    else:    
                        try:    
                            parentInfo = Control.winfo_parent()
                            parentWidget = Control._nametowidget(parentInfo)
                            UIRoot = GetElement(uiName,'root')
                            Form1 = GetElement(uiName,'Form_1')
                            if Form1:    
                                while parentWidget is not None and parentWidget is not Form1 and parentWidget is not UIRoot:    
                                    if parentWidget == element:    
                                        UpdateElementPlace(uiName,elementName)
                                        break    
                                    parentInfo = parentWidget.winfo_parent()
                                    parentWidget = Control._nametowidget(parentInfo)
                        except Exception as ex:    
                            print(ex)
        if uiName in G_UIActiveDictionary.keys() and len(G_UIActiveDictionary[uiName]) == 1:    
            if G_UIActiveDictionary[uiName]['onLoad'] is not None:    
                G_UIActiveDictionary[uiName]['onLoad'](uiName)
                G_UIActiveDictionary[uiName].clear()
                ReDrawCanvasRecord(uiName)
                UpdateAllElementPlace(uiName)
def ActiveFrameChildsElement_InEditor(uiName,element):    
    children = element.winfo_children()
    for child in children:    
        uiName2,elementName = GetElementName(child)
        if uiName2 and elementName:    
            realElementName = elementName    
            if uiName2 in G_UIElementAliasDictionary.keys() and realElementName in G_UIElementAliasDictionary[uiName2].keys():    
                realElementName = G_UIElementAliasDictionary[uiName2][realElementName]    
            if realElementName:    
                UpdateElementPlace(uiName2,realElementName)
def DestroyElement(uiName,elementName):   
    PrintFunctionInfo(DestroyElement,[uiName,elementName])
    #删除指定的控件  
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    if Control:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            G_UIElementAliasDictionary[uiName].pop(elementName)
        if elementName in G_UIElementDictionary[uiName].keys():    
            G_UIElementDictionary[uiName].pop(elementName)
        if uiName in G_UIElementPlaceDictionary.keys():
            if elementName in G_UIElementPlaceDictionary[uiName]:
                G_UIElementPlaceDictionary[uiName].pop(elementName)
        if uiName in G_UIElementRoundRectangleDictionary.keys():
            if elementName in G_UIElementRoundRectangleDictionary.keys():
                G_UIElementRoundRectangleDictionary[uiName].pop(elementName)
        Control.destroy() 
  
def GenNewElementName(uiName,elementType):    
    elementIndex = 1    
    for elementName in G_UIElementDictionary[uiName]:    
        if elementName.find('_') >= 0:    
            splitArray = elementName.split('_')
            elementIndex = splitArray[-1]    
    elementIndex = int(elementIndex) + 1    
    elementName = elementType+'_'+str(elementIndex)
    return elementName    

def CreateElementFromEXUIControl(uiName,ParentElement,elementType):  
    PrintFunctionInfo(CreateElementFromEXUIControl,[uiName,ParentElement,elementType])
    try:    
        uiClass = 'EXUIControl'    
        import importlib    
        from   importlib import import_module    
        importModule = importlib.import_module(uiClass)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,elementType) == True:    
            importModule.G_ExeDir = G_ExeDir    
            importModule.G_ResDir = G_ResDir    
            ElementClass = getattr(importModule,elementType)
            newElement = ElementClass(ParentElement)
            return newElement    
    except Exception as ex:    
        MessageBox('请返回工程主界面保存，由系统生成复合控件代码。')

def CreateLabel(uiName,parentName='Form_1',elementName=''):   
    PrintFunctionInfo(CreateLabel,[uiName,parentName,elementName])
    #创建Label控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newLabel = tkinter.Label(ParentElement,text="Label")
            labelName = GenNewElementName(uiName,'Label')
            Register(uiName,labelName,newLabel,elementName)
            return newLabel    
    return None    
def CreateButton(uiName,parentName='Form_1',elementName=''):  
    PrintFunctionInfo(CreateButton,[uiName,parentName,elementName])
    #创建Button控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newButton = tkinter.Button(ParentElement,text="Button")
            buttonName = GenNewElementName(uiName,'Button')
            Register(uiName,buttonName,newButton,elementName)
            return newButton    
    return None    
def CreateLabelButton(uiName,parentName='Form_1',elementName=''): 
    PrintFunctionInfo(CreateLabelButton,[uiName,parentName,elementName]) 
    #创建LabelButton控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'LabelButton')
            if newElement:    
                labelButtonName = GenNewElementName(uiName,'LabelButton')
                Register(uiName,labelButtonName,newElement,elementName)
                return newElement    
    return None    
def CreateEntry(uiName,parentName='Form_1',elementName=''):  
    PrintFunctionInfo(CreateEntry,[uiName,parentName,elementName]) 
    #创建Entry控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'CustomEntry')
            if newElement:    
                entryName = GenNewElementName(uiName,'Entry')
                Register(uiName,entryName,newElement,elementName)
                return newElement    
    return None    
def CreateText(uiName,parentName='Form_1',elementName=''):  
    PrintFunctionInfo(CreateText,[uiName,parentName,elementName]) 
    #创建Text控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newText = tkinter.Text(ParentElement)
            textName = GenNewElementName(uiName,'Text')
            Register(uiName,textName,newText,elementName)
            return newText    
    return None    
def CreateListBox(uiName,parentName='Form_1',elementName=''):    
    PrintFunctionInfo(CreateListBox,[uiName,parentName,elementName]) 
    #创建ListBox控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newListBox = tkinter.Listbox(ParentElement)
            listBoxName = GenNewElementName(uiName,'ListBox')
            Register(uiName,listBoxName,newListBox,elementName)
            return newListBox    
    return None    
def CreateComboBox(uiName,parentName='Form_1',elementName=''):   
    PrintFunctionInfo(CreateComboBox,[uiName,parentName,elementName]) 
    #创建ComboBox控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            comboBoxName = GenNewElementName(uiName,'ComboBox')
            comboBoxVariable = AddTKVariable(uiName,comboBoxName)
            newComboBox = tkinter.ttk.Combobox(ParentElement,textvariable=comboBoxVariable, state="readonly")
            Register(uiName,comboBoxName,newComboBox,elementName)
            return newComboBox    
    return None    
def CreateRadioButtonGroup(uiName,parentName='Form_1',groupName='',defaultValue=1):    
    PrintFunctionInfo(CreateRadioButtonGroup,[uiName,parentName,groupName,defaultValue]) 
    #创建RadioButtonGroup  
    if uiName in G_UIElementDictionary:    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            groupVariable = AddTKVariable(uiName,groupName,defaultValue)
            AddUserData(uiName,parentName,groupName,"radiogroup",groupVariable,0)
            return groupVariable    
    return None    
def CreateRadioButton(uiName,parentName='Form_1',elementName='',groupName='',defaultValue=1,style='indicatoron'): 
    PrintFunctionInfo(CreateRadioButton,[uiName,parentName,elementName,groupName,defaultValue,style]) 
    #创建RadioButton控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            radioButtonName = GenNewElementName(uiName,'RadioButton')
            groupVariable = GetUserData(uiName,parentName,groupName)
            newRadioButton = tkinter.Radiobutton(ParentElement,variable=groupVariable,value=defaultValue,text="RadioButton",anchor=tkinter.W)
            Register(uiName,radioButtonName,newRadioButton,elementName,groupName)
            if style == 'normal':    
                newRadioButton.configure(indicatoron = False)
            elif style == 'selfdrawing':    
                SetRadioButtonPyMeStyle(uiName,radioButtonName,defaultValue,'#000000','#000000')
            return newRadioButton    
    return None    
def CreateCheckButton(uiName,parentName='Form_1',elementName='',defaultValue=False,style='indicatoron'): 
    PrintFunctionInfo(CreateCheckButton,[uiName,parentName,elementName,defaultValue,style]) 
    #创建CheckButton控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            checkButtonName = GenNewElementName(uiName,'CheckButton')
            checkButtonVariable = AddTKVariable(uiName,checkButtonName)
            checkButtonVariable.set(defaultValue)
            newCheckButton = tkinter.Checkbutton(ParentElement,variable=checkButtonVariable,text="CheckButton",anchor=tkinter.W)
            Register(uiName,checkButtonName,newCheckButton,elementName)
            if style == 'normal':    
                newCheckButton.configure(indicatoron = False)
            elif style == 'selfdrawing':    
                SetCheckButtonPyMeStyle(uiName,checkButtonName,defaultValue,'#000000','#000000')
            return newCheckButton    
    return None    
def CreateSwitchButton(uiName,parentName='Form_1',elementName=''): 
    PrintFunctionInfo(CreateSwitchButton,[uiName,parentName,elementName]) 
    #创建SwitchButton控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'SwitchButton')
            if newElement:    
                switchButtonName = GenNewElementName(uiName,'SwitchButton')
                Register(uiName,switchButtonName,newElement,elementName)
                return newElement    
    return None    
def CreateLabelFrame(uiName,parentName='Form_1',elementName=''): 
    PrintFunctionInfo(CreateLabelFrame,[uiName,parentName,elementName])   
    #创建LabelFrame控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newLabelFrame = tkinter.LabelFrame(ParentElement)
            labelFrameName = GenNewElementName(uiName,'LabelFrame')
            Register(uiName,labelFrameName,newLabelFrame,elementName)
            return newLabelFrame    
    return None    
def CreateFrame(uiName,parentName='Form_1',elementName=''):    
    PrintFunctionInfo(CreateFrame,[uiName,parentName,elementName])   
    #创建Frame控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newFrame = tkinter.Frame(ParentElement)
            frameName = GenNewElementName(uiName,'Frame')
            Register(uiName,frameName,newFrame,elementName)
            return newFrame    
    return None    
def CreateCanvas(uiName,parentName='Form_1',elementName=''):   
    PrintFunctionInfo(CreateCanvas,[uiName,parentName,elementName])   
    #创建Canvas控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newCanvas = tkinter.Canvas(ParentElement)
            canvasName = GenNewElementName(uiName,'Canvas')
            Register(uiName,canvasName,newCanvas,elementName)
            return newCanvas    
    return None    
def CreateScale(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL): 
    PrintFunctionInfo(CreateScale,[uiName,parentName,elementName,orient])   
    #创建Scale控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newScale = tkinter.Scale(ParentElement,orient = tkinter.HORIZONTAL)
            scaleName = GenNewElementName(uiName,'Scale')
            Register(uiName,scaleName,newScale,elementName)
            return newScale    
    return None    
def CreateSlider(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL): 
    PrintFunctionInfo(CreateSlider,[uiName,parentName,elementName,orient])  
    #创建Slider控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Slider')
            if newElement:    
                sliderName = GenNewElementName(uiName,'Slider')
                Register(uiName,sliderName,newElement,elementName)
                return newElement    
    return None    
def CreateProgress(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL):   
    PrintFunctionInfo(CreateProgress,[uiName,parentName,elementName,orient])  
    #创建Progress控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newProgress = tkinter.ttk.Progressbar(ParentElement,orient = orient)
            progressName = GenNewElementName(uiName,'Progress')
            Register(uiName,progressName,newProgress,elementName)
            return newProgress    
    return None    
def CreateProgressDial(uiName,parentName='Form_1',elementName=''):   
    PrintFunctionInfo(CreateProgressDial,[uiName,parentName,elementName])  
    #创建ProgressDial控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ProgressDial')
            if newElement:    
                progressDialName = GenNewElementName(uiName,'ProgressDial')
                Register(uiName,progressDialName,newElement,elementName)
                return newElement    
    return None    
def CreateSpinBox(uiName,parentName='Form_1',elementName=''): 
    PrintFunctionInfo(CreateSpinBox,[uiName,parentName,elementName])  
    #创建SpinBox控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newSpinBox = tkinter.Spinbox(ParentElement)
            spinBoxName = GenNewElementName(uiName,'SpinBox')
            Register(uiName,spinBoxName,newSpinBox,elementName)
            return newSpinBox    
    return None    
def CreateTreeView(uiName,parentName='Form_1',elementName=''):    
    PrintFunctionInfo(CreateTreeView,[uiName,parentName,elementName])  
    #创建TreeView控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newTreeView = tkinter.ttk.Treeview(ParentElement,show="tree")
            treeViewName = GenNewElementName(uiName,'TreeView')
            Register(uiName,treeViewName,newTreeView,elementName)
            return newTreeView    
    return None    
def CreateListView(uiName,parentName='Form_1',elementName=''):
    PrintFunctionInfo(CreateListView,[uiName,parentName,elementName])  
    #创建ListView控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newListView = tkinter.ttk.Treeview(ParentElement,show="headings")
            listViewName = GenNewElementName(uiName,'ListView')
            Register(uiName,listViewName,newListView,elementName)
            return newListView    
    return None    
def CreateNoteBook(uiName,parentName='Form_1',elementName=''):    
    PrintFunctionInfo(CreateNoteBook,[uiName,parentName,elementName])  
    #创建NoteBook控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newNoteBook = tkinter.ttk.Notebook(ParentElement)
            noteBookName = GenNewElementName(uiName,'NoteBook')
            Register(uiName,noteBookName,newNoteBook,elementName)
            return newNoteBook    
    return None    
def CreatePanedWindow(uiName,parentName='Form_1',elementName='',orient = tkinter.HORIZONTAL): 
    PrintFunctionInfo(CreatePanedWindow,[uiName,parentName,elementName,orient])  
    #创建PanedWindow控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newPanedWindow = tkinter.PanedWindow(ParentElement)
            panedWindowName = GenNewElementName(uiName,'PanedWindow')
            Register(uiName,panedWindowName,newPanedWindow,elementName)
            newPanedWindow.configure(showhandle = '0')
            newPanedWindow.configure(sashrelief = 'flat')
            newPanedWindow.configure(sashwidth = '4')
            newPanedWindow.configure(orient = orient)
            return newPanedWindow    
    return None    
def CreateCalendar(uiName,parentName='Form_1',elementName=''):  
    PrintFunctionInfo(CreateCalendar,[uiName,parentName,elementName])  
    #创建Calendar控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Calendar')
            if newElement:    
                calendarName = GenNewElementName(uiName,'Calendar')
                Register(uiName,calendarName,newElement,elementName)
                return newElement    
    return None    
def CreateDatePicker(uiName,parentName='Form_1',elementName=''): 
    PrintFunctionInfo(CreateDatePicker,[uiName,parentName,elementName])  
    #创建DatePicker控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'DatePicker')
            if newElement:    
                datepickerName = GenNewElementName(uiName,'DatePicker')
                Register(uiName,datepickerName,newElement,elementName)
                return newElement    
    return None    
def CreateNavigation(uiName,parentName='Form_1',elementName='',direction = tkinter.HORIZONTAL):   
    PrintFunctionInfo(CreateNavigation,[uiName,parentName,elementName,direction])  
    #创建Navigation控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'Navigation')
            if newElement:    
                navigationName = GenNewElementName(uiName,'Navigation')
                Register(uiName,navigationName,newElement,elementName)
                return newElement    
    return None    
def CreateListMenu(uiName,parentName='Form_1',elementName=''):    
    PrintFunctionInfo(CreateListMenu,[uiName,parentName,elementName])  
    #创建ListMenu控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ListMenu')
            if newElement:    
                listmenuName = GenNewElementName(uiName,'ListMenu')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement    
    return None    
def CreateSwitchPage(uiName,parentName='Form_1',elementName=''):  
    PrintFunctionInfo(CreateSwitchPage,[uiName,parentName,elementName])  
    #创建SwitchPage控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'SwitchPage')
            if newElement:    
                listmenuName = GenNewElementName(uiName,'SwitchPage')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement    
    return None    
def CreateShowCase(uiName,parentName='Form_1',elementName=''):   
    PrintFunctionInfo(CreateShowCase,[uiName,parentName,elementName])  
    #创建ShowCase控件  
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementAliasDictionary[uiName].keys():    
            return None    
        ParentElement = GetElement(uiName,parentName)
        if ParentElement:    
            newElement = CreateElementFromEXUIControl(uiName,ParentElement,'ShowCase')
            if newElement:    
                listmenuName = GenNewElementName(uiName,'ShowCase')
                Register(uiName,listmenuName,newElement,elementName)
                return newElement    
    return None    
def SetBindEventFunction(uiName,elementName,eventName,callbackFunction=None):  
    PrintFunctionInfo(SetBindEventFunction,[uiName,elementName,eventName,callbackFunction])  
    #设置控件的事件响应函数  
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    if Control and callbackFunction:    
        RealElementName = elementName    
        if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():    
            RealElementName = G_UIElementAliasDictionary[uiName][RealElementName]     
        if eventName == 'Command':    
            if RealElementName.find('Scale_') >= 0:     
                Control.configure(command=SetValueChangedFunction(callbackFunction,uiName = uiName,widgetName = elementName))
            else:     
                Control.configure(command=partial(CommandFunction_Adaptor,fun=callbackFunction,uiName = uiName,elementName = ElementInfo['AliasName']))
        elif eventName == 'TreeviewSelect' or eventName == 'TreeviewOpen' or eventName == 'TreeviewClose' or eventName == 'ListboxSelect' or eventName == 'ComboboxSelected' or eventName == 'NotebookTabChanged':    
            bindEventName = str('<<'+eventName+'>>')
            Control.bind(bindEventName,EventFunction_Adaptor(callbackFunction,uiName = uiName,widgetName = elementName),add=True)
        elif eventName == 'ListviewCellSelected':    
            Control.bind('<Button-1>',EventFunction_Adaptor(OnListViewCellClicked,uiName = uiName,widgetName = elementName,callbackFunc=callbackFunction),add=True)
        elif eventName == 'ListViewHeadingClicked':    
            Columns = Control.cget('column')
            G_ListViewCommandDictionary[uiName][elementName] = callbackFunction
            for columnName in Columns:    
                Control.heading(columnName,command=partial(ListViewHeadingFunction_Adaptor,fun=callbackFunction,uiName = uiName,widgetName = elementName,columnname=columnName))
        else:    
            bindEventName = str('<'+eventName+'>')
            Control.bind(bindEventName,EventFunction_Adaptor(callbackFunction,uiName = uiName,widgetName = elementName))
def SetElementScrollbar(uiName,elementName,orient=tkinter.VERTICAL):
    PrintFunctionInfo(SetElementScrollbar,[uiName,elementName,orient])  
    #设置控件的滚动条 
    Control = GetElement(uiName,elementName)  
    if Control:
        if hasattr(Control,"GetEntry") == True:    
            Control = Control.GetEntry()
        elif hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
        ScrollTarget = GetElement(uiName,elementName+"_Child")
        if ScrollTarget is None:
            ScrollTarget = Control
        Control_Width = ScrollTarget.winfo_width()
        Control_Height = ScrollTarget.winfo_height()
        if orient == tkinter.VERTICAL:
            VerticleScrollBar = tkinter.ttk.Scrollbar(Control,orient=tkinter.VERTICAL)
            VerticleScrollBarName = elementName+'_VScrollbar'
            Register(uiName,VerticleScrollBarName,VerticleScrollBar)
            VerticleScrollBar.place(x = Control_Width - 20,y = 0,width = 20,height = Control_Height)
            VerticleScrollBar.config(command = ScrollTarget.yview)
            ScrollTarget.config(yscrollcommand = VerticleScrollBar.set)
            def ResetVerticleScrollBar(event):
                HorizontalScrollBarName = elementName+'_HScrollbar'
                HorizontalScrollBar = GetElement(uiName,HorizontalScrollBarName)
                if HorizontalScrollBar:    
                    VerticleScrollBar.place(x = event.width - 20,y = 0,width = 20,height = event.height-20)
                else:
                    VerticleScrollBar.place(x = event.width - 20,y = 0,width = 20,height = event.height)
            ScrollTarget.bind('<Configure>',ResetVerticleScrollBar,add=True) 
        else:
            HorizontalScrollBar = tkinter.ttk.Scrollbar(Control,orient=tkinter.HORIZONTAL)
            HorizontalScrollBarName = elementName+'_HScrollbar'
            Register(uiName,HorizontalScrollBarName,HorizontalScrollBar)   
            HorizontalScrollBar.place(x = 0,y = Control_Height - 20,width = Control_Width,height = 20)
            HorizontalScrollBar.config(command = ScrollTarget.xview)
            ScrollTarget.config(xscrollcommand = HorizontalScrollBar.set)
            def ResetHorizontalScrollBar(event):
                HorizontalScrollBar.place(x = 0,y = event.height - 20,width = event.width,height = 20)
            ScrollTarget.bind('<Configure>',ResetHorizontalScrollBar,add=True)
def CreateUIFormJson(uiName,root,isTKroot,style,JsonString,SupportModule=True): 
    global G_PrintFunctionMode
    global G_ExeDir
    global G_ResDir
    PrintFunctionInfo(CreateUIFormJson,[uiName,root,isTKroot,style,JsonString,SupportModule]) 
    if EXUIControl.FunLib is None:
        EXUIControl.FunLib = sys.modules[__name__]
    if EXUIControl.G_ExeDir is None:
        EXUIControl.G_ExeDir = G_ExeDir
    if EXUIControl.G_ResDir is None:
        EXUIControl.G_ResDir = G_ResDir
    #从JSON文件中加载界面控件  
    UICmd = G_UICommandDictionary[uiName]   
    Form_1 = None    
    if JsonString !='':    
        try:    
            G_UIGlobalElementDictionary[uiName]={} 
            Register(uiName,'style',style)
            JsonString = JsonString.rstrip('\x00')
            JsonString = JsonString.replace('\x13','')
            BeginIndex = JsonString.rfind('{"Version":')
            JsonString = JsonString[BeginIndex:]
            UIInfoDict = json.loads(JsonString)
            Version = UIInfoDict['Version']    
            UIName = UIInfoDict['UIName']
            Description = UIInfoDict['Description']    
            if isTKroot == True:    
                if UIInfoDict['WindowResizable'] == False:
                    root.resizable(False,False)
                SetTitleBar(root,titleText=UIInfoDict['WindowTitle'],isDarkMode=UIInfoDict['DarkMode'],isDropTitle=UIInfoDict['DropTitle'])
                CenterDlg(uiName,root,UIInfoDict['WindowSize'][0],UIInfoDict['WindowSize'][1])
                WindowDraggable(root,UIInfoDict['DarkMode'],UIInfoDict['BorderWidth'],UIInfoDict['BorderColor'])
                root['background'] = UIInfoDict['BGColor']    
                if UIInfoDict['MinSize'] and UIInfoDict['MinSize'] != [0,0]:
                    root.minsize(UIInfoDict['MinSize'][0],UIInfoDict['MinSize'][1])
                if 'TransparentColor' in UIInfoDict.keys() and  UIInfoDict['TransparentColor']:
                    root.wm_attributes("-transparentcolor",UIInfoDict['TransparentColor'])
                if 'RootTransparency' in UIInfoDict.keys() :
                    SetTransparencyFunction(root,UIInfoDict['RootTransparency'])
                if 'ICOFile' in UIInfoDict.keys() and  UIInfoDict['ICOFile']:
                    if 'ICOMode' in UIInfoDict.keys() and UIInfoDict['ICOMode'] == "Base64":
                        pass
                    else:
                        ICOFilePath = UIInfoDict['ICOFile'].replace('\\','/')
                        if os.path.exists(ICOFilePath)  == False:
                            ICOFilePath = os.path.join(G_ResDir,UIInfoDict['ICOFile'])
                            ICOFilePath = ICOFilePath.replace('\\','/')
                        if os.path.exists(ICOFilePath)  == True:
                            if ICOFilePath.find(".png") > 0:
                                root.iconphoto(False, ImageTk.PhotoImage(file=ICOFilePath))
                            else:
                                root.iconbitmap(ICOFilePath)
                if 'WinState' in UIInfoDict.keys():
                    if UIInfoDict['WinState'] == 3 :
                        root.state("zoomed")
                        SetUIState(uiName,"zoomed")
                if 'WinTopMost' in UIInfoDict.keys():
                    if UIInfoDict['WinTopMost'] == True :
                        root.wm_attributes("-topmost",1)

            SetUIRootSize(uiName,UIInfoDict['WindowSize'][0],UIInfoDict['WindowSize'][1])

            if 'GroupList' in UIInfoDict.keys():    
                for GroupName in UIInfoDict['GroupList']:    
                    Group_Variable = AddTKVariable(uiName,GroupName)
                    Group_Variable.set(UIInfoDict['GroupList'][GroupName])
            
            def GetElementValue(ElementInfo,key,defaultValue = None):    
                if key in ElementInfo.keys():    
                    return ElementInfo[key]    
                else:    
                    return defaultValue

            def SetElementLayout(uiName,ElementName,ElementInfo):    
                if 'PackInfo' in ElementInfo:    
                    SetControlPack(uiName,ElementName,ElementInfo['PackInfo'][0],ElementInfo['PackInfo'][1],ElementInfo['PackInfo'][2],ElementInfo['PackInfo'][3],ElementInfo['PackInfo'][4],ElementInfo['PackInfo'][5],ElementInfo['PackInfo'][6])
                elif 'GridInfo' in ElementInfo:    
                    SetControlGrid(uiName,ElementName,ElementInfo['GridInfo'][0],ElementInfo['GridInfo'][1],ElementInfo['GridInfo'][2],ElementInfo['GridInfo'][3])
                else:   
                    InFrameCanvas = False 
                    if 'ParentName' in ElementInfo.keys():
                        if ElementInfo['ParentName'] != 'Form_1':
                            ParentElement = GetElement(uiName,'PyMe_'+ElementInfo['ParentName'])
                            if ElementInfo['ParentName'].find("Frame") >= 0 and ElementName.find("Form_") < 0:
                                FrameCanvas = GetElement(uiName,'PyMe_'+ElementInfo['ParentName']+"_Child")
                                Control = GetElement(uiName,ElementName) 
                                if FrameCanvas and Control:
                                    if type(ElementInfo['PlaceInfo'][0]) == type(1) and type(ElementInfo['PlaceInfo'][1]) == type(1):
                                        if type(ElementInfo['PlaceInfo'][0]) == type(1) and type(ElementInfo['PlaceInfo'][3]) == type(1):
                                            if hasattr(Control,"GetWidget") == True:    
                                                Control = Control.GetWidget()
                                            ControlHandle = FrameCanvas.create_window(ElementInfo['PlaceInfo'][0], ElementInfo['PlaceInfo'][1], window=Control, anchor=tkinter.NW)
                                            FrameCanvas.itemconfig(ControlHandle,width=ElementInfo['PlaceInfo'][2],height=ElementInfo['PlaceInfo'][3])
                                            InFrameCanvas = True
                                            PlaceDictionary = {}  
                                            PlaceDictionary["type"] = "place"    
                                            PlaceDictionary["x"] = ElementInfo['PlaceInfo'][0]
                                            PlaceDictionary["y"] = ElementInfo['PlaceInfo'][1]
                                            PlaceDictionary["relwidth"] = ElementInfo['PlaceInfo'][2]
                                            PlaceDictionary["relheight"] = ElementInfo['PlaceInfo'][3]
                                            PlaceDictionary["visible"] = True    
                                            PlaceDictionary["anchorpoint"] = ElementInfo['PlaceInfo'][4]    
                                            G_UIElementPlaceDictionary[uiName][ElementName] = PlaceDictionary   
                    if InFrameCanvas == False:
                        SetControlPlace(uiName,ElementName,ElementInfo['PlaceInfo'][0],ElementInfo['PlaceInfo'][1],ElementInfo['PlaceInfo'][2],ElementInfo['PlaceInfo'][3],ElementInfo['PlaceInfo'][4],ElementInfo['PlaceInfo'][5],True)#ElementInfo['PlaceInfo'][6])
                if ElementInfo['Visible'] == False:    
                    SetVisible(uiName,ElementName,False)

            def SetElementFont(ElementInst,ElementInfo,IsEXUIControl = False):  
                if 'Font' in ElementInfo.keys():    
                    FontInfo = ElementInfo['Font']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetFont(newFont)  
                    else:
                        ElementInst.configure(font = newFont)

                if 'Font_Hover' in ElementInfo.keys():    
                    FontInfo = ElementInfo['Font_Hover']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetFont_Hover(newFont)  

                if 'Font_Click' in ElementInfo.keys():    
                    FontInfo = ElementInfo['Font_Click']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetFont_Click(newFont)  

                if 'TitleFont' in ElementInfo.keys():    
                    FontInfo = ElementInfo['TitleFont']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetTitleFont(newFont,False)  

                if 'TitleFont_Hover' in ElementInfo.keys():    
                    FontInfo = ElementInfo['TitleFont_Hover']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetTitleFont_Hover(newFont)  

                if 'TitleFont_Click' in ElementInfo.keys():    
                    FontInfo = ElementInfo['TitleFont_Click']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetTitleFont_Click(newFont)  

                if 'ItemFont' in ElementInfo.keys():    
                    FontInfo = ElementInfo['ItemFont']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetItemFont(newFont,False)  

                if 'ItemFont_Hover' in ElementInfo.keys():    
                    FontInfo = ElementInfo['ItemFont_Hover']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetItemFont_Hover(newFont)  

                if 'ItemFont_Click' in ElementInfo.keys():    
                    FontInfo = ElementInfo['ItemFont_Click']    
                    newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                    if IsEXUIControl == True:
                        ElementInst.SetItemFont_Click(newFont)  


            def SetElementTagList(ElementInst,ElementInfo):    
                ElementType = ElementInfo['Type']
                if 'TagList' in ElementInfo:    
                    for TagInfo in ElementInfo['TagList']:  
                        if ElementType == "TreeView" or ElementType == "ListView":
                            if len(TagInfo) == 2:    
                                ElementInst.tag_configure(TagInfo[0],foreground=TagInfo[1])
                            else:    
                                ElementInst.tag_configure(TagInfo[0],foreground=TagInfo[7])
                                ElementInst.tag_configure(TagInfo[0],font=tkinter.font.Font(family=TagInfo[1], size=TagInfo[2],weight=TagInfo[3],slant=TagInfo[4],underline=TagInfo[5],overstrike=TagInfo[6]))
                        else:  
                            if len(TagInfo) == 2:    
                                ElementInst.tag_config(TagInfo[0],foreground=TagInfo[1])
                            else:    
                                ElementInst.tag_config(TagInfo[0],font=tkinter.font.Font(family=TagInfo[1], size=TagInfo[2],weight=TagInfo[3],slant=TagInfo[4],underline=TagInfo[5],overstrike=TagInfo[6]),foreground=TagInfo[7])
            def LoadElementIconList(ElementName,ElementInfo):
                IconDict = {}
                if 'IconList' in ElementInfo:    
                    for IconInfo in ElementInfo['IconList']:    
                        IconName = IconInfo[0]
                        FileName = IconInfo[1]
                        IconDict[IconName]= LoadImageToIconList(uiName,ElementName,IconName,FileName)
                return IconDict

            #构建TreeView
            def BuildTreeView(ElementInst,ParentItem,ParentList,IconDict):
                for ItemInfo in ParentList:
                    ItemName = ItemInfo[0]
                    ItemValue = ItemInfo[1]
                    if isinstance(ItemValue,str) == True:
                        ItemValue = ItemValue.strip().replace("'","").replace('"','')
                    IconName  = ItemInfo[2]
                    TagName  = ItemInfo[3]
                    if IconName in IconDict.keys():
                        if TagName:
                            ItemInfo[4] = ElementInst.insert(ParentItem,'end',ItemName,text=ItemName,image=IconDict[IconName],values=ItemValue,tag=TagName)
                        else:
                            ItemInfo[4] = ElementInst.insert(ParentItem,'end',ItemName,text=ItemName,image=IconDict[IconName],values=ItemValue)
                    else:
                        if TagName:
                            ItemInfo[4] = ElementInst.insert(ParentItem,'end',ItemName,text=ItemName,values=ItemValue,tag=TagName)
                        else:
                            ItemInfo[4] = ElementInst.insert(ParentItem,'end',ItemName,text=ItemName,values=ItemValue)
                    ChildrenCount = len(ItemInfo[5])
                    if ChildrenCount > 0:
                        BuildTreeView(ElementInst,ItemInfo[4],ItemInfo[5],IconDict)
            #构建ListView
            def BuildListView(ElementInst,ElementInfo):
                if 'ColumnList' in ElementInfo.keys():
                    ColumnList = ElementInfo['ColumnList']
                    EventDict = {}
                    if 'EventList' in ElementInfo.keys():
                        EventDict = ElementInfo['EventList']
                    ColumnNames = []
                    for ColumnInfo in ColumnList:    
                        ColumnNames.append(ColumnInfo[0])
                    ElementInst.configure(columns=ColumnNames)
                    for ColumnInfo in ColumnList:   
                        ColumnName = ColumnInfo[0]
                        AlignType = ColumnInfo[1]
                        ColumnWidth = ColumnInfo[2]
                        ColumnStretch = ColumnInfo[3]
                        ElementInst.column(ColumnName,anchor=AlignType,width=ColumnWidth,stretch=ColumnStretch)
                        ElementInst.heading(ColumnName,anchor=AlignType,text=ColumnName)
            #构建NoteBook
            def BuildNoteBook(uiName,ElementName,ElementInfo):
                if 'PageList' in ElementInfo.keys():
                    for PageInfo in ElementInfo['PageList']:
                        TitleName = PageInfo[0]
                        IconFile = PageInfo[1]
                        ImportUI = PageInfo[2]
                        AddPage(uiName,ElementName,TitleName,IconFile,ImportUI)
            #构建Navigation
            def BuildNavigation(ElementInst,ElementInfo):
                ElementInst.Clear()
                if 'ItemList' in ElementInfo.keys():
                    for ItemInfo in ElementInfo['ItemList']:
                        ElementInst.AddItem(ItemInfo[0],ItemInfo[1],ItemInfo[2])
                ElementInst.Redraw()
            #构建SwitchPage
            def BuildSwitchPage(ElementInst,ElementInfo):
                if 'PageList' in ElementInfo.keys():
                    for PageInfo in ElementInfo['PageList']:
                        ElementInst.AddPage(PageInfo[0],PageInfo[1],PageInfo[2])
                    ElementInst.Play()
                    ElementInst.Redraw()
            #构建ShowCase
            def BuildShowCase(ElementInst,ElementInfo):
                if 'ItemList' in ElementInfo.keys():
                    for ItemInfo in ElementInfo['ItemList']:
                        ElementInst.AddItem(ItemInfo[0],ItemInfo[1],ItemInfo[2])
                    ElementInst.Redraw()
            #构建ListMenu
            def BuildListMenu(ElementInst,ElementInfo):
                if 'TitleList' in ElementInfo.keys():
                    for TitleInfo in ElementInfo['TitleList']:
                        if type(TitleInfo[2]) == type([]):
                            ElementInst.AddTitle(TitleInfo[0],TitleInfo[1])
                            for ItemInfo in TitleInfo[2]:    
                                ElementInst.AddItem(ItemInfo[0],TitleInfo[0],ItemInfo[1],ItemInfo[2])
                        else:
                            ElementInst.AddTitle(TitleInfo[0],TitleInfo[1],TitleInfo[2])
                        if TitleInfo[3] == False:    
                            ElementInst.ExpandTitle(TitleInfo[0],False)
                    ElementInst.Redraw()
            #开始遍历所有的控件
            if 'WidgetList' in UIInfoDict.keys():
                ElementList = UIInfoDict['WidgetList']
                ElementDict = {}
                IsPyMeModule = False
                Form_1 = None
                for ElementInfo in ElementList:
                    if G_PrintFunctionMode == True:
                        print("Load:"+str(ElementInfo))
                    ElementType = ElementInfo['Type']
                    ElementIndex = ElementInfo['Index']
                    ElementName = 'PyMe_'+ElementType + '_'+str(ElementIndex)
                    ElementAliasName = ElementName
                    if 'AliasName' in ElementInfo.keys():
                        ElementAliasName = ElementInfo['AliasName']
                    ParentElement = Form_1
                    ElementInFrameCanvas = False
                    if 'ParentName' in ElementInfo.keys():
                        if ElementInfo['ParentName'] != 'Form_1':
                            ParentElement = GetElement(uiName,'PyMe_'+ElementInfo['ParentName'])
                            if ElementInfo['ParentName'].find("Frame") >= 0:
                                ParentElement = GetElement(uiName,'PyMe_'+ElementInfo['ParentName']+"_Child")
                                ElementInFrameCanvas = True
                    if ParentElement is None:
                        ParentElement = Form_1
                    NewElementInst = None
                    GroupName = None
                    if 'GroupID' in ElementInfo.keys():
                        GroupName = str('Group_%d'%(ElementInfo['GroupID']))
                    StyleName = None
                    if 'Style' in ElementInfo.keys():
                        StyleName = ElementInfo['Style']
                    if ElementType == 'Form':
                        Form_1= tkinter.Canvas(root)
                        Register(uiName,'Form_1',Form_1)
                        Form_1.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=True)
                        if 'BGColor' in ElementInfo.keys():    
                            Form_1.configure(bg = ElementInfo['BGColor'])
                        Form_1.configure(highlightthickness = 0)
                        if 'BGImage' in ElementInfo.keys():    
                            SetCanvasBGImage(uiName,'Form_1',ElementInfo['BGImage'],ElementInfo['BGImageWrap'])
                        NewElementInst = Form_1    
                    elif ElementType == 'Canvas':    
                        NewElementInst = tkinter.Canvas(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        NewElementInst.configure(highlightthickness = 0)
                        if 'BGImage' in ElementInfo.keys():    
                            SetCanvasBGImage(uiName,ElementName,ElementInfo['BGImage'],ElementInfo['BGImageWrap'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'BorderWidth' in ElementInfo.keys():    
                            NewElementInst.configure(highlightthickness = ElementInfo['BorderWidth'])
                            NewElementInst.configure(bd = ElementInfo['BorderWidth'])
                        if 'BorderColor' in ElementInfo.keys():    
                            NewElementInst.configure(highlightbackground = ElementInfo['BorderColor'])
                            NewElementInst.configure(highlightcolor = ElementInfo['BorderColor'])
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.HORIZONTAL)
                            if ElementInfo['ScrollBarList'][1] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.VERTICAL)
                            if 'ScrollRegion' in ElementInfo:  
                                if ElementInfo['ScrollRegion']:
                                    ScrollRegion = ElementInfo['ScrollRegion']
                                    NewElementInst.config(scrollregion=(0,0,ScrollRegion[0],ScrollRegion[1]))
                    elif ElementType == 'LabelFrame' or ElementType == 'Frame': 
                        if ElementType == 'LabelFrame':
                            if 'Style' in ElementInfo.keys():
                                NewElementInst = tkinter.ttk.LabelFrame(ParentElement,text=ElementInfo['Text'],style=ElementInfo['Style'])
                            else:
                                if 'PackInfo' in ElementInfo.keys():
                                    NewElementInst = tkinter.LabelFrame(ParentElement,text=ElementInfo['Text'],width=ElementInfo['Size'][0],height=ElementInfo['Size'][1],takefocus = True)
                                else:
                                    NewElementInst = tkinter.LabelFrame(ParentElement,text=ElementInfo['Text'],takefocus = True)
                        else:
                            if 'Style' in ElementInfo.keys():    
                                NewElementInst = tkinter.ttk.Frame(ParentElement,style=ElementInfo['Style'])
                            else:    
                                if 'PackInfo' in ElementInfo.keys():
                                    NewElementInst = tkinter.Frame(ParentElement,width=ElementInfo['Size'][0],height=ElementInfo['Size'][1])
                                else:
                                    NewElementInst = tkinter.Frame(ParentElement)

                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.configure(fg = ElementInfo['FGColor'])
                        if 'Anchor' in ElementInfo.keys():    
                            NewElementInst.configure(labelanchor = ElementInfo['Anchor'])
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])

                        EmbedUI = None    
                        if 'EmbedUI' in ElementInfo.keys():
                            PagePyClass, PageExtension = os.path.splitext(ElementInfo['EmbedUI'])
                            EmbedUI = LoadUIDialog(uiName,ElementName,PagePyClass)
                        else:
                            LoadUIDialog(uiName,ElementName,None)
                            FrameCanvas = GetElement(uiName,ElementName+"_Child")
                            if FrameCanvas:
                                if 'BGColor' in ElementInfo.keys():    
                                    FrameCanvas.configure(bg = ElementInfo['BGColor'])
                        if 'Drag' in ElementInfo.keys():
                            if ElementInfo['Drag'] == True:
                                if EmbedUI:
                                    FrameDraggable(NewElementInst,EmbedUI)
                                else:    
                                    FrameDraggable(NewElementInst)
                        #滚动条加载
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.HORIZONTAL)
                            if ElementInfo['ScrollBarList'][1] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.VERTICAL)

                            FrameCanvas = GetElement(uiName,ElementName+"_Child")
                            if FrameCanvas :
                                if EmbedUI:
                                    uiDialogWidth = EmbedUI.root.winfo_width()
                                    uiDialogHeight = EmbedUI.root.winfo_height()
                                    if hasattr(EmbedUI,"GetRootSize") == True:    
                                        uiDialogWidth,uiDialogHeight = EmbedUI.GetRootSize()
                                    uiDialogForm1 = None    
                                    ChildWidgetList = EmbedUI.root.children    
                                    for widgetName in ChildWidgetList.keys():    
                                        uiDialogForm1  = ChildWidgetList[widgetName]    
                                        ChildHandle = FrameCanvas.create_window(0,0, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                                        FrameCanvas.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                                    FrameCanvas.config(scrollregion=(0,0,uiDialogWidth,uiDialogHeight))

                                if 'ScrollRegion' in ElementInfo:  
                                    if ElementInfo['ScrollRegion']:
                                        ScrollRegion = ElementInfo['ScrollRegion']
                                        FrameCanvas.config(scrollregion=(0,0,ScrollRegion[0],ScrollRegion[1]))

                    elif ElementType == 'Label':    
                        if 'AutoWrap' in ElementInfo.keys():    
                            if 'Style' in ElementInfo.keys():    
                                NewElementInst = tkinter.ttk.Message(ParentElement,text=ElementInfo['Text'],style=ElementInfo['Style'])
                            else:    
                                NewElementInst = tkinter.Message(ParentElement,text=ElementInfo['Text'])
                        else:    
                            if 'Style' in ElementInfo.keys():    
                                NewElementInst = tkinter.ttk.Label(ParentElement,text=ElementInfo['Text'],style=ElementInfo['Style'])
                            else:    
                                NewElementInst = tkinter.Label(ParentElement,text=ElementInfo['Text'])
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.configure(fg = ElementInfo['FGColor'])
                        Anchor = 'center'    
                        if 'Anchor' in ElementInfo.keys():    
                            Anchor = ElementInfo['Anchor']    
                            NewElementInst.configure(anchor = Anchor)
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'AutoWrap' in ElementInfo.keys():    
                            if Anchor == 'center':    
                                NewElementInst.configure(justify = 'center')
                            elif Anchor.find('w') >= 0:    
                                NewElementInst.configure(justify = 'left')
                            elif Anchor.find('e') >= 0:    
                                NewElementInst.configure(justify = 'right')
                        autoSize = False
                        if 'Compound' in ElementInfo.keys():
                            if ElementInfo['Compound'] == "none" or ElementInfo['Compound'] == "center":    
                                autoSize = True
                        if 'BGImage' in ElementInfo.keys():
                            SetImage(uiName,ElementName,ElementInfo['BGImage'],autoSize)
                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.configure(compound = ElementInfo['Compound'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])   
                    elif ElementType == 'Entry':    
                        NewElementInst = EXUIControl.CustomEntry(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'BGColor_ReadOnly' in ElementInfo.keys():    
                            NewElementInst.SetBGColor_ReadOnly(ElementInfo['BGColor_ReadOnly'])
                        SetElementFont(NewElementInst,ElementInfo,True)  
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.SetFGColor(ElementInfo['FGColor'])
                        if 'Justify' in ElementInfo.keys():    
                            NewElementInst.SetJustify(ElementInfo['Justify'])
                        if 'ShowChar' in ElementInfo.keys():    
                            NewElementInst.SetShowChar(ElementInfo['ShowChar'])
                        if 'Restriction' in ElementInfo.keys():    
                            NewElementInst.SetRestriction(ElementInfo['Restriction'])
                        if 'InnserspaceX' in ElementInfo.keys():    
                            NewElementInst.SetInnerSpacingX(int(ElementInfo['InnserspaceX']))
                        if 'InnserspaceY' in ElementInfo.keys():    
                            NewElementInst.SetInnerSpacingY(int(ElementInfo['InnserspaceY']))
                        if 'InnerBorderType' in ElementInfo.keys():    
                            NewElementInst.SetInnerBorderType(ElementInfo['InnerBorderType'])
                        if 'InnerBorderWidth' in ElementInfo.keys():    
                            NewElementInst.SetInnerBorderWidth(int(ElementInfo['InnerBorderWidth']))
                        if 'InnerBorderColor' in ElementInfo.keys():    
                            NewElementInst.SetInnerBorderColor(ElementInfo['InnerBorderColor'])
                        if 'InnerBorderDash' in ElementInfo.keys():    
                            NewElementInst.SetInnerBorderDash(ElementInfo['InnerBorderDash'])
                        if 'LeftIcon' in ElementInfo.keys():    
                            NewElementInst.SetLeftIcon(ElementInfo['LeftIcon'])
                        if 'RightIcon' in ElementInfo.keys():    
                            NewElementInst.SetRightIcon(ElementInfo['RightIcon'])
                        if 'Text' in ElementInfo.keys():    
                            NewElementInst.SetText(ElementInfo['Text'])  
                        if 'TipText' in ElementInfo.keys():    
                            NewElementInst.SetTipText(ElementInfo['TipText'])
                        if 'TipFGColor' in ElementInfo.keys():    
                            NewElementInst.SetTipFGColor(ElementInfo['TipFGColor'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.SetRelief(ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.SetState(ElementInfo['State'])
                        NewElementInst.Redraw()
                    elif ElementType == 'Text':    
                        if 'AutoWrap' in ElementInfo.keys():    
                            NewElementInst = EXUIControl.CustomText(ParentElement,ElementInfo['AutoWrap'])
                        else:    
                            NewElementInst = EXUIControl.CustomText(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        SetElementTagList(NewElementInst,ElementInfo)
                        if 'Text' in ElementInfo.keys():    
                            NewElementInst.SetText(ElementInfo['Text'])
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.SetFGColor(ElementInfo['FGColor'])
                        SetElementFont(NewElementInst,ElementInfo,True)  
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.SetRelief(ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.SetState(ElementInfo['State'])
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                NewElementInst.SetHScrollBar()
                            if ElementInfo['ScrollBarList'][1] == True:
                                NewElementInst.SetVScrollBar()
                    elif ElementType == 'ListBox':    
                        NewElementInst = tkinter.Listbox(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'ExportSelection' in ElementInfo.keys():    
                            NewElementInst.configure(exportselection = ElementInfo['ExportSelection'])
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.configure(fg = ElementInfo['FGColor']) 
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'SelectMode' in ElementInfo.keys():    
                            if ElementInfo['SelectMode'] == 'SINGLE':
                                NewElementInst.configure(selectmode = tkinter.SINGLE)
                            elif ElementInfo['SelectMode'] == 'BROWSE':
                                NewElementInst.configure(selectmode = tkinter.BROWSE)
                            else:
                                NewElementInst.configure(selectmode = tkinter.EXTENDED)
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                        if 'TextList' in ElementInfo.keys():    
                            for Text in ElementInfo['TextList']:    
                                NewElementInst.insert(tkinter.END,Text)
                        #滚动条加载
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.HORIZONTAL)
                            if ElementInfo['ScrollBarList'][1] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.VERTICAL)
                        EnableCtrlCCopyContent(uiName,ElementName)
                    elif ElementType == 'ComboBox':    
                        ComboBoxVariable = AddTKVariable(uiName,ElementName)
                        if 'Style' in ElementInfo.keys():    
                            NewElementInst = tkinter.ttk.Combobox(ParentElement,textvariable=ComboBoxVariable,state='normal',style=ElementInfo['Style'])
                        elif '.TCombobox' in ElementInfo.keys():    
                            NewElementInst = tkinter.ttk.Combobox(ParentElement,textvariable=ComboBoxVariable,state='normal',style='.TCombobox')
                            if StyleName is None:
                                StyleName = '.TCombobox'
                        else:    
                            NewElementInst = tkinter.ttk.Combobox(ParentElement,textvariable=ComboBoxVariable,state='normal',style=ElementAliasName+'.TCombobox')
                            if StyleName is None:
                                StyleName = ElementAliasName+'.TCombobox'
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                        if 'TextList' in ElementInfo.keys():    
                            NewElementInst['values'] = ElementInfo['TextList']   
                            NewElementInst.current(0)  
                        ListBGColor = '#FFFFFF'
                        ListFGColor = '#000000'
                        if 'ListBGColor' in ElementInfo.keys():
                            ListBGColor = ElementInfo['ListBGColor']
                        if 'ListFGColor' in ElementInfo.keys():   
                            ListFGColor = ElementInfo['ListFGColor']
                        if ListBGColor != '#FFFFFF' or ListFGColor != '#000000':
                            SetComboBoxListColor(uiName,ElementName,ListBGColor,ListFGColor)
                    elif ElementType == 'RadioButton':
                        if GroupName:    
                            Group_Variable = G_UIElementVariableArray[uiName][GroupName]
                            NewElementInst = tkinter.Radiobutton(ParentElement,variable=Group_Variable,value=ElementInfo['Value'],text=ElementInfo['Text'],anchor=tkinter.W)
                        else:    
                            NewElementInst = tkinter.Radiobutton(ParentElement,value=ElementInfo['Value'],text=ElementInfo['Text'],anchor=tkinter.W)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        FGColor = '#000000'    
                        if 'FGColor' in ElementInfo.keys():    
                            FGColor = ElementInfo['FGColor']    
                            NewElementInst.configure(fg = FGColor)   
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'Indicatoron' in ElementInfo.keys():    
                            NewElementInst.configure(indicatoron = ElementInfo['Indicatoron'])
                        if 'ActiveBGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activebackground = ElementInfo['ActiveBGColor'])
                        if 'ActiveFGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activeforeground = ElementInfo['ActiveFGColor'])
                        if 'SelectColor' in ElementInfo.keys():    
                            NewElementInst.configure(selectcolor = ElementInfo['SelectColor'])
                        #事件处理延后
                        #SetRadioButtonSelectedColor(uiName,ElementName,ElementInfo['SelectBGColor'],ElementInfo['SelectFGColor'])
                        autoSize = False
                        if 'Compound' in ElementInfo.keys():
                            if ElementInfo['Compound'] == "none" or ElementInfo['Compound'] == "center":    
                                autoSize = True
                        if 'BGImage' in ElementInfo.keys():    
                            SetImage(uiName,ElementName,ElementInfo['BGImage'],autoSize)
                        if 'SelectImage' in ElementInfo.keys():    
                            SetImage(uiName,ElementName,ElementInfo['SelectImage'],True,'RGBA','selected')
                        if 'SelfDrawing' in ElementInfo.keys():    
                            SetRadioButtonPyMeStyle(uiName,ElementName,ElementInfo['Value'],FGColor,ElementInfo['SelectFGColor'],ElementInfo['Visible'])
                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.configure(compound = ElementInfo['Compound']) 
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                    elif ElementType == 'CheckButton':
                        CheckButtonVariable = AddTKVariable(uiName,ElementName)
                        CheckButtonVariable.set(ElementInfo['Value'])
                        NewElementInst = tkinter.Checkbutton(ParentElement,variable=CheckButtonVariable,text=ElementInfo['Text'],anchor=tkinter.W)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        FGColor = '#000000'    
                        if 'FGColor' in ElementInfo.keys():    
                            FGColor = ElementInfo['FGColor']    
                            NewElementInst.configure(fg = FGColor)   
                        SetElementFont(NewElementInst,ElementInfo) 
                        if 'Indicatoron' in ElementInfo.keys():    
                            NewElementInst.configure(indicatoron = ElementInfo['Indicatoron'])
                        if 'ActiveBGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activebackground = ElementInfo['ActiveBGColor'])
                        if 'ActiveFGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activeforeground = ElementInfo['ActiveFGColor'])
                        if 'SelectColor' in ElementInfo.keys():    
                            NewElementInst.configure(selectcolor = ElementInfo['SelectColor'])
                        #事件处理延后
                        #SetCheckButtonSelectedColor(uiName,ElementName,ElementInfo['SelectBGColor'],ElementInfo['SelectFGColor'])
                        autoSize = False
                        if 'Compound' in ElementInfo.keys():
                            if ElementInfo['Compound'] == "none" or ElementInfo['Compound'] == "center":    
                                autoSize = True
                        if 'BGImage' in ElementInfo.keys():    
                            SetImage(uiName,ElementName,ElementInfo['BGImage'],autoSize)
                        if 'SelectImage' in ElementInfo.keys():    
                            SetImage(uiName,ElementName,ElementInfo['SelectImage'],True,'RGBA','selected')
                        if 'SelfDrawing' in ElementInfo.keys():    
                            SetCheckButtonPyMeStyle(uiName,ElementName,ElementInfo['Value'],FGColor,ElementInfo['SelectFGColor'],ElementInfo['Visible'])
                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.configure(compound = ElementInfo['Compound'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State']) 
                    elif ElementType == 'Scale':
                        NewElementInst = tkinter.Scale(ParentElement,orient = ElementInfo['Orient'],from_ = ElementInfo['From'],to = ElementInfo['To'],bigincrement = ElementInfo["BigIncrement"],length = ElementInfo["Length"])
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        FGColor = '#000000'    
                        if 'FGColor' in ElementInfo.keys():
                            FGColor = ElementInfo['FGColor']    
                            NewElementInst.configure(fg = FGColor)   
                        SetElementFont(NewElementInst,ElementInfo) 
                        NewElementInst.configure(showvalue = ElementInfo['ShowValue'])
                        NewElementInst.configure(tickinterval = ElementInfo['Tickinterval'])
                        NewElementInst.configure(resolution = ElementInfo['Resolution'])
                        if 'Value' in ElementInfo.keys():
                            NewElementInst.set(ElementInfo['Value'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                    elif ElementType == 'SpinBox':
                        SpinBoxVariable = AddTKVariable(uiName,ElementName)
                        if 'Value' in ElementInfo.keys():
                            SpinBoxVariable.set(ElementInfo['Value'])
                        NewElementInst = tkinter.Spinbox(ParentElement,textvariable=SpinBoxVariable)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        SetElementFont(NewElementInst,ElementInfo) 
                        NewElementInst.configure(to = ElementInfo['To'])
                        NewElementInst.configure(from_ = ElementInfo['From'])
                        NewElementInst.configure(increment = ElementInfo['Increment'])
                        NewElementInst.configure(wrap = ElementInfo['Wrap'])
                        if 'ValueList' in ElementInfo.keys():    
                            NewElementInst.configure(values = ElementInfo['ValueList'])  
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                    elif ElementType == 'Slider':
                        NewElementInst = EXUIControl.Slider(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        if 'MaxValue' in ElementInfo.keys():    
                            NewElementInst.SetMaxValue(ElementInfo['MaxValue'],False)
                        if 'CurrValue' in ElementInfo.keys():    
                            NewElementInst.SetCurrValue(ElementInfo['CurrValue'],False)
                        if 'BgColor1' in ElementInfo.keys():    
                            NewElementInst.SetBarBGColor1(ElementInfo['BgColor1'])
                        if 'BgColor2' in ElementInfo.keys():    
                            NewElementInst.SetBarBGColor2(ElementInfo['BgColor2'])
                        if 'BtnColor' in ElementInfo.keys():    
                            NewElementInst.SetBarButtonColor(ElementInfo['BtnColor'])
                        if 'BGImage1' in ElementInfo.keys():    
                            NewElementInst.SetBarImage1(ElementInfo['BGImage1'],False)
                        if 'BGImage2' in ElementInfo.keys():    
                            NewElementInst.SetBarImage2(ElementInfo['BGImage2'],False)
                        if 'BtnImage' in ElementInfo.keys():    
                            NewElementInst.SetButtonBGImage(ElementInfo['BtnImage'],False)
                        if 'BtnImage_Hover' in ElementInfo.keys():    
                            NewElementInst.SetButtonBGImage_Hover(ElementInfo['BtnImage_Hover'])
                        if 'BtnImage_Click' in ElementInfo.keys():    
                            NewElementInst.SetButtonBGImage_Click(ElementInfo['BtnImage_Click'])  
                        #皮肤先更新再进行布局，否则会出现换肤闪烁
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        NewElementInst.Redraw()    
                    elif ElementType == 'Progress':
                        NewElementInst = tkinter.ttk.Progressbar(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        NewElementInst.configure(orient = ElementInfo['Orient'])
                        NewElementInst.configure(mode = ElementInfo['Mode'])
                        NewElementInst.configure(maximum = ElementInfo['MaxValue'])
                        NewElementInst.configure(value = ElementInfo['Value'])  
                    elif ElementType == 'ProgressDial':
                        NewElementInst = EXUIControl.ProgressDial(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'],False)   
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.SetTextColor(ElementInfo['FGColor'],False)   
                        if 'BGColor_Center' in ElementInfo.keys():    
                            NewElementInst.SetBGColor_Center(ElementInfo['BGColor_Center'],False)   
                        if 'FillColor' in ElementInfo.keys():    
                            NewElementInst.SetFillColor(ElementInfo['FillColor'],False)
                        if 'FillWidth' in ElementInfo.keys():    
                            NewElementInst.SetFillWidth(ElementInfo['FillWidth'],False)   
                        if 'BeginAngle' in ElementInfo.keys():    
                            NewElementInst.SetBeginAngle(ElementInfo['BeginAngle'],False)   
                        if 'EndAngle' in ElementInfo.keys():    
                            NewElementInst.SetEndAngle(ElementInfo['EndAngle'],False)   
                        if 'MaxValue' in ElementInfo.keys():    
                            NewElementInst.SetMaxValue(ElementInfo['MaxValue'],False)  
                        if 'Value' in ElementInfo.keys():    
                            NewElementInst.SetCurrValue(ElementInfo['Value'],False)   
                        if 'Sections' in ElementInfo.keys():    
                            NewElementInst.SetSections(ElementInfo['Sections'],False)  
                        if 'Percent' in ElementInfo.keys():    
                            NewElementInst.SetPersentage(ElementInfo['Percent'],False)
                        if 'Font' in ElementInfo.keys():    
                            FontInfo = ElementInfo['Font']    
                            newFont = tkinter.font.Font(family=FontInfo[0], size=FontInfo[1],weight=FontInfo[2],slant=FontInfo[3],underline=FontInfo[4],overstrike=FontInfo[5])
                            NewElementInst.SetFont(newFont,False) 
                        NewElementInst.Rebuild() 
                    elif ElementType == 'TreeView':    
                        NewElementInst = tkinter.ttk.Treeview(ParentElement,show="tree")
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'SelectMode' in ElementInfo.keys():    
                            if ElementInfo['SelectMode'] == 'SINGLE':
                                NewElementInst.configure(selectmode = tkinter.SINGLE)
                            elif ElementInfo['SelectMode'] == 'BROWSE':
                                NewElementInst.configure(selectmode = tkinter.BROWSE)
                            else:
                                NewElementInst.configure(selectmode = tkinter.EXTENDED)
                        if 'RowHeight' in ElementInfo.keys():
                            styleName = ElementAliasName+".Treeview"
                            style.configure(styleName, rowheight=str(ElementInfo['RowHeight']))
                            NewElementInst.configure(style = styleName)
                        SetElementTagList(NewElementInst,ElementInfo) 
                        IconDict = LoadElementIconList(ElementName,ElementInfo)
                        if 'TreeItemList' in ElementInfo.keys():    
                            BuildTreeView(NewElementInst,'',ElementInfo['TreeItemList'],IconDict) 
                        if 'TreeExpand' in ElementInfo.keys():    
                            ExpandAllTreeItem(NewElementInst,ElementInfo['TreeExpand']) 
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.HORIZONTAL)
                            if ElementInfo['ScrollBarList'][1] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.VERTICAL)
                    elif ElementType == 'ListView':
                        if StyleName is None:
                            StyleName = ElementAliasName+".Treeview"
                        NewElementInst = tkinter.ttk.Treeview(ParentElement,show="headings")
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'SelectMode' in ElementInfo.keys():    
                            if ElementInfo['SelectMode'] == 'SINGLE':
                                NewElementInst.configure(selectmode = tkinter.SINGLE)
                            elif ElementInfo['SelectMode'] == 'BROWSE':
                                NewElementInst.configure(selectmode = tkinter.BROWSE)
                            else:
                                NewElementInst.configure(selectmode = tkinter.EXTENDED)
                        if 'RowHeight' in ElementInfo.keys():
                            style.configure(StyleName, rowheight=str(ElementInfo['RowHeight']))
                            NewElementInst.configure(style = StyleName)
                        SetElementTagList(NewElementInst,ElementInfo) 
                        BuildListView(NewElementInst,ElementInfo)
                        if 'ScrollBarList' in ElementInfo:    
                            if ElementInfo['ScrollBarList'][0] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.HORIZONTAL)
                            if ElementInfo['ScrollBarList'][1] == True:
                                SetElementScrollbar(uiName,ElementName,tkinter.VERTICAL)
                        ListView_EnableCtrlCCopyContent(uiName,ElementName)
                    elif ElementType == 'NoteBook': 
                        if StyleName is None:
                            StyleName = ElementAliasName+".TNotebook"
                        if 'Closebtn' in ElementInfo.keys():  
                            if ElementInfo['Closebtn'] == True:    
                                NewElementInst = EXUIControl.CustomNoteBook(ParentElement,style=StyleName)
                            else:    
                                NewElementInst = tkinter.ttk.Notebook(ParentElement)
                        else:    
                            NewElementInst = tkinter.ttk.Notebook(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
            
                        if 'BtnPosition' in ElementInfo.keys():    
                            style.configure(StyleName, tabposition=ElementInfo['BtnPosition'])

                        # if 'SelectedBgcolor' in ElementInfo.keys():    
                        #     style.map(StyleName+".Tab", background=[('selected',ElementInfo['SelectedBgcolor'])])

                        # if 'SelectedFgcolor' in ElementInfo.keys():    
                        #     style.map(StyleName+".Tab", foreground=[('selected',ElementInfo['SelectedFgcolor'])])
                        # NewElementInst.configure(style=StyleName)

                        bgColor = '#EFEFEF'
                        fgColor = '#000000'
                        SelectedBGColor = '#EFEFEF'
                        SelectedFGColor = '#000000'
                        BtnPosition = 'nw'
                        #右边背景色
                        if 'BtnPosition' in ElementInfo.keys():
                            BtnPosition = ElementInfo['BtnPosition']
                        #设置背景颜色
                        if 'BGColor' in ElementInfo:
                            bgColor = ElementInfo['BGColor']
                        #设置文字颜色
                        if 'FGColor' in ElementInfo:
                            fgColor = ElementInfo['FGColor']
                        #右边背景色
                        if 'SelectedBGColor' in ElementInfo.keys():
                            SelectedBGColor = ElementInfo['SelectedBGColor']
                        #右边背景色
                        if 'SelectedFGColor' in ElementInfo.keys():
                            SelectedFGColor = ElementInfo['SelectedFGColor']

                        style.configure(StyleName, background=bgColor, fieldbackground=bgColor)
                        style.configure(StyleName, foreground=fgColor)
                        style.configure(StyleName+".Tab", background=bgColor, fieldbackground=bgColor)
                        style.configure(StyleName+".Tab", foreground=fgColor)
                        style.map(StyleName+".Tab", background=[("selected", SelectedBGColor)], foreground=[("selected", SelectedFGColor)])
                        NewElementInst.configure(style = StyleName)
                        NewElementInst.update()
                        BuildNoteBook(uiName,ElementName,ElementInfo)
                    elif ElementType == 'PanedWindow':   
                        NewElementInst = tkinter.PanedWindow(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        
                        NewElementInst.configure(style=StyleName)
                        NewElementInst.configure(orient = ElementInfo['Orient'])
                        NewElementInst.configure(showhandle = ElementInfo['Showhandle'])
                        NewElementInst.configure(sashrelief = ElementInfo['Sashrelief'])
                        NewElementInst.configure(sashwidth = ElementInfo['Sashwidth'])
                        if 'Window1Place' in ElementInfo.keys():
                            PanedWindow_Child1 = tkinter.Canvas(NewElementInst,bg="#FFFFFF")
                            Register(uiName,ElementName+"_Child1",PanedWindow_Child1)
                            XYWH = ElementInfo["Window1Place"]
                            PanedWindow_Child1.place(x = XYWH[0],y = XYWH[1],width = XYWH[2],height = XYWH[3])
                            if ElementInfo['Orient'] == 'horizontal':
                                NewElementInst.add(PanedWindow_Child1,width=XYWH[2])
                            else:
                                NewElementInst.add(PanedWindow_Child1,height=XYWH[3])
                            if 'Window1UI' in ElementInfo.keys():   
                                EmbedUI = LoadUIDialog(uiName,ElementName+'_Child1',ElementInfo['Window1UI'])
          
                        if 'Window2Place' in ElementInfo.keys():
                            PanedWindow_Child2 = tkinter.Canvas(NewElementInst,bg="#FFFFFF")
                            Register(uiName,ElementName+"_Child2",PanedWindow_Child2)
                            XYWH = ElementInfo["Window2Place"]
                            PanedWindow_Child2.place(x = XYWH[0],y = XYWH[1],width = XYWH[2],height = XYWH[3])
                            if ElementInfo['Orient'] == 'horizontal':
                                NewElementInst.add(PanedWindow_Child2,width=XYWH[2])
                            else:
                                NewElementInst.add(PanedWindow_Child2,height=XYWH[3])
                            if 'Window2UI' in ElementInfo.keys():   
                                EmbedUI = LoadUIDialog(uiName,ElementName+'_Child2',ElementInfo['Window2UI'])
                    elif ElementType == 'Calendar':    
                        NewElementInst = EXUIControl.Calendar(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.SetRelief(ElementInfo['Relief'])
                        if 'DatebarBGColor' in ElementInfo.keys():    
                            NewElementInst.SetDatebarBGColor(ElementInfo['DatebarBGColor'])
                        if 'DatebarFGColor' in ElementInfo.keys():    
                            NewElementInst.SetDatebarFGColor(ElementInfo['DatebarFGColor'])
                        if 'SelectedBGColor' in ElementInfo.keys():    
                            NewElementInst.SetSelectedBGColor(ElementInfo['SelectedBGColor'])
                        if 'SelectedFGColor' in ElementInfo.keys():    
                            NewElementInst.SetSelectedFGColor(ElementInfo['SelectedFGColor'])
                        if 'YearRange' in ElementInfo.keys():    
                            NewElementInst.SetRangeOfYears(ElementInfo['YearRange'][0],ElementInfo['YearRange'][1])
                    elif ElementType == 'DatePicker':    
                        NewElementInst = EXUIControl.DatePicker(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.SetFGColor(ElementInfo['FGColor'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.SetRelief(ElementInfo['Relief'])
                        if 'CalendarBGColor' in ElementInfo.keys():    
                            NewElementInst.SetCalendarBGColor(ElementInfo['CalendarBGColor'])
                        if 'SelectedBGColor' in ElementInfo.keys():    
                            NewElementInst.SetSelectedBGColor(ElementInfo['SelectedBGColor'])
                        if 'SelectedFGColor' in ElementInfo.keys():    
                            NewElementInst.SetSelectedFGColor(ElementInfo['SelectedFGColor'])   
                        if 'YearRange' in ElementInfo.keys():    
                            NewElementInst.SetRangeOfYears(ElementInfo['YearRange'][0],ElementInfo['YearRange'][1])
                        if 'SeparatorChar' in ElementInfo.keys():    
                            NewElementInst.SetSeparatorChar(ElementInfo['SeparatorChar'])
                        SetElementFont(NewElementInst,ElementInfo,True)
                    elif ElementType == 'LabelButton':    
                        NewElementInst = EXUIControl.LabelButton(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.SetFGColor(ElementInfo['FGColor']) 
                        if 'Text' in ElementInfo.keys():    
                            NewElementInst.SetText(ElementInfo['Text'])  
                        SetElementFont(NewElementInst,ElementInfo,True)
                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.SetCompound(ElementInfo['Compound'])
                        if 'BGImage' in ElementInfo.keys():
                            NewElementInst.SetBGImage(ElementInfo['BGImage'])
                        if 'BGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetBGColor_Hover(ElementInfo['BGColor_Hover'])
                        if 'FGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetFGColor_Hover(ElementInfo['FGColor_Hover'])
                        if 'BGImage_Hover' in ElementInfo.keys():    
                            NewElementInst.SetBGImage_Hover(ElementInfo['BGImage_Hover'])

                        if 'BGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetBGColor_Click(ElementInfo['BGColor_Click'])
                        if 'FGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetFGColor_Click(ElementInfo['FGColor_Click'])
                        if 'BGImage_Click' in ElementInfo.keys():    
                            NewElementInst.SetBGImage_Click(ElementInfo['BGImage_Click'])
                        if 'Droplist' in ElementInfo.keys():    
                            if ElementInfo['Droplist'] == True:
                                if 'DroplistValues' in ElementInfo.keys():    
                                    NewElementInst.SetDropList(ElementInfo['DroplistValues']) 
                                else:
                                    NewElementInst.SetDropList([]) 
                        if 'Anchor' in ElementInfo.keys():    
                            NewElementInst.SetAnchor(ElementInfo['Anchor']) 
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.SetRelief(ElementInfo['Relief']) 
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.SetState(ElementInfo['State'])

                    elif ElementType == 'SwitchButton':
                        NewElementInst = EXUIControl.SwitchButton(ParentElement)   
                        if 'Shape' in ElementInfo.keys():    
                            NewElementInst.SetShape(ElementInfo['Shape'])
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor_Off' in ElementInfo.keys():    
                            NewElementInst.SetOffStateBGColor(ElementInfo['BGColor_Off']) 
                        if 'Text_Off' in ElementInfo.keys():    
                            NewElementInst.SetOffStateText(ElementInfo['Text_Off'])  
                        if 'FGColor_Off' in ElementInfo.keys():    
                            NewElementInst.SetOffStateTextColor(ElementInfo['FGColor_Off']) 
                        if 'BtnColor_Off' in ElementInfo.keys():    
                            NewElementInst.SetOffStateButtonColor(ElementInfo['BtnColor_Off']) 

                        if 'BGColor_On' in ElementInfo.keys():    
                            NewElementInst.SetOnStateBGColor(ElementInfo['BGColor_On']) 
                        if 'Text_On' in ElementInfo.keys():    
                            NewElementInst.SetOnStateText(ElementInfo['Text_On'])  
                        if 'FGColor_On' in ElementInfo.keys():    
                            NewElementInst.SetOnStateTextColor(ElementInfo['FGColor_On']) 
                        if 'BtnColor_On' in ElementInfo.keys():    
                            NewElementInst.SetOnStateButtonColor(ElementInfo['BtnColor_On']) 
                            
                        SetElementFont(NewElementInst,ElementInfo,True)

                        if 'Value' in ElementInfo.keys():    
                            NewElementInst.SetCurrValue(ElementInfo['Value']) 

                        if 'SwitchMode' in ElementInfo.keys():    
                            NewElementInst.SetSwitchMode(ElementInfo['SwitchMode']) 

                        if 'State' in ElementInfo.keys():    
                            NewElementInst.SetState(ElementInfo['State']) 
                        NewElementInst.Redraw()
                    elif ElementType == 'Navigation':    
                        NewElementInst = EXUIControl.Navigation(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'Orient' in ElementInfo.keys():    
                            NewElementInst.SetDirection(ElementInfo['Orient'],False)

                        if 'Anchor' in ElementInfo.keys():    
                            NewElementInst.SetAnchor(ElementInfo['Anchor'],False) 

                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.SetCompound(ElementInfo['Compound'],False) 

                        if 'BorderWidth' in ElementInfo.keys():    
                            NewElementInst.SetBorderWidth(int(ElementInfo['BorderWidth']),False) 
                        
                        if 'BorderHeight' in ElementInfo.keys():    
                            NewElementInst.SetBorderHeight(int(ElementInfo['BorderHeight']),False) 

                        if 'Spacing' in ElementInfo.keys():    
                            NewElementInst.SetItemSpacing(int(ElementInfo['Spacing']),False) 

                        if 'InnerSpacing' in ElementInfo.keys():    
                            NewElementInst.SetItemInnerSpacing(int(ElementInfo['InnerSpacing']),False)  

                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor']) 

                        if 'ItemBGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor(ElementInfo['ItemBGColor']) 
                        
                        if 'ItemFGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor(ElementInfo['ItemFGColor'],False) 
                        
                        if 'ItemImage' in ElementInfo.keys():    
                            NewElementInst.SetItemImage(ElementInfo['ItemImage']) 

                        if 'ItemBGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Hover(ElementInfo['ItemBGColor_Hover']) 
                        
                        if 'ItemFGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Hover(ElementInfo['ItemFGColor_Hover']) 
                            
                        if 'ItemImage_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemImage_Hover(ElementInfo['ItemImage_Hover']) 

                        if 'ItemBGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Click(ElementInfo['ItemBGColor_Click']) 
                        
                        if 'ItemFGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Click(ElementInfo['ItemFGColor_Click']) 
                            
                        if 'ItemImage_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemImage_Click(ElementInfo['ItemImage_Click']) 

                        SetElementFont(NewElementInst,ElementInfo,True)
                        BuildNavigation(NewElementInst,ElementInfo)
                    elif ElementType == 'SwitchPage':    
                        NewElementInst = EXUIControl.SwitchPage(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)   

                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])

                        if 'BarX' in ElementInfo.keys():    
                            NewElementInst.SetProgressBarLeft(ElementInfo['BarX']) 

                        if 'BarY' in ElementInfo.keys():    
                            NewElementInst.SetProgressBarTop(ElementInfo['BarY']) 

                        if 'PointRadius' in ElementInfo.keys():    
                            NewElementInst.SetProgressBarButtonRadius(ElementInfo['PointRadius']) 
                        
                        if 'CurrPointWidth' in ElementInfo.keys():    
                            NewElementInst.SetProgressBarCurrButtonWidth(ElementInfo['CurrPointWidth']) 

                        if 'PointSpacingX' in ElementInfo.keys():    
                            NewElementInst.SetProgressBarButtonSpacingX(ElementInfo['PointSpacingX']) 

                        BuildSwitchPage(NewElementInst,ElementInfo)
                    elif ElementType == 'ShowCase':    
                        NewElementInst = EXUIControl.ShowCase(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)   

                        if 'ItemWidth' in ElementInfo.keys():    
                            NewElementInst.SetItemWidth(int(ElementInfo['ItemWidth']))
                        if 'ItemHeight' in ElementInfo.keys():    
                            NewElementInst.SetItemHeight(int(ElementInfo['ItemHeight']))
                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.SetCompound(ElementInfo['Compound'])
                        if 'ItemSpacing' in ElementInfo.keys():    
                            NewElementInst.SetItemSpacing(int(ElementInfo['ItemSpacing']))
                        if 'InnerSpacing' in ElementInfo.keys():    
                            NewElementInst.SetItemInnerSpacing(int(ElementInfo['InnerSpacing']))

                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])

                        if 'ItemBGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor(ElementInfo['ItemBGColor']) 

                        if 'ItemFGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor(ElementInfo['ItemFGColor']) 
                        
                        # if 'ItemImage' in ElementInfo.keys():    
                        #     NewElementInst.SetItemImage(ElementInfo['ItemImage']) 

                        if 'ItemBGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Hover(ElementInfo['ItemBGColor_Hover']) 
                        
                        if 'ItemFGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Hover(ElementInfo['ItemFGColor_Hover']) 
                            
                        # if 'ItemImage_Hover' in ElementInfo.keys():    
                        #     NewElementInst.SetItemImage_Hover(ElementInfo['ItemImage_Hover']) 

                        if 'ItemBGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Click(ElementInfo['ItemBGColor_Click']) 
                        
                        if 'ItemFGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Click(ElementInfo['ItemFGColor_Click']) 
                            
                        # if 'ItemImage_Click' in ElementInfo.keys():    
                        #     NewElementInst.SetItemImage_Click(ElementInfo['ItemImage_Click']) 

                        SetElementFont(NewElementInst,ElementInfo,True)
                        BuildShowCase(NewElementInst,ElementInfo)
                    elif ElementType == 'ListMenu':    
                        NewElementInst = EXUIControl.ListMenu(ParentElement)   
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)   

                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.SetBGColor(ElementInfo['BGColor'])
                        if 'TitleAnchor' in ElementInfo.keys():    
                            NewElementInst.SetTitleAnchor(ElementInfo['TitleAnchor'],False)
                        if 'TitleCompound' in ElementInfo.keys():    
                            NewElementInst.SetTitleCompound(ElementInfo['TitleCompound'],False)
                        if 'TitleSpacingX' in ElementInfo.keys():    
                            NewElementInst.SetTitleSpacingX(int(ElementInfo['TitleSpacingX']),False)
                        if 'TitleSpacingY' in ElementInfo.keys():    
                            NewElementInst.SetTitleSpacingY(int(ElementInfo['TitleSpacingY']),False)
                        if 'TitleBGColor' in ElementInfo.keys():    
                            NewElementInst.SetTitleBGColor(ElementInfo['TitleBGColor']) 
                        if 'TitleFGColor' in ElementInfo.keys():    
                            NewElementInst.SetTitleFGColor(ElementInfo['TitleFGColor'],False) 
                        if 'TitleBGImage' in ElementInfo.keys():    
                            NewElementInst.SetTitleImage(ElementInfo['TitleBGImage'],False) 

                        if 'TitleBGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetTitleBGColor_Hover(ElementInfo['TitleBGColor_Hover']) 
                        if 'TitleFGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetTitleFGColor_Hover(ElementInfo['TitleFGColor_Hover']) 
                        # if 'ItemImage_Hover' in ElementInfo.keys():    
                        #     ListMenuInst.SetItemImage_Hover(ElementInfo['ItemImage_Hover']) 

                        if 'TitleBGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetTitleBGColor_Click(ElementInfo['TitleBGColor_Click']) 
                        if 'TitleFGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetTitleFGColor_Click(ElementInfo['TitleFGColor_Click']) 
                        # if 'ItemImage_Click' in ElementInfo.keys():    
                        #     ListMenuInst.SetItemImage_Click(ElementInfo['ItemImage_Click']) 
                            
                        if 'ItemAnchor' in ElementInfo.keys():    
                            NewElementInst.SetItemAnchor(ElementInfo['ItemAnchor'],False)
                        if 'ItemCompound' in ElementInfo.keys():    
                            NewElementInst.SetItemCompound(ElementInfo['ItemCompound'],False)
                        if 'ItemSpacingX' in ElementInfo.keys():    
                            NewElementInst.SetItemSpacingX(int(ElementInfo['ItemSpacingX']),False)
                        if 'ItemSpacingY' in ElementInfo.keys():    
                            NewElementInst.SetItemSpacingY(int(ElementInfo['ItemSpacingY']),False)
                        if 'ItemBGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor(ElementInfo['ItemBGColor']) 
                        if 'ItemFGColor' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor(ElementInfo['ItemFGColor'],False) 
                        if 'ItemBGImage' in ElementInfo.keys():    
                            NewElementInst.SetItemImage(ElementInfo['ItemBGImage'],False) 

                        if 'ItemBGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Hover(ElementInfo['ItemBGColor_Hover']) 
                        if 'ItemFGColor_Hover' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Hover(ElementInfo['ItemFGColor_Hover']) 
                        # if 'ItemImage_Hover' in ElementInfo.keys():    
                        #     NewElementInst.SetItemImage_Hover(ElementInfo['ItemImage_Hover']) 

                        if 'ItemBGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemBGColor_Click(ElementInfo['ItemBGColor_Click']) 
                        if 'ItemFGColor_Click' in ElementInfo.keys():    
                            NewElementInst.SetItemFGColor_Click(ElementInfo['ItemFGColor_Click']) 
                        # if 'ItemImage_Click' in ElementInfo.keys():    
                        #     NewElementInst.SetItemImage_Click(ElementInfo['ItemImage_Click']) 

                        SetElementFont(NewElementInst,ElementInfo,True)
                        BuildListMenu(NewElementInst,ElementInfo)

                    elif ElementType == 'Button':    
                        NewElementInst = tkinter.Button(ParentElement,text=ElementInfo['Text'])
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            NewElementInst.configure(bg = ElementInfo['BGColor'])
                        if 'FGColor' in ElementInfo.keys():    
                            NewElementInst.configure(fg = ElementInfo['FGColor'])
                        if 'Anchor' in ElementInfo.keys():    
                            NewElementInst.configure(anchor = ElementInfo['Anchor']) 
                        SetElementFont(NewElementInst,ElementInfo)
                        autoSize = False
                        if 'Compound' in ElementInfo.keys():
                            if ElementInfo['Compound'] == "none" or ElementInfo['Compound'] == "center":    
                                autoSize = True
                        if 'BGImage' in ElementInfo.keys():    
                            SetImage(uiName,ElementName,ElementInfo['BGImage'],autoSize)

                        if 'Compound' in ElementInfo.keys():    
                            NewElementInst.configure(compound = ElementInfo['Compound'])  

                        if 'ActiveBGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activebackground = ElementInfo['ActiveBGColor'])
                        if 'ActiveFGColor' in ElementInfo.keys():    
                            NewElementInst.configure(activeforeground = ElementInfo['ActiveFGColor'])
                        if 'Relief' in ElementInfo.keys():    
                            NewElementInst.configure(relief = ElementInfo['Relief'])
                        if 'State' in ElementInfo.keys():    
                            NewElementInst.configure(state = ElementInfo['State'])
                    elif ElementType == 'PyMeGLFrame':    
                        NewElementInst = EXUIControl.PyMeGLFrame(ParentElement)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo)
                        if 'BGColor' in ElementInfo.keys():    
                            BgColor = ElementInfo['BGColor']
                            # 16进制颜色格式颜色转换为RGB格式
                            r = int(BgColor[1:3],16)
                            g = int(BgColor[3:5],16)
                            b = int(BgColor[5:7],16)
                            NewElementInst.SetBGColor(r/255,g/255,b/255)
                    elif ElementType == 'Scatter' or ElementType == 'Line' or ElementType == 'Curve' or ElementType == 'Histogram' or ElementType == 'Bar' or ElementType == 'Box' or ElementType == 'Pie' or ElementType == 'Spider' or ElementType == 'XYZ3d' or ElementType == 'XYZSurface3d':   
                        NewElementInst = BuildChart(ElementType,uiName,ParentElement,ElementName)
                        Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                        SetElementLayout(uiName,ElementName,ElementInfo) 
                    elif ElementType == 'FileReader':
                        IsPyMeModule = True
                        if SupportModule == True:
                            DataType = GetElementValue(ElementInfo,'datatype')
                            filename = GetElementValue(ElementInfo,'filename')
                            fileorurl = GetElementValue(ElementInfo,'fileorurl')
                            encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            TargetElementName = GetElementValue(ElementInfo,'elementName')
                            if DataType == 'TXT':
                                NewElementInst = FileReader_ReadTXTFile(filename=filename,encoding=encoding,uiName = uiName,elementName = TargetElementName)
                            elif DataType == 'CSV':
                                NewElementInst = FileReader_ReadCSVFile(filename=filename,encoding=encoding,uiName = uiName,elementName = TargetElementName)
                            elif DataType == 'XML':
                                NewElementInst = FileReader_ReadXMLFile(filename=filename,encoding=encoding,uiName = uiName,elementName = TargetElementName)
                            elif DataType == 'JSON':
                                NewElementInst = FileReader_ReadJSONFile(filename=filename,encoding=encoding,uiName = uiName,elementName = TargetElementName)
                            elif DataType == 'WEB':
                                NewElementInst = FileReader_ReadWEBFile(fileorurl=fileorurl,encoding=encoding,uiName = uiName,elementName = TargetElementName)
                            else:
                                NewElementInst = FileReader()
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                    elif ElementType == 'Socket':
                        IsPyMeModule = True
                        if SupportModule == True:
                            socket_ip = GetElementValue(ElementInfo,'ip','127.0.0.1')
                            socket_port = GetElementValue(ElementInfo,'port','8888')
                            socket_protocol = GetElementValue(ElementInfo,'protocol','tcp')
                            socket_listen = GetElementValue(ElementInfo,'listen','10')
                            socket_buffsize = GetElementValue(ElementInfo,'buffsize','1024')
                            socket_encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            socket_netMsgTable = GetElementValue(ElementInfo,'netMsgTable')
                            socket_listbox = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = Socket(protocol=socket_protocol,ip=socket_ip,port=socket_port,listen=socket_listen,encoding=socket_encoding,buffsize=socket_buffsize,netMsgTable=socket_netMsgTable)
                            #名称有问题
                            NewElementInst.SetListBox(socket_listbox)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                        #事件处理暂时未处理
                    elif ElementType == 'MQTT':
                        IsPyMeModule = True
                        if SupportModule == True:
                            mqtt_broker = GetElementValue(ElementInfo,'broker','broker.emqx.io')
                            mqtt_port = GetElementValue(ElementInfo,'port','1883')
                            mqtt_keeplive = GetElementValue(ElementInfo,'keeplive','60')
                            mqtt_encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            mqtt_username = GetElementValue(ElementInfo,'username')
                            mqtt_password = GetElementValue(ElementInfo,'password')
                            mqtt_block = GetElementValue(ElementInfo,'block',False)
                            mqtt_listbox = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = MQTT(broker=mqtt_broker,port=mqtt_port,username=mqtt_username,password=mqtt_password,keeplive=mqtt_keeplive,block=mqtt_block,encoding=mqtt_encoding)
                            #名称有问题
                            NewElementInst.SetListBox(mqtt_listbox)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'SSH':
                        IsPyMeModule = True
                        if SupportModule == True:
                            ssh_hostname = GetElementValue(ElementInfo,'hostname','127.0.0.1')
                            ssh_username = GetElementValue(ElementInfo,'username')
                            ssh_password = GetElementValue(ElementInfo,'password')
                            ssh_encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            ssh_listbox = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = MQTT(hostname=ssh_hostname,username=ssh_username,password=ssh_password,encoding=ssh_encoding)
                            #名称有问题
                            NewElementInst.SetListBox(ssh_listbox)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'Serial':
                        IsPyMeModule = True
                        if SupportModule == True:
                            serial_port = GetElementValue(ElementInfo,'serialport','')
                            serial_baudrate = GetElementValue(ElementInfo,'baudrate','9600')
                            serial_databit = GetElementValue(ElementInfo,'databit','8')
                            serial_parity = GetElementValue(ElementInfo,'parity','None')
                            serial_stopbit = GetElementValue(ElementInfo,'stopbit','ONE')
                            serial_readbufsize = GetElementValue(ElementInfo,'readbufsize','4096')
                            serial_sendbufsize = GetElementValue(ElementInfo,'sendbufsize','4096')
                            serial_encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            serial_listbox = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = Serial(serialport=serial_port,baudrate=serial_baudrate,databit=serial_databit,parity=serial_parity,stopbit=serial_stopbit,readbufsize=serial_readbufsize,sendbufsize=serial_sendbufsize,encoding=serial_encoding)
                            #名称有问题
                            NewElementInst.SetListBox(serial_listbox)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'USB':
                        IsPyMeModule = True
                        if SupportModule == True:
                            usb_readbufsize = GetElementValue(ElementInfo,'readbufsize','4096')
                            usb_sendbufsize = GetElementValue(ElementInfo,'sendbufsize','4096')
                            usb_encoding = GetElementValue(ElementInfo,'encoding','utf-8')
                            usb_listbox = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = USB(readbufsize=usb_readbufsize,sendbufsize=usb_sendbufsize,encoding=usb_encoding)
                            #名称有问题
                            NewElementInst.SetListBox(usb_listbox)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'Bluetooth':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = Bluetooth()
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'SMTP':
                        IsPyMeModule = True
                        if SupportModule == True:
                            usb_server = GetElementValue(ElementInfo,'server','')
                            usb_port = GetElementValue(ElementInfo,'port','')
                            usb_email = GetElementValue(ElementInfo,'email','')
                            usb_password = GetElementValue(ElementInfo,'password','')
                            NewElementInst = SMTP(server=usb_server,port=usb_port,email=usb_email,password=usb_password)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'DHT':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = DHT()
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'WMI':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = WMI()
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'AudioPlayer':
                        IsPyMeModule = True
                        if SupportModule == True:
                            filename = GetElementValue(ElementInfo,'filename')
                            NewElementInst = AudioPlayer(filename = filename)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'VideoPlayer':
                        IsPyMeModule = True
                        if SupportModule == True:
                            canvasname = GetElementValue(ElementInfo,'elementName')
                            filename = GetElementValue(ElementInfo,'filename')
                            vlcpath = GetElementValue(ElementInfo,'vlcpath','')
                            NewElementInst = VideoPlayer(uiName=uiName,elementName=canvasname,filename = filename,vlcpath=vlcpath)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'VideoCapture':
                        IsPyMeModule = True
                        if SupportModule == True:
                            canvasname = GetElementValue(ElementInfo,'elementName')
                            NewElementInst = VideoCapture(uiName=uiName,elementName=canvasname)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'DataTable':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = DataTable()
                            if 'datatype' in ElementInfo.keys():
                                DataType = ElementInfo['datatype']
                                TargetElementName = None
                                if 'elementName' in ElementInfo.keys():
                                    TargetElementName = ElementInfo['elementName']
                                if NewElementInst.BindingListView(uiName,TargetElementName) == True:
                                    if DataType == 'EXCEL':
                                        NewElementInst.OpenExcel(ElementInfo['filename'],ElementInfo['sheetname'])
                                    elif DataType == 'SQLITE':
                                        NewElementInst.OpenSQLITE(ElementInfo['filename'],ElementInfo['sheetname'])
                                    elif DataType == 'MYSQL':
                                        NewElementInst.OpenMYSQL(ElementInfo['ip'],ElementInfo['port'],ElementInfo['user'],ElementInfo['password'],ElementInfo['database'],ElementInfo['sheetname'])
                                    elif DataType == 'SQLSERVER':
                                        NewElementInst.OpenSQLSERVER(ElementInfo['ip'],ElementInfo['port'],ElementInfo['user'],ElementInfo['password'],ElementInfo['database'],ElementInfo['sheetname'])
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                    elif ElementType == 'DataBase':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = DataBase()
                            if 'datatype' in ElementInfo.keys():
                                DataType = ElementInfo['datatype']
                                TargetElementName = None
                                if 'elementName' in ElementInfo.keys():
                                    TargetElementName = ElementInfo['elementName']
                                if DataType == 'SQLITE':
                                    NewElementInst.OpenSQLITE(ElementInfo['filename'])
                                elif DataType == 'MYSQL':
                                    NewElementInst.OpenMYSQL(ElementInfo['ip'],ElementInfo['port'],ElementInfo['user'],ElementInfo['password'],ElementInfo['database'])
                                elif DataType == 'SQLSERVER':
                                    NewElementInst.OpenSQLSERVER(ElementInfo['ip'],ElementInfo['port'],ElementInfo['user'],ElementInfo['password'],ElementInfo['database'])
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                    elif ElementType == 'Printer':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = Printer()
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'Selenium':
                        IsPyMeModule = True
                        if SupportModule == True:
                            drivertype = GetElementValue(ElementInfo,'drivertype','')
                            url = GetElementValue(ElementInfo,'url','')
                            headless = GetElementValue(ElementInfo,'headless',False)
                            profile_dir = GetElementValue(ElementInfo,'profile_dir','')
                            proxy_path = GetElementValue(ElementInfo,'proxy_path','')
                            server_path = GetElementValue(ElementInfo,'server_path','')
                            NewElementInst = Selenium(drivertype=drivertype,url=url,headless=headless,profile_dir=profile_dir,proxy_path=proxy_path,server_path=server_path)
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName) 
                    elif ElementType == 'Timer':
                        IsPyMeModule = True
                        if SupportModule == True:
                            NewElementInst = Timer()
                            if 'interval' in ElementInfo.keys():
                                Interval = ElementInfo['interval']
                                NewElementInst.SetInterval(Interval)
                            TargetElementName = None
                            if 'elementName' in ElementInfo.keys():
                                TargetElementName = ElementInfo['elementName']
                                if TargetElementName:
                                    TargetElement = GetElement(uiName,TargetElementName)
                                    NewElementInst.SetWidget(TargetElement) 
                            Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                    else:
                        IsPyMeModule = True
                        if SupportModule == True:
                            if 'CommonModule' in ElementInfo.keys():
                                ModuleName = ElementInfo['CommonModule'][0]
                                ModuleXY = ElementInfo['CommonModule'][1]
                                import importlib    
                                from   importlib import import_module    
                                importModule = importlib.import_module(ModuleName)
                                importModule = importlib.reload(importModule)  
                                classfunc = getattr(importModule,ModuleName)
                                NewElementInst = classfunc()
                                Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                                SetElementLayout(uiName,ElementName,ElementInfo) 
                                if 'ModuleAttrib' in ElementInfo.keys():
                                    for Attribute in ElementInfo['ModuleAttrib'].keys():
                                        AttributeValue = ElementInfo['ModuleAttrib'][Attribute]
                                        if type(AttributeValue) == type(''):
                                            AttributeValue = GetElement(uiName,AttributeValue)
                                        SetFunctionName = 'set_' + Attribute
                                        HasSetFunction = hasattr(NewElementInst,SetFunctionName)
                                        if HasSetFunction:
                                            SetAttribFunction = getattr(NewElementInst,SetFunctionName)
                                            SetAttribFunction(AttributeValue)
                                        else:
                                            setattr(NewElementInst,Attribute,AttributeValue)

                            elif 'UIModule' in ElementInfo.keys():
                                NewElementInst = tkinter.ttk.Frame(ParentElement)
                                Register(uiName,ElementName,NewElementInst,ElementAliasName,GroupName,StyleName)
                                SetElementLayout(uiName,ElementName,ElementInfo)
                                NewElementInst.configure(relief = 'flat')
                                ModuleName = "Module"+ElementInfo['UIModule'][0]
                                ModuleXY = ElementInfo['UIModule'][1]
                                import importlib    
                                from   importlib import import_module    
                                importModule = importlib.import_module(ModuleName)
                                importModule = importlib.reload(importModule)  
                                classfunc = getattr(importModule,ModuleName)
                                if classfunc:
                                    NewElementInst = classfunc(NewElementInst)
                    if SupportModule == False and IsPyMeModule == True:
                        NewElementInst = tkinter.Label(ParentElement,text=ElementAliasName)
                        NewElementInst.configure(bg='#333333')
                        NewElementInst.configure(fg='#FFFFFF')
                        Register(uiName,ElementName,NewElementInst,ElementAliasName)
                        ElementInfo['PlaceInfo'] = [ElementInfo['XY'][0],ElementInfo['XY'][1],50,20,'nw',True]
                        ElementInfo['Visible'] = True
                        SetElementLayout(uiName,ElementName,ElementInfo)      
                    #提示文字
                    if ElementType != 'Entry':    
                        if 'TipText' in ElementInfo.keys():    
                            CreateToolTip(uiName,ElementName,ElementInfo['TipText'])
                    #圆角处理
                    if 'RoundCorner' in ElementInfo.keys():    
                        SetRoundedRectangle(uiName,ElementName,ElementInfo['RoundCorner'],ElementInfo['RoundCorner']) 
                        ShowRoundedRectangle(NewElementInst,ElementInfo['RoundCorner'],ElementInfo['RoundCorner']) 
                    #图层顺序
                    if 'Layer' in ElementInfo.keys():
                        SetElementLayer(uiName,ElementName,direction=ElementInfo["Layer"])
                    #加载变量    
                    if 'DataList' in ElementInfo.keys():
                        for DataInfo in ElementInfo['DataList']:
                            AddUserData(uiName,ElementAliasName,DataInfo[0],DataInfo[1],DataInfo[2],DataInfo[3])
                    #是否是全局变量
                    if IsPyMeModule == True:
                        G_UIGlobalElementDictionary[uiName][ElementAliasName] = NewElementInst
                    ElementDict[ElementName] = NewElementInst 

            #最后再遍历所有的控件事件进行处理,主要是个别函数如LoadData这时可能引发某些逻辑找不到控件的情况，所以放在最后处理
            if 'WidgetList' in UIInfoDict.keys():
                ElementList = UIInfoDict['WidgetList']
                for ElementInfo in ElementList:
                    ElementType = ElementInfo['Type']
                    ElementIndex = ElementInfo['Index']
                    ElementName = 'PyMe_'+ElementType + '_'+str(ElementIndex)
                    NewElementInst = ElementDict[ElementName]

                    #把颜色设置中事件处理延后到这里,否则不响应
                    if ElementType == 'RadioButton':
                        if 'SelectBGColor' in ElementInfo.keys() and 'SelectFGColor' in ElementInfo.keys():
                            SetRadioButtonSelectedColor(uiName,ElementName,ElementInfo['SelectBGColor'],ElementInfo['SelectFGColor'])
                        if 'GroupID' in ElementInfo.keys():
                            currvalue = GetCurrentValue(uiName,ElementName)
                            GroupID = ElementInfo['GroupID'] 
                            OnRadioButtonClick1(uiName,ElementName,GroupID,currvalue,True)
                            OnRadioButtonClick2(uiName,ElementName,GroupID,currvalue)
                    elif ElementType == 'CheckButton':
                        if 'SelectBGColor' in ElementInfo.keys() and 'SelectFGColor' in ElementInfo.keys():
                            SetCheckButtonSelectedColor(uiName,ElementName,ElementInfo['SelectBGColor'],ElementInfo['SelectFGColor'])
                    elif ElementType == 'LabelFrame' or ElementType == 'Frame': 
                        if 'EmbedUI' not in ElementInfo.keys():
                            if 'ScrollRegion' in ElementInfo:  
                                if ElementInfo['ScrollRegion'] is None:
                                    HScrollWidth = 0
                                    if 'ScrollBarList' in ElementInfo and ElementInfo['ScrollBarList'][0] == True:
                                        HScrollWidth = 20
                                    VScrollHeight = 0
                                    if 'ScrollBarList' in ElementInfo and ElementInfo['ScrollBarList'][1] == True:
                                        VScrollHeight = 20
                                    FrameCanvas = GetElement(uiName,ElementName+"_Child")
                                    if FrameCanvas:    
                                        uiDialogWidth = 0
                                        uiDialogHeight = 0
                                        widgetNameTagList = FrameCanvas.find_all()
                                        for widgetTag in widgetNameTagList:
                                            x1,y1,x2,y2 = FrameCanvas.bbox(widgetTag)
                                            if (x2 > uiDialogWidth):
                                                uiDialogWidth = x2
                                            if (y2> uiDialogHeight):
                                                uiDialogHeight = y2
                                        FrameCanvas.config(scrollregion=(0,0,uiDialogWidth+HScrollWidth,uiDialogHeight+VScrollHeight))
                    #加载函数    
                    if 'EventList' in ElementInfo.keys():    
                        for eventName in ElementInfo['EventList']:    
                            funcName = ElementInfo['EventList'][eventName]    
                            if hasattr(UICmd,funcName) == True:    
                                eventFunc = getattr(UICmd, funcName)
                                if ElementType == 'Form':
                                    if 'Load' == eventName or 'InitCheck' == eventName or 'Display' == eventName or 'Exit' == eventName or 'Configure' == eventName:    
                                        continue    
                                    if eventName in G_TKKey:    
                                        root.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName="Form_1"))
                                    else:    
                                        Form_1.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName="Form_1"))
                                    continue
                                if 'ListboxSelect' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventTwoFunction_Adaptor(OnListBoxSelect,eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'ComboboxSelected' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'TreeviewSelect' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'TreeviewOpen' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'TreeviewClose' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'NotebookTabChanged' == eventName:
                                    NewElementInst.bind('<<'+eventName+'>>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'FocusOut' == eventName:
                                    if ElementType == 'ListBox' :
                                        EventTwoFunction_Adaptor(OnListBoxFocusOut,eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    else:
                                        NewElementInst.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))  
                                elif 'Motion' == eventName:
                                    if ElementType == 'ListView' :
                                        EventTwoFunction_Adaptor(OnListViewRowMouseMotion,eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    else:
                                        NewElementInst.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
                                elif 'SelectDate' == eventName:
                                    NewElementInst.SetBtnCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'Switch' == eventName:
                                    NewElementInst.SetSwitchCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'ItemSelect' == eventName:
                                    if ElementType == 'LabelButton':
                                        NewElementInst.SetDropListCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    elif ElementType == 'Navigation':
                                        NewElementInst.SetNavigationCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    elif ElementType == 'ShowCase':
                                        NewElementInst.SetClickItemCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    elif ElementType == 'ListMenu':
                                        NewElementInst.SetListMenuCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    else:
                                        NewElementInst.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))  
                                elif 'PageClick' == eventName:
                                    NewElementInst.SetPageClickCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'CellClicked' == eventName:
                                    NewElementInst.bind("<Button-1>",EventFunction_Adaptor(OnListViewCellClicked,uiName=uiName,widgetName=ElementInfo['AliasName'],callbackFunc=eventFunc),add=True)   
                                elif 'CellDoubleClicked' == eventName:
                                    NewElementInst.bind("<Double-1>",EventFunction_Adaptor(OnListViewCellDoubleClicked,uiName=uiName,widgetName=ElementInfo['AliasName'],callbackFunc=eventFunc),add=True)   
                                elif 'HeadingClicked' == eventName:
                                    G_ListViewCommandDictionary[uiName][ElementName] = eventFunc
                                    if 'ColumnList' in ElementInfo.keys():
                                        ColumnList = ElementInfo['ColumnList']
                                        for ColumnInfo in ColumnList:   
                                            ColumnName = ColumnInfo[0]
                                            AlignType = ColumnInfo[1]
                                            ColumnWidth = ColumnInfo[2]
                                            ColumnStretch = ColumnInfo[3]
                                            NewElementInst.heading(ColumnName,command=partial(ListViewHeadingFunction_Adaptor,fun=eventFunc,uiName=uiName,widgetName=ElementName,columnname=ColumnName))
                                elif 'Timer' == eventName:
                                    NewElementInst.SetTimerCallBackFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'LoadData' == eventName:
                                    argspec = inspect.getfullargspec(eventFunc)
                                    chartFigure = GetUserData(uiName,ElementInfo['AliasName'],'ChartFigure')
                                    if 'subplot' in argspec.args:
                                        subplot = GetUserData(uiName,ElementInfo['AliasName'],'subplot111')
                                        if subplot:
                                            eventFunc(uiName,ElementInfo['AliasName'],chartFigure,subplot)
                                            if 'Title' in ElementInfo.keys():
                                                if ElementInfo['Title']:
                                                    subplot.set_title(ElementInfo['Title'])
                                            if 'XLabel' in ElementInfo.keys():
                                                if ElementInfo['XLabel']:
                                                    subplot.set_xlabel(ElementInfo['XLabel'])
                                            if 'YLabel' in ElementInfo.keys():
                                                if ElementInfo['YLabel']:
                                                    subplot.set_ylabel(ElementInfo['YLabel'])
                                            if 'ZLabel' in ElementInfo.keys():
                                                if ElementInfo['ZLabel']:
                                                    subplot.set_zlabel(ElementInfo['ZLabel'])
                                    else:
                                        eventFunc(uiName,ElementInfo['AliasName'],chartFigure)
                                    UpdateChart(uiName,ElementInfo['AliasName'])
                                elif 'ClickXY' == eventName:
                                    SetClickXYFunction(uiName = uiName,elementName = ElementInfo['AliasName'],callBackFunction = eventFunc)
                                elif 'Drop' == eventName:
                                    SetControlAcceptDrop(uiName = uiName,elementName = ElementInfo['AliasName'],functionCallback = eventFunc)
                                elif 'LeftIconClicked' == eventName:
                                    NewElementInst.SetLeftIconClickFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'RightIconClicked' == eventName:
                                    NewElementInst.SetRightIconClickFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'TextChanged' == eventName:
                                    NewElementInst.SetTextChangedFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'ValueChanged' == eventName:
                                    NewElementInst.SetValueChangedFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                elif 'Command' == eventName:    
                                    if ElementType == 'Scale':
                                        NewElementInst.configure(command=SetValueChangedFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName']))  
                                    elif ElementType == 'SpinBox' or ElementType == 'Button':
                                        NewElementInst.configure(command=partial(CommandFunction_Adaptor,fun=eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName']))
                                    elif ElementType == 'LabelButton':
                                        NewElementInst.SetCommandFunction(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName'])
                                    else:
                                        NewElementInst.configure(command=partial(eventFunc,uiName = uiName,widgetName = ElementInfo['AliasName']))  
                                else:
                                    NewElementInst.bind('<'+eventName+'>',EventFunction_Adaptor(eventFunc,uiName=uiName,widgetName=ElementInfo['AliasName']))   
        
            #快键转换
            def ConvAccEventKey(text,BorS):
                text = text.replace('Ctrl+','Control-')
                if BorS == 'B':
                    lastKey = text[-1].upper()
                    text = text[0:-1] + lastKey
                else:
                    lastKey = text[-1].lower()
                    text = text[0:-1] + lastKey
                return text
            #构建MainMenu
            def BuildMainMenu(ParentMenu,MenuInfoList,MenuIconDict):
                for MenuInfo in MenuInfoList:
                    MenuType = MenuInfo[0]
                    if MenuType == 'cascade':
                        title = MenuInfo[1]
                        imageFile = MenuInfo[2]
                        AccKey = MenuInfo[3]
                        FontName = MenuInfo[4]
                        FontSize = MenuInfo[5]
                        MenuFont = None
                        if FontName and FontSize:
                            MenuFont = (FontName,FontSize)
                        SubMenu = tkinter.Menu(ParentMenu,tearoff = 0)
                        BuildMainMenu(SubMenu,MenuInfo[6],MenuIconDict)
                        if imageFile and MenuFont :
                            IconName ='MainMenu_' + shotname
                            ParentMenu.add_cascade(label=title,font=MenuFont,image=MenuIconDict[IconName],compound='left',menu=SubMenu)
                        elif imageFile :
                            IconName ='MainMenu_' + shotname
                            ParentMenu.add_cascade(label=title,image=MenuIconDict[IconName],compound='left',menu=SubMenu)
                        elif MenuFont :
                            ParentMenu.add_cascade(label=title,font=MenuFont,menu=SubMenu)
                        else:
                            ParentMenu.add_cascade(label=title,menu=SubMenu)
                    elif MenuType == 'separator':
                        ParentMenu.add_separator()
                    elif MenuType == 'checkbutton':
                        title = MenuInfo[1]
                        imageFile = MenuInfo[2]
                        AccKey = MenuInfo[3]
                        FontName = MenuInfo[4]
                        FontSize = MenuInfo[5]
                        MenuFont = None
                        if FontName and FontSize:
                            MenuFont = (FontName,FontSize)
                        eventFunc = None
                        funcName = 'Menu_'+title
                        CheckButton_Var = AddTKVariable(uiName,'MainMenu_checkbutton_'+title,False)
                        if hasattr(UICmd,funcName) == True:    
                            eventFunc = getattr(UICmd, funcName)
                        def onCheckButton(eventFunc,uiName,itemName,CheckButton_Var):
                            eventFunc(uiName=uiName,itemName=itemName,statusVar=CheckButton_Var.get())
                        if eventFunc:
                            if imageFile and MenuFont and AccKey:
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_checkbutton(label=title,font=MenuFont,image=MenuIconDict[IconName],compound='left',accelerator=AccKey,variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            elif imageFile and MenuFont :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_checkbutton(label=title,font=MenuFont,image=MenuIconDict[IconName],compound='left',variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            elif MenuFont and AccKey :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_checkbutton(label=title,font=MenuFont,accelerator=AccKey,variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            elif imageFile and AccKey :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_checkbutton(label=title,image=MenuIconDict[IconName],compound='left',accelerator=AccKey,variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            elif imageFile :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_checkbutton(label=title,image=MenuIconDict[IconName],compound='left',variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            elif MenuFont :
                                ParentMenu.add_checkbutton(label=title,font=MenuFont,variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc = eventFunc,uiName=uiName,itemName=title,CheckButton_Var=CheckButton_Var))
                            else:
                                ParentMenu.add_checkbutton(label=title,variable=CheckButton_Var,command=lambda:onCheckButton(eventFunc = eventFunc,uiName=uiName,itemName=title,CheckButton_Var = CheckButton_Var))
                            if AccKey !='':
                                root.bind("<"+ConvAccEventKey(AccKey,'B')+">",MenuFunction_Adaptor(onCheckButton,uiName=uiName,itemName=title,CheckButton_Var = CheckButton_Var))
                                root.bind("<"+ConvAccEventKey(AccKey,'S')+">",MenuFunction_Adaptor(onCheckButton,uiName=uiName,itemName=title,CheckButton_Var = CheckButton_Var))
                    else:#command
                        title = MenuInfo[1]
                        imageFile = MenuInfo[2]
                        AccKey = MenuInfo[3]
                        FontName = MenuInfo[4]
                        FontSize = MenuInfo[5]
                        MenuFont = None
                        if FontName and FontSize:
                            MenuFont = (FontName,FontSize)
                        eventFunc = None
                        funcName = 'Menu_'+title
                        if hasattr(UICmd,funcName) == True:    
                            eventFunc = getattr(UICmd, funcName)
                        if eventFunc:
                            if imageFile and MenuFont and AccKey:
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_command(label=title,font=MenuFont,image=MenuIconDict[IconName],compound='left',accelerator=AccKey,command=partial(eventFunc,uiName=uiName,itemName=title))
                            elif imageFile and MenuFont :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_command(label=title,font=MenuFont,image=MenuIconDict[IconName],compound='left',command=partial(eventFunc,uiName=uiName,itemName=title))
                            elif MenuFont and AccKey :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_command(label=title,font=MenuFont,accelerator=AccKey,command=partial(eventFunc,uiName=uiName,itemName=title))
                            elif imageFile and AccKey :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_command(label=title,image=MenuIconDict[IconName],compound='left',accelerator=AccKey,command=partial(eventFunc,uiName=uiName,itemName=title))
                            elif imageFile :
                                IconName ='MainMenu_' + shotname
                                ParentMenu.add_command(label=title,image=MenuIconDict[IconName],compound='left',command=partial(eventFunc,uiName=uiName,itemName=title))
                            elif MenuFont :
                                ParentMenu.add_command(label=title,font=MenuFont,command=partial(eventFunc,uiName=uiName,itemName=title))
                            else:
                                ParentMenu.add_command(label=title,command=partial(eventFunc,uiName=uiName,itemName=title))
                            if AccKey !='':
                                root.bind("<"+ConvAccEventKey(AccKey,'B')+">",MenuFunction_Adaptor(eventFunc,uiName=uiName,itemName=title))
                                root.bind("<"+ConvAccEventKey(AccKey,'S')+">",MenuFunction_Adaptor(eventFunc,uiName=uiName,itemName=title))
            if isinstance(root,tkinter.Tk) == True:
                MainMenuIconDict = {}
                if 'MainMenuIconList' in UIInfoDict:    
                    for IconInfo in UIInfoDict['MainMenuIconList']:    
                        IconName = IconInfo[0]
                        FileName = IconInfo[1]
                        MainMenuIconDict[IconName]= LoadImageToIconList(uiName,'MainMenu',IconName,FileName)
                if 'MainMenuInfoList' in UIInfoDict:  
                    MainMenu = tkinter.Menu(root)
                    BuildMainMenu(MainMenu,UIInfoDict['MainMenuInfoList'],MainMenuIconDict)
                    root.config(menu=MainMenu)
        except Exception as ex:   
            MessageBox(str(ex))
            # except_type, except_value, except_traceback = sys.exc_info()
            # except_value_str = str(except_value)
            # except_stack_end = except_traceback.tb_frame    
            # except_stack_next = except_traceback.tb_next    
            # except_stack_lineno = except_traceback.tb_lineno    
            # while except_stack_next:    
            #     except_stack_end = except_stack_next.tb_frame    
            #     except_stack_lineno = except_stack_next.tb_lineno    
            #     except_stack_next = except_stack_next.tb_next    
            # except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
            # MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+except_stack_lineno,'运行错误')
    return Form_1    
 
def GetElementType(uiName,elementName):    
    #取得控件类型:参数1 :界面类名, 参数2:控件名称。  
    if uiName in G_UIElementAliasDictionary:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            splitArray = elementName.split('_')
            ElementType = splitArray[0]    
            if ElementType == "PyMe":    
                ElementType = splitArray[1]    
            return ElementType    
    return None    
 
def GetElementXYWH(uiName,elementName):    
    #取得控件所在矩形  
    Control = GetElement(uiName,elementName)
    if Control:
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget() 
        x = Control.winfo_x()
        y = Control.winfo_y()
        width = Control.winfo_width()
        height = Control.winfo_height()
        return (x,y,width,height)
    return None    
def SetElementXY(uiName,elementName,x,y):    
    #设置控件显示位置  
    Control = GetElement(uiName,elementName)
    if Control:
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget() 
        Control.place(x=x,y=y)
def SetElementWH(uiName,elementName,width,height):    
    #移动控件显示大小  
    Control = GetElement(uiName,elementName)
    if Control:
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget() 
        Control.place(width=width,height=height)
def SetElementXYWH(uiName,elementName,x,y,width,height):    
    #设置控件显示位置和大小  
    Control = GetElement(uiName,elementName)
    if Control:
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget() 
        Control.place(x=x,y=y,width=width,height=height)
    
def AddTKVariable(uiName,elementName,defaultValue = None):    
    #为控件增加一个Tkinter的内置控件变量,参数1 :界面类名, 参数2:控件名称,参数3:默认值。  
    PrintFunctionInfo(AddTKVariable,[uiName,elementName,defaultValue])  
    if uiName not in G_UIElementVariableArray:     
        G_UIElementVariableArray[uiName]={}     
    NameLower = elementName.lower() 
    if NameLower.find('combobox_') >= 0:     
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar() 
    elif NameLower.find('group_') >= 0:     
        G_UIElementVariableArray[uiName][elementName]=tkinter.IntVar() 
    elif NameLower.find('checkbutton_') >= 0:     
        G_UIElementVariableArray[uiName][elementName]=tkinter.BooleanVar() 
    else:     
        G_UIElementVariableArray[uiName][elementName]=tkinter.StringVar() 
    if defaultValue:     
        G_UIElementVariableArray[uiName][elementName].set(defaultValue)  
    return G_UIElementVariableArray[uiName][elementName]  
def SetTKVariable(uiName,elementName,value):    
    PrintFunctionInfo(AddTKVariable,[uiName,elementName,value])  
    #设置控件的tkinter变量.参数1 :界面类名, 参数2:控件名称,参数3:值。  
    if uiName in G_UIElementVariableArray:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]      
        if elementName in G_UIElementVariableArray[uiName]:     
            G_UIElementVariableArray[uiName][elementName].set(value) 
        if elementName in G_UIGroupDictionary[uiName]:     
            GroupName = G_UIGroupDictionary[uiName][elementName]    
            if GroupName in G_UIElementVariableArray[uiName]:     
                G_UIElementVariableArray[uiName][GroupName].set(value) 
def GetTKVariable(uiName,elementName):    
    #取得控件的tkinter变量.参数1 :界面类名, 参数2:控件名称。  
    PrintFunctionInfo(GetTKVariable,[uiName,elementName])  
    if uiName in G_UIElementVariableArray:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName in G_UIElementVariableArray[uiName]:     
            return G_UIElementVariableArray[uiName][elementName].get()  
        if elementName in G_UIGroupDictionary[uiName]:     
            GroupName = G_UIGroupDictionary[uiName][elementName]    
            if GroupName in G_UIElementVariableArray[uiName]:     
                return G_UIElementVariableArray[uiName][GroupName].get()  
    return None   

def AddUserData(uiName,elementName,dataName,datatype,datavalue,isMapToText = 0):   
    PrintFunctionInfo(AddUserData,[uiName,elementName,dataName,datatype,datavalue,isMapToText])  
    #为控件添加一个用户数据,参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,datatype为数据类型,可以包括int、float、string、list、dictionary等,一般在设计软件中用鼠标右键操作控件,在弹出的“绑定数据”对话枉中设置,参数4:datavalue为数据值,而ismaptotext则是是否将数据直接反映到控件的text变量中。  
    if uiName not in G_UIElementUserDataArray:    
        G_UIElementUserDataArray[uiName]={}     
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if elementName not in G_UIElementUserDataArray[uiName]:    
        G_UIElementUserDataArray[uiName][elementName]=[]    
    else:    
        for EBData in G_UIElementUserDataArray[uiName][elementName]:    
            if EBData[0] == dataName:    
                EBData[1] = datatype    
                EBData[2] = datavalue    
                EBData[3] = isMapToText    
                if int(EBData[3]) == 1 :    
                    SetText(uiName,elementName,datavalue)     
                return    
    G_UIElementUserDataArray[uiName][elementName].append([dataName,datatype,datavalue,isMapToText])
def DelUserData(uiName,elementName,dataName):  
    PrintFunctionInfo(DelUserData,[uiName,elementName,dataName])  
    #删除一个用户变量  
    if uiName in G_UIElementUserDataArray:       
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName in G_UIElementUserDataArray[uiName]:    
            dataIndex = 0    
            for EBData in G_UIElementUserDataArray[uiName][elementName]:    
                if EBData[0] == dataName:    
                    G_UIElementUserDataArray[uiName][elementName].pop(dataIndex)
                    return     
                dataIndex = dataIndex + 1   
 
def SetUserData(uiName,elementName,dataName,datavalue):   
    PrintFunctionInfo(SetUserData,[uiName,elementName,dataName,datavalue])  
    #设置控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名,参数4:datavalue为数据值。  
    if uiName in G_UIElementUserDataArray:       
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName in G_UIElementUserDataArray[uiName]:    
            for EBData in G_UIElementUserDataArray[uiName][elementName]:    
                if EBData[0] == dataName:    
                    EBData[2] = datavalue    
                    if int(EBData[3]) == 1:    
                        SetText(uiName,elementName,datavalue)     
                    return  
  
def GetUserData(uiName,elementName,dataName):   
    PrintFunctionInfo(GetUserData,[uiName,elementName,dataName])  
    #取得控件的用户数据值。参数1 :界面类名, 参数2:控件名称,参数3:dataname为数据名。  
    if  uiName in G_UIElementUserDataArray:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName in G_UIElementUserDataArray[uiName]:    
            for EBData in G_UIElementUserDataArray[uiName][elementName]:    
                if EBData[0] == dataName:    
                    if EBData[1]=='int':    
                        return int(EBData[2])
                    elif EBData[1]=='float':    
                        return float(EBData[2])
                    else:    
                        return EBData[2]    
    return None
  
def SetTKAttrib(uiName,elementName,AttribName,attribValue): 
    PrintFunctionInfo(SetTKAttrib,[uiName,elementName,AttribName,attribValue])  
    #设置控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名,参数4:attribValue为数据值。  
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    if Control:    
        if AttribName in Control.configure().keys():    
            Control[AttribName]=attribValue    
   
def GetTKAttrib(uiName,elementName,AttribName):  
    PrintFunctionInfo(GetTKAttrib,[uiName,elementName,AttribName]) 
    #获取控件的tkinter属性值。参数1 :界面类名, 参数2:控件名称,参数3:AttribName为属性名。  
    Control = GetElement(uiName,elementName)
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    if Control:    
        return Control.cget(AttribName)
    return None
   
def SetElementVisible(uiName,elementName,Visible):  
    if Visible == 1:
        Visible = True
    elif Visible == 0:
        Visible = False
    PrintFunctionInfo(SetElementVisible,[uiName,elementName,Visible]) 
    #设置控件显示或隐藏（旧函数，请使用SetVisible）  
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return     
    if hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    RealElementName = elementName    
    if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():    
        RealElementName = G_UIElementAliasDictionary[uiName][RealElementName]     
    G_UIElementPlaceDictionary[uiName][RealElementName]["visible"] = Visible    
    if Visible == True :    
        if G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "pack":    
            fill = G_UIElementPlaceDictionary[uiName][RealElementName]["fill"]    
            side = G_UIElementPlaceDictionary[uiName][RealElementName]["side"]    
            padx = G_UIElementPlaceDictionary[uiName][RealElementName]["padx"]    
            pady = G_UIElementPlaceDictionary[uiName][RealElementName]["pady"]    
            expand = G_UIElementPlaceDictionary[uiName][RealElementName]["expand"]    
            SetControlPack(uiName,elementName,fill,side,padx,pady,expand)
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "grid":    
            row = G_UIElementPlaceDictionary[uiName][RealElementName]["row"]    
            column = G_UIElementPlaceDictionary[uiName][RealElementName]["column"]    
            rowspan = G_UIElementPlaceDictionary[uiName][RealElementName]["rowspan"]    
            columnspan = G_UIElementPlaceDictionary[uiName][RealElementName]["columnspan"]    
            SetControlGrid(uiName,elementName,row,column,rowspan,columnspan)
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "place":    
            x = 0    
            if "relx" in G_UIElementPlaceDictionary[uiName][RealElementName]:    
                x = G_UIElementPlaceDictionary[uiName][RealElementName]["relx"]    
            else:    
                x = G_UIElementPlaceDictionary[uiName][RealElementName]["x"]    
            y = 0    
            if "rely" in G_UIElementPlaceDictionary[uiName][RealElementName]:    
                y = G_UIElementPlaceDictionary[uiName][RealElementName]["rely"]    
            else:    
                y = G_UIElementPlaceDictionary[uiName][RealElementName]["y"]    
            w = 0    
            if "relwidth" in G_UIElementPlaceDictionary[uiName][RealElementName]:    
                w = G_UIElementPlaceDictionary[uiName][RealElementName]["relwidth"]    
            else:    
                w = G_UIElementPlaceDictionary[uiName][RealElementName]["width"]    
            h = 0    
            if "relheight" in G_UIElementPlaceDictionary[uiName][RealElementName]:    
                h = G_UIElementPlaceDictionary[uiName][RealElementName]["relheight"]    
            else:    
                h = G_UIElementPlaceDictionary[uiName][RealElementName]["height"]    
            SetControlPlace(uiName,elementName,x,y,w,h)
    else:    
        if G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "pack":    
            Control.pack_forget()
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "grid":    
            Control.grid_forget()
        elif G_UIElementPlaceDictionary[uiName][RealElementName]["type"] == "place":    
            Control.place_forget()
        G_UIElementPlaceDictionary[uiName][RealElementName]['visible'] = False    
def SetVisible(uiName,elementName,Visible):    
    #设置控件显示或隐藏  
    SetElementVisible(uiName,elementName,Visible)
def SetElementEnable(uiName,elementName,Enable): 
    if Enable == 1:
        Enable = True
    elif Enable == 0:
        Enable = False
    PrintFunctionInfo(SetElementEnable,[uiName,elementName,Enable]) 
    #设置控件可用或无效（旧函数，请使用SetEnable）  
    element = GetElement(uiName,elementName)
    if element:    
        if elementName and uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Frame_') >= 0 or elementName.find('LabelFrame_') >= 0:    
            def SetChildrenState(child,state):    
                childlist = child.winfo_children()
                for child in childlist:    
                    try:    
                        child.configure(state=state)
                    except:    
                        pass    
                    SetChildrenState(child,state)
            if Enable == True:    
                SetChildrenState(element,'normal')
            else:    
                SetChildrenState(element,'disabled')
        if elementName.find('Entry_') >= 0 or elementName.find('LabelButton_') >= 0:    
            if Enable == True:    
                element.SetState('normal')
            else:    
                element.SetState('disabled')
        else:    
            if hasattr(element,"GetEntry") == True:    
                element = element.GetEntry()
            elif hasattr(element,"GetWidget") == True:    
                element = element.GetWidget()
            try:    
                if Enable == True:    
                    element.configure(state='normal')
                else:    
                    element.configure(state='disabled')
            except:    
                pass    
def SetEnable(uiName,elementName,Enable):    
    #设置控件可用或无效  
    SetElementEnable(uiName,elementName,Enable)   

def IsElementVisible(uiName,elementName):  
    PrintFunctionInfo(IsElementVisible,[uiName,elementName]) 
    #取得控件显示或隐藏（旧函数，请使用IsVisible）  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    return G_UIElementPlaceDictionary[uiName][elementName]['visible']    
def IsVisible(uiName,elementName):    
    #取得控件显示或隐藏  
    return IsElementVisible(uiName,elementName)
def IsElementEnable(uiName,elementName):   
    PrintFunctionInfo(IsElementEnable,[uiName,elementName]) 
    #取得控件可用或无效（旧函数，请使用IsEnable）  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if elementName.find('Entry_') >= 0 or elementName.find('LabelButton_') >= 0:    
        return G_UIElementDictionary[uiName][elementName].GetState()
    else:    
        ElementState = G_UIElementDictionary[uiName][elementName].cget('state')
        ElementState = str(ElementState)
        if ElementState == 'disabled':    
            return False    
        else:    
            return True    
def IsEnable(uiName,elementName):    
    #取得控件可用或无效  
    return IsElementEnable(uiName,elementName)
   
def SetText(uiName,elementName,textValue): 
    PrintFunctionInfo(SetText,[uiName,elementName,textValue]) 
    #设置控件的文本(Label、Button、RadioButton、CheckButton、Entry、Text、ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称,参数3:文本内容。  
    showtext = str("%s"%textValue)
    if elementName and uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementVariableArray:     
        if elementName in G_UIElementVariableArray[uiName]:    
            G_UIElementVariableArray[uiName][elementName].set(showtext)
            return    
    element = GetElement(uiName,elementName)
    if element:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            try:    
                if elementName == "root":    
                    G_UIElementDictionary[uiName][elementName].title(textValue)
                elif elementName.find('Text_') >= 0:    
                    Control = G_UIElementDictionary[uiName][elementName]    
                    if hasattr(Control,"GetEntry") == True:    
                        Control = Control.GetEntry()
                    Control.delete('0.0',tkinter.END)
                    if len(showtext) > 0:    
                        Control.insert(tkinter.END,showtext)
                        Control.see(tkinter.END)
                elif elementName.find('Entry_') >= 0 or elementName.find('LabelButton_') >= 0:    
                    G_UIElementDictionary[uiName][elementName].SetText(showtext) 
                else:    
                    G_UIElementDictionary[uiName][elementName].configure(text=showtext)
            except Exception as ex:    
                print(ex)
def InsertText(uiName,elementName,position=tkinter.END,textValue='',tag=''): 
    PrintFunctionInfo(InsertText,[uiName,elementName,position,textValue,tag]) 
    #在文本框插入文本  
    showtext = str("%s"%textValue)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            if elementName.find('Text_') >= 0:    
                if len(showtext) > 0:    
                    Control = G_UIElementDictionary[uiName][elementName]    
                    if hasattr(Control,"GetEntry") == True:    
                        Control = Control.GetEntry()
                    Control.mark_set(tkinter.INSERT,position)
                    Control.insert(position,showtext,tag)
                    currentLine = Control.index(tkinter.INSERT)
                    Control.see(currentLine)
                    return  currentLine    
    return  None    
def GetCurrentLine(uiName,elementName):   
    PrintFunctionInfo(GetCurrentLine,[uiName,elementName]) 
    #取得文本框当前行号  
    element = GetElement(uiName,elementName)
    if element:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            if elementName.find('Text_') >= 0:    
                if hasattr(element,"GetEntry") == True:    
                    element = element.GetEntry()
                return element.index(tkinter.INSERT)
    return  None    
def DeleteContent(uiName,elementName,fromPosition='',toPosition=None):  
    PrintFunctionInfo(DeleteContent,[uiName,elementName,fromPosition,toPosition]) 
    #删除文本框区域内容  
    element = GetElement(uiName,elementName)
    if element:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            if elementName.find('Text_') >= 0:    
                if hasattr(element,"GetEntry") == True:    
                    element = element.GetEntry()
                if toPosition:    
                    element.delete(fromPosition,toPosition)
                else:    
                    element.delete(fromPosition) 
   
def GetText(uiName,elementName):   
    PrintFunctionInfo(GetText,[uiName,elementName]) 
    #获取控件的文本(Label、Button、RadioButton、CheckButton、Entry、Text、 ComboBox, SpinBox)。参数1 :界面类名, 参数2:控件名称。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            if elementName.find('Text_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if hasattr(Control,"GetEntry") == True:    
                    Control = Control.GetEntry()
                return Control.get('0.0', tkinter.END)
            elif elementName.find('Spinbox_') >= 0:    
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find('ComboBox_') >= 0:    
                return str(G_UIElementDictionary[uiName][elementName].get())
            elif elementName.find('ListBox_') >= 0:    
                currIndex = G_UIElementDictionary[uiName][elementName].curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:    
                    return  G_UIElementDictionary[uiName][elementName].get(currIndex[0])
            elif elementName.find('Entry_') >= 0:    
                if elementName in  G_UIElementVariableArray[uiName]:      
                    text = G_UIElementVariableArray[uiName][elementName].get()  
                else:      
                    text = G_UIElementDictionary[uiName][elementName].GetText() 
                return text    
            elif elementName.find('LabelButton_') >= 0:    
                text = G_UIElementDictionary[uiName][elementName].GetText() 
                return text    
            else:    
                if uiName in G_UIElementVariableArray:     
                    if elementName in G_UIElementVariableArray[uiName]:    
                        text = G_UIElementVariableArray[uiName][elementName].get()
                        return text    
                return G_UIElementDictionary[uiName][elementName].cget('text')
    return str("")
   
def CreateFont(fontName,fontSize,fontWeight=False,fontSlant=False,fontUnderline=False,fontOverstrike=False):    
    PrintFunctionInfo(CreateFont,[fontName,fontSize,fontWeight,fontSlant,fontUnderline,fontOverstrike]) 
    #创建控件字体  
    if type(fontWeight) == type(bool):
        if fontWeight == True:
            fontWeight = 'bold'
        else:
            fontWeight = 'normal'
    if type(fontSlant) == type(bool):
        if fontSlant == True:
            fontSlant = 'italic'
        else:
            fontSlant = 'roman'
    if type(fontUnderline) == type(bool):
        if fontUnderline == True:
            fontUnderline = 1
        else:
            fontUnderline = 0
    if type(fontOverstrike) == type(bool):
        if fontOverstrike == True:
            fontOverstrike = 1
        else:
            fontOverstrike = 0
    return tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
def SetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0):  
    PrintFunctionInfo(SetFont,[uiName,elementName,fontName,fontSize,fontWeight,fontSlant,fontUnderline,fontOverstrike]) 
    #设置控件字体  
    if type(fontWeight) == type(bool):
        if fontWeight == True:
            fontWeight = 'bold'
        else:
            fontWeight = 'normal'
    if type(fontSlant) == type(bool):
        if fontSlant == True:
            fontSlant = 'italic'
        else:
            fontSlant = 'roman'
    if type(fontUnderline) == type(bool):
        if fontUnderline == True:
            fontUnderline = 1
        else:
            fontUnderline = 0
    if type(fontOverstrike) == type(bool):
        if fontOverstrike == True:
            fontOverstrike = 1
        else:
            fontOverstrike = 0
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:      
            newFont = None    
            if elementName in G_CanvasFontDictionary[uiName]:       
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:    
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):    
                        newFont = fontInfo[0]                    
                        break    
            else:    
                G_CanvasFontDictionary[uiName][elementName] = []    
            if newFont is None:    
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
            if elementName.find('Entry_') >= 0 or elementName.find('LabelButton_') >= 0:    
                G_UIElementDictionary[uiName][elementName].SetFont(font=newFont)
            elif elementName.find('Canvas_') < 0 and elementName.find('Form_') < 0:    
                G_UIElementDictionary[uiName][elementName].configure(font=newFont)
            G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])                
def GetFont(uiName,elementName,fontName,fontSize,fontWeight='normal',fontSlant='roman',fontUnderline=0,fontOverstrike=0,createifnofind=True):  
    PrintFunctionInfo(GetFont,[uiName,elementName,fontName,fontSize,fontWeight,fontSlant,fontUnderline,fontOverstrike,createifnofind]) 
    #取得字体  
    if type(fontWeight) == type(bool):
        if fontWeight == True:
            fontWeight = 'bold'
        else:
            fontWeight = 'normal'
    if type(fontSlant) == type(bool):
        if fontSlant == True:
            fontSlant = 'italic'
        else:
            fontSlant = 'roman'
    if type(fontUnderline) == type(bool):
        if fontUnderline == True:
            fontUnderline = 1
        else:
            fontUnderline = 0
    if type(fontOverstrike) == type(bool):
        if fontOverstrike == True:
            fontOverstrike = 1
        else:
            fontOverstrike = 0
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            if elementName in G_CanvasFontDictionary[uiName]:       
                for fontInfo in G_CanvasFontDictionary[uiName][elementName]:    
                    if fontInfo[1] == fontName and fontInfo[2] == str(fontSize) and fontInfo[3] == fontWeight and fontInfo[4] == fontSlant and fontInfo[5] == str(fontUnderline) and fontInfo[6] == str(fontOverstrike):    
                        return fontInfo[0]    
            else:    
                G_CanvasFontDictionary[uiName][elementName] = []    
            if createifnofind == True:    
                newFont = tkinter.font.Font(family=fontName, size=fontSize,weight=fontWeight,slant=fontSlant,underline=fontUnderline,overstrike=fontOverstrike)
                G_CanvasFontDictionary[uiName][elementName].append([newFont,fontName,str(fontSize),fontWeight,fontSlant,str(fontUnderline),str(fontOverstrike)])                
                return newFont    
    return None    
   
def SetBGColor(uiName,elementName,RGBColor):  
    PrintFunctionInfo(SetBGColor,[uiName,elementName,RGBColor]) 
    #设置控件的背景色。参数1 :界面类名, 参数2:控件名称,参数3:背景颜色。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if hasattr(Control,"SetBGColor") == True:    
                Control.SetBGColor(RGBColor)
            else:  
                if elementName.find('ComboBox_') >= 0:  
                    StyleName = G_UIStyleDictionary[uiName][elementName]
                    if 'style' in G_UIElementDictionary[uiName]:
                        G_UIElementDictionary[uiName]['style'].configure(StyleName,fieldbackground=RGBColor)
                else:
                    Control.configure(bg=RGBColor)
def SetRadioButtonSelectedColor(uiName,elementName,BGColor,FGColor):  
    PrintFunctionInfo(SetRadioButtonSelectedColor,[uiName,elementName,BGColor,FGColor]) 
    #设置RadioButton控件的选中时候背景色与文字色  
    GroupName = G_UIGroupDictionary[uiName][elementName]
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if GroupName not in G_UIRadioButtonGroupArray[uiName]:    
                G_UIRadioButtonGroupArray[uiName][GroupName] = {}    
            if elementName not in G_UIRadioButtonGroupArray[uiName][GroupName]:      
                G_UIRadioButtonGroupArray[uiName][GroupName][elementName]=[[Control.cget('bg'),Control.cget('fg')],[BGColor,FGColor]] 
            else:
                G_UIRadioButtonGroupArray[uiName][GroupName][elementName][1]=[BGColor,FGColor]
def SetCheckButtonSelectedColor(uiName,elementName,BGColor,FGColor):    
    PrintFunctionInfo(SetCheckButtonSelectedColor,[uiName,elementName,BGColor,FGColor]) 
    #设置CheckButton控件的选中时候背景色与文字色  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if elementName not in G_UIRadioButtonGroupArray[uiName]:    
                G_UIRadioButtonGroupArray[uiName][elementName] = [[Control.cget('bg'),Control.cget('fg')],[BGColor,FGColor]]
            else:
                G_UIRadioButtonGroupArray[uiName][GroupName][elementName][1]=[BGColor,FGColor]

G_ComboBoxPopdownWindowSettingEnable = True
def SetComboBoxListColor(uiName,elementName,BGColor,FGColor):  
    global G_ComboBoxPopdownWindowSettingEnable 
    PrintFunctionInfo(SetComboBoxListColor,[uiName,elementName,BGColor,FGColor]) 
    #设置ComboBox控件下拉框的背景色与文字色  
    if G_ComboBoxPopdownWindowSettingEnable == True:
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if uiName in G_UIElementDictionary:    
            if elementName in G_UIElementDictionary[uiName]:       
                Control = G_UIElementDictionary[uiName][elementName]    
                try:
                    Control.tk.eval('[ttk::combobox::PopdownWindow %s].f.l configure -foreground %s -background %s' % (Control,FGColor,BGColor))
                except: 
                    print("SetComboBoxListColor Error!")
                    G_ComboBoxPopdownWindowSettingEnable = False
   
def GetBGColor(uiName,elementName):    
    PrintFunctionInfo(GetBGColor,[uiName,elementName]) 
    #获取控件的背景色。参数1 :界面类名, 参数2:控件名称。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if hasattr(elementName,"GetBGColor") == True:    
                return Control.GetBGColor()
            else:    
                if elementName.find('ComboBox_') >= 0:  
                    StyleName = G_UIStyleDictionary[uiName][elementName]
                    if 'style' in G_UIElementDictionary[uiName]:
                        return G_UIElementDictionary[uiName]['style'].lookup(StyleName,'fieldbackground')
                else:
                    return Control.cget('bg')
    return None    
     
def SetTextColor(uiName,elementName,RGBColor):  
    PrintFunctionInfo(SetTextColor,[uiName,elementName,RGBColor]) 
    #设置控件的文字色。参数1 :界面类名, 参数2:控件名称,参数3:文字颜色。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if hasattr(Control,"SetFGColor") == True:    
                Control.SetFGColor(RGBColor)
            else:    
                if elementName.find('ComboBox_') >= 0:  
                    StyleName = G_UIStyleDictionary[uiName][elementName]
                    if 'style' in G_UIElementDictionary[uiName]:
                        G_UIElementDictionary[uiName]['style'].configure(StyleName,foreground=RGBColor)
                else:
                    Control.configure(fg=RGBColor)
       
def GetTextColor(uiName,elementName):  
    PrintFunctionInfo(GetTextColor,[uiName,elementName]) 
    #获取控件的文字色。参数1 :界面类名, 参数2:控件名称。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:       
            Control = G_UIElementDictionary[uiName][elementName]    
            if hasattr(elementName,"GetFGColor") == True:    
                return Control.GetFGColor()
            else:   
                if elementName.find('ComboBox_') >= 0:  
                    StyleName = G_UIStyleDictionary[uiName][elementName]
                    if 'style' in G_UIElementDictionary[uiName]:
                        return G_UIElementDictionary[uiName]['style'].lookup(StyleName,'foreground')
                else:
                    return Control.cget('fg')
    return None    
 
def LoadImageFromPMEFile(imagePath):
 
    return None
 
def SetImage(uiName,elementName,imagePath,autoSize = True,format='RGBA',state='normal'):  
    PrintFunctionInfo(SetImage,[uiName,elementName,imagePath,autoSize,format,state]) 
    #设置控件的背景图片(Label,Button,Text)。参数1 :界面类名, 参数2:控件名称,参数3:图片名称。  
    from   PIL import Image,ImageTk    
    Control = GetElement(uiName,elementName) 
    if Control :     
        if hasattr(Control,"GetEntry") == True:    
            Control = Control.GetEntry()
        elif hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()  
        Control_Width = Control.winfo_width() 
        Control_Height = Control.winfo_height() 
        if isinstance(imagePath,str) == True:    
            pathName,fileName = os.path.split(imagePath)
            shotName,extension = os.path.splitext(fileName)
            if extension.lower() == '.gif':    
                if autoSize == True:    
                    LoadGIF(uiName,elementName,imagePath,Control_Width,Control_Height)
                else:    
                    LoadGIF(uiName,elementName,imagePath)
                return    
        image = None    
        if isinstance(imagePath,str) == True:    
            imagePath_Lower = imagePath.lower()
            if os.path.exists(imagePath) == False:    
                if imagePath_Lower in G_ResourcesFileList:    
                    imagePath = G_ResourcesFileList[imagePath_Lower]    
                elif os.path.exists(imagePath) == False:
                    imageDir, imageFile = os.path.split(imagePath)
                    imagePath = os.path.join(G_ResDir,imageFile)
                if os.path.exists(imagePath) == False:                 
                    image = LoadImageFromPMEFile(imagePath)
                    if image is None:    
                        Control.configure(image = '')
                        return    
            if image is None:    
                image = Image.open(imagePath).convert(format)
        elif isinstance(imagePath,Image.Image) == True:    
            image = imagePath.convert(format)
        if image is None:    
            Control.configure(image = '')
            return    
        realElementName = elementName     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            realElementName = G_UIElementAliasDictionary[uiName][elementName]     
        if realElementName.find('Label_') >= 0 or realElementName.find('Button_') >= 0 :    
            if uiName in G_UIElementUserDataArray:    
                if realElementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][realElementName]:       
                        if EBData[0] == 'image' and EBData[1] == 'imageInfo':  
                            for ImageData in EBData[2]:       
                                if ImageData[3] == state:    
                                    ImageData[1] = imagePath    
                                    if autoSize == True:    
                                        image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
                                    else:    
                                        image_Resize = image    
                                    ImageData[0] = ImageTk.PhotoImage(image_Resize)
                                    ImageData[2] = autoSize    
                                    if state == 'selected':    
                                        Control.configure(selectimage = ImageData[0])
                                    else:    
                                        Control.configure(image = ImageData[0])
                                    return
                            
                            if autoSize == True:    
                                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
                            else:    
                                image_Resize = image    
                            newPTImage = ImageTk.PhotoImage(image_Resize)
                            if state == 'selected':    
                                Control.configure(selectimage = EBData[2][0])
                            else:    
                                Control.configure(image = EBData[2][0])
                            EBData[2].append([newPTImage,imagePath,autoSize,state])
                            return     
            if autoSize == True:    
                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
            else:    
                image_Resize = image    
            newPTImage = ImageTk.PhotoImage(image_Resize)
            AddUserData(uiName,elementName,'image','imageInfo',[[newPTImage,imagePath,autoSize,state]],0)
            if state == 'selected':    
                Control.configure(selectimage = newPTImage)
            else:    
                Control.configure(image = newPTImage)
        if realElementName.find('Text_') >= 0:    
            if hasattr(Control,"GetEntry") == True:    
                Control = Control.GetEntry()
            Control.delete('0.0',tkinter.END)
            imagePath_Lower = imagePath.lower()
            if autoSize == True:    
                image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
            else:    
                image_Resize = image    
            newPTImage = ImageTk.PhotoImage(image_Resize)
            Control.image_create(tkinter.END, image=newPTImage)
            AddUserData(uiName,elementName,'image','imageInfo',[[newPTImage,imagePath,autoSize,state]],0)
        if realElementName.find('Form_') >= 0 or realElementName.find('Canvas_') >= 0:    
            if autoSize == True:    
                SetCanvasBGImage(uiName,elementName,imagePath)
            else:    
                SetCanvasBGImage(uiName,elementName,imagePath,'')
def InsertImage(uiName,elementName,position=tkinter.END,imagePath='',imageSize=None): 
    PrintFunctionInfo(InsertImage,[uiName,elementName,position,imagePath,imageSize]) 
    #在文本框插入图片  
    Control = GetElement(uiName,elementName) 
    if Control == True:     
        from   PIL import Image,ImageTk    
        image = None    
        if isinstance(imagePath,str) == True:    
            imagePath_Lower = imagePath.lower()
            if os.path.exists(imagePath) == False:    
                if imagePath_Lower in G_ResourcesFileList:    
                    imagePath = G_ResourcesFileList[imagePath_Lower]  
                elif os.path.exists(imagePath) == False:
                    imageDir, imageFile = os.path.split(imagePath)
                    imagePath = os.path.join(G_ResDir,imageFile)
                if os.path.exists(imagePath) == False:
                    image = LoadImageFromPMEFile(imagePath)
                    if image is None:    
                        return    
            if image is None:    
                image = Image.open(imagePath).convert(format)
        elif isinstance(imagePath,Image.Image) == True:    
            image = imagePath.convert(format)
        if image:    
            image_Resize = image    
            if imageSize:    
                image_Resize = image.resize(imageSize,Image.LANCZOS)
            newPTImage = ImageTk.PhotoImage(image_Resize)
            Control.image_create(position, image=newPTImage)
            ImageDataList = GetUserData(uiName,elementName,'image')
            if ImageDataList:
                ImageDataList.append([newPTImage,imagePath,False,'normal'])
                SetUserData(uiName,elementName,'image',ImageDataList)
            else:
                AddUserData(uiName,elementName,'image','imageInfo',[[newPTImage,imagePath,False,'normal']],0)
            currentLine = Control.index(tkinter.INSERT)
            return  currentLine
    return  None
def SetCanvasBGImage(uiName,elementName,imagePath,wrapType='zoom'): 
    PrintFunctionInfo(SetCanvasBGImage,[uiName,elementName,imagePath,wrapType]) 
    #设置画布Canvas的背景图片。参数1 :界面类名, 参数2:画布名称,参数3:图片文件,参数4:绘图方式:Original为原始大小,Zoom为缩放匹配画布大小,Tiling为平铺满画布  
    Control = GetElement(uiName,elementName) 
    if Control:     
        realElementName = elementName     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            realElementName = G_UIElementAliasDictionary[uiName][elementName]     
        if realElementName.find('Form_') >= 0 or realElementName.find('Canvas_') >= 0 :    
            newImage = None    
            if imagePath:    
                if isinstance(imagePath,str) == True:    
                    imagePath_Lower = imagePath.lower()
                    if os.path.exists(imagePath) == False:    
                        if imagePath_Lower in G_ResourcesFileList:    
                            imagePath = G_ResourcesFileList[imagePath_Lower]    
                        elif os.path.exists(imagePath) == False:
                            imageDir, imageFile = os.path.split(imagePath)
                            imagePath = os.path.join(G_ResDir,imageFile)
                        if os.path.exists(imagePath) == False:                         
                            newImage = LoadImageFromPMEFile(imagePath)
                    if newImage is None:    
                        newImage = Image.open(imagePath).convert('RGBA')   
                else:    
                    newImage = imagePath    
            if newImage is None:    
                return
            Control.delete('BGImage')
            Control_Width = Control.winfo_width()
            Control_Height = Control.winfo_height()
            if realElementName.find('Form_') >= 0:
                if Control_Width == 1 and Control_Height == 1:
                    Root = GetElement(uiName,'root')
                    if isinstance(Root,tkinter.Tk) == True:
                        Control_Width = Root.winfo_width()
                        Control_Height = Root.winfo_height()
                    elif isinstance(Root.master,tkinter.Frame) == True or isinstance(Root.master,tkinter.LabelFrame) == True:
                        Control_Width = Root.master.winfo_width()
                        Control_Height = Root.master.winfo_height()
                    elif isinstance(Root.master, tkinter.ttk.Notebook) == True:
                        Control_Width = Root.winfo_width()
                        Control_Height = Root.winfo_height()
            # try:    
            #     Form_1_Pack = Control.pack_info()
            #     if  len(Form_1_Pack) > 0:    
            #         if uiName in G_UIRootSizeDictionary.keys() and "width" in G_UIRootSizeDictionary[uiName].keys():    
            #             Control_Width = G_UIRootSizeDictionary[uiName]["width"]    
            #         elif G_RootSize:    
            #             Control_Width = G_RootSize[0]    
            #         if uiName in G_UIRootSizeDictionary.keys() and "height" in G_UIRootSizeDictionary[uiName].keys():    
            #             Control_Height = G_UIRootSizeDictionary[uiName]["height"]    
            #         elif G_RootSize:    
            #             Control_Height = G_RootSize[1]    
            # except:    
            #     pass   
            wrapType = wrapType.lower() 
            if wrapType == "zoom" :    
                reSizeImage = newImage.resize((Control_Width, Control_Height),Image.LANCZOS)
                newPTImage = ImageTk.PhotoImage(reSizeImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            elif wrapType == "tiling" :    
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                RepeatRow = int(Control_Height / newImage.height) + 1    
                RepeatCow = int(Control_Width / newImage.width) + 1    
                for r in range(RepeatRow):    
                    for c in range(RepeatCow):    
                        Control.create_image(c * newImage.width, r * newImage.height,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
            else:    
                newPTImage = ImageTk.PhotoImage(newImage)
                AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,imagePath,wrapType],0)
                Control.create_image(0,0,anchor=tkinter.NW,image=newPTImage,tag="BGImage")
        ReDrawCanvasShape(uiName,elementName)
g_DownLoadImageDictionary = {}    
def SetImageFromURL(uiName,elementName,url,autoSize = True):  
    PrintFunctionInfo(SetImageFromURL,[uiName,elementName,url,autoSize]) 
    #多线程设置控件的图片背景。参数1:界面类名,参数2:控件名称,参数3:网址,参数4:缩放匹配控件大小  
    Control = GetElement(uiName,elementName) 
    ControlType = "Label"    
    if elementName.find('Form_') >= 0 or elementName.find('Canvas_') >= 0 :    
        ControlType = "Canvas"    
    if elementName.find('Text_') >= 0 :    
        ControlType = "Text"    
    if Control:    
        def DownLoadImageFromURL(Control,ControlType,url,autoSize):    
            try:    
                if url in g_DownLoadImageDictionary:        
                    if ControlType == "Canvas":       
                        Control.delete('BGImage')
                        Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                    elif ControlType == "Text":       
                        if hasattr(Control,"GetEntry") == True:    
                            Control = Control.GetEntry()
                        Control.delete('0.0',tkinter.END)
                        Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                    else:       
                        Control.configure(image=g_DownLoadImageDictionary[url])    
                else:     
                    urlOpen = urlopen(url) 
                    if urlOpen :     
                        image_bytes = urlOpen.read() 
                        data_stream = io.BytesIO(image_bytes) 
                        pil_image = Image.open(data_stream) 
                        if autoSize == True:     
                            pil_image = pil_image.resize((Control.winfo_width(), Control.winfo_height()),Image.LANCZOS) 
                        g_DownLoadImageDictionary[url] = ImageTk.PhotoImage(pil_image) 
                        if ControlType == "Canvas":       
                            Control.delete('BGImage')
                            Control.create_image(0,0,anchor=tkinter.NW,image=g_DownLoadImageDictionary[url],tag="BGImage")
                        elif ControlType == "Text":       
                            Control.delete('0.0',tkinter.END)
                            Control.image_create(tkinter.END, image=g_DownLoadImageDictionary[url])
                        else:       
                            Control.configure(image=g_DownLoadImageDictionary[url]) 
            except Exception as ex:    
                print(ex)
        run_thread = threading.Thread(target=DownLoadImageFromURL, args=[Control,ControlType,url,autoSize])
        run_thread.Daemon = True    
        run_thread.start() 
def RemoveImage(uiName,elementName):  
    PrintFunctionInfo(RemoveImage,[uiName,elementName]) 
    #删除控件的背景图像文件(Label、Button,Canvas,Form)。参数1 :界面类名, 参数2:控件名称。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        DelUserData(uiName,elementName,'image')
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 :    
            Control.configure(image = '')
        if elementName.find('Form_') >= 0 or elementName.find('Canvas_') >= 0 :    
            Control.delete('BGImage')   
 
def GetImage(uiName,elementName,state='normal'):  
    PrintFunctionInfo(GetImage,[uiName,elementName,state]) 
    #获取控件的背景图像文件(Label、Button)。参数1 :界面类名, 参数2:控件名称。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 :    
            if uiName in G_UIElementUserDataArray:    
                if elementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:       
                        if EBData[0] == 'image' and EBData[1] =='imageInfo':    
                            for imageInfo in EBData[2]:       
                                if imageInfo[3] == state:    
                                    return imageInfo[0]
        if elementName.find('Form_') >= 0 or elementName.find('Canvas_') >= 0 :    
            if uiName in G_UIElementUserDataArray:    
                if elementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:       
                        if EBData[0] == 'BGImage' and EBData[1] =='imageInfo':    
                            return EBData[2][0] 
    return str("")
def GetImageFileName(uiName,elementName):  
    PrintFunctionInfo(GetImageFileName,[uiName,elementName]) 
    #取得控件图片文件  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 :    
            if uiName in G_UIElementUserDataArray:    
                if elementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:       
                        if EBData[0] == 'image' and EBData[1] =='imageInfo':    
                            for imageInfo in EBData[2]:       
                                if imageInfo[3] == state:    
                                    return imageInfo[1]
        if elementName.find('Form_') >= 0 or elementName.find('Canvas_') >= 0 :    
            if uiName in G_UIElementUserDataArray:    
                if elementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:       
                        if EBData[0] == 'BGImage' and EBData[1] =='imageInfo':    
                            return EBData[2][1]    
    return str("")
def LoadImageFromFile(imagefile,imageSize=None,uiName=None,elementName=None): 
    PrintFunctionInfo(LoadImageFromFile,[imagefile,imageSize,uiName,elementName]) 
    #从文件加载图片  
    if imagefile != None:    
        resourPath = imagefile    
        newImage = None    
        if os.path.exists(resourPath) == False:    
            resourPath, imagefile = os.path.split(imagefile)
            imagefile_Lower = imagefile.lower()
            if imagefile_Lower in G_ResourcesFileList:    
                resourPath = G_ResourcesFileList[imagefile_Lower]    
            else:    
                newImage = LoadImageFromPMEFile(imagefile)
        try:    
            if os.path.exists(resourPath) == True and newImage is None:    
                pathname_noext, extension = os.path.splitext(resourPath)
                newImage = None    
                extension = extension.lower()
                if extension == ".png" or extension == ".gif":    
                    newImage = Image.open(resourPath).convert('RGBA')
                elif extension == ".jpg" or extension == ".bmp":    
                    newImage = Image.open(resourPath).convert('RGB')
                else:    
                    return None    
            if newImage == None:    
                return None    
            if imageSize:    
                newImage = newImage.resize(imageSize,Image.LANCZOS)
            if uiName and elementName:    
                realElementName = elementName    
                if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
                    realElementName = G_UIElementAliasDictionary[uiName][elementName]    
                newPTImage = ImageTk.PhotoImage(newImage)
                if realElementName.find('Form_') >= 0 or realElementName.find('Canvas_') >= 0 :    
                    AddUserData(uiName,elementName,'BGImage','imageInfo',[newPTImage,resourPath,False],0)
                else:    
                    AddUserData(uiName,elementName,'image','imageInfo',[[newPTImage,resourPath,False,'normal']],0)
            return newImage    
        except Exception as ex:    
            print(imagefile+'加载图片失败')
    return None    
def LoadGIF(uiName,elementName,imagefile,width=0,height=0):  
    PrintFunctionInfo(LoadGIF,[uiName,elementName,imagefile,width,height]) 
    #播放GIF动画  
    newImage = None    
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0 or elementName.find('Text_') >= 0:    
            hasGIFAnimation = False    
            if imagefile != None:    
                resourPath = imagefile     
                if os.path.exists(resourPath) == False:    
                    resourPath, imagefile = os.path.split(imagefile)
                    imagefile_Lower = imagefile.lower()
                    if imagefile_Lower in G_ResourcesFileList:    
                        resourPath = G_ResourcesFileList[imagefile_Lower]    
                if os.path.exists(resourPath) == True:    
                    try:    
                        if imagefile.find('.gif') >= 0:    
                            GifData = Image.open(resourPath)
                            seq = []    
                            try:    
                                while 1:    
                                    imageRGBA = GifData.copy().convert('RGBA')
                                    if newImage is None:    
                                        newImage = imageRGBA    
                                    if width > 0 and height > 0:    
                                        resizeImage = imageRGBA.resize((width, height),Image.LANCZOS)
                                        newFrame = ImageTk.PhotoImage(resizeImage)
                                    else:    
                                        newFrame = ImageTk.PhotoImage(imageRGBA)
                                    seq.append(newFrame)
                                    GifData.seek(len(seq))
                            except EOFError:    
                                pass    
                            delay = 100    
                            try:    
                                delay = GifData.info['duration']    
                            except KeyError:    
                                delay = 100    
                            if delay == 0:    
                                delay = 100    
                            hasGIFAnimation = True    
                            if elementName not in G_CanvasImageDictionary[uiName]:    
                                G_CanvasImageDictionary[uiName][elementName] = []    
                            G_CanvasImageDictionary[uiName][elementName].append([imagefile,[seq,delay,0,None],width,height])
                        else:    
                            newImage = Image.open(resourPath).convert('RGBA')
                    except:    
                        return newImage    
                if hasGIFAnimation == True:    
                    Control.after(100,lambda: updateGIFFrame(uiName,elementName))
    return newImage    
def StopGIF(uiName,elementName):  
    PrintFunctionInfo(StopGIF,[uiName,elementName]) 
    #停止GIF动画  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0 or elementName.find('Text_') >= 0:    
            Control.after_cancel(updateGIFFrame)
            if elementName in G_CanvasImageDictionary[uiName]:    
                G_CanvasImageDictionary[uiName][elementName].clear()
   
def LoadImageToIconList(uiName,elementName,IconName,imageFile):  
    PrintFunctionInfo(LoadImageToIconList,[uiName,elementName,IconName,imageFile]) 
    #加载控件的图像文件:参数1 :界面类名, 参数2:控件名称, 参数3:树项名称, 参数4:图片文件  
    imagePath = imageFile    
    imageFile_Lower = imageFile.lower()
    if imageFile_Lower in G_ResourcesFileList:    
        imagePath = G_ResourcesFileList[imageFile_Lower]    
    if os.path.exists(imagePath) == True:    
        image = ImageTk.PhotoImage(file = imagePath)
        if elementName not in G_UIElementIconDictionary[uiName].keys():    
            G_UIElementIconDictionary[uiName][elementName] = {}    
        G_UIElementIconDictionary[uiName][elementName][IconName] = image    
        return image    
    return None    
  
def SetItemBGColor(uiName,elementName,lineIndex,color):   
    PrintFunctionInfo(SetItemBGColor,[uiName,elementName,lineIndex,color]) 
    #设置选项背景色  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:    
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {'bg':color})
def SetItemFGColor(uiName,elementName,lineIndex,color):   
    PrintFunctionInfo(SetItemFGColor,[uiName,elementName,lineIndex,color]) 
    #设置选项文字色  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ComboBox_') >= 0 or elementName.find('ListBox_') >= 0:    
                    G_UIElementDictionary[uiName][elementName].itemconfig(lineIndex, {'fg':color})
  
def AddItemText(uiName,elementName,text,lineIndex="end",set_see=False):    
    PrintFunctionInfo(SetItemFGColor,[uiName,elementName,text,lineIndex,set_see]) 
    #增加当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ComboBox_') >= 0:

                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                if type(lineIndex)==type(1):    
                    ValueArray.insert(lineIndex,text)
                else:    
                    ValueArray.append(text)
                G_UIElementDictionary[uiName][elementName]['value'] = ValueArray 

            elif elementName.find('ListBox_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if type(lineIndex)==type(1):    
                    Control.insert(lineIndex,text)
                else:    
                    Control.insert(lineIndex, text)
                if set_see == True:    
                    Control.see(lineIndex)
    def GetItemText(uiName,elementName,lineIndex=0):    
        #取得当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:索引值。  
           
            
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]    
        if uiName in G_UIElementDictionary:    
            if elementName in G_UIElementDictionary[uiName]:    
                Control = G_UIElementDictionary[uiName][elementName]    

                if elementName.find('ComboBox_') >= 0:
                    ValueArray = list(Control['value'])
                    if lineIndex < len(ValueArray):    
                        return ValueArray[lineIndex]   
                elif elementName.find('ListBox_') >= 0:   
                    return Control.get(lineIndex)

def AddLineText(uiName,elementName,text,lineIndex="end",textTag='',set_see=False): 
    PrintFunctionInfo(AddLineText,[uiName,elementName,text,lineIndex,textTag,set_see]) 
    #为Text控件或ListBox控件增加一行文字。参数1 :界面类名, 参数2:控件名称, 参数3:文字内容,参数4:目标行号,参数5:标记名称  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('Text_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if hasattr(Control,"GetEntry") == True:    
                    Control = Control.GetEntry()
                if type(lineIndex)==type(1):    
                    lineIndex = lineIndex + 1    
                    if textTag != '':    
                        Control.insert("%d.0"%lineIndex,text,textTag)
                    else:    
                        Control.insert("%d.0"%lineIndex,text)
                else:    
                    if textTag != '':    
                        Control.insert(lineIndex,text,textTag)
                    else:    
                        Control.insert(lineIndex,text)
                if set_see == True:    
                    Control.see(lineIndex)
            if elementName.find('ListBox_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if type(lineIndex)==type(1):    
                    if textTag != '' :    
                        Control.insert("%d"%lineIndex, text,textTag)
                    else:    
                        Control.insert("%d"%lineIndex, text)
                else:    
                    if textTag != '':    
                        Control.insert(lineIndex,text,textTag)
                    else:    
                        Control.insert(lineIndex,text)
                if set_see == True:    
                    Control.see(lineIndex)
def SetLineText(uiName,elementName,lineIndex=0,text=''):   
    PrintFunctionInfo(SetLineText,[uiName,elementName,lineIndex,text])  
    #增加当前Text和ListBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:行号。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            Control = G_UIElementDictionary[uiName][elementName]    
            if elementName.find('Text_') >= 0:  
                linestart = str("%s.0" % (lineIndex))
                lineend = str("%s.end" % (lineIndex))
                Control.delete(linestart, lineend)  
                Control.delete(linestart, text)  
            elif elementName.find('ListBox_') >= 0: 
                Control.delete(index)
                Control.insert(index, text)
def GetLineText(uiName,elementName,lineIndex=0):  
    PrintFunctionInfo(GetLineText,[uiName,elementName,lineIndex])  
    #增加当前Text和ListBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:行号。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            Control = G_UIElementDictionary[uiName][elementName]    
   
            if elementName.find('Text_') >= 0:  
                linestart = str("%s.0" % (lineIndex))
                lineend = str("%s.end" % (lineIndex))
                return Control.get(linestart, lineend).strip().replace('\n','')   
            elif elementName.find('ListBox_') >= 0: 
                return Control.get(lineIndex)

def AddPage(uiName,elementName,title="",iconFile="",importUI=''):  
    PrintFunctionInfo(AddPage,[uiName,elementName,title,iconFile,importUI])  
    #增加选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面标题,参数4:页面图标,参数5:目标界面或文件  
    NoteBook = GetElement(uiName,elementName)
    PageFrame = tkinter.Frame(NoteBook)
    PageFrame.place(relx = 0.0,rely = 0.0,relwidth = 1.0,relheight = 1.0)
    PageFrame.configure(bg='#888888')
    if len(iconFile) > 0 and os.path.exists(iconFile) == True:    
        if elementName not in G_UIElementIconDictionary[uiName]:    
            G_UIElementIconDictionary[uiName][elementName] = {}
        G_UIElementIconDictionary[uiName][elementName][title] = ImageTk.PhotoImage(file=iconFile) 
        NoteBook.add(PageFrame,text = title,image=G_UIElementIconDictionary[uiName][elementName][title],compound="left")
    else:    
        NoteBook.add(PageFrame,text = title)
    if importUI and len(importUI) > 0:    
        try:    
            uiClass = importUI    
            if importUI.find(".py") > 0:    
                UIPath, UIFile = os.path.split(importUI)
                if UIPath.find(":") < 0:    
                    UIPath = os.path.join(G_ExeDir,UIPath)
                import sys    
                sys.path.append(UIPath)
                uiClass, extension = os.path.splitext(UIFile)
            import importlib    
            from   importlib import import_module    
            importModule = importlib.import_module(uiClass)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:    
                importModule.Fun.G_ExeDir = G_ExeDir    
                importModule.Fun.G_ResDir = G_ResDir    
                if hasattr(importModule,"EXUIControl") == True:    
                    importModule.EXUIControl.G_ExeDir = G_ExeDir    
                    importModule.EXUIControl.G_ResDir = G_ResDir    
            if uiClass.find('Modules.') == 0:    
                LibNameArray =  uiClass.partition("Modules.")
                uiClass = LibNameArray[2]    
                newClass = getattr(importModule, uiClass)
            else:    
                newClass = getattr(importModule, uiClass)
            PageFrame.update()
            PageInstance = newClass(PageFrame,False)
            if elementName not in G_UILoadPageDictionary[uiName]:
                G_UILoadPageDictionary[uiName][elementName] = []
            G_UILoadPageDictionary[uiName][elementName].append(PageInstance)
        except Exception as ex:    
            MessageBox(str(ex))
def GetPage(uiName,elementName,index=0):  
    PrintFunctionInfo(GetPage,[uiName,elementName,index])  
    #取得指定页。参数1 :界面类名, 参数2:控件名称 ,参数3:索引值。  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):    
            return Pages[index]    
    return None    
def SelectPage(uiName,elementName,index=0):
    PrintFunctionInfo(SelectPage,[uiName,elementName,index])   
    #选中选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):    
            NoteBook.select(index)
def GetSelectedPageIndex(uiName,elementName):    
    PrintFunctionInfo(GetSelectedPageIndex,[uiName,elementName]) 
    #取得选中页索引  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        return NoteBook.index("current")
    return -1    
def GetPageText(uiName,elementName,index=0):  
    PrintFunctionInfo(GetPageText,[uiName,elementName,index]) 
    #取得指定页标题  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        return NoteBook.tab(index,"text")
    return -1    
def GetPageIndex(uiName,elementName,title):  
    PrintFunctionInfo(GetPageIndex,[uiName,elementName,title]) 
    #取得指定页索引  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        Tabs = NoteBook.tabs()
        for i in range(0,len(Tabs)):    
            tabTitle = NoteBook.tab(i,"text")
            if tabTitle == title:    
                return i    
    return -1    
def HidePage(uiName,elementName,index=0):    
    PrintFunctionInfo(HidePage,[uiName,elementName,index]) 
    #隐藏选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):    
            NoteBook.hide(index)
def DelPage(uiName,elementName,index=0):  
    PrintFunctionInfo(DelPage,[uiName,elementName,index]) 
    #删除选项页:参数1 :界面类名, 参数2:控件名称, 参数3:页面索引  
    NoteBook = GetElement(uiName,elementName)
    if NoteBook:    
        Pages = NoteBook.winfo_children()
        if index >= 0 and index < len(Pages):    
            NoteBook.forget(Pages[index])
            DestoryChild(Pages[index])

def AddPanedWindowPage(uiName,elementName='',WidthOrHeight=100):  
    PrintFunctionInfo(AddPanedWindowPage,[uiName,elementName,WidthOrHeight]) 
    #增加分割窗体页面  
    realElementName = elementName    
    if uiName in G_UIElementAliasDictionary:    
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            realElementName = G_UIElementAliasDictionary[uiName][elementName]    
        PanedWindow = GetElement(uiName,elementName)
        if PanedWindow:    
            PanedWindow_child = tkinter.Canvas(PanedWindow,bg="#888888")
            if PanedWindow.cget('orient') == tkinter.HORIZONTAL:    
                PanedWindow.add(PanedWindow_child,width = WidthOrHeight)
            else:    
                PanedWindow.add(PanedWindow_child,height = WidthOrHeight)
            Pages = PanedWindow.panes()
            PageCount = len(Pages)
            realChildName = str('%s_child%s'%(realElementName,PageCount+1))
            aliasChildName = str('%s_child%s'%(elementName,PageCount+1))
            Register(uiName,realChildName,PanedWindow_child,aliasChildName)
            return PanedWindow_child    
    return None    

def DelPanedWindowPage(uiName,elementName='',index=0):    
    PrintFunctionInfo(DelPanedWindowPage,[uiName,elementName,index]) 
    #删除分割窗体页面  
    PanedWindow = GetElement(uiName,elementName)
    if PanedWindow:    
        Pages = PanedWindow.panes()
        if index >= 0 and index < len(Pages):    
            PanedWindow.forget(Pages[index])
def AddTreeItem(uiName,elementName,parentItem="",insertItemPosition="end",itemName="",itemText="",itemValues=(),iconName="",tag=""):
    PrintFunctionInfo(AddTreeItem,[uiName,elementName,parentItem,insertItemPosition,itemName,itemText,itemValues,iconName,tag]) 
    #增加树项:参数1 :界面类名, 参数2:控件名称, 参数3:父结点,参数4:插入位置项文字,参数5:树项值,参数6:文字内容,参数7:图标文件,参数8:标记名称  
    Item = None    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                if iconName != "":    
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:    
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]    
                        Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                    else:    
                        ItemIcon = None    
                        if os.path.exists(iconName) == True:    
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:    
                            imagePath = iconName    
                            iconName_Lower = iconName.lower()
                            if iconName_Lower in G_ResourcesFileList:    
                                imagePath = G_ResourcesFileList[iconName_Lower]    
                            if os.path.exists(imagePath) == True:    
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:    
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,image=ItemIcon,tag=tag)
                            G_UIElementIconDictionary[uiName][elementName][Item] = ItemIcon    
                        else:    
                            Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
                else:    
                    Item = G_UIElementDictionary[uiName][elementName].insert(parentItem,insertItemPosition,itemName,text=itemText,values=itemValues,tag=tag)
    return Item    
def SetTreeItemText(uiName,elementName,itemName,itemText):   
    PrintFunctionInfo(SetTreeItemText,[uiName,elementName,itemName,itemText]) 
    #设置树项的文字  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                G_UIElementDictionary[uiName][elementName].item(itemName,text=itemText)
def GetTreeItemText(uiName,elementName,itemName):  
    PrintFunctionInfo(GetTreeItemText,[uiName,elementName,itemName]) 
    #取得树项的文字  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                item_text = G_UIElementDictionary[uiName][elementName].item(itemName,"text")
                return item_text    
    return None    
def SetTreeItemValues(uiName,elementName,itemName,itemValues): 
    PrintFunctionInfo(SetTreeItemValues,[uiName,elementName,itemName,itemValues])  
    #设置树项的值  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                G_UIElementDictionary[uiName][elementName].item(itemName,values=itemValues)
def GetTreeItemValues(uiName,elementName,itemName):    
    PrintFunctionInfo(GetTreeItemValues,[uiName,elementName,itemName])  
    #取得树项的值  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                item_value = G_UIElementDictionary[uiName][elementName].item(itemName,"values")
                return item_value    
    return None    
def SetTreeItemIcon(uiName,elementName,itemName,iconName=''):    
    PrintFunctionInfo(SetTreeItemIcon,[uiName,elementName,itemName,iconName])  
    #设置树项的图片  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                if iconName != "":    
                    if iconName in G_UIElementIconDictionary[uiName][elementName]:    
                        ItemIcon = G_UIElementIconDictionary[uiName][elementName][iconName]    
                        G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                        G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon    
                    else:    
                        ItemIcon = None    
                        if os.path.exists(iconName) == True:    
                            ItemIcon = ImageTk.PhotoImage(file = iconName)
                        else:    
                            imagePath = iconName    
                            iconName_Lower = iconName.lower()
                            if iconName_Lower in G_ResourcesFileList:    
                                imagePath = G_ResourcesFileList[iconName_Lower]    
                            if os.path.exists(imagePath) == True:    
                                ItemIcon = ImageTk.PhotoImage(file = imagePath)
                        if ItemIcon:    
                            G_UIElementDictionary[uiName][elementName].item(itemName,image=ItemIcon)
                            G_UIElementIconDictionary[uiName][elementName][itemName]=ItemIcon    
def ExpandTreeItem(uiName,elementName,itemName,expand=True): 
    PrintFunctionInfo(ExpandTreeItem,[uiName,elementName,itemName,expand])  
    #展开或收缩树项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                G_UIElementDictionary[uiName][elementName].item(itemName,open=expand)

def SetColumnList(uiName,elementName,columnList):   
    PrintFunctionInfo(SetColumnList,[uiName,elementName,columnList])  
    #设置列名称列表  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0 :    
                G_UIElementDictionary[uiName][elementName].configure(columns = columnList)
                for columnName in columnList:    
                    G_UIElementDictionary[uiName][elementName].column(columnName,anchor='center',width=100,stretch=True)
                    if elementName in G_ListViewCommandDictionary[uiName]:
                        eventFunc = G_ListViewCommandDictionary[uiName][elementName]
                        G_UIElementDictionary[uiName][elementName].heading(columnName,anchor='center',text=columnName,command=partial(ListViewHeadingFunction_Adaptor,fun=eventFunc,uiName=uiName,widgetName=elementName,columnname=columnName))
                    else:
                        G_UIElementDictionary[uiName][elementName].heading(columnName,anchor='center',text=columnName)

def SetColumnInfo(uiName,elementName,columnName='',anchor='center',width=100,stretch=True): 
    PrintFunctionInfo(SetColumnInfo,[uiName,elementName,columnName,anchor,width,stretch])  
    #设置各列信息  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0 :    
                columnList = G_UIElementDictionary[uiName][elementName].cget('columns')
                for columnName in columnList:    
                    G_UIElementDictionary[uiName][elementName].column(columnName,anchor=anchor,width=width,stretch=stretch)
                    if elementName in G_ListViewCommandDictionary[uiName]:
                        eventFunc = G_ListViewCommandDictionary[uiName][elementName]
                        G_UIElementDictionary[uiName][elementName].heading(columnName,anchor='center',text=columnName,command=partial(ListViewHeadingFunction_Adaptor,fun=eventFunc,uiName=uiName,widgetName=elementName,columnname=columnName))
                    else:
                        G_UIElementDictionary[uiName][elementName].heading(columnName,anchor=anchor,text=columnName)

def AddRowText(uiName,elementName,rowIndex ='end',values=(''),tag=''): 
    PrintFunctionInfo(AddRowText,[uiName,elementName,rowIndex,values,tag])  
    #为ListView插入一行  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                if rowIndex == '':    
                    rowIndex = 'end'    
                values_list = []    
                if isinstance(values,str) == True:    
                    values_list = values.split(',')
                else:    
                    values_list = list(values)
                for i in range(len(values_list)):    
                    if isinstance(values_list[i],bool) == True:    
                        if values_list[i] == True:    
                            values_list[i] = '☑'    
                        elif values_list[i] == False:    
                            values_list[i] = '☐'    
                ListView = G_UIElementDictionary[uiName][elementName]    
                currentRowIndex = len(ListView.get_children())
                if isinstance(rowIndex,int):    
                    currentRowIndex = rowIndex    
                if tag == '':    
                    tag = 'even'    
                    if currentRowIndex%2 == 0:    
                        tag = 'even'    
                    else:    
                        tag = 'odd'    
                G_UIElementDictionary[uiName][elementName].insert('',rowIndex, values=values_list,tag=tag)
                G_ListViewTagDictionary[uiName][elementName].append(tag)
                return currentRowIndex    
    return -1    
def AddMultiRowText(uiName,elementName,rowIndex ='end',rowValuesList=[],tagList=[]):  
    PrintFunctionInfo(AddMultiRowText,[uiName,elementName,rowIndex,rowValuesList,tagList])  
    #按列表填充ListView的多行数据    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                if rowIndex == '':    
                    rowIndex = 'end'    
                values_list = []    
                ListView = G_UIElementDictionary[uiName][elementName]    
                currentRowIndex = len(ListView.get_children())
                if isinstance(rowIndex,int):    
                    currentRowIndex = rowIndex    
                rowCount = len(rowValuesList)
                tagCount = len(tagList)
                for rowOffset in range(rowCount):    
                    rowValues = rowValuesList[rowOffset]    
                    if isinstance(rowValues,str) == True:    
                        values_list = rowValues.split(',')
                    else:    
                        values_list = list(rowValues)
                    for i in range(len(values_list)):    
                        if isinstance(values_list[i],bool) == True:    
                            if values_list[i] == True:    
                                values_list[i] = '☑'    
                            elif values_list[i] == False:    
                                values_list[i] = '☐'    
                    if rowOffset < tagCount:    
                        tag = tagList[rowOffset]    
                    else:    
                        tag = 'even'    
                        if (currentRowIndex + rowOffset)%2 == 0:    
                            tag = 'even'    
                        else:    
                            tag = 'odd'    
                    ListView.insert('',rowIndex, values=values_list,tag=tag)
                    G_ListViewTagDictionary[uiName][elementName].append(tag)
                return currentRowIndex    
    return -1    

def GetRowTextList(uiName,elementName,rowIndex):   
    PrintFunctionInfo(GetRowTextList,[uiName,elementName,rowIndex])  
    #取得ListView指定行的所有列文本  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                rowHandle = ListView.get_children()[rowIndex]    
                rowValues = list(ListView.item(rowHandle,"values"))
                for i in range(len(rowValues)):    
                    if rowValues[i] == '☑':    
                        rowValues[i] = True    
                    elif rowValues[i] == '☐':    
                        rowValues[i] = False    
                return rowValues    
    return None    

def GetColumnTextList(uiName,elementName,columnIndex):  
    PrintFunctionInfo(GetColumnTextList,[uiName,elementName,columnIndex])  
    #取得ListView指定列的所有行文本  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                RowList = ListView.get_children() 
                ColumnTextlist = []     
                for rowHandle in RowList:    
                    rowValues = ListView.item(rowHandle,"values")
                    columnText = rowValues[columnIndex]    
                    if columnText == '☑':    
                        ColumnTextlist.append(True)
                    elif columnText == '☐':    
                        ColumnTextlist.append(False)
                    else:    
                        ColumnTextlist.append(columnText)
                return ColumnTextlist    
    return None    
def GetAllRowTextList(uiName,elementName): 
    PrintFunctionInfo(GetAllRowTextList,[uiName,elementName])  
    #取得ListView所有行和列文本  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                allrowValues = []    
                for rowHandle in ListView.get_children():    
                    rowValues = list(ListView.item(rowHandle,"values"))
                    allrowValues.append(rowValues)
                return allrowValues    
    return None    
def GetCellText(uiName,elementName,rowIndex,columnIndex):   
    PrintFunctionInfo(GetCellText,[uiName,elementName,rowIndex,columnIndex])  
    #取得ListView指定单元格的文本  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                rowHandle = ListView.get_children()[rowIndex]
   
                rowValues = ListView.item(rowHandle,"values")
                if rowValues[columnIndex] == '☑':    
                    return True    
                elif rowValues[columnIndex] == '☐':    
                    return False    
                return rowValues[columnIndex]    

    return None    
def SetCellText(uiName,elementName,rowIndex,columnIndex,text):    
    PrintFunctionInfo(SetCellText,[uiName,elementName,rowIndex,columnIndex,text])  
    #设置ListView指定单元格文字  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]    
                G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value=text)
def SetCellCheckBox(uiName,elementName,rowIndex,columnIndex,selected=True):
    PrintFunctionInfo(SetCellCheckBox,[uiName,elementName,rowIndex,columnIndex,selected])  
    #设置ListView指定单元格复选框  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]    
                if selected == True:    
                    G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☑')
                else:    
                    G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☐')
def SetColumnCheckBox(uiName,elementName,beginRowIndex=0,endRowIndex=-1,columnIndex=0,selected=True): 
    PrintFunctionInfo(SetColumnCheckBox,[uiName,elementName,beginRowIndex,endRowIndex,columnIndex,selected])  
    #设置ListView指定行范围的单元格复选框  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                if endRowIndex == -1:    
                    endRowIndex = len(G_UIElementDictionary[uiName][elementName].get_children())
                rowHandleList = G_UIElementDictionary[uiName][elementName].get_children()[beginRowIndex:endRowIndex]    
                for rowHandle in rowHandleList:    
                    if selected == True:    
                        G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☑') 
                    else:    
                        G_UIElementDictionary[uiName][elementName].set(rowHandle,column=columnIndex,value='☐')
def GetCellBox(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(GetCellBox,[uiName,elementName,rowIndex,columnIndex])  
    #取得ListView指定单元格位置大小  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]
                RowItem = ListView.get_children()[rowIndex]    
                #取得对应行和列的位置和大小
                return ListView.bbox(RowItem,columnIndex)
    return None
def SetCellIcon(uiName,elementName,rowIndex,columnIndex,imageFile=''):
    PrintFunctionInfo(SetCellIcon,[uiName,elementName,rowIndex,columnIndex,imageFile])  
    #设置ListView指定单元格为文本标签  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]
                RowItem = ListView.get_children()[rowIndex]    
                inittext = ListView.item(RowItem)["values"][columnIndex] 
                #取得对应行和列的位置和大小
                CellBox = ListView.bbox(RowItem,columnIndex)
                #在这个位置创建一个输入框
                CellLabel = tkinter.Label(ListView)
                CellLabel.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                CellLabel.configure(text=inittext)
                CellLabel.configure(bg='#FFFFFF')
                image = None
                if isinstance(imageFile,str) == True:    
                    imageFile_Lower = imageFile.lower()
                    if os.path.exists(imageFile) == False:    
                        if imageFile_Lower in G_ResourcesFileList:    
                            imageFile = G_ResourcesFileList[imageFile_Lower]    
                        elif os.path.exists(imageFile) == False:
                            imageDir, imageFile = os.path.split(imageFile)
                            imageFile = os.path.join(G_ResDir,imageFile)
                    if os.path.exists(imageFile) == True:
                        image = Image.open(imageFile).convert('RGBA')
                elif isinstance(imageFile,Image.Image) == True:    
                    image = imageFile.convert('RGBA')
                PTImage = None
                if image:
                    PTImage =  ImageTk.PhotoImage(image)
                    CellLabel.configure(image = PTImage)
                    CellLabel.configure(compound='left')
                else:
                    CellLabel.configure(image = '')  
                CellLabelInfoList = GetUserData(uiName,elementName,'CellLabelInfo')
                if CellLabelInfoList:
                    CellLabelInfoList.append([rowIndex,columnIndex,CellLabel,PTImage])
                    SetUserData(uiName,elementName,'CellLabelInfo',CellLabelInfoList)
                else:
                    AddUserData(uiName,elementName,'CellLabelInfo','object',[[rowIndex,columnIndex,CellLabel,PTImage]],0)
                def on_column_width_change(event):
                    #取得当前光标类型
                    cursor_type = str(event.widget.cget("cursor"))
                    #如果是鼠标左键拖动，更新列宽
                    if cursor_type == "size_we":
                        col1 = event.widget.identify_column(event.x-10)
                        col2 = event.widget.identify_column(event.x+10)
                        col1Index = -1
                        if col1 != "":
                            col1Index = int(col1[1:]) - 1
                        col2Index = -1
                        if col2!= "":
                            col2Index = int(col2[1:]) - 1
                        if columnIndex == col1Index:
                            CellBox = ListView.bbox(RowItem,col1Index)
                            CellLabel.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                        elif columnIndex == col2Index:
                            CellBox = ListView.bbox(RowItem,col2Index)
                            CellLabel.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                ListView.bind("<B1-Motion>", on_column_width_change,add=True)

def CloseCellLabel(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(CloseCellLabel,[uiName,elementName,rowIndex,columnIndex])  
    #关闭ListView指定单元格本标签  
    CellLabelInfoList = GetUserData(uiName,elementName,'CellLabelInfo')
    if CellLabelInfoList:
        for CellLabelInfo in CellLabelInfoList:
            if CellLabelInfo[0] == rowIndex and CellLabelInfo[1] == columnIndex:
                CellLabelInfo[0].destroy()
                CellLabelInfo.remove(CellLabelInfo)
                break
        SetUserData(uiName,elementName,'CellLabelInfo',CellLabelInfoList)

def SetCellEntry(uiName,elementName,rowIndex,columnIndex,callback=None):
    PrintFunctionInfo(SetCellEntry,[uiName,elementName,rowIndex,columnIndex,callback])  
    #设置ListView指定单元格为输入框  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]
                RowItem = ListView.get_children()[rowIndex]    
                inittext = ListView.item(RowItem)["values"][columnIndex] 
                #取得对应行和列的位置和大小
                CellBox = ListView.bbox(RowItem,columnIndex)
                CellEntry_TextVariable = StringVar()
                CellEntry_TextVariable.set(inittext)
                #在这个位置创建一个输入框
                CellEntry = tkinter.Entry(ListView,textvariable=CellEntry_TextVariable)
                CellEntry.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                def InputEntry(event):
                    EntryText = CellEntry_TextVariable.get()
                    SetCellText(uiName,elementName,rowIndex,columnIndex,EntryText)
                    event.widget.destroy()
                    if callback:
                        callback(rowIndex,columnIndex,EntryText)
                CellEntry.bind('<Return>',InputEntry)
                CellEntryInfoList = GetUserData(uiName,elementName,'CellEntryInfo')
                if CellEntryInfoList:
                    CellEntryInfoList.append([rowIndex,columnIndex,CellEntry,CellEntry_TextVariable])
                    SetUserData(uiName,elementName,'CellEntryInfo',CellEntryInfoList)
                else:
                    AddUserData(uiName,elementName,'CellEntryInfo','object',[[rowIndex,columnIndex,CellEntry,CellEntry_TextVariable]],0)
                def on_column_width_change(event):
                    #取得当前光标类型
                    cursor_type = str(event.widget.cget("cursor"))
                    #如果是鼠标左键拖动，更新列宽
                    if cursor_type == "size_we":
                        col1 = event.widget.identify_column(event.x-10)
                        col2 = event.widget.identify_column(event.x+10)
                        col1Index = -1
                        if col1 != "":
                            col1Index = int(col1[1:]) - 1
                        col2Index = -1
                        if col2!= "":
                            col2Index = int(col2[1:]) - 1
                        if columnIndex == col1Index:
                            CellBox = ListView.bbox(RowItem,col1Index)
                            CellEntry.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                        elif columnIndex == col2Index:
                            CellBox = ListView.bbox(RowItem,col2Index)
                            CellEntry.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                ListView.bind("<B1-Motion>", on_column_width_change,add=True)

def GetCellEntry(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(GetCellEntry,[uiName,elementName,rowIndex,columnIndex])  
    #取得ListView指定单元格输入框  
    CellEntryInfoList = GetUserData(uiName,elementName,'CellEntryInfo')
    if CellEntryInfoList:
        for CellEntryInfo in CellEntryInfoList:
            if CellEntryInfo[0] == rowIndex and CellEntryInfo[1] == columnIndex:
                return CellEntryInfo[0]
    return None

def GetCellEntryText(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(GetCellEntryText,[uiName,elementName,rowIndex,columnIndex])  
    #取得ListView指定单元格输入框的文本  
    CellEntryInfoList = GetUserData(uiName,elementName,'CellEntryInfo')
    if CellEntryInfoList:
        for CellEntryInfo in CellEntryInfoList:
            if CellEntryInfo[0] == rowIndex and CellEntryInfo[1] == columnIndex:
                return CellEntryInfo[1].get()
    return None

def CloseCellEntry(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(CloseCellEntry,[uiName,elementName,rowIndex,columnIndex])  
    #关闭ListView指定单元格输入框  
    CellEntryInfoList = GetUserData(uiName,elementName,'CellEntryInfo')
    if CellEntryInfoList:
        for CellEntryInfo in CellEntryInfoList:
            if CellEntryInfo[0] == rowIndex and CellEntryInfo[1] == columnIndex:
                CellEntryInfo[0].destroy()
                CellEntryInfoList.remove(CellEntryInfo)
                break
        SetUserData(uiName,elementName,'CellEntryInfo',CellEntryInfoList)

def SetCellComboBox(uiName,elementName,rowIndex,columnIndex,initList=[],callback=None):
    #设置ListView指定单元格为下拉框  
    PrintFunctionInfo(SetCellComboBox,[uiName,elementName,rowIndex,columnIndex,initList,callback])
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]
                RowItem = ListView.get_children()[rowIndex]  
                inittext = ListView.item(RowItem)["values"][columnIndex] 
                #取得对应行和列的位置和大小
                CellBox = ListView.bbox(RowItem,columnIndex)
                CellComboBox_TextVariable = StringVar()
                CellComboBox_TextVariable.set(inittext)
                #在这个位置创建一个输入框
                CellComboBox = tkinter.ttk.Combobox(ListView,textvariable=CellComboBox_TextVariable, state="readonly")
                CellComboBox.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                CellComboBox['values'] = initList
                def SelectedCellComboBox(event):
                    ComboBoxText = event.widget.get()
                    SetCellText(uiName,elementName,rowIndex,columnIndex,ComboBoxText)
                    event.widget.destroy()
                    if callback:
                        callback(rowIndex,columnIndex,ComboBoxText)
                CellComboBox.bind("<<ComboboxSelected>>",SelectedCellComboBox)
                CellComboBoxInfoList = GetUserData(uiName,elementName,'CellComboBoxInfo')
                if CellComboBoxInfoList:
                    CellComboBoxInfoList.append([rowIndex,columnIndex,CellComboBox,CellComboBox_TextVariable])
                    SetUserData(uiName,elementName,'CellComboBoxInfo',CellComboBoxInfoList)
                else:
                    AddUserData(uiName,elementName,'CellComboBoxInfo','object',[[rowIndex,columnIndex,CellComboBox,CellComboBox_TextVariable]],0)
                def on_column_width_change(event):
                    #取得当前光标类型
                    cursor_type = str(event.widget.cget("cursor"))
                    #如果是鼠标左键拖动，更新列宽
                    if cursor_type == "size_we":
                        col1 = event.widget.identify_column(event.x-10)
                        col2 = event.widget.identify_column(event.x+10)
                        col1Index = -1
                        if col1 != "":
                            col1Index = int(col1[1:]) - 1
                        col2Index = -1
                        if col2!= "":
                            col2Index = int(col2[1:]) - 1
                        if columnIndex == col1Index:
                            CellBox = ListView.bbox(RowItem,col1Index)
                            CellComboBox.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                        elif columnIndex == col2Index:
                            CellBox = ListView.bbox(RowItem,col2Index)
                            CellComboBox.place(x=CellBox[0],y=CellBox[1],width=CellBox[2],height=CellBox[3])
                ListView.bind("<B1-Motion>", on_column_width_change,add=True)

def GetCellComboBox(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(GetCellComboBox,[uiName,elementName,rowIndex,columnIndex])
    #取得ListView指定单元格下拉列表框  
    CellComboBoxInfoList = GetUserData(uiName,elementName,'CellComboBoxInfo')
    if CellComboBoxInfoList:
        for CellComboBoxInfo in CellComboBoxInfoList:
            if CellComboBoxInfo[0] == rowIndex and CellComboBoxInfo[1] == columnIndex:
                return CellComboBoxInfo[0]
    return None

def GetCellComboBoxValue(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(GetCellComboBoxValue,[uiName,elementName,rowIndex,columnIndex])
    #取得ListView指定单元格下拉列表框的文本  
    CellComboBoxInfoList = GetUserData(uiName,elementName,'CellComboBoxInfo')
    if CellComboBoxInfoList:
        for CellComboBoxInfo in CellComboBoxInfoList:
            if CellComboBoxInfo[0] == rowIndex and CellComboBoxInfo[1] == columnIndex:
                return CellComboBoxInfo[1].get()
    return None

def CloseCellComboBox(uiName,elementName,rowIndex,columnIndex):
    PrintFunctionInfo(CloseCellComboBox,[uiName,elementName,rowIndex,columnIndex])
    #关闭ListView指定单元格下拉列表框  
    CellComboBoxInfoList = GetUserData(uiName,elementName,'CellComboBoxInfo')
    if CellComboBoxInfoList:
        for CellComboBoxInfo in CellComboBoxInfoList:
            if CellComboBoxInfo[0] == rowIndex and CellComboBoxInfo[1] == columnIndex:
                CellComboBoxInfo[0].destroy()
                CellComboBoxInfoList.remove(CellComboBoxInfo)
                break
        SetUserData(uiName,elementName,'CellComboBoxInfo',CellComboBoxInfoList)

def DeleteRow(uiName,elementName,rowIndex):   
    PrintFunctionInfo(DeleteRow,[uiName,elementName,rowIndex])  
    #删除ListView指定行  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                rowHandle = G_UIElementDictionary[uiName][elementName].get_children()[rowIndex]    
                G_UIElementDictionary[uiName][elementName].delete(rowHandle)

    CellLabelInfoList = GetUserData(uiName,elementName,'CellLabelInfo')
    if CellLabelInfoList:
        for CellLabelInfo in CellLabelInfoList:
            if CellLabelInfo[0] == rowIndex :
                CellLabelInfo[0].destroy()
                CellLabelInfo.remove(CellLabelInfo)
                break
        SetUserData(uiName,elementName,'CellLabelInfo',CellLabelInfoList)

    CellEntryInfoList = GetUserData(uiName,elementName,'CellEntryInfo')
    if CellEntryInfoList:
        for CellEntryInfo in CellEntryInfoList:
            if CellEntryInfo[0] == rowIndex :
                CellEntryInfo[0].destroy()
                CellEntryInfoList.remove(CellEntryInfo)
                break
        SetUserData(uiName,elementName,'CellEntryInfo',CellEntryInfoList)

    CellComboBoxInfoList = GetUserData(uiName,elementName,'CellComboBoxInfo')
    if CellComboBoxInfoList:
        for CellComboBoxInfo in CellComboBoxInfoList:
            if CellComboBoxInfo[0] == rowIndex:
                CellComboBoxInfo[0].destroy()
                CellComboBoxInfoList.remove(CellComboBoxInfo)
        SetUserData(uiName,elementName,'CellComboBoxInfo',CellComboBoxInfoList)

def DeleteAllRows(uiName,elementName): 
    PrintFunctionInfo(DeleteAllRows,[uiName,elementName])  
    #清空ListView所有行  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]
                DelUserData(uiName,elementName,'CellLabelInfo')
                DelUserData(uiName,elementName,'CellEntryInfo')
                DelUserData(uiName,elementName,'CellComboBoxInfo')
              
                RootChildren = ListView.get_children()
                ListView.delete(*RootChildren)
  
def CheckPickedRow(uiName,elementName,x,y): 
    PrintFunctionInfo(CheckPickedRow,[uiName,elementName,x,y])  
    #取得鼠标位置ListView的行号  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:    
                    RootChildren = ListView.get_children()
                    return RootChildren.index(PickedItem)
    return None    
def CheckPickedCell(uiName,elementName,x,y):  
    PrintFunctionInfo(CheckPickedCell,[uiName,elementName,x,y])  
    #取得鼠标位置ListView的单元格  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                PickedItem = ListView.identify("item",x,y)
                if PickedItem:    
                    row = ListView.index(PickedItem)
                    column = ListView.identify_column(x)
                    column = column.replace("#","")
                    column = int(column) - 1    
                    return (row,column)
    return (-1,-1)
def OnListViewCellClicked(event,uiName,widgetName,callbackFunc):  
    PrintFunctionInfo(OnListViewCellClicked,[event,uiName,widgetName,callbackFunc])  
    #点击单元格   
    elementName = widgetName    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                PickedItem = ListView.identify("item",event.x,event.y)
                if PickedItem:    
                    rowIndex = ListView.index(PickedItem)
                    rowHandle = ListView.get_children()[rowIndex]    
                    rowValues = ListView.item(rowHandle,"values")
                    column = ListView.identify_column(event.x)
                    column = column.replace("#","")
                    columnIndex = int(column) - 1    
                    if rowValues[columnIndex] == '☑':    
                        ListView.set(rowHandle,column=columnIndex,value='☐')
                    elif rowValues[columnIndex] == '☐':    
                        ListView.set(rowHandle,column=columnIndex,value='☑')
                    CellEntryInfo = GetUserData(uiName,widgetName,'CellEntryInfo')
                    if CellEntryInfo:
                        CellEntryInfo[0].destroy()
                        DelUserData(uiName,widgetName,'CellEntryInfo')
                    CellComboBoxInfo = GetUserData(uiName,widgetName,'CellComboBoxInfo')
                    if CellComboBoxInfo:
                        CellComboBoxInfo[0].destroy()
                        DelUserData(uiName,widgetName,'CellComboBoxInfo')
                    if callbackFunc:    
                        callbackFunc(uiName,widgetName,rowIndex,columnIndex)

def OnListViewCellDoubleClicked(event,uiName,widgetName,callbackFunc):  
    PrintFunctionInfo(OnListViewCellDoubleClicked,[event,uiName,widgetName,callbackFunc])  
    #双击单元格   
    elementName = widgetName    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                PickedItem = ListView.identify("item",event.x,event.y)
                if PickedItem:    
                    rowIndex = ListView.index(PickedItem)
                    rowHandle = ListView.get_children()[rowIndex]    
                    rowValues = ListView.item(rowHandle,"values")
                    column = ListView.identify_column(event.x)
                    column = column.replace("#","")
                    columnIndex = int(column) - 1    
                    if callbackFunc:    
                        callbackFunc(uiName,widgetName,rowIndex,columnIndex)
def SelectRow(uiName,elementName,beginRowIndex=0,endRowIndex=None):
    PrintFunctionInfo(SelectRow,[uiName,elementName,beginRowIndex,endRowIndex])  
    #选中ListView指定行  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                RootChildren = ListView.get_children()
                RowCount = len(RootChildren)
                if beginRowIndex >= 0 or beginRowIndex < RowCount:    
                    select = []    
                    if endRowIndex is None:    
                        endRowIndex = beginRowIndex 
                    elif endRowIndex < 0:    
                        endRowIndex = RowCount + endRowIndex  
                    for index in range(beginRowIndex,endRowIndex+1):    
                        select.append(RootChildren[index])
                    ListView.selection_set(select)
def GetSelectedRowIndex(uiName,elementName):  
    PrintFunctionInfo(GetSelectedRowIndex,[uiName,elementName])  
    #取得ListView选中行的行索引  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                selectionList = ListView.selection()
                if selectionList and len(selectionList) > 0:    
                    if len(selectionList) == 1:    
                        rowHandle = selectionList[0]    
                        rowIndex = ListView.index(rowHandle)
                        return rowIndex    
                    else:    
                        rowIndexList = []    
                        for rowHandle in selectionList:    
                            rowIndex = ListView.index(rowHandle)
                            rowIndexList.append(rowIndex)
                        return rowIndexList    
    return -1    
def SortLineByColumn(uiName,elementName,columnIndex=0,reverse = False):    
    PrintFunctionInfo(SortLineByColumn,[uiName,elementName,columnIndex,reverse])  
    #设置ListView按指定列排序  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                AllLineValues = []    
                RootChildren = ListView.get_children()
                for Item in RootChildren:    
                    itemInfo = ListView.item(Item)
                    AllLineValues.append(itemInfo["values"])
                    AllLineValues.sort(key=lambda x:str(x[columnIndex]),reverse=reverse)
                for Item in RootChildren:    
                    ListView.delete(Item)
                for line in AllLineValues:    
                    itemHandle = ListView.insert("",0,text=line[0],values=line)
def SetRowStyle(uiName,elementName,rowIndex='even',bgColor='lightblue',fgColor='#000000',textFont=None): 
    PrintFunctionInfo(SetRowStyle,[uiName,elementName,rowIndex,bgColor,fgColor,textFont])   
    #设置ListView的行样式  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                if rowIndex == 'even':    
                    if textFont:    
                        ListView.tag_configure('even', background=bgColor,font=textFont,foreground=fgColor)
                    else:    
                        ListView.tag_configure('even', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    row = 0    
                    rowTag = 'even'    
                    for Item in RootChildren:    
                        if row/2 != int(row/2):    
                            rowTag = 'even'    
                        else:    
                            rowTag = 'odd'    
                        ListView.item(Item,tag=rowTag)
                        row = row + 1    
                elif rowIndex == 'odd':    
                    if textFont:    
                        ListView.tag_configure('odd', background=bgColor,font=textFont,foreground=fgColor)
                    else:    
                        ListView.tag_configure('odd', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    row = 0    
                    rowTag = 'even'    
                    for Item in RootChildren:    
                        if row/2 != int(row/2):    
                            rowTag = 'even'    
                        else:    
                            rowTag = 'odd'    
                        ListView.item(Item,tag=rowTag)
                        row = row + 1    
                elif rowIndex == 'all':    
                    if textFont:    
                        ListView.tag_configure('all', background=bgColor,font=textFont,foreground=fgColor)
                    else:    
                        ListView.tag_configure('all', background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    rowTag = 'all'    
                    for Item in RootChildren:    
                        ListView.item(Item,tag=rowTag)
                elif rowIndex == 'hover':    
                    if textFont:    
                        ListView.tag_configure('hover', background=bgColor,font=textFont,foreground=fgColor)
                    else:    
                        ListView.tag_configure('hover', background=bgColor,foreground=fgColor)
                    AddUserData(uiName,elementName,'HoverItem','list',[None,None,bgColor],0)
                else:    
                    if textFont:    
                        ListView.tag_configure(str('row_%d'%rowIndex), background=bgColor,font=textFont,foreground=fgColor)
                    else:    
                        ListView.tag_configure(str('row_%d'%rowIndex), background=bgColor,foreground=fgColor)
                    RootChildren = ListView.get_children()
                    Item = RootChildren[rowIndex]    
                    ListView.item(Item,tag=str('row_%d'%rowIndex))
def SetRowBGColor(uiName,elementName,rowIndex='even',bgColor='lightblue'): 
    #设置ListView的行背景色  
    SetRowStyle(uiName,elementName,rowIndex=rowIndex,bgColor=bgColor,fgColor='#000000',textFont=None)

def OnListViewRowMouseMotion(event,uiName,widgetName): 
    PrintFunctionInfo(OnListViewRowMouseMotion,[event,uiName,widgetName])  
    #设置ListView的当前鼠标悬停背景色  
    elementName = widgetName    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListView_') >= 0:    
                ListView = G_UIElementDictionary[uiName][elementName]    
                PickedItem = ListView.identify("item",event.x,event.y)
                if PickedItem:    
                    RootChildren = ListView.get_children()
                    RowIndex =  RootChildren.index(PickedItem)
                    if RowIndex >= 0:    
                        HoverItem = GetUserData(uiName,elementName,"HoverItem")
                        if HoverItem:    
                            LastItem = HoverItem[0]    
                            LastItemTag = HoverItem[1]    
                            LastItemBG = HoverItem[2]    
                            if LastItem:    
                                ListView.item(LastItem,tag=LastItemTag)
                            RootChildren = ListView.get_children()
                            NewItem = RootChildren[RowIndex]    
                            NewItemTag = ListView.item(NewItem,'tag')
                            ListView.item(NewItem,tag=str('hover'))
                            if HoverItem:    
                                SetUserData(uiName,elementName,'HoverItem',[NewItem,NewItemTag,LastItemBG])
                            else:    
                                AddUserData(uiName,elementName,'HoverItem','list',[NewItem,NewItemTag,LastItemBG],0)
 
def CheckPickedTreeItem(uiName,elementName,x,y):   
    PrintFunctionInfo(CheckPickedTreeItem,[uiName,elementName,x,y])  
    #判断当前点击的树结点项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                return G_UIElementDictionary[uiName][elementName].identify("item",x,y)
    return None    
def CheckClickedTreeItem(uiName,elementName,x,y):   
    PrintFunctionInfo(CheckClickedTreeItem,[uiName,elementName,x,y])  
    #判断当前点击的树结点项  
    return CheckPickedTreeItem(uiName,elementName,x,y)
def SelectTreeItem(uiName,elementName,itemName):   
    PrintFunctionInfo(SelectTreeItem,[uiName,elementName,itemName]) 
    #选中对应树结点项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary and itemName:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                G_UIElementDictionary[uiName][elementName].selection_set(itemName)
def GetSelectedTreeItem(uiName,elementName):   
    PrintFunctionInfo(GetSelectedTreeItem,[uiName,elementName]) 
    #取得选中项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                return G_UIElementDictionary[uiName][elementName].selection()
    return None    
def UnSelecteTreeItem(uiName,elementName): 
    PrintFunctionInfo(UnSelecteTreeItem,[uiName,elementName]) 
    #取消选中项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                selected_item = G_UIElementDictionary[uiName][elementName].selection()
                if selected_item:    
                    G_UIElementDictionary[uiName][elementName].selection_remove(selected_item)
 
def MoveTreeItem(uiName,elementName,itemName,parentItemName="",insertPosition="end"):
    PrintFunctionInfo(MoveTreeItem,[uiName,elementName,itemName,parentItemName,insertPosition]) 
    #移动树结点项的位置   
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0 and len(itemName) > 0:    
                G_UIElementDictionary[uiName][elementName].move(itemName,parentItemName,insertPosition)
 
def DelItemText(uiName,elementName,lineIndexOrText): 
    PrintFunctionInfo(DelItemText,[uiName,elementName,lineIndexOrText]) 
    #删除当前ListBox和ComboBox的文字项内容。参数1 :界面类名, 参数2:控件名称 ,参数3:文本内容。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ComboBox_') >= 0:    
                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                if type(lineIndexOrText)==type(1):    
                    ValueArray.pop(lineIndexOrText)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray    
                else:    
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:    
                        ValueArray.pop(ValueIndex)
                    G_UIElementDictionary[uiName][elementName]['value'] = ValueArray    
            elif elementName.find('ListBox_') >= 0:    
                if type(lineIndexOrText)==type(1):    
                    G_UIElementDictionary[uiName][elementName].delete(lineIndexOrText)
                else:    
                    ValueArray = G_UIElementDictionary[uiName][elementName].get(0,tkinter.END)
                    ValueIndex = ValueArray.index(lineIndexOrText)
                    if ValueIndex >= 0:    
                        G_UIElementDictionary[uiName][elementName].delete(ValueIndex)
def DelLineText(uiName,elementName,lineIndex="end"):   
    PrintFunctionInfo(DelLineText,[uiName,elementName,lineIndex]) 
    #删除Text控件或ListBox控件的指定行文字。参数1 :界面类名, 参数2:控件名称, 参数3:行数  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('Text_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if hasattr(Control,"GetEntry") == True:    
                    Control = Control.GetEntry()
                if type(lineIndex)==type(1):    
                    lineIndex = lineIndex + 1    
                    beginIndex = str("%d.0"%lineIndex)
                    endIndex = str("%d.0"%(lineIndex+1))
                    Control.delete(beginIndex,endIndex)
                else:    
                    beginIndex = str("%s.0"%lineIndex)
                    endIndex = str("%s.end"%lineIndex)
                    Control.delete(beginIndex,endIndex)
            elif elementName.find('ListBox_') >= 0:    
                G_UIElementDictionary[uiName][elementName].delete("%s"%lineIndex)   
            elif elementName.find('ComboBox_') >= 0:    
                ValueArray = list(G_UIElementDictionary[uiName][elementName]['value'])
                ValueArray.pop(lineIndexOrText)
                G_UIElementDictionary[uiName][elementName]['value'] = ValueArray    

def DelTreeItem(uiName,elementName,itemName):   
    PrintFunctionInfo(DelTreeItem,[uiName,elementName,itemName]) 
    #删除树项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary and itemName:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                G_UIElementDictionary[uiName][elementName].delete(itemName)

def Clear(uiName,elementName):
    PrintFunctionInfo(Clear,[uiName,elementName]) 
    #清空控件  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListBox_') >= 0:    
                G_UIElementDictionary[uiName][elementName].delete(0,tkinter.END)
            elif elementName.find('Text_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if hasattr(Control,"GetEntry") == True:    
                    Control = Control.GetEntry()
                Control.delete('0.0',tkinter.END)   
            elif elementName.find('TreeView_') >= 0:    
                TreeView = G_UIElementDictionary[uiName][elementName]    
                RootChildren = TreeView.get_children()
                for Item in RootChildren:    
                    TreeView.delete(Item)  
            elif elementName.find('ComboBox_') >= 0:    
                G_UIElementDictionary[uiName][elementName]['value'] = []

def DelAllTreeItem(uiName,elementName):  
    PrintFunctionInfo(DelAllTreeItem,[uiName,elementName]) 
    #删除所有的树结点项  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('TreeView_') >= 0:    
                TreeView = G_UIElementDictionary[uiName][elementName]    
                RootChildren = TreeView.get_children()
                for Item in RootChildren:    
                    TreeView.delete(Item)
def DelAllLines(uiName,elementName):  
    PrintFunctionInfo(DelAllLines,[uiName,elementName]) 
    #清空Text控件或ListBox控件的文字内容。参数1 :界面类名, 参数2:控件名称。  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ListBox_') >= 0:    
                G_UIElementDictionary[uiName][elementName].delete(0,tkinter.END)
            elif elementName.find('Text_') >= 0:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if hasattr(Control,"GetEntry") == True:    
                    Control = Control.GetEntry()
                Control.delete('0.0',tkinter.END)
def DelAllItemText(uiName,elementName):
    PrintFunctionInfo(DelAllItemText,[uiName,elementName]) 
    #删除ComboBox控件的所有行文字  
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]    
    if uiName in G_UIElementDictionary:    
        if elementName in G_UIElementDictionary[uiName]:    
            if elementName.find('ComboBox_') >= 0:    
                G_UIElementDictionary[uiName][elementName]['value'] = []
   
def GetSelectText(uiName,elementName): 
    PrintFunctionInfo(GetSelectText,[uiName,elementName]) 
    #取得Text控件的选中文字  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Text_') >= 0 :     
            if hasattr(Control,"GetEntry") == True:    
                Control = Control.GetEntry()
            return Control.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None    
   
def DelSelectText(uiName,elementName):   
    PrintFunctionInfo(DelSelectText,[uiName,elementName]) 
    #删除Text控件的选中文字  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Text_') >= 0 :    
            if hasattr(Control,"GetEntry") == True:    
                Control = Control.GetEntry()
            return Control.delete(tkinter.SEL_FIRST,tkinter.SEL_LAST)
    return None    
 
def GetValueList(uiName,elementName):   
    PrintFunctionInfo(GetValueList,[uiName,elementName])  
    #取得当前ListBox、ComboBox和SpinBox等控件值列表的函数  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('ComboBox_') >= 0 :     
            return Control["values"]    
        elif elementName.find('ListBox_') >= 0 :    
            listValueList = Control.get(0,tkinter.END)   
            return listValueList       
        elif elementName.find('SpinBox_') >= 0 :     
            return Control["values"]    
    return None    
def GetSelectedValueList(uiName,elementName): 
    PrintFunctionInfo(GetSelectedValueList,[uiName,elementName])  
    #取得当前ListBo控件选中项的值列表  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('ListBox_') >= 0 :    
            selectedIndexList = Control.curselection()   
            selectedValueList = []       
            for index in selectedIndexList:       
                itemText = Control.get(index)   
                selectedValueList.append(itemText)   
            return selectedValueList       
    return None
 
def SetValueList(uiName,elementName,valueList):  
    PrintFunctionInfo(SetValueList,[uiName,elementName,valueList]) 
    #设置当前ListBox、ComboBox和SpinBox等控件值列表的函数  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('ComboBox_') >= 0 :     
            Control["values"] = valueList    
        elif elementName.find('ListBox_') >= 0 :    
            Control.delete(0,tkinter.END)   
            for value in valueList:       
                Control.insert(tkinter.END,value)   
        elif elementName.find('SpinBox_') >= 0 :     
            Control["values"] = valueList    
 
def OnListBoxSelect(event,uiName,widgetName):   
    PrintFunctionInfo(OnListBoxSelect,[event,uiName,widgetName]) 
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index < 0:    
        if widgetName in  G_UIElementVariableArray[uiName]:     
            ListBox_Index = G_UIElementVariableArray[uiName][widgetName].get()
            SetCurrentIndex(uiName,widgetName,ListBox_Index)
def OnListBoxFocusOut(event,uiName,widgetName):  
    PrintFunctionInfo(OnListBoxFocusOut,[event,uiName,widgetName]) 
    ListBox_Index = GetCurrentIndex(uiName,widgetName)
    if ListBox_Index >= 0:    
        G_UIElementVariableArray[uiName][widgetName].set(ListBox_Index)
def GetCurrentValue(uiName,elementName): 
    PrintFunctionInfo(GetCurrentValue,[uiName,elementName]) 
    #取得控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('RadioButton_') >= 0 :     
            return GetTKVariable(uiName,elementName)
        elif elementName.find('CheckButton_') >= 0 :     
            return GetTKVariable(uiName,elementName)
        elif elementName.find('ComboBox_') >= 0 :     
            return Control.get()
        elif elementName.find('Scale_') >= 0 :     
            return Control.get()
        elif elementName.find('SpinBox_') >= 0 :     
            return Control.get()
        elif elementName.find('SwitchButton_') >= 0 :     
            return Control.GetCurrValue()
        elif elementName.find('ProgressDial_') >= 0 :     
            return Control.GetCurrValue()
        elif elementName.find('Slider_') >= 0 :     
            return Control.GetCurrValue()
        elif elementName.find('ListBox_') >= 0 :    
            currIndex = Control.curselection()   
            if len(currIndex) > 0 and currIndex[0] >= 0:       
                return Control.get(currIndex[0])   
        elif elementName.find('Progress_') >= 0 :     
            return Control["value"]    
        elif elementName.find('Navigation_') >= 0 :     
            return Control.GetCurrentItemValue()
    return -1    
def GetCurrentIndex(uiName,elementName):   
    PrintFunctionInfo(GetCurrentIndex,[uiName,elementName]) 
    #取得ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('ComboBox_') >= 0 :     
            return Control.current()
        elif elementName.find('ListBox_') >= 0 :    
            currIndex = Control.curselection()   
            if len(currIndex) > 0 and currIndex[0] >= 0:       
                return currIndex[0]       
        if elementName.find('Navigation_') >= 0 :     
            return Control.GetCurrentIndex()
    return -1    

      
def SetCurrentValue(uiName,elementName,value):    
    PrintFunctionInfo(SetCurrentValue,[uiName,elementName,value]) 
    #设置控件的选中值(RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton)  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('RadioButton_') >= 0 :     
            SetTKVariable(uiName,elementName,value)
        if elementName in G_UIGroupDictionary[uiName]:     
            GroupName = G_UIGroupDictionary[uiName][elementName]    
            if GroupName.find("Group_") == 0:    
                GroupText = GroupName[6:]     
                GroupID = int(GroupText) 
                OnRadioButtonClick1(uiName,elementName,GroupID,value,True) 
        elif elementName.find('CheckButton_') >= 0 :     
            event = ChartEvent(0,0,Control)
            if value != GetCurrentValue(uiName,elementName):    
                OnCheckButtonClick1(event,uiName,elementName)
            SetTKVariable(uiName,elementName,value)
        elif elementName.find('ComboBox_') >= 0 :     
            Control.set(value)
        elif elementName.find('Scale_') >= 0 :     
            Control.set(value)
        elif elementName.find('SpinBox_') >= 0 :     
            SetTKVariable(uiName,elementName,value)
        elif elementName.find('SwitchButton_') >= 0 :     
            Control.SetCurrValue(value)
        elif elementName.find('Slider_') >= 0 :     
            Control.SetCurrValue(value)
        elif elementName.find('Slider_') >= 0 :     
            Control.SetCurrValue(value)
        elif elementName.find('ProgressDial_') >= 0 :     
            Control.SetCurrValue(value)
        elif elementName.find('ListBox_') >= 0 :    
            Control.selection_clear(0,tkinter.END)  
            itemCount = Control.size()  
            for itemIndex in range(0,itemCount):       
                itemText = Control.get(itemIndex)   
                if itemText == value:       
                    Control.select_set(itemIndex)   
                    break       
        elif elementName.find('Progress_') >= 0 :     
            Control["value"] = value     
def SetCurrentIndex(uiName,elementName,index): 
    PrintFunctionInfo(SetCurrentIndex,[uiName,elementName,index]) 
    #设置ListBox、ComboBox、Navigation的选中索引值。参数1 :界面类名, 参数2:控件名称,参数3:索引值。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('ComboBox_') >= 0 :     
            Control.current(index)
        elif elementName.find('ListBox_') >= 0 :    
            Control.selection_clear(0,tkinter.END)   
            Control.selection_set(index)   
        elif elementName.find('Navigation_') >= 0 :    
            Control.SetCurrentIndex(index)
   
def SetScale(uiName,elementName,minimum,maximum,tickinterval):  
    PrintFunctionInfo(SetScale,[uiName,elementName,minimum,maximum,tickinterval]) 
    #设置Scale.参数1 :界面类名, 参数2:控件名称,参数3:最小值,参数4:最大值,参数5:刻度间隔。   
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Scale_') >= 0 :     
            Control.configure(from_=minimum) 
            Control.configure(to=maximum) 
            Control.configure(tickinterval=tickinterval) 
def SetSlider(uiName,elementName,minimum,maximum,value=0):
    PrintFunctionInfo(SetSlider,[uiName,elementName,minimum,maximum,value]) 
    #设置Slider.参数1 :界面类名, 参数2:控件名称,参数3:最小值,参数4:最大值,参数5:当前值。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find('Slider_') >= 0 :     
            Control.SetMinValue(minimum) 
            Control.SetMaxValue(maximum) 
            Control.SetCurrValue(value)
 
def SetProgress(uiName,elementName,maximum,value=0): 
    PrintFunctionInfo(SetProgress,[uiName,elementName,maximum,value]) 
    #设置进度条Progress:参数1 :界面类名, 参数2:控件名称, 参数3:最大值 参数4: 当前值 。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if elementName.find("ProgressDial_") >= 0:    
            Control.SetMaxValue(maximum)
            Control.GetCurrValue(value)
        elif elementName.find("Progress_") >= 0:    
            Control.configure(maximum=maximum) 
            Control.configure(value=value) 
 
def MovingChildPageXViewOffset(uiName,elementName,step=1):  
    PrintFunctionInfo(MovingChildPageXViewOffset,[uiName,elementName,step]) 
    #面板内视野横向移动指定步长:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块移动步长值  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        elementName = elementName + "_Child"    
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:     
            ChildPage.xview("scroll",step,"units")
def MovingChildPageYViewOffset(uiName,elementName,step=1):  
    PrintFunctionInfo(MovingChildPageYViewOffset,[uiName,elementName,step]) 
    #面板内视野纵向移动指定步长:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块移动步长值  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        elementName = elementName + "_Child"    
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:     
            ChildPage.yview("scroll",step,"units")
def MovingChildPageXViewTo(uiName,elementName,x=1.0):
    PrintFunctionInfo(MovingChildPageXViewTo,[uiName,elementName,x])    
    #面板内视野横向移动到目标位置:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块目标位置  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        elementName = elementName + "_Child"    
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:     
            ChildPage.xview_moveto(x)
def MovingChildPageYViewTo(uiName,elementName,y=1.0):   
    PrintFunctionInfo(MovingChildPageYViewTo,[uiName,elementName,y])  
    #面板内视野纵向移动到目标位置:参数1 :界面类名, 参数2:控件名称, 参数3:滑动块目标位置  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        elementName = elementName + "_Child"    
        ChildPage = GetElement(uiName,elementName)
        if ChildPage:     
            ChildPage.yview_moveto(y)
 
def GetDate(uiName,elementName):   
    PrintFunctionInfo(GetDate,[uiName,elementName])  
    #取得选择的日期  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        return Control.GetDate() 
    return None     
def SetDate(uiName,elementName,year,month,day):  
    PrintFunctionInfo(SetDate,[uiName,elementName,year,month,day])  
    #设置当前的日期  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        return Control.SetDate(year,month,day) 
    return None   
  
def InitElementData(uiName):  
    PrintFunctionInfo(InitElementData,[uiName])   
    #初始化界面各控件初始数。参数1 :界面类名。
    global G_WindowDraggable    
    if uiName in G_UIElementUserDataArray:    
        for elementName in G_UIElementUserDataArray[uiName].keys():    
            for EBData in G_UIElementUserDataArray[uiName][elementName]:    
                if int(EBData[3]) == 1:    
                    SetText(uiName,elementName,EBData[2])    
    UIScale = G_UIScale    
    if uiName in G_UIRootSizeDictionary.keys():    
        if "scale" in G_UIRootSizeDictionary[uiName].keys():    
            UIScale = G_UIRootSizeDictionary[uiName]["scale"]    
    LoadCanvasRecord(uiName,UIScale)     
    uiClass = GetElement(uiName,"UIClass")
    if uiClass:    
        # 在Form_1_onLoad之前不要调用Form_1_onConfigure
        # Form_1 = GetElement(uiName,"Form_1")
        # if Form_1:    
        #     Form_1_Width = Form_1.winfo_width()
        #     Form_1_Pack = Form_1.pack_info()
        #     if Form_1_Width == 1 or len(Form_1_Pack) > 0:    
        #         if uiName in G_UIRootSizeDictionary.keys() and "width" in G_UIRootSizeDictionary[uiName].keys():    
        #             Form_1_Width = G_UIRootSizeDictionary[uiName]["width"]    
        #         elif G_RootSize:    
        #             Form_1_Width = G_RootSize[0]    
        #     Form_1_Height = Form_1.winfo_height()
        #     if Form_1_Height == 1 or len(Form_1_Pack) > 0:    
        #         if uiName in G_UIRootSizeDictionary.keys() and "height" in G_UIRootSizeDictionary[uiName].keys():    
        #             Form_1_Height = G_UIRootSizeDictionary[uiName]["height"]    
        #         elif G_RootSize:    
        #             Form_1_Height = G_RootSize[1]    
        #     event = ChartEvent(Form_1_Width,Form_1_Height,Form_1)
        #     if hasattr(uiClass,"Configure") == True:    
        #         uiClass.Configure(event)
        if G_WindowDraggable:    
            uiRoot = GetElement(uiName,"root")
            if uiRoot is G_WindowDraggable.GetWidget():    
                for formName in uiRoot.children.keys():    
                    formwidget = uiRoot.children[formName]    
                    formwidget.bind('<ButtonPress-1>',G_WindowDraggable.StartDrag)
                    formwidget.bind('<ButtonRelease-1>',G_WindowDraggable.StopDrag)
                    formwidget.bind('<B1-Motion>',G_WindowDraggable.MoveDragPos)
                    for childName in formwidget.children.keys():    
                        childwidget = formwidget.children[childName]    
                        if childwidget.winfo_class() == "Label" or childwidget.winfo_class() == "Labelframe" or childwidget.winfo_class() == "Frame":    
                            childUiName,childElementName = GetElementName(childwidget,False)
                            if childElementName == None or childElementName.find("LabelButton_") >= 0:    
                                continue    
                            bindingFunc = childwidget.bind('<ButtonPress-1>')
                            if bindingFunc:                           
                                continue    
                            childwidget.bind('<ButtonPress-1>',G_WindowDraggable.StartDrag)
                            childwidget.bind('<ButtonRelease-1>',G_WindowDraggable.StopDrag)
                            childwidget.bind('<B1-Motion>',G_WindowDraggable.MoveDragPos)
    for elementName in G_UIElementLayerDictionary[uiName]:    
        Control = GetElement(uiName,elementName)
        direction = G_UIElementLayerDictionary[uiName][elementName]    
        if direction == 'lift':    
            Control.lift()
        else:    
            Control.lower()
    ResizeAllChart(uiName,True)
    #显示界面    
    if uiName in G_UIRootStateDictionary.keys() and G_UIRootStateDictionary[uiName] == 'deiconify':    
        return    
    else:    
        RestoreUI(uiName)
def InitElementStyle(uiName,Style):   
    PrintFunctionInfo(InitElementStyle,[uiName,Style])   
    #初始化界面各控件初始样式。参数1 :界面类名, 参数2:样式名称。  
    StyleArray = ReadStyleFile(Style+".py")
    if uiName in G_UIElementDictionary:    
        Root = GetElement(uiName,'root')
        TFormKey = '.TForm'    
        if TFormKey in StyleArray:    
            if 'background' in StyleArray[TFormKey]:    
                Root['background'] = StyleArray[TFormKey]['background']    
        for elementName in G_UIElementDictionary[uiName].keys():    
            Widget = G_UIElementDictionary[uiName][elementName]    
            if elementName != "UIClass" and elementName != "root":    
                try:    
                    OldWidget = Widget    
                    if hasattr(Widget,"GetWidget") == True:    
                        Widget = Widget.GetWidget()
                    if  Widget.winfo_exists() == 1:    
                        WinClass = Widget.winfo_class()
                        StyleName = ".T"+WinClass    
                        if StyleName in StyleArray.keys():    
                            for attribute in StyleArray[StyleName].keys():    
                                if attribute == "relief":    
                                    continue    
                                if attribute == "highlightthickness":    
                                    continue    
                                if attribute == "bd":    
                                    continue    
                                if attribute == "background" and elementName != "Form_1":    
                                    if hasattr(OldWidget,"SetBGColor") == True:    
                                        OldWidget.SetBGColor(StyleArray[StyleName][attribute])
                                    if Widget["background"] == "#EFEFEF":    
                                        Widget[attribute] = StyleArray[StyleName][attribute]    
                                    else:    
                                        continue    
                                else:    
                                    if elementName.find("_LabelButton_") > 0:    
                                        continue    
                                    Widget[attribute] = StyleArray[StyleName][attribute]    
                                    if attribute == "foreground" :    
                                        if hasattr(OldWidget,"SetFGColor") == True:    
                                            OldWidget.SetFGColor(StyleArray[StyleName][attribute])
                except Exception as ex:    
                    errorText = str(ex)
                    if errorText.find("no attribute 'winfo_exists'") < 0:    
                        print(ex)
 
def GetUIDataDictionary(uiName):   
    PrintFunctionInfo(GetUIDataDictionary,[uiName])
    #取得界面的所有控件数据。参数1 :界面类名。  
    if uiName not in G_UIElementDictionary:    
        if "UIClass" in G_UIInputDataArray.keys():    
            if uiName == G_UIInputDataArray["UIClass"]:    
                return G_UIInputDataArray    
    else:    
        G_UIInputDataArray.clear()
        for elementName in G_UIElementDictionary[uiName].keys():    
            Widget = G_UIElementDictionary[uiName][elementName]    
            widgetAliasName = elementName    
            if uiName in G_UIElementAliasDictionary.keys():    
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                        widgetAliasName = aliasName    
                        break    
            if elementName == "UIClass":    
                G_UIInputDataArray[elementName] = uiName    
            else:    
                G_UIInputDataArray[widgetAliasName] = ''    
            Widget = G_UIElementDictionary[uiName][elementName]    
            if elementName.find('Label_') >= 0:    
                text = Widget.cget('text')
                G_UIInputDataArray[widgetAliasName] = text      
            elif elementName.find('Text_') >= 0:    
                if elementName.find('Scroll') >= 0:    
                    continue    
                if hasattr(Widget,"GetEntry") == True:    
                    Widget = Widget.GetEntry()
                text = Widget.get('0.0', tkinter.END)
                G_UIInputDataArray[widgetAliasName] = text      
            elif elementName.find('Entry_') >= 0:      
                if elementName in G_UIElementVariableArray[uiName]:      
                    text = G_UIElementVariableArray[uiName][elementName].get()  
                else:      
                    text = Widget.GetText()  
                G_UIInputDataArray[widgetAliasName] = text      
            elif elementName.find('RadioButton_') >= 0 :     
                value = GetTKVariable(uiName,elementName)  
                G_UIInputDataArray[widgetAliasName] = value      
            elif elementName.find('CheckButton_') >= 0 :     
                value = GetTKVariable(uiName,elementName)  
                G_UIInputDataArray[widgetAliasName] = value      
            elif elementName.find('Spinbox_') >= 0:    
                text = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = text      
            elif elementName.find('ComboBox_') >= 0:    
                text = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = text      
            elif elementName.find('Scale_') >= 0:    
                value = Widget.get()  
                G_UIInputDataArray[widgetAliasName] = value      
            elif elementName.find('Progress_') >= 0 :     
                value = Widget["value"]      
                G_UIInputDataArray[widgetAliasName] = value      
            elif elementName.find('ListBox_') >= 0:    
                if elementName.find('Scroll') >= 0:    
                    continue    
                currIndex = Widget.curselection()
                if len(currIndex) > 0 and currIndex[0] >= 0:    
                    text = Widget.get(currIndex[0])
                    G_UIInputDataArray[widgetAliasName] = text      
    if uiName in G_UIElementVariableArray:    
        for elementName in G_UIElementVariableArray[uiName].keys():      
            if elementName.find('Group_') >= 0:      
                widgetAliasName = elementName    
                if uiName in G_UIElementAliasDictionary.keys():    
                    for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                        if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                            widgetAliasName = aliasName    
                            break    
                ElementIntValue = G_UIElementVariableArray[uiName][elementName].get()  
                G_UIInputDataArray[widgetAliasName] = ElementIntValue      
    return G_UIInputDataArray     
 
def DestoryChild(frame,destroy=True):    
    PrintFunctionInfo(DestoryChild,[frame,destroy])
    if frame:    
        for child in frame.winfo_children():    
            DestoryChild(child)
            uiName,elementName = GetElementName(child,False)
            if uiName in G_UIElementDictionary.keys():    
                if elementName in G_UIElementDictionary[uiName]:    
                    G_UIElementDictionary[uiName].pop(elementName)
            if uiName in G_UIElementPlaceDictionary.keys():    
                if elementName in G_UIElementPlaceDictionary[uiName]:    
                    G_UIElementPlaceDictionary[uiName].pop(elementName)
            if uiName in G_UIElementAliasDictionary.keys():    
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                        G_UIElementAliasDictionary[uiName].pop(aliasName)
                        break    
            if uiName in G_UIElementRoundRectangleDictionary.keys():    
                if elementName in G_UIElementRoundRectangleDictionary[uiName]:    
                    G_UIElementRoundRectangleDictionary[uiName].pop(elementName)
            if destroy:    
                child.destroy()
        for className in G_UIRootIDDictionary.keys():    
            if G_UIRootIDDictionary[className] is frame:    
                G_UIRootIDDictionary.pop(className)
                G_UIRootSizeDictionary.pop(className)
                G_UIElementDictionary.pop(className)
                G_UICommandDictionary.pop(className)
                G_UIElementAliasDictionary.pop(className)
                G_UIElementPlaceDictionary.pop(className)
                G_UIElementRoundRectangleDictionary.pop(className)
                G_UIGroupDictionary.pop(className)
                G_UIStyleDictionary.pop(className)
                G_CanvasSizeDictionary.pop(className)
                G_CanvasShapeDictionary.pop(className)
                G_CanvasParamDictionary.pop(className)
                G_CanvasFontDictionary.pop(className)
                G_CanvasImageDictionary.pop(className)
                G_CanvasEventDictionary.pop(className)
                G_CanvasPointDictionary.pop(className)
                G_UIElementIconDictionary.pop(className)
                break    
def GoToUIDialog(uiName,targetUIName,params=None):  
    PrintFunctionInfo(GoToUIDialog,[uiName,targetUIName,params])
    #从当前界面跳转到另一个界面  
    root = GetElement(uiName,'root')
    try:    
        parentinfo = root.winfo_parent()
        while parentinfo:    
            root = root._nametowidget(parentinfo)
            parentinfo = root.winfo_parent()
        for childName in root.children.keys():    
            child = root.children[childName]    
            DestoryChild(child,False)
            child.pack_forget()
    except:    
        try:    
            Form1 = GetElement(uiName,'Form_1')
            if Form1:    
                Form1.pack_forget()
        except:    
            pass    
    import importlib    
    from   importlib import import_module    
    try:    
        importModule = importlib.import_module("Compile_"+targetUIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:    
            importModule.Fun.G_ExeDir = G_ExeDir    
            importModule.Fun.G_ResDir = G_ResDir    
            if hasattr(importModule,"EXUIControl") == True:    
                importModule.EXUIControl.G_ExeDir = G_ExeDir    
                importModule.EXUIControl.G_ResDir = G_ResDir    
        if hasattr(importModule,targetUIName) == True:    
            uiClass = getattr(importModule,targetUIName)
            if params is None:    
                uiDialog = uiClass(root,False)
            else:    
                try:    
                    uiDialog = uiClass(root,False,params)
                except Exception as ex:    
                    uiDialog = uiClass(root,False)
            if hasattr(importModule,"Fun") == True:    
                try :    
                    user32 = ctypes.windll.user32    
                    sw = user32.GetSystemMetrics(0)
                    sh = user32.GetSystemMetrics(1)
                    zw,zh = uiDialog.GetRootSize()
                    zx = int((sw-zw)/2) 
                    zy = int((sh-zh)/2)
                    root.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
                except ImportError:    
                    pass   
            ReDrawCanvasRecord(targetUIName,True)
    except ModuleNotFoundError:    
        try:    
            importModule = importlib.import_module(targetUIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:    
                importModule.Fun.G_ExeDir = G_ExeDir    
                importModule.Fun.G_ResDir = G_ResDir    
                if hasattr(importModule,"EXUIControl") == True:    
                    importModule.EXUIControl.G_ExeDir = G_ExeDir    
                    importModule.EXUIControl.G_ResDir = G_ResDir    
            if hasattr(importModule,targetUIName) == True:    
                uiClass = getattr(importModule,targetUIName)
                if params is None:    
                    uiDialog = uiClass(root,False)
                else:    
                    try:    
                        uiDialog = uiClass(root,False,params)
                    except Exception as ex:    
                        uiDialog = uiClass(root,False)
                if hasattr(importModule,"Fun") == True:    
                    try :    
                        user32 = ctypes.windll.user32    
                        sw = user32.GetSystemMetrics(0)
                        sh = user32.GetSystemMetrics(1)
                        zw,zh = uiDialog.GetRootSize()
                        zx = int((sw-zw)/2) 
                        zy = int((sh-zh)/2)
                        root.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
                    except ImportError:    
                        pass    
            ReDrawCanvasRecord(targetUIName,True)
        except Exception as ex:    
            MessageBox(str(ex))
    except Exception as ex:    
        MessageBox(str(ex))
def PlayCallUIDialogAction(topLevel,uiInstance,animation='zoomin'):
    PrintFunctionInfo(PlayCallUIDialogAction,[topLevel,uiInstance,animation])
    def FadeIn(topLevel,uiInstance,alpha):    
        try :    
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32    
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000    
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha+1, 2 )
            alpha = alpha + 1    
        except ImportError:    
            pass    
        if alpha < 255:    
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = alpha))
    def ZoomIn(topLevel,uiInstance,zoom,width,height):    
        try :    
            user32 = ctypes.windll.user32    
            sw = user32.GetSystemMetrics(0)
            sh = user32.GetSystemMetrics(1)
            zw = int(width * zoom)
            zh = int(height * zoom)
            zx = int((sw-zw)/2) 
            zy = int((sh-zh)/2)
            topLevel.geometry('%dx%d+%d+%d'%(zw,zh,zx,zy))
            zoom = zoom + 0.01    
        except ImportError:    
            pass    
        if zoom < 1.0:    
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = zoom ,width=width,height=height))
    animation = animation.lower()
    if animation == "fadein":    
        try :    
            hwnd = windll.user32.GetParent(topLevel.winfo_id())
            _winlib = ctypes.windll.user32    
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000    
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, 0, 2 )
            topLevel.deiconify()
            topLevel.after(1,lambda:FadeIn(topLevel = topLevel,uiInstance = uiInstance,alpha = 0))
        except ImportError:    
            pass    
    elif animation == "zoomin":    
        try :    
            sw = windll.user32.GetSystemMetrics(0)
            sh = windll.user32.GetSystemMetrics(1)
            topLevel.geometry('%dx%d+%d+%d'%(0,0,int(sw/2),int(sh/2)))
            form1_width,form1_height = uiInstance.GetRootSize()
            topLevel.deiconify()
            topLevel.after(1,lambda:ZoomIn(topLevel = topLevel,uiInstance = uiInstance,zoom = 0.0,width=form1_width,height=form1_height))
        except ImportError:    
            pass    
def CallUIDialog(uiName,topmost = 1,toolwindow = 1,grab_set = 1,wait_window = 1,animation='',params=None):  
    PrintFunctionInfo(CallUIDialog,[uiName,topmost,toolwindow,grab_set,wait_window,animation,params])
    #调用显示一个界面对话框并返回所有控件的输入值。参数1 :界面类名 ,参数2 :是否置最前,参数3:是否有标题栏,参数4:只有当前界面接收消息。参数5:动画类型fadein - 渐显动画,zoomin - 缩放动画。  
    #兼容之前的函数版本  
    global G_TopDialog
    if isinstance(wait_window,str) == True and params is None:    
        params = animation    
        animation = wait_window    
        wait_window = 1    
    import importlib
    from   importlib import import_module
    try:
        importModule = importlib.import_module("Compile_"+uiName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:
            importModule.Fun.G_ExeDir = G_ExeDir
            importModule.Fun.G_ResDir = G_ResDir
            if hasattr(importModule,"EXUIControl") == True:
                importModule.EXUIControl.G_ExeDir = G_ExeDir
                importModule.EXUIControl.G_ResDir = G_ResDir
        if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :
            uiClass = getattr(importModule,uiName)
            funClass = getattr(importModule,"Fun")
            #Tk会导致卡住
            #topLevel = tkinter.Tk()
            #因为Toplevel会显示一个小窗口导致闪烁，所以用之前创建的
            topLevel = tkinter.Toplevel()
            topLevel.withdraw()
            topLevel.attributes("-toolwindow", toolwindow)
            topLevel.wm_attributes("-topmost", topmost)
            G_TopDialog = topLevel
            if grab_set == 1:
                topLevel.grab_set()
            if params is None:
                uiInstance = uiClass(topLevel,True)
            else:
                try:
                    uiInstance = uiClass(topLevel,True,params)
                except Exception as ex:
                    uiInstance = uiClass(topLevel,True)
                if topLevel.winfo_exists() == False:    
                    return funClass.G_UIInputDataArray    
            try:    
                if topmost == 0:    
                    topLevel.wm_attributes("-topmost", 0)
                if hasattr(uiInstance,"uiName") == True:    
                    uiName = uiInstance.uiName    
                def CloseWindow():    
                    funClass.GetUIDataDictionary(uiName)
                    DestroyUI(uiName)
                    topLevel.destroy()
                topLevel.protocol('WM_DELETE_WINDOW', CloseWindow)
                if animation !='':    
                    PlayCallUIDialogAction(topLevel,uiInstance,animation)
                else:    
                    topLevel.deiconify()
                dialog_w,dialog_h = uiInstance.GetRootSize()
                CenterDlg(uiName,topLevel,dialog_w,dialog_h)
                if wait_window == 1:    
                    tkinter.Tk.wait_window(topLevel)
                    G_TopDialog = None    
            except Exception as ex:    
                print(uiName+"被销毁，不再弹出窗口")
            return funClass.G_UIInputDataArray    
    except ModuleNotFoundError:    
        try:    
            importModule = importlib.import_module(uiName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:    
                importModule.Fun.G_ExeDir = G_ExeDir    
                importModule.Fun.G_ResDir = G_ResDir    
                if hasattr(importModule,"EXUIControl") == True:    
                    importModule.EXUIControl.G_ExeDir = G_ExeDir    
                    importModule.EXUIControl.G_ResDir = G_ResDir    
            if hasattr(importModule,uiName) == True and hasattr(importModule,"Fun") == True :    
                uiClass = getattr(importModule,uiName)
                funClass = getattr(importModule,"Fun")  
                #Tk会导致卡住
                #topLevel = tkinter.Tk()
                #因为Toplevel会显示一个小窗口导致闪烁，所以用之前创建的
                topLevel = tkinter.Toplevel()
                topLevel.withdraw()
                topLevel.attributes("-toolwindow", toolwindow)
                topLevel.wm_attributes("-topmost", topmost)
                G_TopDialog = topLevel    
                if grab_set == 1:    
                    topLevel.grab_set()
                if params is None:    
                    uiInstance = uiClass(topLevel,True)
                else:    
                    try:    
                        uiInstance = uiClass(topLevel,True,params)
                    except Exception as ex:    
                        uiInstance = uiClass(topLevel,True)
                if hasattr(uiInstance,"uiName") == True:    
                    uiName = uiInstance.uiName    
                if topLevel.winfo_exists() == False:    
                    return funClass.G_UIInputDataArray    
                try:    
                    if topmost == 0:    
                        topLevel.wm_attributes("-topmost", 0)
                    def CloseWindow():    
                        funClass.GetUIDataDictionary(uiName)
                        DestroyUI(uiName)
                        topLevel.destroy()
                    topLevel.protocol('WM_DELETE_WINDOW',CloseWindow)
                    if animation !='':    
                        PlayCallUIDialogAction(topLevel,uiInstance,animation)
                    else:    
                        topLevel.deiconify()
                    dialog_w,dialog_h = uiInstance.GetRootSize()
                    CenterDlg(uiName,topLevel,dialog_w,dialog_h)
                    if wait_window == 1:    
                        tkinter.Tk.wait_window(topLevel)
                        G_TopDialog = None    
                except Exception as ex:    
                    print(uiName+"被销毁，不再弹出窗口")
                return funClass.G_UIInputDataArray    
        except Exception as ex:    
            ErrorText = str(ex)
            if ErrorText.find("application has been destroyed") != -1:    
                return None    
            MessageBox(ErrorText)
    except Exception as ex:    
        ErrorText = str(ex)
        if ErrorText.find("application has been destroyed") != -1:    
            return None    
        MessageBox(ErrorText)
    return None    
def LoadUIDialog(uiName,elementName,targetUIName,params=None,ignoreSameUI=True):  
    PrintFunctionInfo(LoadUIDialog,[uiName,elementName,targetUIName,params,ignoreSameUI])
    #在指定控件上加载一个界面  
    global G_ExeDir
    global G_UIElementAliasDictionary
    currUIDialog = GetUserData(uiName,elementName,"CurrUI")
    lastLoadTime = GetUserData(uiName,elementName,"LoadTime")
    if currUIDialog is None:    
        AddUserData(uiName,elementName,"CurrUI","string",targetUIName,0)
        AddUserData(uiName,elementName,"LoadTime","long",time.time())
    else:    
        if currUIDialog == targetUIName and ignoreSameUI == True:    
            print('忽略重复加载'+":"+targetUIName)
            return GetElement(targetUIName,'UIClass')
        SetUserData(uiName,elementName,"CurrUI",targetUIName)
        SetUserData(uiName,elementName,"LoadTime",time.time())
    Root = GetElement(uiName,'root')
    ParentFrame = GetElement(uiName,elementName)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in  G_UIElementAliasDictionary[uiName].keys():    
        realName = G_UIElementAliasDictionary[uiName][elementName]    
        ParentFrame_Child = GetElement(uiName,realName+"_Child")
    else:    
        ParentFrame_Child = GetElement(uiName,elementName+"_Child")
    DestoryChild(ParentFrame)
    ParentFrame_Child = tkinter.Canvas(ParentFrame,relief=tkinter.FLAT,background='#CCCCCC',highlightthickness=0)
    ParentFrame_Child.pack(side=TOP,fill=BOTH,expand=True)
    Register(uiName,elementName+"_Child",ParentFrame_Child)
    ParentFrame = ParentFrame_Child
    ParentFrame.update()
    if targetUIName:
        print("LoadUIDialog %s,%s => %s"%(uiName,elementName,targetUIName))
        import importlib    
        from   importlib import import_module    
        try:    
            UIPath, UIFile = os.path.split(targetUIName)
            if UIPath.find(":") < 0:    
                UIPath = os.path.join(G_ExeDir,UIPath)
            UIName, extension = os.path.splitext(UIFile)
            import sys    
            sys.path.append(UIPath)
            importModule = importlib.import_module(UIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:    
                importModule.Fun.G_ExeDir = G_ExeDir    
                importModule.Fun.G_ResDir = G_ResDir    
                if hasattr(importModule,"EXUIControl") == True:    
                    importModule.EXUIControl.G_ExeDir = G_ExeDir    
                    importModule.EXUIControl.G_ResDir = G_ResDir    
            if hasattr(importModule,UIName) == True:    
                uiClass = getattr(importModule,UIName)
                if params is None:    
                    uiDialog = uiClass(ParentFrame,False)
                else:    
                    try:    
                        uiDialog = uiClass(ParentFrame,False,params)
                    except Exception as ex:    
                        uiDialog = uiClass(ParentFrame,False)
                UIName = uiDialog.uiName    
                G_UIElementDictionary[UIName]['root'] = Root    
                G_UILoadPageDictionary[uiName][elementName] = [uiDialog]
                return uiDialog    
        except ModuleNotFoundError:    
            try:    
                UIPath, UIFile = os.path.split(targetUIName)
                if UIPath.find(":") < 0:    
                    UIPath = os.path.join(G_ExeDir,UIPath)
                UIName, extension = os.path.splitext(UIFile)
                import sys    
                sys.path.append(UIPath)
                importModule = importlib.import_module("Compile_"+UIName)
                importModule = importlib.reload(importModule)
                if hasattr(importModule,"Fun") == True:    
                    importModule.Fun.G_ExeDir = G_ExeDir    
                    importModule.Fun.G_ResDir = G_ResDir    
                    if hasattr(importModule,"EXUIControl") == True:    
                        importModule.EXUIControl.G_ExeDir = G_ExeDir    
                        importModule.EXUIControl.G_ResDir = G_ResDir    
                if hasattr(importModule,UIName) == True:    
                    uiClass = getattr(importModule,UIName)
                    if params is None:    
                        uiDialog = uiClass(ParentFrame,False)
                    else:    
                        try:    
                            uiDialog = uiClass(ParentFrame,False,params)
                        except Exception as ex:    
                            uiDialog = uiClass(ParentFrame,False)
                    UIName = uiDialog.uiName    
                    #uiDialog.root = Root      
                    G_UIElementDictionary[UIName]['root'] = Root    
                    G_UILoadPageDictionary[uiName][elementName] = [uiDialog]
                    return uiDialog    
            except Exception as ex:    
                except_type, except_value, except_traceback = sys.exc_info()
                except_value_str = str(except_value)
                except_stack_end = except_traceback.tb_frame    
                except_stack_next = except_traceback.tb_next    
                except_stack_lineno = except_traceback.tb_lineno    
                while except_stack_next:    
                    except_stack_end = except_stack_next.tb_frame    
                    except_stack_lineno = except_stack_next.tb_lineno    
                    except_stack_next = except_stack_next.tb_next    
                except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
                MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+except_stack_lineno,'运行错误')
        except Exception as ex:    
            except_type, except_value, except_traceback = sys.exc_info()
            except_value_str = str(except_value)
            except_stack_end = except_traceback.tb_frame    
            except_stack_next = except_traceback.tb_next    
            except_stack_lineno = except_traceback.tb_lineno    
            while except_stack_next:    
                except_stack_end = except_stack_next.tb_frame    
                except_stack_lineno = except_stack_next.tb_lineno    
                except_stack_next = except_stack_next.tb_next    
            except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
            MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+except_stack_lineno,'运行错误')
            MessageBox(str(ex))
    return None
def SetChildFrameScrollRegion(uiName,elementName,width,height): 
    PrintFunctionInfo(SetChildFrameScrollRegion,[uiName,elementName,width,height])
    #设置Frame可观察导入界面的区域大小  
    Frame_ChildName = elementName + "_Child"
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        Frame_ChildName = G_UIElementAliasDictionary[uiName][elementName]+"_Child"    
    Frame_Child = GetElement(uiName,Frame_ChildName)
    UIChildren = Frame_Child.winfo_children()
    if UIChildren and len(UIChildren) > 0:    
        Form_1 = UIChildren[0]    
        Frame_ChildHandle = Frame_Child.create_window(0,0, window=Form_1, anchor=tkinter.NW,tag="Form_1")
        Frame_Child.itemconfig(Frame_ChildHandle,width=width,height=height)
    Frame_Child.config(scrollregion=(0,0,width,height))
# def  Resize_Frame(event):    
#    realWidth = width    
#    if isinstance(realWidth,float) == True:    
#        realWidth = int(width*event.width)
#        realHeight = height    
#        if isinstance(realHeight,float) == True:    
#            realHeight = int(height*event.height)
#            event.widget.config(scrollregion=(0,0,event,event))
#            Frame_Child.bind('<Configure>',Resize_Frame)
def AddUIDialog(uiName,elementName,targetUIName,x,y,params=None):    
    PrintFunctionInfo(AddUIDialog,[uiName,elementName,targetUIName,x,y,params])
    #在指定控件上加载一个界面    
    def OnFrameConfigure(event,targetUIName): 
        if uiClass and event:
            Form_1_Width = event.widget.winfo_width()
            Form_1_Height = event.widget.winfo_height()
            event = ChartEvent(Form_1_Width,Form_1_Height,uiClass.root)
            if hasattr(uiClass,"Configure") == True:    
                uiClass.Configure(event)
            uiForm1 = GetElement(targetUIName,'Form_1')
            if uiForm1:
                event = ChartEvent(Form_1_Width,Form_1_Height,uiForm1)
                if hasattr(uiClass,"Configure") == True:    
                    uiClass.Configure(event)
                    return 
        ReDrawCanvasRecord(targetUIName,True)
    print("AddUIDialog %s,%s => %s"%(uiName,elementName,targetUIName))
    Root = GetElement(uiName,'root')
    ParentFrame = GetElement(uiName,elementName)
    ChildName = elementName+"_Child"    
    HScrollName = elementName+"_HScrollbar"    
    VScrollName = elementName+"_VScrollbar"    
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        ChildName = G_UIElementAliasDictionary[uiName][elementName]+"_Child"    
        HScrollName = G_UIElementAliasDictionary[uiName][elementName]+"_HScrollbar"    
        VScrollName = G_UIElementAliasDictionary[uiName][elementName]+"_VScrollbar"    
        ParentFrame_Child = GetElement(uiName,ChildName)
    else:    
        ParentFrame_Child = GetElement(uiName,elementName+"_Child")
    if ParentFrame_Child:    
        ParentFrame = ParentFrame_Child    
    else:    
        ParentFrame_Child = tkinter.Canvas(ParentFrame,bg=ParentFrame.cget('bg'))
        ParentFrame_Child.place(x=x,y=y,width=ParentFrame.winfo_width()-30,height=ParentFrame.winfo_height())
        Register(uiName,ChildName,ParentFrame_Child)
        AddUserData(uiName,ChildName,"scrollregion","list",[0,0,0,0],0)
        ParentFrame = ParentFrame_Child    
        HScrollbar = GetElement(uiName,HScrollName)
        if HScrollbar:    
            HScrollbar.config(command = ParentFrame.xview)
            ParentFrame.config(xscrollcommand=HScrollbar.set)
        VScrollbar = GetElement(uiName,VScrollName)
        if VScrollbar:    
            VScrollbar.config(command = ParentFrame.yview)
            ParentFrame.config(yscrollcommand=VScrollbar.set)
    import importlib    
    from   importlib import import_module    
    try:    
        UIPath, UIFile = os.path.split(targetUIName)
        if UIPath.find(":") < 0:    
            UIPath = os.path.join(G_ExeDir,UIPath)
        UIName, extension = os.path.splitext(UIFile)
        import sys    
        sys.path.append(UIPath)
        importModule = importlib.import_module(UIName)
        importModule = importlib.reload(importModule)
        if hasattr(importModule,"Fun") == True:    
            importModule.Fun.G_ExeDir = G_ExeDir    
            importModule.Fun.G_ResDir = G_ResDir    
            if hasattr(importModule,"EXUIControl") == True:    
                importModule.EXUIControl.G_ExeDir = G_ExeDir    
                importModule.EXUIControl.G_ResDir = G_ResDir    
        if hasattr(importModule,UIName) == True:    
            uiClass = getattr(importModule,UIName)
            if params is None:    
                uiDialog = uiClass(ParentFrame,False)
            else:    
                try:    
                    uiDialog = uiClass(ParentFrame,False,params)
                except Exception as ex:    
                    uiDialog = uiClass(ParentFrame,False)
            UIName = uiDialog.uiName    
            scrollregion_info = GetUserData(uiName,ChildName,"scrollregion")
            scrollregion_width = scrollregion_info[2]    
            scrollregion_height = scrollregion_info[3]    
            if ParentFrame_Child:    
                if hasattr(uiDialog,"GetRootSize") == True:    
                    uiDialogWidth,uiDialogHeight = uiDialog.GetRootSize()
                    ChildWidgetList = uiDialog.GetAllElement()
                    if 'Form_1' in ChildWidgetList.keys():    
                        uiDialogForm1  = ChildWidgetList['Form_1']    
                        ChildHandle = ParentFrame.create_window(x,y, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                        ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                if (x + uiDialogWidth) > scrollregion_width:    
                    scrollregion_width = (x + uiDialogWidth) 
                if (y + uiDialogHeight) > scrollregion_height:    
                    scrollregion_height = (y + uiDialogHeight) 
            #2024-08-17暂时屏蔽，会造成FrameDraggable拖动界面无效
            #uiDialog.root = Root    
            G_UIElementDictionary[UIName]['root'] = Root    
            OnFrameConfigure(None,UIName)
            ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
            ParentFrame.config(scrollregion=(0,0,scrollregion_width,scrollregion_height))
            SetUserData(uiName,ChildName,"scrollregion",[0,0,scrollregion_width,scrollregion_height])
            ParentFrame.update()
            return uiDialog    
    except ModuleNotFoundError:    
        try:    
            UIPath, UIFile = os.path.split(targetUIName)
            if UIPath.find(":") < 0:    
                UIPath = os.path.join(G_ExeDir,UIPath)
            UIName, extension = os.path.splitext(UIFile)
            import sys    
            sys.path.append(UIPath)
            importModule = importlib.import_module("Compile_"+UIName)
            importModule = importlib.reload(importModule)
            if hasattr(importModule,"Fun") == True:    
                importModule.Fun.G_ExeDir = G_ExeDir    
                importModule.Fun.G_ResDir = G_ResDir    
                if hasattr(importModule,"EXUIControl") == True:    
                    importModule.EXUIControl.G_ExeDir = G_ExeDir    
                    importModule.EXUIControl.G_ResDir = G_ResDir    
            if hasattr(importModule,UIName) == True:    
                uiClass = getattr(importModule,UIName)
                if params is None:    
                    uiDialog = uiClass(ParentFrame,False)
                else:    
                    try:    
                        uiDialog = uiClass(ParentFrame,False,params)
                    except Exception as ex:    
                        uiDialog = uiClass(ParentFrame,False)
                UIName = uiDialog.uiName    
                scrollregion_info = GetUserData(uiName,ChildName,"scrollregion")
                scrollregion_width = scrollregion_info[2]    
                scrollregion_height = scrollregion_info[3]    
                if ParentFrame_Child:    
                    if hasattr(uiDialog,"GetRootSize") == True:    
                        uiDialogWidth,uiDialogHeight = uiDialog.GetRootSize()
                        ChildWidgetList = uiDialog.GetAllElement()
                        if 'Form_1' in ChildWidgetList.keys():    
                            uiDialogForm1  = ChildWidgetList['Form_1']    
                            ChildHandle = ParentFrame.create_window(x,y, window=uiDialogForm1, anchor=tkinter.NW,tag="Form_1")
                            ParentFrame.itemconfig(ChildHandle,width=uiDialogWidth,height=uiDialogHeight)
                    if (x + uiDialogWidth) > scrollregion_width:    
                        scrollregion_width = (x + uiDialogWidth) 
                    if (y + uiDialogHeight) > scrollregion_height:    
                        scrollregion_height = (y + uiDialogHeight) 
                #2024-08-17暂时屏蔽，会造成FrameDraggable拖动界面无效
                #uiDialog.root = Root    
                G_UIElementDictionary[UIName]['root'] = Root    
                OnFrameConfigure(None,UIName)
                ParentFrame.bind('<Configure>',EventFunction_Adaptor(OnFrameConfigure,targetUIName = UIName))
                ParentFrame.config(scrollregion=(0,0,scrollregion_width,scrollregion_height))
                SetUserData(uiName,ChildName,"scrollregion",[0,0,scrollregion_width,scrollregion_height])
                ParentFrame.update()
                return uiDialog    
        except Exception as ex:    
            except_type, except_value, except_traceback = sys.exc_info()
            except_value_str = str(except_value)
            except_stack_end = except_traceback.tb_frame    
            except_stack_next = except_traceback.tb_next    
            except_stack_lineno = except_traceback.tb_lineno    
            while except_stack_next:    
                except_stack_end = except_stack_next.tb_frame    
                except_stack_lineno = except_stack_next.tb_lineno    
                except_stack_next = except_stack_next.tb_next    
            except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
            MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+except_stack_lineno,'运行错误')
#            MessageBox(ex)
    except Exception as ex:    
        except_type, except_value, except_traceback = sys.exc_info()
        except_value_str = str(except_value)
        except_stack_end = except_traceback.tb_frame    
        except_stack_next = except_traceback.tb_next    
        except_stack_lineno = except_traceback.tb_lineno    
        while except_stack_next:    
            except_stack_end = except_stack_next.tb_frame    
            except_stack_lineno = except_stack_next.tb_lineno    
            except_stack_next = except_stack_next.tb_next    
        except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
        MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+except_stack_lineno,'运行错误')
#        MessageBox(ex)

def ShowWindow(uiName,WindowState):  
    PrintFunctionInfo(ShowWindow,[uiName,WindowState])
    #设置窗口显示状态(0:隐藏,1:正常显示,2:最小化,3最大化)  
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())
    if  type(WindowState) == type(''):
        if WindowState == 'normal':
            win32gui.ShowWindow(hwnd,1)   
        elif WindowState == 'hide':
            win32gui.ShowWindow(hwnd,0)   
        elif WindowState == 'minimize':
            win32gui.ShowWindow(hwnd,2)   
        elif WindowState == 'maximize':
            win32gui.ShowWindow(hwnd,3)   
    else:
        win32gui.ShowWindow(hwnd,WindowState) 

def SetWindowTitle(uiName,title=''):    
    PrintFunctionInfo(SetWindowTitle,[uiName,title])
    #设置窗口标题  
    root = GetElement(uiName,'root')
    root.title(title)
def SetWindowIco(uiName,imageFile=''):  
    PrintFunctionInfo(SetWindowIco,[uiName,imageFile])
    #设置窗口图标  
    imageFile_noExt,extension = os.path.splitext(imageFile)
    root = GetElement(uiName,'root')
    if extension == '.ico':    
        root.iconbitmap(imageFile)
    else:    
        import base64    
        open_icon = open(imageFile,"rb")
        open_icon_base64 = base64.b64encode(open_icon.read())
        icoFileName = imageFile_noExt+".ico"    
        tmp = open(icoFileName,"wb+")
        tmp.write(open_icon_base64)
        tmp.close()
        img = Image.open(icoFileName)
        img.save(icoFileName)
        root.iconbitmap(icoFileName)
        os.remove(icoFileName)
g_ToolBar_lastX = 0    
g_ToolBar_lastY = 0    
def SetToolBar(root,uiFileName):  
    PrintFunctionInfo(SetToolBar,[root,uiFileName])
    #导入标题栏  
    try:    
        if uiFileName.find(".py") >= 0:    
            pathName,fileName = os.path.split(uiFileName)
            sys.path.insert(0,pathName)
            importSplitArray = fileName.partition('.py')
            uiClass = importSplitArray[0]    
        else:    
            uiClass = uiFileName    
        import importlib    
        from   importlib import import_module    
        importModule = importlib.import_module(uiClass)
        importModule = importlib.reload(importModule)
        newClass = getattr(importModule, uiClass)
        if newClass:    
            def ButtonDown_ToolBar(event):    
                global g_ToolBar_lastX    
                global g_ToolBar_lastY    
                g_ToolBar_lastX = event.x_root    
                g_ToolBar_lastY = event.y_root    
            def ButtonMotion_ToolBar(event):    
                global g_ToolBar_lastX    
                global g_ToolBar_lastY    
                offsetX = event.x_root - g_ToolBar_lastX    
                offsetY = event.y_root - g_ToolBar_lastY    
                root_x = root.winfo_x()
                root_y = root.winfo_y()
                root_w = root.winfo_width()
                root_h = root.winfo_height()
                if offsetX != 0 or offsetY != 0:    
                    root.geometry('%dx%d+%d+%d'%(root_w,root_h,root_x+offsetX,root_y+offsetY))
                g_ToolBar_lastX = event.x_root    
                g_ToolBar_lastY = event.y_root    
            def ButtonUp_ToolBar(event):    
                pass    
            newClassInstance = newClass(root,False)
            ChildWidgetList = newClassInstance.GetAllElement()
            for widgetName in ChildWidgetList.keys():    
                if widgetName == 'UIClass':    
                    continue    
                if widgetName == 'root':    
                    continue    
                ChildWidget = ChildWidgetList[widgetName]    
                if widgetName == 'Form_1':    
                    ChildWidget.pack(side=tkinter.TOP,fill=tkinter.X)
                if hasattr(ChildWidget,'GetWidget') == True:    
                    ChildWidget = ChildWidget.GetWidget()
                bindList = ChildWidget.bind()
                if widgetName.find('Entry_') >= 0:    
                    continue    
                if widgetName.find('Text_') >= 0:    
                    continue    
                if widgetName.find('Button_') >= 0:    
                    continue    
                if '<Button-1>' not in bindList and '<B1-Motion>' not in bindList and '<ButtonRelease-1>' not in bindList:    
                    ChildWidget.bind('<Button-1>',ButtonDown_ToolBar)
                    ChildWidget.bind('<B1-Motion>',ButtonMotion_ToolBar)
                    ChildWidget.bind('<ButtonRelease-1>',ButtonUp_ToolBar)
    except Exception as ex:    
        print(ex)
def SetWindowTitleBar(uiName,uiFileName=""):  
    PrintFunctionInfo(SetWindowTitleBar,[uiName,uiFileName])
    #设置窗口标题栏    
    root = GetElement(uiName,'root')
    if root:
        SetToolBar(root,uiFileName)

def CenterDlg(uiName,popupDlg,dw=0,dh=0,keepHide=False,popui_xy='Center'):
    PrintFunctionInfo(CenterDlg,[uiName,popupDlg,dw,dh,keepHide,popui_xy])
    #将弹出界面对话框居中。参数1 :界面类名, 参数2:对话框窗体,参数3:窗体宽度,参数4:窗体高度。  
    global G_LaunchDlg    
    if dw == 0:    
        dw = popupDlg.winfo_width()
    if dh == 0:    
        dh = popupDlg.winfo_height()
    root = GetElement(uiName,'root')
    if root != None and popupDlg != root:    
        sw = root.winfo_width()
        sh = root.winfo_height()
        sx = root.winfo_x()
        sy = root.winfo_y()
        if popui_xy == 'Center':    
            x = int(sx+(sw-dw)/2)
            if x < 0:    
                x = 0    
            y = int(sy+(sh-dh)/2)
            if y < 0:    
                y = 0    
        else:    
            x = popui_xy[0]    
            y = popui_xy[1]    
        popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,x,y))
        popupDlg.update()
        if keepHide == False:    
            popupDlg.deiconify()
            G_UIRootStateDictionary[uiName] = 'deiconify'    
    else:    
        user32 = ctypes.windll.user32    
        try:    
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
#            ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        except:    
            ctypes.windll.user32.SetProcessDPIAware()
        sw = user32.GetSystemMetrics(0)
        sh = user32.GetSystemMetrics(1)
        sx = 0    
        sy = 0    
        if popui_xy == 'Center':    
            x = int(sx+(sw-dw)/2)
            if x < 0:    
                x = 0    
            y = int(sy+(sh-dh)/2)
            if y < 0:    
                y = 0    
        else:    
            x = popui_xy[0]    
            y = popui_xy[1]    
        popupDlg.tk.call('tk', 'scaling',g_TKScaling)
        popupDlg.geometry('%dx%d+%d+%d'%(dw,dh,x,y))
        popupDlg.update()
        if keepHide == False:    
            popupDlg.deiconify()
            G_UIRootStateDictionary[uiName] = 'deiconify'    
        from win32gui import GetParent, SetWindowPos, UpdateWindow, SetWindowLong, GetWindowLong, ReleaseCapture, PostMessage    
        from win32con import NULL, SWP_NOSIZE, SWP_NOMOVE, SWP_NOZORDER, SWP_DRAWFRAME, GWL_STYLE, WS_CAPTION, WM_SYSCOMMAND, SC_MOVE, HTCAPTION, WS_THICKFRAME    
        WindowHandle = ctypes.windll.user32.GetParent(popupDlg.winfo_id())    
        SetWindowPos(WindowHandle, NULL, x, y, dw, dh, SWP_DRAWFRAME|SWP_NOSIZE|SWP_NOZORDER)
        #UpdateWindow有时会导致界面卡住
        #UpdateWindow(WindowHandle)  
        WM_PAINT = 0x000F
        PostMessage(WindowHandle,WM_PAINT,0,0)  
        if G_LaunchDlg is None:    
            popupDlg.attributes('-topmost', 1)
            popupDlg.attributes('-topmost', 0)
            G_LaunchDlg = popupDlg    
def SetUIDialogXYWH(uiName,x,y,width,height):  
    PrintFunctionInfo(SetUIDialogXYWH,[uiName,x,y,width,height])
    #设置窗口显示位置和大小  
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:    
        G_UIElementPlaceDictionary[uiName]['root'] = {}    
    G_UIElementPlaceDictionary[uiName]['root']['x'] = x    
    G_UIElementPlaceDictionary[uiName]['root']['y'] = y    
    G_UIElementPlaceDictionary[uiName]['root']['width'] = width    
    G_UIElementPlaceDictionary[uiName]['root']['height'] = height    
    while root.master:    
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d+%d+%d'%(width,height,x,y))
    root.update()
def SetUIDialogXY(uiName,x,y):  
    PrintFunctionInfo(SetUIDialogXY,[uiName,x,y])
    #设置窗口显示位置  
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:    
        G_UIElementPlaceDictionary[uiName]['root'] = {}    
    G_UIElementPlaceDictionary[uiName]['root']['x'] = x    
    G_UIElementPlaceDictionary[uiName]['root']['y'] = y    
    while root.master:    
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%d+%d'%(x,y))
def SetUIDialogWH(uiName,width,height):   
    PrintFunctionInfo(SetUIDialogWH,[uiName,width,height])
    #移动窗口显示大小  
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:    
        G_UIElementPlaceDictionary[uiName]['root'] = {}    
    G_UIElementPlaceDictionary[uiName]['root']['width'] = width    
    G_UIElementPlaceDictionary[uiName]['root']['height'] = height    
    while root.master:    
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d'%(width,height))
    root.update()
def MaximizeUI(uiName):
    PrintFunctionInfo(MaximizeUI,[uiName])  
    #最大化窗口  
    root = GetElement(uiName,'root')
    if 'root' not in G_UIElementPlaceDictionary[uiName]:    
        G_UIElementPlaceDictionary[uiName]['root'] = {}    
    G_UIElementPlaceDictionary[uiName]['root']['x'] = root.winfo_x()
    G_UIElementPlaceDictionary[uiName]['root']['y'] = root.winfo_y()
    G_UIElementPlaceDictionary[uiName]['root']['width'] = root.winfo_width()
    G_UIElementPlaceDictionary[uiName]['root']['height'] = root.winfo_height()
    user32 = ctypes.windll.user32    
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    while root.master:    
        root = root._nametowidget(root.winfo_parent())
    root.geometry('%dx%d+%d+%d'%(sw,sh,0,0))
    root.update()
    ReDrawCanvasRecord(uiName,True)
def MinimizeUI(uiName):   
    PrintFunctionInfo(MinimizeUI,[uiName])  
    #最小化窗口  
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())  
    win32gui.ShowWindow(hwnd,2)
def RestoreUI(uiName):  
    PrintFunctionInfo(RestoreUI,[uiName])  
    #恢复窗口  
    global G_TKRoot    
        
    root = GetElement(uiName,'root')
    if 'root' in G_UIElementPlaceDictionary[uiName]:    
        hwnd = windll.user32.GetParent(root.winfo_id())
        win32gui.ShowWindow(hwnd,1)
        root.geometry('%dx%d+%d+%d'%(G_UIElementPlaceDictionary[uiName]['root']['width'],G_UIElementPlaceDictionary[uiName]['root']['height'],G_UIElementPlaceDictionary[uiName]['root']['x'],G_UIElementPlaceDictionary[uiName]['root']['y']))
    else:    
        hwnd = windll.user32.GetParent(root.winfo_id())
        state = 'normal'    
        if uiName in G_UIRootStateDictionary.keys():    
            state = G_UIRootStateDictionary[uiName]    
        if state == "iconic":    
            win32gui.ShowWindow(hwnd,2)
        elif state == "zoomed":    
            win32gui.ShowWindow(hwnd,3)
        else:    
            win32gui.ShowWindow(hwnd,1)
        root.update()
def HideUI(uiName):
    PrintFunctionInfo(HideUI,[uiName])  
    #隐藏窗口  
    root = GetElement(uiName,'root')
    hwnd = windll.user32.GetParent(root.winfo_id())  
    win32gui.ShowWindow(hwnd,0)
def SetUIState(uiName,state): 
    PrintFunctionInfo(SetUIState,[uiName,state])  
    #最大化窗口  
    G_UIRootStateDictionary[uiName] = state    

def SetRoundedRectangle(uiName,elementName,WidthEllipse=20,HeightEllipse=20): 
    PrintFunctionInfo(SetRoundedRectangle,[uiName,elementName,WidthEllipse,HeightEllipse])  
    #在界面布局文件中调用设置控件的圆角属性,但由于尚未创建接口,因此有必要在两次之后调用ShowRoundedRectangle。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。  
    if isinstance(elementName,int) == True:    
        WidthEllipse = elementName    
        HeightEllipse = WidthEllipse    
        uiName,elementName = GetElementName(uiName)
    if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
        elementName = G_UIElementAliasDictionary[uiName][elementName]     
    G_UIElementRoundRectangleDictionary[uiName][elementName] = [WidthEllipse,HeightEllipse]    
def ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse): 
    PrintFunctionInfo(ShowRoundedRectangle,[Control,WidthEllipse,HeightEllipse])  
    #立即设置控件的圆角属性。注意 :此功能不跨平台。参数1 :控件, 参数2:圆角宽度,参数3:圆角高度。  
    if Control != None:    
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
        import win32gui    
        control_width = Control.winfo_width()
        control_height = Control.winfo_height()
        if control_width > 1 and control_height > 1:    
            HRGN = win32gui.CreateRoundRectRgn(0,0,control_width,control_height,WidthEllipse,HeightEllipse)
            win32gui.SetWindowRgn(Control.winfo_id(), HRGN,1)
        else:    
            Control.after(10, lambda: ShowRoundedRectangle(Control,WidthEllipse,HeightEllipse))
  
def SetTransparencyFunction(root,alpha):   
    PrintFunctionInfo(SetTransparencyFunction,[root,alpha])  
    #设置窗体透明值。注意 :此功能不跨平台。  
    if root:    
        try :    
            hwnd = windll.user32.GetParent(root.winfo_id())
            _winlib = ctypes.windll.user32    
            style = _winlib.GetWindowLongA( hwnd, 0xffffffec ) | 0x00080000    
            _winlib.SetWindowLongA( hwnd, 0xffffffec, style )
            _winlib.SetLayeredWindowAttributes( hwnd, 0, alpha, 2 )
        except ImportError:       
            pass     
def SetWindowTransparency(uiName,alpha): 
    PrintFunctionInfo(SetWindowTransparency,[uiName,alpha])  
    #设置窗体透明值。注意 :此功能不跨平台。  
    root = GetElement(uiName,'root')
    if root:
        SetTransparencyFunction(root,alpha)
    
def ExpandAllTreeItem(targetTree,isOpen,parentItem = None):   
    PrintFunctionInfo(ExpandAllTreeItem,[targetTree,isOpen,parentItem])  
    #展开或关闭树项  
    ParentItemArray = [parentItem]    
    if parentItem == None:    
        ParentItemArray = targetTree.get_children()
    for Item in ParentItemArray:    
        targetTree.item(Item,open=isOpen)
        for childItem in targetTree.get_children(Item):    
            targetTree.item(childItem,open=isOpen)
            ExpandAllTreeItem(targetTree,isOpen,childItem) 

def ExpandTreeView(uiName,elementName): 
    PrintFunctionInfo(ExpandTreeView,[uiName,elementName])  
    #展开或关闭树项  
    targetTree = GetElement(uiName,elementName)
    if targetTree:
        ItemArray = targetTree.get_children()
        for ChildItem in ItemArray:    
            targetTree.item(ChildItem,open=1)
            ExpandAllTreeItem(targetTree,1,targetTree.get_children(ChildItem)) 
    
def MessageBox(text="",title="info",type="info",parent=None):  
    text = str(text)
    title = str(title)
    type = str(type)
    PrintFunctionInfo(MessageBox,[text,title,type,parent])  
    #弹出一个信息对话框。参数1 :对话框显示文字 ,参数1:显示文字,参数2:标题文字,参数3:对话框类型,可选:info、warning、error,参数4:父控件  
    global G_TKRoot    
    global G_TopDialog
    if G_TopDialog:    
        parent = G_TopDialog    
    winhandle = None    
    try:    
        if parent:    
            winhandle = parent.winfo_id()
        elif G_TKRoot:    
            winhandle = G_TKRoot.winfo_id()
    except:    
        pass    
    if type == "error":    
#        tkinter.messagebox.showerror(title,text)
        import win32api    
        import win32con    
        ICONERROR=16 #错误图标    
        win32api.MessageBox(winhandle,text,title,win32con.MB_OK|ICONERROR)
    else:    
        import win32api    
        import win32con    
        ICONQUESTION=32 #警告图标    
        win32api.MessageBox(winhandle,text,title,win32con.MB_OK|ICONQUESTION) 

def RunApplication(uiClass,deiconify=False,projName='',InitCheckFunc=None): 
    PrintFunctionInfo(RunApplication,[uiClass,deiconify,projName,InitCheckFunc])  
    #运行PyMe工程  
    try:    
        global G_TKRoot 
        G_TKRoot = tkinter.Tk()
        G_TKRoot.withdraw()
        if deiconify == True:    
            if RunForm1_CallBack(projName,"InitCheck",InitCheckFunc) == False:    
                sys.exit()
                return    
            MyDlg = uiClass(G_TKRoot)
        else:    
            MyDlg = uiClass(G_TKRoot)
        if G_TKRoot:
            G_TKRoot.attributes('-topmost',1)   
            G_TKRoot.attributes('-topmost',0)  
            G_TKRoot.mainloop()
        sys.exit()
    except Exception as Ex:    
        except_type, except_value, except_traceback = sys.exc_info()
        except_value_str = str(except_value)
        except_stack_end = except_traceback.tb_frame    
        except_stack_next = except_traceback.tb_next    
        except_stack_lineno = except_traceback.tb_lineno    
        while except_stack_next:    
            except_stack_end = except_stack_next.tb_frame    
            except_stack_lineno = except_stack_next.tb_lineno    
            except_stack_next = except_stack_next.tb_next    
        except_file = os.path.split(except_stack_end.f_code.co_filename)[1]    
        MessageBox('错误信息：'+except_value_str+'\n'+'文件:'+except_file+'\n'+'行号:'+str(except_stack_lineno),'运行错误')
     
def InputBox(title='',prompt='',initialvalue='',parent=None):   
    PrintFunctionInfo(InputBox,[title,prompt,initialvalue,parent])  
    #弹出一个输入对话框。参数1 :对话框标题文字 ,参数2:提示说明文字(可影响输入框的长度),参数3:对话框默认框输入文字  
    res = tkinter.simpledialog.askstring(title,prompt=prompt,initialvalue=initialvalue)
    return res    

def InputDialog(width,lines=1,bgColor='#EFEFEF',titleText='',promptText='',defaultText='',callBackFunction=None):   
    PrintFunctionInfo(InputDialog,[width,lines,bgColor,titleText,promptText,defaultText,callBackFunction])  
    #弹出一个输入对话框，可以自定义输入窗口大小，数入文字采用单行还是多行。  
    theInputDialog = tkinter.Toplevel()
    theInputDialog.attributes("-toolwindow", 1)
    theInputDialog.resizable(1,1)
    theInputDialog.wm_attributes("-topmost", 1)
    theInputDialog.title(titleText)
    height = 140    
    if lines > 1:    
        height = 110 + lines * 20    
    user32 = ctypes.windll.user32    
    sw = user32.GetSystemMetrics(0)
    sh = user32.GetSystemMetrics(1)
    zx = int((sw-width)/2) 
    zy = int((sh-height)/2)
    geoinfo = str('%dx%d+%d+%d'%(width,height,zx,zy))
    theInputDialog.geometry(geoinfo)
    theForm = tkinter.Canvas(theInputDialog,bg = bgColor,width = width,height=height,highlightthickness=0,bd=0)
    theForm.pack(expand=1, fill='both')
    theDataLabel = tkinter.Label(theForm,anchor = tkinter.W,text=promptText,width = width,bg = bgColor,fg = '#000000',font = ('宋体',12),justify = tkinter.LEFT,height = 1)
    theDataLabel.place(x = 20,y = 10,width = width-40,height = 30)
    theYPos = 75    
    theEntryText = StringVar()
    theEntryText.set('')
    if lines == 1:    
        theEntry= tkinter.Entry(theForm,textvariable=theEntryText,bg='#FFFFFF',relief=tkinter.FLAT)
        theEntry.place(x = 20,y = 45,width = width-40,height = 30)
    else:    
        theEntry= tkinter.Text(theForm,bg="#FFFFFF",relief=tkinter.FLAT)
        theEntry.place(x = 20,y = 45,width = width-40,height = lines * 20)
        theYPos = 45 + lines * 20    
    def submitDialog():    
        if lines == 1:    
            inputText = theEntryText.get()
        else:    
            inputText = theEntry.get('1.0',tkinter.END)
            inputText = inputText.strip()
            theEntryText.set(inputText)
        if callBackFunction:    
            callBackFunction(inputText)
        theInputDialog.destroy()
    def closeDialog():
        theInputDialog.destroy()

    centerX = int(width/2)
    theOKButton = tkinter.Button(theForm,anchor = tkinter.CENTER,text='确定',width = 100,height = 1,command=submitDialog)
    theOKButton.place(x = centerX - 110 ,y = theYPos + 10,width = 100,height = 30)
    theCancelButton = tkinter.Button(theForm,anchor = tkinter.CENTER,text='取消',width = 100,height = 1,command=closeDialog)
    theCancelButton.place(x = centerX + 10,y = theYPos + 10,width = 100,height = 30)
    tkinter.Tk.wait_window(theInputDialog)
    inputText = theEntryText.get()
    return inputText
   
def AskBox(title,text,parent=None):  
    PrintFunctionInfo(AskBox,[title,text,parent]) 
    #弹出一个选择对话框,你需要选择YES或NO。参数1 :对话框标题文字 ,参数2 :对话框显示文字,参数3:父窗口的uiName或root句柄 。  
    global G_TopDialog
    if G_TopDialog:    
        parent = G_TopDialog    
#res = tkinter.messagebox.askyesno(title,text,parent=parent)
    winhandle = None    
    try:    
        if parent:    
            if isinstance(parent,str) == True:    
                parent = GetElement(parent,'root')
                if parent :    
                    winhandle = parent.winfo_id()
            else:    
                winhandle = parent.winfo_id()
        elif G_TKRoot:    
            winhandle = G_TKRoot.winfo_id()
    except:    
        pass    
    import win32api    
    import win32con    
    ICONQUESTION=32 #警告图标    
    res =  win32api.MessageBox(winhandle,text,title,win32con.MB_YESNO|ICONQUESTION)
    if res == 6:    
        return True    
    return False    
def AskCancelBox(title,text,parent=None): 
    PrintFunctionInfo(AskCancelBox,[title,text,parent]) 
    #弹出一个选择对话框,你需要选择YES、NO或CANCEL。参数1 :对话框标题文字 ,参数2 :对话框显示文字，参数3:父窗口的uiName或root句柄 。  
    global G_TopDialog
    if G_TopDialog:    
        parent = G_TopDialog    
#res = tkinter.messagebox.askyesno(title,text,parent=parent)
    winhandle = None    
    try:    
        if parent:    
            if isinstance(parent,str) == True:    
                parent = GetElement(parent,'root')
                if parent :    
                    winhandle = parent.winfo_id()
            else:    
                winhandle = parent.winfo_id()
        elif G_TKRoot:    
            winhandle = G_TKRoot.winfo_id()
    except:    
        pass    
    import win32api    
    import win32con    
    ICONQUESTION=32 #警告图标    
    res =  win32api.MessageBox(winhandle,text,title,win32con.MB_YESNOCANCEL|ICONQUESTION)
    if res == 6:    
        return "Yes"    
    elif res == 7:    
        return "No"    
    return "Cancel"   
 
def SelectDirectory(title='选择路径',initDir = os.path.abspath('.'),parent=None):  
    PrintFunctionInfo(SelectDirectory,[title,initDir,parent])
    #打开查找目录对话框  
    #如果导入pywinauto会导致卡死，需要在导入前加入sys.coinit_flags = 2  
    global G_TopDialog
    if G_TopDialog:    
        parent = G_TopDialog    
    import tkinter.filedialog    
    openPath = tkinter.filedialog.askdirectory(title=title,initialdir=initDir,parent=parent)
    return openPath    
 
def SelectColor(title='请选择颜色'):  
    PrintFunctionInfo(SelectColor,[title])
    #打开选取颜色对话框  
    import tkinter.colorchooser    
    color = tkinter.colorchooser.askcolor(title=title)
    return color
 
def EnumFontName():    
    #罗列当前系统的所有文字  
    import tkinter.font    
    return tkinter.font.families()  

def WalkAllResFiles(parentPath,alldirs=True,extName=None):    
    #返回对应目录的所有指定类型文件。参数1 :目录名称 ,参数2 :是否进入子目录,参数3:是否有扩展名筛选 。  
    ResultFilesArray = []    
    if os.path.exists(parentPath) == True:    
        for fileName in os.listdir(parentPath):    
            if '__pycache__' not in fileName:    
                if '.git' not in fileName:    
                    newPath = os.path.join(parentPath,fileName)
                    newPath = newPath.replace("/","\\")
                    if os.path.isdir(newPath):    
                        if extName == None:    
                            ResultFilesArray.append(newPath)
                        if alldirs == True:    
                            ResultFilesArray.extend(WalkAllResFiles(newPath,alldirs,extName))
                    else:    
                        if extName == None:    
                            ResultFilesArray.append(newPath)
                        else:    
                            file_extension = os.path.splitext(fileName)[1].replace('.','')
                            file_extension_lower = file_extension.lower().strip()
                            if isinstance(extName,list) == True:    
                                extName_lower = [s.lower() for s in extName]    
                                if file_extension_lower in extName_lower:    
                                    ResultFilesArray.append(newPath)
                            else:    
                                file_extName_lower = extName.lower().strip()
                                if file_extension_lower == file_extName_lower:    
                                    ResultFilesArray.append(newPath)
    return ResultFilesArray    

def ImportResources(srcFile,coverMode=True):  
    PrintFunctionInfo(ImportResources,[srcFile,coverMode]) 
    #将文件复制到资源目录  
    try:     
        srcPathName,srcFileName = os.path.split(srcFile) 
        dstFile = os.path.join(G_ResDir,srcFileName) 
        if os.path.normcase(srcFile) != os.path.normcase(dstFile):     
            if os.path.exists(dstFile) == True and coverMode == True:     
                os.remove(dstFile) 
            shutil.copyfile(srcFile,dstFile)
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def CopyFile(srcFile,dstFile,coverMode=True):  
    PrintFunctionInfo(CopyFile,[srcFile,dstFile,coverMode]) 
    #复制文件  
    try:     
        if os.path.exists(dstFile) == True and coverMode == True:     
            os.remove(dstFile) 
        def CreateParentDir(PathName):    
            ParentPath,DirName = os.path.split(PathName)
            if os.path.exists(ParentPath) == False:    
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        dstPathName,dstFileName = os.path.split(dstFile)
        if os.path.exists(dstPathName) == False:    
            CreateParentDir(dstPathName)
        shutil.copyfile(srcFile,dstFile)
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def MoveFile(srcFile,dstFile,coverMode=True):    
    PrintFunctionInfo(MoveFile,[srcFile,dstFile,coverMode]) 
    #移动文件  
    try:     
        if os.path.exists(dstFile) == True and coverMode == True:     
            os.remove(dstFile) 
        shutil.move(srcFile,dstFile)
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def DeleteFile(dstFile):   
    PrintFunctionInfo(DeleteFile,[dstFile]) 
    #删除文件  
    if os.path.exists(dstFile) == True:     
        os.remove(dstFile)
def GetFileMD5(srcFile):  
    PrintFunctionInfo(GetFileMD5,[srcFile]) 
    #取得文件MD5码  
    import hashlib    
    try:    
        if os.path.exists(srcFile) == True:     
            with open(srcFile, 'rb') as file:    
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()
                return md5_hash    
    except Exception as ex:     
        print(ex) 
    return None    
def CompareFileMD5(srcFile,dstFile): 
    PrintFunctionInfo(CompareFileMD5,[srcFile,dstFile])  
    #比较两个文件是否一致  
    MD51 = GetFileMD5(srcFile)
    MD52 = GetFileMD5(dstFile) 
    return MD51 != None and MD51 == MD52    
def CreateDir(dstDir,coverMode=True):   
    PrintFunctionInfo(CreateDir,[dstDir,coverMode])  
    #创建目录  
    try:     
        if os.path.exists(dstDir) == True:     
            if coverMode == True:     
                shutil.rmtree(dstDir) 
            else:     
                return True     
        def CreateParentDir(PathName):    
            ParentPath,DirName = os.path.split(PathName)
            if ParentPath and os.path.exists(ParentPath) == False:    
                CreateParentDir(ParentPath)
            os.mkdir(PathName)
        CreateParentDir(dstDir)
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def CopyDir(srcDir,dstDir,coverMode=True): 
    PrintFunctionInfo(CopyDir,[srcDir,dstDir,coverMode])  
    #复制目录  
    try:     
        if os.path.exists(dstDir) == True and coverMode == True:     
            shutil.rmtree(dstDir) 
        shutil.copytree(srcDir, dstDir)
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def MoveDir(srcDir,dstDir,coverMode=True): 
    PrintFunctionInfo(MoveDir,[srcDir,dstDir,coverMode])   
    #移动目录  
    try:     
        if os.path.exists(dstDir) == True and coverMode == True:     
            shutil.rmtree(dstDir) 
        shutil.copytree(srcDir, dstDir) 
        shutil.rmtree(srcDir) 
        return True     
    except Exception as ex:     
        print(ex) 
    return False     
def DeleteDir(srcDir):    
    PrintFunctionInfo(DeleteDir,[srcDir])   
    #删除目录  
    return shutil.rmtree(srcDir)
def CheckIsDir(srcDir):
    PrintFunctionInfo(CheckIsDir,[srcDir])       
    #判断是否是目录  
    return os.path.isdir(srcDir)
def CheckExist(srcDir):
    PrintFunctionInfo(CheckExist,[srcDir])       
    #判断文件或目录是否存在  
    return os.path.exists(srcDir)
def GetFileExtension(srcFile):  
    PrintFunctionInfo(GetFileExtension,[srcFile])       
    #取得文件扩展名  
    pathName,fileName = os.path.split(srcFile)
    shotname,extension = os.path.splitext(fileName)
    return extension    
 
def SetControlPack(uiName,elementName,fill,side,padx,pady,expand,width=0,height=0): 
    PrintFunctionInfo(SetControlPack,[uiName,elementName,fill,side,padx,pady,expand,width,height])       
    #设置控件的打包布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :填充方式,参数4:方位 ,参数5 :横向边距,参数6:纵向边距。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
        Control.pack(fill = fill,side = side,padx = padx,pady = pady,expand = expand)
        if expand == 0:    
            Control.pack_propagate(0)
            try:    
                Control.configure(width=width)
                Control.configure(height=height)
            except:    
                pass    
        PackDictionary = {}    
        PackDictionary["type"] = "pack"    
        PackDictionary["fill"] = fill    
        PackDictionary["side"] = side    
        PackDictionary["padx"] = padx    
        PackDictionary["pady"] = pady    
        PackDictionary["expand"] = expand    
        PackDictionary["visible"] = True    
        G_UIElementPlaceDictionary[uiName][elementName]=PackDictionary   
 
def SetControlGrid(uiName,elementName,row,column,rowspan,columnspan):  
    PrintFunctionInfo(SetControlGrid,[uiName,elementName,row,column,rowspan,columnspan])  
    #设置控件的表格布局。参数1 :界面类名, 参数2:控件名称 ,参数3 :行位置,参数4:列位置 ,参数5 :合并行数,参数6:合并列数。  
    Control = GetElement(uiName,elementName) 
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
        Control.grid(row = row,column = column,rowspan = rowspan,columnspan = columnspan)
        GridDictionary = {}    
        GridDictionary["type"] = "grid"    
        GridDictionary["row"] = row    
        GridDictionary["column"] = column    
        GridDictionary["rowspan"] = rowspan    
        GridDictionary["columnspan"] = columnspan    
        GridDictionary["visible"] = True    
        G_UIElementPlaceDictionary[uiName][elementName]=GridDictionary  
  
def SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint='nw',visible=True,modify=True): 
    PrintFunctionInfo(SetControlPlace,[uiName,elementName,x,y,w,h,anchorpoint,visible,modify])  
    #设置控件的绝对或相对位置。参数1 :界面类名, 参数2:控件名称 ,参数3 :x位置,参数4:y位置 ,参数5 :宽度,参数6:高度 。  
    Control = GetElement(uiName,elementName) 
    OldControl = Control     
    if Control:     
        if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
            elementName = G_UIElementAliasDictionary[uiName][elementName]     
        if hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
    def getXW(value):    
        return value    
    def getYH(value):    
        return value    
    if Control != None:    
        ParentWidth,ParentHeight = GetUIRootSize(uiName)
        try:    
            PlaceInfo = Control.place_info()
            if len(PlaceInfo) > 0:    
                #避免拖动窗体时闪烁    
                if ("relx" in PlaceInfo and float(PlaceInfo["relx"]) > 0) or ("rely" in PlaceInfo and float(PlaceInfo["rely"]) > 0) :    
                    Control.place_forget()
        except Exception as ex:    
#对于某些非界面组件也调用了，就直接返回
            return    
        Control.place(x=0,y=0,width=0,height=0)
        if type(x) == type(1.0):    
            if type(y) == type(1.0):    
                if type(w) == type(1.0):    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(relx=x,rely=y,relwidth=w,relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(relx=x,rely=y,relwidth=w,height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                else:    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(relx=x,rely=y,width=getXW(w),relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(relx=x,rely=y,width=getXW(w),height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
            else:    
                if type(w) == type(1.0):    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(relx=x,y=getYH(y),relwidth=w,relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(relx=x,y=getYH(y),relwidth=w,height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                else:    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(relx=x,y=getYH(y),width=w,relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(relx=x,y=getYH(y),width=w,height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["relx"] = x    
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
        else:    
            if type(y) == type(1.0):    
                if type(w) == type(1.0):    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(x=getXW(x),rely=y,relwidth=w,relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(x=getXW(x),rely=y,relwidth=w,height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                else:    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(x=getXW(x),rely=y,width=getXW(w),relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(x=getXW(x),rely=y,width=getXW(w),height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["rely"] = y    
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
            else:    
                if type(w) == type(1.0):    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(x=getXW(x),y=getYH(y),relwidth=w,relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:    
                        if visible == True:    
                            Control.place(x=getXW(x),y=getYH(y),relwidth=w,height=getYH(h))
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["relwidth"] = w    
                            PlaceDictionary["height"] = getYH(h)
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                else:    
                    if type(h) == type(1.0):    
                        if visible == True:    
                            Control.place(x=getXW(x),y=getYH(y),width=getXW(w),relheight=h)
                        if modify == True:    
                            PlaceDictionary = {}    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["width"] = getXW(w)
                            PlaceDictionary["relheight"] = h    
                            PlaceDictionary["visible"] = visible    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
                    else:
                        PlaceDictionary = {}    
                        if h == '' and w == '':    
                            if visible == True:    
                                Control.place(x=getXW(x),y=getYH(y))
                            if modify == True:    
                                PlaceDictionary["width"] = ''    
                                PlaceDictionary["height"] = ''    
                        elif h == '':    
                            if visible == True:    
                                Control.place(x=getXW(x),y=getYH(y),width=getXW(w))
                            if modify == True:    
                                PlaceDictionary["width"] = getXW(w)
                                PlaceDictionary["height"] = ''    
                        elif w == '':    
                            if visible == True:    
                                Control.place(x=getXW(x),y=getYH(y),height=getYH(h))
                            if modify == True:    
                                PlaceDictionary["width"] = ''    
                                PlaceDictionary["height"] = getYH(h)
                        else:    
                            if visible == True:    
                                Control.place(x=getXW(x),y=getYH(y),width=getXW(w),height=getYH(h))
                            if modify == True:    
                                PlaceDictionary["width"] =  getXW(w)
                                PlaceDictionary["height"] = getYH(h)
                        if modify == True:    
                            PlaceDictionary["type"] = "place"    
                            PlaceDictionary["x"] = getXW(x)
                            PlaceDictionary["y"] = getYH(y)
                            PlaceDictionary["visible"] = True    
                            PlaceDictionary["anchorpoint"] = anchorpoint    
                            G_UIElementPlaceDictionary[uiName][elementName]=PlaceDictionary    
    if Control != None and visible == True:    
        Control.update()
        if elementName.find("Frame_") >= 0 or elementName.find("LabelFrame_") >= 0 or elementName.find("PanedWindow_") >= 0:    
            for childWidgetName in Control.children.keys():    
                frameCanvas = Control.children[childWidgetName]    
                for uiName in G_UIElementDictionary.keys():    
                    if G_UIElementDictionary[uiName]["root"] is frameCanvas:    
                        if "UIClass" in  G_UIElementDictionary[uiName].keys():    
                            uiClass = GetElement(uiName,"UIClass")
                            if uiClass:    
                                Form_1 = GetElement(uiName,"Form_1")
                                if Form_1:    
                                    Form_1_Width = frameCanvas.winfo_width()
                                    Form_1_Height = frameCanvas.winfo_height()
                                    event = ChartEvent(Form_1_Width,Form_1_Height,Form_1)
                                    if hasattr(uiClass,"Configure") == True:    
                                        uiClass.Configure(event)
    if elementName.find("LabelButton_") >= 0 or elementName.find("Entry") >= 0 or elementName.find("Text") >= 0:    
        if hasattr(OldControl,"Configure") == True:    
            event = ChartEvent(w,h,OldControl)
            OldControl.Configure(event)
    if elementName.find("Calendar_") >= 0 or elementName.find("DatePicker_") >= 0 or elementName.find("Navigation_") >= 0 or elementName.find("ListMenu_") >= 0 or elementName.find("SwitchPage_") >= 0 or elementName.find("ShowCase_") >= 0:    
        if visible == False:    
            if hasattr(OldControl,"Hide") == True:    
                OldControl.Hide()
    if anchorpoint !='nw':    
        UpdateElementPlace(uiName,elementName)
# def ResizeControlImage(uiName,elementName):    
#     #设置控件的背景图片(Label,Button,Text)。参数1 :界面类名, 参数2:控件名称,参数3:图片名称。  
#     Control = GetElement(uiName,elementName) 
#     if Control:     
#         Control_Width = Control.winfo_width() 
#         Control_Height = Control.winfo_height() 
#         realElementName = elementName     
#         if uiName in G_UIElementAliasDictionary.keys() and elementName in G_UIElementAliasDictionary[uiName].keys():    
#             realElementName = G_UIElementAliasDictionary[uiName][elementName]     
#         if realElementName:    
#             if uiName in G_UIElementUserDataArray:    
#                 if realElementName in G_UIElementUserDataArray[uiName]:    
#                     for EBData in G_UIElementUserDataArray[uiName][realElementName]:       
#                         if EBData[0] == 'image' and EBData[1] == 'imageInfo':    
#                             imagePath = EBData[2][1]    
#                             autoSize = EBData[2][2]    
#                             from   PIL import Image,ImageTk    
#                             imagePath_Lower = imagePath.lower()
#                             if os.path.exists(imagePath) == False:    
#                                 if imagePath_Lower in G_ResourcesFileList:    
#                                    imagePath = G_ResourcesFileList[imagePath_Lower]    
#                                 if os.path.exists(imagePath) == False:    
#                                     return    
#                             image=Image.open(imagePath).convert('RGBA')
#                             if autoSize == True:    
#                                 image_Resize = image.resize((Control_Width, Control_Height),Image.LANCZOS)
#                             else:    
#                                 image_Resize = image    
#                             EBData[2][0] = ImageTk.PhotoImage(image_Resize)
#                             if realElementName.find('Label_') >= 0 or realElementName.find('Button_') >= 0 :    
#                                 Control.configure(image = EBData[2][0])
#                             elif realElementName.find('Text_') >= 0:     
#                                 Control.delete('0.0',tkinter.END)
#                                 Control.image_create(tkinter.END, image=newPTImage)

def GetControlPlace_AnchorPoint(uiName,elementName):   
    PrintFunctionInfo(GetControlPlace_AnchorPoint,[uiName,elementName])  
    if uiName not in G_UIElementPlaceDictionary:    
        return    
    RealElementName = elementName    
    if uiName in G_UIElementAliasDictionary.keys() and RealElementName in G_UIElementAliasDictionary[uiName].keys():    
        RealElementName = G_UIElementAliasDictionary[uiName][RealElementName]     
    anchorPoint = 'nw'    
    if RealElementName in  G_UIElementPlaceDictionary[uiName].keys():    
        if "anchorpoint" in G_UIElementPlaceDictionary[uiName][RealElementName]:    
            anchorPoint = G_UIElementPlaceDictionary[uiName][RealElementName]["anchorpoint"]    
    return anchorPoint    

def UpdateAllElementPlace(uiName,HScrollBarOffsetY=0,VScrollBarOffsetX=0):  
    PrintFunctionInfo(UpdateAllElementPlace,[uiName,HScrollBarOffsetY,VScrollBarOffsetX])  
    #按参考位置更新控件位置  
    if uiName not in G_UIElementPlaceDictionary:    
        return    
    for elementName in G_UIElementPlaceDictionary[uiName]:    
        if elementName == "Form_1":    
            continue    
        UpdateElementPlace(uiName,elementName,HScrollBarOffsetY,VScrollBarOffsetX)
def UpdateElementPlace(uiName,elementName,HScrollBarOffsetY=0,VScrollBarOffsetX=0):  
    PrintFunctionInfo(UpdateElementPlace,[uiName,elementName,HScrollBarOffsetY,VScrollBarOffsetX])  
    #按参考位置更新控件位置  
    def getPercentXY(x,y,width,height,parentWidth,parentHeight,anchorpoint):    
        if width =='' or height == '':    
            return x,y    
        if isinstance(x,float) == True:    
            x = x * parentWidth    
        if isinstance(y,float) == True:    
            y = y * parentHeight    
        anchorX = x / parentWidth    
        anchorY = y / parentHeight    
        return anchorX,anchorY    
    if uiName not in G_UIElementPlaceDictionary:    
        return    
    if elementName in G_UIElementPlaceDictionary[uiName]:    
        Control = G_UIElementDictionary[uiName][elementName]    
        if hasattr(Control,"GetEntry") == True:    
            Control = Control.GetEntry()
        elif hasattr(Control,"GetWidget") == True:    
            Control = Control.GetWidget()
        ControlParentInfo = Control.winfo_parent()
        ControlParentWidget = Control._nametowidget(ControlParentInfo)
        ParentWidth = ControlParentWidget.winfo_width()
        ParentHeight = ControlParentWidget.winfo_height()
        if ParentWidth == 1 and ParentHeight == 1:    
            return  
        if isinstance(ControlParentWidget,tkinter.Canvas) == True:
            uiName,parentElementName = GetElementName(ControlParentWidget)
            if parentElementName == "Form_1":
                ParentWidth = ControlParentWidget.master.winfo_width()
                ParentHeight = ControlParentWidget.master.winfo_height()
        Visible = True    
        if "visible" in G_UIElementPlaceDictionary[uiName][elementName]:    
            Visible = G_UIElementPlaceDictionary[uiName][elementName]["visible"]    
        PlaceType = "pack"    
        if "type" in G_UIElementPlaceDictionary[uiName][elementName]:    
            PlaceType = G_UIElementPlaceDictionary[uiName][elementName]["type"]    
        if Visible == True:    
            if PlaceType == "place":    
                x = 0    
                if "x" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    x = G_UIElementPlaceDictionary[uiName][elementName]["x"]    
                elif "relx" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    x = G_UIElementPlaceDictionary[uiName][elementName]["relx"]    
                y = 0    
                if "y" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    y = G_UIElementPlaceDictionary[uiName][elementName]["y"]    
                elif "rely" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    y = G_UIElementPlaceDictionary[uiName][elementName]["rely"]    
                w = 0    
                if "width" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    w = G_UIElementPlaceDictionary[uiName][elementName]["width"]    
                elif "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    w = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]    
                h = 0    
                if "height" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    h = G_UIElementPlaceDictionary[uiName][elementName]["height"]    
                elif "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    h = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]    
                if "anchorpoint" in G_UIElementPlaceDictionary[uiName][elementName]:    
                    anchorpoint = G_UIElementPlaceDictionary[uiName][elementName]["anchorpoint"]    
                    ax,ay = getPercentXY(x,y,w,h,ParentWidth,ParentHeight,anchorpoint)
                    if anchorpoint == "n":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:    
                                x = int(ax * ParentWidth - w * 0.5)
                        #x = int(ax * ParentWidth - w * 0.5)
                    elif anchorpoint == "ne":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth  - w * ParentWidth)
                            else:    
                                x = int(ax * ParentWidth  - w)
                        #x = int(ax * ParentWidth - w)
                    elif anchorpoint == "w":    
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:    
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight    
                            else:    
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight    
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:    
                                y = int(ay * ParentHeight - h * 0.5)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "center":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:    
                                x = int(ax * ParentWidth - w * 0.5)
                        if isinstance(y,float) == True:        
                            if isinstance(h,float) == True:    
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight    
                            else:    
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight    
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:    
                                y = int(ay * ParentHeight - h * 0.5)
                        #x = int(ax * ParentWidth - w * 0.5)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "e":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth - w * ParentWidth)
                            else:    
                                x = int(ax * ParentWidth - w)
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:    
                                y = (ay * ParentHeight - h * ParentHeight * 0.5)/ParentHeight    
                            else:    
                                y = (ay * ParentHeight - h * 0.5)/ParentHeight    
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight * 0.5)
                            else:    
                                y = int(ay * ParentHeight - h * 0.5)
                        #x = int(ax * ParentWidth - w)
                        #y = int(ay * ParentHeight - h * 0.5)
                    elif anchorpoint == "sw":    
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:    
                                y = (ay * ParentHeight - h * ParentHeight )/ParentHeight    
                            else:    
                                y = (ay * ParentHeight - h )/ParentHeight    
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:    
                                y = int(ay * ParentHeight - h )
                        #y = int(ay * ParentHeight - h)
                    elif anchorpoint == "s":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth * 0.5)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w * 0.5)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth - w * ParentWidth * 0.5)
                            else:    
                                x = int(ax * ParentWidth - w * 0.5)
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight )/ParentHeight    
                            else:    
                                y = int(ay * ParentHeight - h )
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:    
                                y = int(ay * ParentHeight - h )
                        # x = int(ax * ParentWidth - w * 0.5)
                        # y = int(ay * ParentHeight - h)
                    elif anchorpoint == "se":    
                        if isinstance(x,float) == True:    
                            if isinstance(w,float) == True:    
                                x = (ax * ParentWidth - w * ParentWidth)/ParentWidth    
                            else:    
                                x = (ax * ParentWidth - w)/ParentWidth    
                        else:    
                            if isinstance(w,float) == True:    
                                x = int(ax * ParentWidth - w * ParentWidth)
                            else:    
                                x = int(ax * ParentWidth - w)
                        if isinstance(y,float) == True:    
                            if isinstance(h,float) == True:    
                                y = (ay * ParentHeight - h * ParentHeight )/ParentHeight    
                            else:    
                                y = (ay * ParentHeight - h )/ParentHeight    
                        else:    
                            if isinstance(h,float) == True:    
                                y = int(ay * ParentHeight - h * ParentHeight )
                            else:    
                                y = int(ay * ParentHeight - h )
                        #x = int(ax * ParentWidth - w)
                        #y = int(ay * ParentHeight - h)
                for aliasName in  G_UIElementAliasDictionary[uiName].keys():    
                    if G_UIElementAliasDictionary[uiName][aliasName] == elementName:    
                        SetControlPlace(uiName,aliasName,x,y,w,h,'nw',True,False)
                        break    
            else:    
                Control.update()
                x = Control.winfo_x()
                y = Control.winfo_y()
                w = Control.winfo_width()
                h = Control.winfo_height()
            Width_PX = w    
            if isinstance(w,float) == True:    
                Width_PX = int(w * ParentWidth)
            Height_PX = h    
            if isinstance(h,float) == True:    
                Height_PX = int(h * ParentHeight)
            HScrollbarName = elementName + "_HScrollbar"    
            HScrollbar= GetElement(uiName,HScrollbarName)
            if HScrollbar:  
                if elementName.find("LabelFrame") >= 0 :
                    HScrollbar.place(x = 0,y = Height_PX-46+HScrollBarOffsetY,width = Width_PX,height = 20)
                else:
                    HScrollbar.place(x = 0,y = Height_PX-20+HScrollBarOffsetY,width = Width_PX,height = 20)
            VScrollbarName = elementName + "_VScrollbar"    
            VScrollbar= GetElement(uiName,VScrollbarName)
            if VScrollbar:    
                if elementName.find("LabelFrame") >= 0 :
                    VScrollbar.place(x = Width_PX-20+VScrollBarOffsetX,y = 0,width = 20,height = Height_PX-30)
                else:
                    VScrollbar.place(x = Width_PX-20+VScrollBarOffsetX,y = 0,width = 20,height = Height_PX)
            VScrollbarName = elementName + "_Scrollbar"    
            VScrollbar= GetElement(uiName,VScrollbarName)
            if VScrollbar:    
                VScrollbar.place(x = Width_PX-20+VScrollBarOffsetX,y = 0,width = 20,height = Height_PX)
            ChildCanvasName = elementName + "_Child"    
            ChildCanvas = GetElement(uiName,ChildCanvasName)
            if ChildCanvas:    
                ChildHandleName = elementName + "_ChildHandle"    
                ChildHandle = GetElement(uiName,ChildHandleName)
                if ChildHandle:       
                    ChildCanvas.itemconfig(ChildHandle,width=ParentWidth,height=ParentHeight)       
                    ChildCanvas.config(scrollregion=(0,0,ParentWidth,ParentHeight))  
            if uiName in G_UILoadPageDictionary:
                if elementName in G_UILoadPageDictionary[uiName]:
                    for PageInstance in G_UILoadPageDictionary[uiName][elementName]:
                        if hasattr(PageInstance,"Configure") == True:      
                            event = ChartEvent(Width_PX,Height_PX,PageInstance.root)
                            PageInstance.Configure(event)
                            ChildWidgetList = PageInstance.root.children    
                            for childKey in ChildWidgetList.keys():    
                                Form_1 = ChildWidgetList[childKey]    
                                event = ChartEvent(Width_PX,Height_PX,Form_1)
                                PageInstance.Configure(event)    
            if uiName in G_UIElementUserDataArray:    
                if elementName in G_UIElementUserDataArray[uiName]:    
                    for EBData in G_UIElementUserDataArray[uiName][elementName]:       
                        if EBData[0] == 'image' and EBData[1] == 'imageInfo':  
                            for imageInfo in EBData[2]:       
                                oldImagePT = imageInfo[0]    
                                if oldImagePT.width() == 1 and oldImagePT.height() == 1:    
                                    imagePath = imageInfo[1]    
                                    autoSize = imageInfo[2]    
                                    from   PIL import Image,ImageTk    
                                    imagePath_Lower = imagePath.lower()
                                    if os.path.exists(imagePath) == False:    
                                        if imagePath_Lower in G_ResourcesFileList:    
                                            imagePath = G_ResourcesFileList[imagePath_Lower]    
                                        if os.path.exists(imagePath) == False:    
                                            continue    
                                    image=Image.open(imagePath).convert('RGBA')
                                    if autoSize == True:    
                                        image_Resize = image.resize((Width_PX, Height_PX),Image.LANCZOS)
                                    else:    
                                        image_Resize = image    
                                    imageInfo[0] = ImageTk.PhotoImage(image_Resize)
                                    if elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 :    
                                        if imageInfo[2] == 'selected':    
                                            Control.configure(selectimage = imageInfo[0])
                                        else:   
                                            Control.configure(image = imageInfo[0])
                                    elif elementName.find('Text_') >= 0:     
                                        Control.delete('0.0',tkinter.END)
                                        Control.image_create(tkinter.END, image=imageInfo[0])
def SetUIRootSize(uiName,width,height,scale=1.0): 
    PrintFunctionInfo(SetUIRootSize,[uiName,width,height,scale])  
    global G_RootSize    
    global G_UIScale    
    if uiName in G_UIRootSizeDictionary:    
        G_UIRootSizeDictionary[uiName]["width"] = width    
        G_UIRootSizeDictionary[uiName]["height"] = height    
        G_UIRootSizeDictionary[uiName]["scale"] = scale    
        if "init" not in G_UIRootSizeDictionary[uiName].keys():    
            G_UIRootSizeDictionary[uiName]["init"] = [width,height]    
    else:    
        G_RootSize = [width,height]    
        G_UIScale = scale    
def GetUIRootSize(uiName,init=False):   
    PrintFunctionInfo(GetUIRootSize,[uiName,init])  
    global G_RootSize    
    if uiName in G_UIRootSizeDictionary:    
        if init == True and "init" in G_UIRootSizeDictionary[uiName]:    
            return G_UIRootSizeDictionary[uiName]["init"][0],G_UIRootSizeDictionary[uiName]["init"][1]    
        if "width" in G_UIRootSizeDictionary[uiName].keys() and "height" in G_UIRootSizeDictionary[uiName].keys():    
            return G_UIRootSizeDictionary[uiName]["width"],G_UIRootSizeDictionary[uiName]["height"]    
    return G_RootSize    

def ResizeRoot(uiName,root,event):    
    PrintFunctionInfo(ResizeRoot,[uiName,root,event])  
    if isinstance(root,tkinter.Frame) == True or isinstance(root,tkinter.LabelFrame) == True or isinstance(root,tkinter.ttk.Frame) == True:    
        oldWidth  = root.winfo_width()
        oldHeight = root.winfo_height()
        if oldWidth== event.width and oldHeight== event.height:    
            return     
        event.width = oldWidth    
        event.height = oldHeight    
        Form_1 = GetElement(uiName,'Form_1')
        if Form_1:    
            Form_1.configure(width = event.width)
            Form_1.configure(height = event.height)
        HScrollBarOffsetY = 0    
        VScrollBarOffsetX = 0    
        if isinstance(root,tkinter.LabelFrame) == True:    
            HScrollBarOffsetY = -30    
        UpdateAllElementPlace(uiName,HScrollBarOffsetY,VScrollBarOffsetX)
    else:
        UpdateAllElementPlace(uiName)
#     for elementName in G_UIElementPlaceDictionary[uiName]:    
#         PlaceDictionary = G_UIElementPlaceDictionary[uiName][elementName]    
#         if "anchorpoint" in PlaceDictionary:    
#             anchorpoint = PlaceDictionary["anchorpoint"]    
#             if anchorpoint != "nw":    
#                 x = 0    
#                 if "relx" in PlaceDictionary:    
#                     x = PlaceDictionary["relx"]    
#                 else:    
#                     x = PlaceDictionary["x"]    
#                 y = 0    
#                 if "rely" in PlaceDictionary:    
#                     y = PlaceDictionary["rely"]    
#                 else:    
#                     y = PlaceDictionary["y"]    
#                 w = 0    
#                 if "relwidth" in PlaceDictionary:    
#                     w = PlaceDictionary["relwidth"]    
#                 else:    
#                     w = PlaceDictionary["width"]    
#                 h = 0    
#                 if "relheight" in PlaceDictionary:    
#                     h = PlaceDictionary["relheight"]    
#                 else:    
#                     h = PlaceDictionary["height"]    
#                 SetControlPlace(uiName,elementName,x,y,w,h,anchorpoint)
    SetUIRootSize(uiName,event.width,event.height)
 
def SetElementLayer(uiName,elementName,direction='lift'):    
    #设置控件的层次升降。参数1 :界面类名, 参数2:控件名称 ,参数3 :升降方向 lift 为提升,lower 为降低,top 为置顶,bottom 为置底。  
        
    if uiName in G_UIElementDictionary.keys():    
        G_UIElementLayerDictionary[uiName][elementName] = direction  
 
def DoCanvasRecord(drawCanvas,shapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag=''):    
    PrintFunctionInfo(DoCanvasRecord,[drawCanvas,shapeType,x,y,x2,y2,fillcolor,outlinecolor,fillwidth,dash1,dash2,newImage,text,textFont ,textColor,shapeTag])  
    #画板动作处理函数  
    if  drawCanvas != None: 
        drawCanvas_width = drawCanvas.winfo_width()
        drawCanvas_height = drawCanvas.winfo_height()
        if isinstance(x,float) == True:    
            x = int(x * drawCanvas_width)  
        if isinstance(x2,float) == True:    
            x2 = int(x2 * drawCanvas_width)  
        if isinstance(y,float) == True:    
            y = int(y * drawCanvas_height)  
        if isinstance(y2,float) == True:    
            y2 = int(y2 * drawCanvas_height)  
 
        if shapeType == 'line' or shapeType == 'pen':
            if  dash1 > 0 :    
                drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:    
                uiName,drawCanvasName = GetElementName(drawCanvas)
                if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName].keys():    
                    if G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5]:    
                        left = x    
                        right = x2    
                        if x2 < x:    
                            left = x2    
                            right = x    
                        top = y    
                        bottom = y2            
                        if y2 < y:    
                            top = y2    
                            bottom = y    
                        width = right - left + 2 * fillwidth    
                        height = bottom - top + 2 * fillwidth    
                        startx = x-left+fillwidth    
                        starty =  y-top+fillwidth    
                        endx = x2-left+fillwidth    
                        endy = y2-top+fillwidth    
                        img = Image.new('RGBA', (width, height), '#00000000')
                        draw = aggdraw.Draw(img)
                        p = aggdraw.Pen(fillcolor,fillwidth)
                        draw.line((x-left+fillwidth,y-top+fillwidth,x2-left+fillwidth,y2-top+fillwidth), p)
                        draw.flush()
                        newImage = ImageTk.PhotoImage(img)
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage    
                        drawCanvas.create_image(left-fillwidth, top-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
                    else:    
                        drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,width = fillwidth,tag=shapeTag)
                else:    
                    drawCanvas.create_line(x, y, x2, y2, fill=fillcolor,width = fillwidth,tag=shapeTag)
    
        elif shapeType == 'arrow':    
            if  dash1 > 0 :    
                drawCanvas.create_line(x, y, x2, y2, arrow=tkinter.LAST,fill=fillcolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:    
                drawCanvas.create_line(x, y, x2, y2,arrow=tkinter.LAST,fill=fillcolor, width = fillwidth,tag=shapeTag)
        elif shapeType.find('triangle') == 0:    
            width = x2 - x    
            height = y2 - y    
            direction = 'up'    
            if shapeType.find('_left')>0:    
                direction = 'left'    
            elif shapeType.find('_right')>0:    
                direction = 'right'    
            elif shapeType.find('_down')>0:    
                direction = 'down'    
            if direction == 'left':    
                points = [    
                    x,    
                    y + int(height/2),    
                    x + width,    
                    y ,    
                    x + width,    
                    y + height,    
                    x,    
                    y + int(height/2),]    
            elif direction == 'right':    
                points = [    
                    x,    
                    y,    
                    x + width,    
                    y + int(height/2) ,    
                    x,    
                    y + height,    
                    x,    
                    y,]    
            elif direction == 'down':    
                points = [    
                    x,    
                    y,    
                    x + width,    
                    y,    
                    x + int(width/2),    
                    y + height,    
                    x,    
                    y,]    
            else:    
                points = [    
                    x,    
                    y + height,    
                    x + int(width/2),    
                    y ,    
                    x + width,    
                    y + height,    
                    x,    
                    y + height,]    
            if  fillcolor.find('#') < 0:    
                if  dash1 > 0 :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill='',    
                        outline=outlinecolor,    
                        width= fillwidth,    
                        dash=(dash1,dash2),    
                        tag=shapeTag)
                else :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill='',    
                        outline=outlinecolor,    
                        width= fillwidth,    
                        tag=shapeTag)
            else:    
                if  dash1 > 0 :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill=fillcolor,    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        dash=(dash1,dash2),    
                        tag=shapeTag)
                else :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill=fillcolor,    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        tag=shapeTag)
        elif shapeType == 'diamond':    
            width = x2 - x    
            height = y2 - y    
            points = [    
                x,    
                y + int(height/2),    
                x + int(width/2),    
                y ,    
                x + width,    
                y + int(height/2),    
                x + int(width/2),    
                y + height,]    
            if  fillcolor.find('#') < 0:    
                if  dash1 > 0 :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill='',    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        dash=(dash1,dash2),    
                        tag=shapeTag)
                else :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill='',    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        tag=shapeTag)
            else:    
                if  dash1 > 0 :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill=fillcolor,    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        dash=(dash1,dash2),    
                        tag=shapeTag)
                else :    
                    drawCanvas.create_polygon(    
                        points,    
                        fill=fillcolor,    
                        outline=outlinecolor,     
                        width= fillwidth,    
                        tag=shapeTag)
        elif shapeType == 'rect':    
            if  fillcolor.find('#') < 0:    
                if  dash1 > 0 :    
                    drawCanvas.create_rectangle(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:    
                    drawCanvas.create_rectangle(x, y, x2, y2,outline=outlinecolor, width = fillwidth,tag=shapeTag)
            else:    
                if  dash1 > 0 :    
                    drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:    
                    drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor,outline=outlinecolor, width = fillwidth,tag=shapeTag)
        elif shapeType == 'roundrect':    
            width = x2 - x    
            height = y2 - y    
            if newImage:    
                roundRadius = int(newImage)
            else:    
                roundRadius = int(0.2 * height)
            if roundRadius == 0:    
                if  fillcolor.find('#') < 0:    
                    if  dash1 > 0 :    
                        drawCanvas.create_rectangle(x, y, x2, y2, fill='',outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:    
                        drawCanvas.create_rectangle(x, y, x + width,y + height,fill='', outline=outlinecolor,width = fillwidth,tag=shapeTag)
                else:    
                    if  dash1 > 0 :    
                        drawCanvas.create_rectangle(x, y, x2, y2, fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    else:    
                        drawCanvas.create_rectangle(x, y, x + width,y + height,fill=fillcolor, outline=outlinecolor,width = fillwidth,tag=shapeTag)
            else:    
                if  fillcolor.find('#') == 0:    
                    drawCanvas.create_rectangle(x+roundRadius,y+roundRadius,x+width-roundRadius, y+height-roundRadius,fill=fillcolor, width = 0,tag=shapeTag)
                    drawCanvas.create_rectangle(x+roundRadius,y,x+width-roundRadius,y+roundRadius,fill=fillcolor, width=0,tag=shapeTag)
                    drawCanvas.create_rectangle(x+roundRadius,y+height-roundRadius,x+width-roundRadius,y+height,fill=fillcolor, width=0,tag=shapeTag)
                    drawCanvas.create_rectangle(x,y+roundRadius,x+roundRadius,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
                    drawCanvas.create_rectangle(x+width-roundRadius,y+roundRadius,x+width,y+height-roundRadius,fill=fillcolor,width=0,tag=shapeTag)
            OutLineTag = shapeTag+"_outline"    
            if fillwidth > 0:    
                if  dash1 > 0:    
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,dash=(dash1,dash2),width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,dash=(dash1,dash2),tag=OutLineTag,width=fillwidth)
                else:    
                    drawCanvas.create_line(x+roundRadius,y,x+width-roundRadius,y,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+roundRadius,y+height,x+width-roundRadius,y+height,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x,y+roundRadius,x,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
                    drawCanvas.create_line(x+width,y+roundRadius,x+width,y+height-roundRadius,fill=outlinecolor,tag=OutLineTag,width=fillwidth)
            if  fillcolor.find('#') == 0:    
                drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
                drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,fill=fillcolor,outline=fillcolor,width=0,tag=shapeTag)
            OutArcTag = shapeTag+"_arc"    
            if fillwidth > 0:    
                if  dash1 > 0:    
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,dash=(dash1,dash2),width=fillwidth, style='arc',tag=OutArcTag)
                else:    
                    drawCanvas.create_arc(x,y,x+2*roundRadius,y+2*roundRadius,start=180,extent=-90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y,x+width,y+2*roundRadius,extent=90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x+width-2*roundRadius,y+height-2*roundRadius,x+width,y+height,extent=-90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
                    drawCanvas.create_arc(x,y+height-2*roundRadius,x+2*roundRadius,y+height,start=180,extent=90,outline=outlinecolor,width=fillwidth, style='arc',tag=OutArcTag)
        elif shapeType == 'circle':
 
            if  fillcolor.find('#') < 0:    
                if  dash1 > 0 :    
                    drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:    
                    width = x2 - x + 2 * fillwidth    
                    height = y2 - y + 2 * fillwidth    
                    img = Image.new('RGBA', (width, height), '#00000000')
                    draw = aggdraw.Draw(img)
                    p = aggdraw.Pen(outlinecolor,fillwidth)
                    draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p)
                    draw.flush()
                    newImage = ImageTk.PhotoImage(img)
                    uiName,drawCanvasName = GetElementName(drawCanvas)
                    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage    
                    drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
            else:    
                if  dash1 > 0 :    
                    width = x2 - x + 2 * fillwidth    
                    height = y2 - y + 2 * fillwidth    
                    img = Image.new('RGBA', (width, height), '#00000000')
                    draw = aggdraw.Draw(img)
                    p = aggdraw.Pen(outlinecolor,0)
                    b = aggdraw.Brush(fillcolor)
                    draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p, b)
                    draw.flush()
                    newImage = ImageTk.PhotoImage(img)
                    uiName,drawCanvasName = GetElementName(drawCanvas)
                    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage    
                    drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
                    drawCanvas.create_oval(x, y, x2, y2, outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                else:    
                    width = x2 - x + 2 * fillwidth    
                    height = y2 - y + 2 * fillwidth    
                    img = Image.new('RGBA', (width, height), '#00000000')
                    draw = aggdraw.Draw(img)
                    p = aggdraw.Pen(outlinecolor,fillwidth)
                    b = aggdraw.Brush(fillcolor)
                    draw.ellipse((fillwidth,fillwidth,width-fillwidth,height-fillwidth), p, b)
                    draw.flush()
                    newImage = ImageTk.PhotoImage(img)
                    uiName,drawCanvasName = GetElementName(drawCanvas)
                    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][5] = newImage    
                    drawCanvas.create_image(x-fillwidth, y-fillwidth,image=newImage,anchor='nw',tag=shapeTag)
 
        elif shapeType == 'cylinder':      
            width = x2 - x    
            height = y2 - y    
            OvalHeight = height * 0.2    
            OvalHeight_Half = height * 0.1    
            OutLineTag = shapeTag+"_outline"    
            if  fillcolor.find('#') < 0:    
                if  dash1 > 0 :    
                    drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill='',outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill='',width=0,tag=shapeTag)
                    drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill='',outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                else:    
                    drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill='',outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill='',width=0,tag=shapeTag)
                    drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill='',outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
            else:    
                if  dash1 > 0 :    
                    drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                    drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=OutLineTag)
                else:    
                    drawCanvas.create_oval(x,y2-OvalHeight,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_rectangle(x,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=fillcolor,width=0,tag=shapeTag)
                    drawCanvas.create_oval(x,y,x2,y+OvalHeight,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                    drawCanvas.create_line(x,y+OvalHeight_Half,x,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                    drawCanvas.create_line(x2,y+OvalHeight_Half,x2,y2-OvalHeight_Half,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
        elif shapeType == 'star':    
            center_x = (x + x2)/2    
            center_y = (y + y2)/2    
            rx = (x2 - x)/2    
            ry = (y2 - y)/2    
            points = [    
                center_x - int(rx * math.sin(2 * math.pi / 5)),    
                center_y - int(ry * math.cos(2 * math.pi / 5)),    
                center_x + int(rx * math.sin(2 * math.pi / 5)),    
                center_y - int(ry * math.cos(2 * math.pi / 5)),    
                center_x - int(rx * math.sin(math.pi / 5)),    
                center_y + int(ry * math.cos(math.pi / 5)),    
                center_x,    
                center_y - ry,    
                center_x + int(rx * math.sin(math.pi / 5)),    
                center_y + int(ry * math.cos(math.pi / 5)),    
                ]    
            if  dash1 > 0 :    
                drawCanvas.create_polygon(    
                    points,    
                    fill=fillcolor,    
                    outline=outlinecolor,     
                    width= fillwidth,    
                    dash=(dash1,dash2),    
                    tag=shapeTag)
            else :    
                drawCanvas.create_polygon(    
                    points,    
                    fill=fillcolor,    
                    outline=outlinecolor,     
                    width= fillwidth,    
                    tag=shapeTag)
        elif shapeType == 'eraser':    
            drawCanvas.create_rectangle(x, y, x2, y2,fill=fillcolor, width = 0,tag=shapeTag) 
        elif shapeType == 'grid':    
            rows = int((y2 - y)/dash2)+1    
            cows = int((x2 - x)/dash1)+1    
            for i in range(rows):    
                for j in range(cows):    
                    if (i+j)%2 == 0:    
                        tx = x + j*dash1    
                        ty = y + i*dash2    
                        drawCanvas.create_rectangle(tx, ty, tx+dash1, ty+dash2,fill=fillcolor, width = 0,tag=shapeTag) 
        elif shapeType == 'text':    
            drawCanvas.create_text(x, int((y+y2)/2),fill=fillcolor,text=text,font = textFont,anchor='w',tag=shapeTag)
        elif shapeType == 'button':    
            center_x = (x + x2)/2    
            center_y = (y + y2)/2    
            if newImage:    
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
            else:    
                oval_rx = 20    
                OutLineTag = shapeTag+"_outline"    
                half_width = int((fillwidth+1)/2)
                if  dash1 > 0 :    
                    if  fillcolor.find('#') < 0:    
                        startAngle = 90    
                        extentAngle = 180    
                        drawCanvas.create_arc(x,y,x+2*oval_rx,y2,start=startAngle,extent=extentAngle,fill='',outline=outlinecolor,dash=(dash1,dash2),style=tkinter.ARC,width=fillwidth,tag=shapeTag)
                        drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                        drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                        startAngle = 90    
                        extentAngle = -180    
                        drawCanvas.create_arc(x2-2*oval_rx,y,x2,y2,start=startAngle,extent=extentAngle,fill='',outline=outlinecolor,dash=(dash1,dash2),style=tkinter.ARC,width=fillwidth,tag=shapeTag)
                    else:    
                        drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                        drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
                        drawCanvas.create_rectangle(x+oval_rx, y, x2-oval_rx, y2+1,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = fillwidth,tag=shapeTag)
                        drawCanvas.create_line(x+oval_rx, y+half_width, x+oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=shapeTag)
                        drawCanvas.create_line(x2-oval_rx, y+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = fillwidth,tag=shapeTag)
                else:    
                    if  fillcolor.find('#') < 0:    
                        startAngle = 90    
                        extentAngle = 180    
                        drawCanvas.create_arc(x,y,x+2*oval_rx,y2,start=startAngle,extent=extentAngle,fill='',outline=outlinecolor,style=tkinter.ARC,width=fillwidth,tag=shapeTag)
                        drawCanvas.create_line(x+oval_rx, y, x2-oval_rx, y,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                        drawCanvas.create_line(x+oval_rx, y2, x2-oval_rx, y2,fill=outlinecolor,width = fillwidth,tag=OutLineTag) 
                        startAngle = 90    
                        extentAngle = -180    
                        drawCanvas.create_arc(x2-2*oval_rx,y,x2,y2,start=startAngle,extent=extentAngle,fill='',outline=outlinecolor,style=tkinter.ARC,width=fillwidth,tag=shapeTag)
                    else:    
                        drawCanvas.create_oval(x,y,x+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                        drawCanvas.create_oval(x2-2*oval_rx,y,x2,y2,fill=fillcolor,outline=outlinecolor,width = fillwidth,tag=shapeTag)
                        drawCanvas.create_rectangle(x+oval_rx+1, y + half_width, x2-oval_rx-1, y2+1-half_width,fill=fillcolor,outline=outlinecolor, width = 0,tag=shapeTag)
                        drawCanvas.create_line(x+oval_rx, y, x2-oval_rx, y,fill=outlinecolor,width = fillwidth,tag=OutLineTag)
                        drawCanvas.create_line(x+oval_rx, y2, x2-oval_rx, y2,fill=outlinecolor,width = fillwidth,tag=OutLineTag)    

            if len(text) > 0:    
                drawCanvas.create_text(center_x, center_y,fill=textColor,text=text,font = textFont,anchor='center',tag=shapeTag+"_text")
        elif shapeType == 'image':    
            if type(newImage) == type([]):    
                drawCanvas.create_image(x, y,image=newImage[0][0],anchor='nw',tag=shapeTag)
            else:    
                drawCanvas.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
        elif shapeType == 'switch':    
            SwitchWidth = x2 - x    
            SwitchHeight = y2 - y    
            Switch_radius = int(SwitchHeight/2)
            fillcolor = '#777777'    
            drawCanvas.create_oval(x, y, x+SwitchHeight, y+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+(SwitchWidth-SwitchHeight), y, x+SwitchWidth,y+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_rectangle(x+Switch_radius,y,x+(SwitchWidth-Switch_radius),y+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
            drawCanvas.create_oval(x+2, y+2, x+(SwitchHeight-3), y+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
            drawCanvas.create_text(x+(SwitchWidth-int(1.0*SwitchHeight)), y+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag) 
        elif shapeType == 'listmenu':    
            if  dash1 > 0 :    
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:    
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            MenuInfo = newImage    
            SubMenus = MenuInfo['SubMenus']    
            ListMenuWidth = x2 - x    
            ListMenuHeight = y2 - y    
            SubMenuTitleHeight = 24    
            SubMenuTitleSpacingX = 2    
            SubMenuTitleSpacingY = 5    
            SubMenuItemHeight = 22    
            SubMenuItemSpacingX = 2    
            SubMenuItemSpacingY = 4    
            centerX = x + int(ListMenuWidth/2)
            SubMeshX = x + SubMenuTitleSpacingX    
            SubMenuTitleHeight_Half = int(SubMenuTitleHeight/2)
            IconX = x+int(0.25 * ListMenuWidth)
            ListMenuTop = y + SubMenuTitleSpacingY    
            for subMenu in SubMenus:    
                titleText = subMenu[0]    
                bgImgFile = subMenu[1]    
                itemList = subMenu[2]    
                subMeshTag = shapeTag + "_"+titleText    
                drawCanvas.create_oval(SubMeshX, ListMenuTop, SubMeshX + SubMenuTitleHeight, ListMenuTop+SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_oval(x2-SubMenuTitleHeight, ListMenuTop, x2,ListMenuTop+ SubMenuTitleHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                drawCanvas.create_rectangle(x+SubMenuTitleHeight_Half,ListMenuTop,x2-SubMenuTitleHeight_Half,ListMenuTop+SubMenuTitleHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=subMeshTag)
                centerY = ListMenuTop + int(SubMenuTitleHeight/2)
                drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',14,'bold'),fill = outlinecolor,tag=subMeshTag) 
                ListMenuTop = ListMenuTop + (SubMenuTitleHeight + SubMenuTitleSpacingY)
                if subMenu[3] == True:    
                    for itemInfo in itemList:    
                        titleText = itemInfo[0]    
                        centerY = ListMenuTop + int(SubMenuItemHeight/2)
                        drawCanvas.create_oval(IconX-5, centerY-5, IconX+5, centerY+5,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                        drawCanvas.create_text(centerX ,centerY,text=titleText,anchor=tkinter.CENTER,font=('Arial',10,'bold'),fill = outlinecolor,tag=shapeTag) 
                        ListMenuTop = ListMenuTop + (SubMenuItemHeight + SubMenuItemSpacingY)
        elif shapeType == 'table':    
            if  dash1 > 0 :    
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,dash=(dash1,dash2),width = fillwidth,tag=shapeTag)
            else:    
                drawCanvas.create_rectangle(x, y, x2, y2,fill='#FFFFFF', outline=outlinecolor,width = fillwidth,tag=shapeTag)
            TableWidth = x2 - x    
            TableHeight = y2 - y    
            if TableHeight > 0:    
                TableTopY = y    
                TableInfo = newImage    
                RowCount = len(TableInfo['rows'])
                CowInfo = TableInfo['cows']    
                TableRowHeight = TableHeight    
                if RowCount > 0:    
                    TableRowHeight = TableHeight / RowCount    
                RowTopY = TableTopY    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    left = 0    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        x1 = x + int(left * TableWidth) 
                        y1 = int(RowTopY)
                        x2 = x + int((left + CowInfo[CowIndex])* TableWidth) 
                        y2 = int(RowTopY + TableRowHeight)
                        CellText = rowInfo[0]    
                        StyleIndex = rowInfo[1]    
                        StyleInfo = TableInfo['style'][StyleIndex]    
                        FillColor = StyleInfo[0]    
                        if FillColor == '':    
                            FillColor = '#FFFFFF'    
                        FontIndex = StyleInfo[1]    
                        TextAnchor = StyleInfo[2]    
                        TextColor = StyleInfo[3]    
                        if TextColor == '':    
                            TextColor = '#000000'    
                        BorderWidth = StyleInfo[4]    
                        OutLineColor = StyleInfo[5]    
                        if OutLineColor == '':    
                            OutLineColor = '#000000'    
                        drawCanvas.create_rectangle(x1,y1,x2,y2,fill = FillColor,outline = OutLineColor,width = BorderWidth,tag = 'drawing_shape')
                        #显示文字    
                        if CellText != '':    
                            if CellText.find("┇") >= 0:    
                                drawCanvas.create_line(x1,y1,x2,y2,fill = OutLineColor,width = BorderWidth,tag = 'drawing_shape')
                                TextSplitArray = CellText.split('┇')
                                Text1 = TextSplitArray[0]    
                                Text2 = TextSplitArray[1]    
                                CellWidth  = x2 - x1    
                                CellHeight = y2 - y1    
                                cell_cx1 = x1 + int(CellWidth * 0.67)
                                cell_cy1 = y1 + int(CellHeight * 0.33)
                                TextAnchor1 = 'center'    
                                cell_cx2 = x2 - int(CellWidth * 0.67)
                                cell_cy2 = y2 - int(CellHeight * 0.33)
                                TextAnchor2 = 'center'    
                                if FontIndex >= 0:    
                                    FontInfo = TableInfo['font'][FontIndex]    
                                    fontName = FontInfo[0]    
                                    fontSize = FontInfo[1]    
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, font=(fontName,fontSize),anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, font=(fontName,fontSize),anchor=TextAnchor2,tag='drawing_shape')
                                else:    
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, anchor=TextAnchor2,tag='drawing_shape')
                            else:    
                                cell_cx = int((x1 + x2)/2)
                                cell_cy = int((y1 + y2)/2)
                                #['WN','N','EN','W','CENTER','E','WS','S','ES','XY']    
                                TextAnchor = TextAnchor.lower()
                                if TextAnchor == 'n' or TextAnchor == 'wn' or TextAnchor == 'en'  or TextAnchor == 'nw' or TextAnchor == 'ne':    
                                    cell_cy = int(y1)
                                elif TextAnchor == 's' or TextAnchor == 'ws' or TextAnchor == 'es' or TextAnchor == 'sw' or TextAnchor == 'se':    
                                    cell_cy = int(y2)
                                if TextAnchor == 'w' or TextAnchor == 'wn' or TextAnchor == 'ws' or TextAnchor == 'nw' or TextAnchor == 'sw':    
                                    cell_cx = int(x1)
                                elif TextAnchor == 'e' or TextAnchor == 'en' or TextAnchor == 'es' or TextAnchor == 'ne' or TextAnchor == 'se':    
                                    cell_cx = int(x2)
                                if FontIndex >= 0:    
                                    FontInfo = TableInfo['font'][FontIndex]    
                                    fontName = FontInfo[0]    
                                    fontSize = FontInfo[1]    
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, font=(fontName,fontSize),anchor=TextAnchor,tag='drawing_shape')
                                else:    
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, anchor=TextAnchor,tag='drawing_shape')
                        left = left + CowInfo[CowIndex]    
                        CowIndex = CowIndex + 1    
                    RowTopY = RowTopY + TableRowHeight    
                    RowIndex = RowIndex + 1    
                for mergeCell in TableInfo['merge']:    
                    BeginRow = mergeCell[0][0]    
                    BeginCow = mergeCell[0][1]    
                    EndRow = mergeCell[1][0]    
                    EndCow = mergeCell[1][1]    
                    CellText = mergeCell[2]    
                    StyleIndex = mergeCell[3]    
                    StyleInfo = TableInfo['style'][StyleIndex]    
                    FillColor = StyleInfo[0]    
                    if FillColor == '':    
                        FillColor = '#FFFFFF'    
                    FontIndex = StyleInfo[1]    
                    TextAnchor = StyleInfo[2]    
                    TextColor = StyleInfo[3]    
                    if TextColor == '':    
                        TextColor = '#000000'    
                    BorderWidth = StyleInfo[4]    
                    BorderColor = StyleInfo[5]    
                    if BorderColor == '':    
                        BorderColor = '#000000'    
                    Left = x + TableWidth    
                    Right = x     
                    Top = TableTopY + TableHeight    
                    Bottom = TableTopY    
                    RowTopY = TableTopY    
                    RowIndex = 0    
                    for rowInfoLine in TableInfo['rows']:    
                        left = 0    
                        CowIndex = 0    
                        for rowInfo in rowInfoLine:    
                            x1 = x + int(left * TableWidth)
                            y1 = int(RowTopY)
                            x2 = x + int((left + CowInfo[CowIndex])* TableWidth)
                            y2 = int(RowTopY + TableRowHeight)
                            if checkPtInRect(CowIndex,RowIndex,BeginCow,EndCow,BeginRow,EndRow) == True:    
                                if x1 < Left:    
                                    Left = x1    
                                if y1 < Top:    
                                    Top = y1    
                                if x2 > Right:    
                                    Right = x2    
                                if y2 > Bottom:    
                                    Bottom = y2    
                            left = left + CowInfo[CowIndex]    
                            CowIndex = CowIndex + 1    
                        RowTopY = RowTopY + TableRowHeight    
                        RowIndex = RowIndex + 1    
                    if Right >= Left and Bottom >= Top:    
                        drawCanvas.create_rectangle(Left,Top,Right,Bottom,fill = FillColor,outline = BorderColor,width = BorderWidth,tag = 'drawing_shape')
                        #显示文字    
                        if CellText != '':    
                            if CellText.find('┇') >= 0:    
                                drawCanvas.create_line(Left,Top,Right,Bottom,fill = BorderColor,width = BorderWidth,tag = 'drawing_shape')
                                TextSplitArray = CellText.split('┇')
                                Text1 = TextSplitArray[0]    
                                Text2 = TextSplitArray[1]    
                                CellWidth  = Right - Left    
                                CellHeight = Bottom - Top    
                                cell_cx1 = Left + int(CellWidth * 0.67)
                                cell_cy1 = Top + int(CellHeight * 0.33)
                                TextAnchor1 = 'center'    
                                cell_cx2 = Left + int(CellWidth * 0.33)
                                cell_cy2 = Top + int(CellHeight * 0.67)
                                TextAnchor2 = 'center'    
                                if FontIndex >= 0:    
                                    FontInfo = TableInfo['font'][FontIndex]    
                                    fontName = FontInfo[0]    
                                    fontSize = FontInfo[1]    
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, font=(fontName,fontSize),anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, font=(fontName,fontSize),anchor=TextAnchor2,tag='drawing_shape')
                                else:    
                                    drawCanvas.create_text(cell_cx1,cell_cy1,fill=TextColor,text=Text1, anchor=TextAnchor1,tag='drawing_shape')
                                    drawCanvas.create_text(cell_cx2,cell_cy2,fill=TextColor,text=Text2, anchor=TextAnchor2,tag='drawing_shape')
                            else:    
                                cell_cx = int((Left + Right)/2)
                                cell_cy = int((Top + Bottom)/2)
                                #['WN','N','EN','W','CENTER','E','WS','S','ES','XY']    
                                if TextAnchor == 'n' or TextAnchor == 'wn' or TextAnchor == 'en'  or TextAnchor == 'nw' or TextAnchor == 'ne':    
                                    cell_cy = int(Top)
                                elif TextAnchor == 's' or TextAnchor == 'ws' or TextAnchor == 'es' or TextAnchor == 'sw' or TextAnchor == 'se':    
                                    cell_cy = int(Bottom)
                                if TextAnchor == 'w' or TextAnchor == 'wn' or TextAnchor == 'ws' or TextAnchor == 'nw' or TextAnchor == 'sw':    
                                    cell_cx = int(Left)
                                elif TextAnchor == 'e' or TextAnchor == 'en' or TextAnchor == 'es' or TextAnchor == 'ne' or TextAnchor == 'se':    
                                    cell_cx = int(Right)
                                if FontIndex >= 0:    
                                    FontInfo = TableInfo['font'][FontIndex]    
                                    fontName = FontInfo[0]    
                                    fontSize = FontInfo[1]    
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, font=(fontName,fontSize),anchor=TextAnchor,tag='drawing_shape')
                                else:    
                                    drawCanvas.create_text(cell_cx,cell_cy,fill=TextColor,text=CellText, anchor=TextAnchor,tag='drawing_shape')
def DrawLine(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''):  
    PrintFunctionInfo(DrawLine,[uiName,drawCanvasName,x1,y1,x2,y2,color,width,dash,shapeTag])    
    #在画布上画线  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('line_') == 0:    
                NameSplitArray = ShepTagName.partition('line_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("line_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['line',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'line',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawArrow(uiName,drawCanvasName,x1,y1,x2,y2,color,width=1,dash=(0,0),shapeTag=''): 
    PrintFunctionInfo(DrawArrow,[uiName,drawCanvasName,x1,y1,x2,y2,color,width,dash,shapeTag])       
    #在画布上画箭头  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('arrow_') == 0:    
                NameSplitArray = ShepTagName.partition('arrow_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("arrow_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['arrow',x1,y1,x2,y2,color,color,width,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,width,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'arrow',x1,y1,x2,y2,color,color,width,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    

def DrawTriangle(uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):  
    PrintFunctionInfo(DrawTriangle,[uiName,drawCanvasName,direction,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])  
    #在画布上画三角形  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    TriangleType = "triangle_up"    
    if direction == "down":    
        TriangleType = "triangle_down"    
    if direction == "left":    
        TriangleType = "triangle_left"    
    if direction == "right":    
        TriangleType = "triangle_right"    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('triangle_') == 0:    
                NameSplitArray = ShepTagName.partition('triangle_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("triangle_%d"%Index)
    G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,TriangleType,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''): 
    PrintFunctionInfo(DrawRectangle,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上画矩形  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('rect_') == 0:    
                NameSplitArray = ShepTagName.partition('rect_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("rect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'rect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    

def DrawRoundedRectangle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),roundRadius=10,shapeTag=''): 
    PrintFunctionInfo(DrawRoundedRectangle,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,roundRadius,shapeTag])
    #在画布上显示圆角矩形  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('roundrect_') == 0:    
                NameSplitArray = ShepTagName.partition('roundrect_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("roundrect_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'roundrect',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=roundRadius,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    

def DrawCircle(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):  
    PrintFunctionInfo(DrawCircle,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上画圆  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('circle_') == 0:    
                NameSplitArray = ShepTagName.partition('circle_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("circle_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'circle',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawDiamond(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):  
    PrintFunctionInfo(DrawDiamond,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上画菱形  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('diamond_') == 0:    
                NameSplitArray = ShepTagName.partition('diamond_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("diamond_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'diamond',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawCylinder(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):   
    PrintFunctionInfo(DrawCylinder,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上画圆柱  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('cylinder_') == 0:    
                NameSplitArray = ShepTagName.partition('cylinder_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("cylinder_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'cylinder',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawStar(uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):    
    PrintFunctionInfo(DrawStar,[uiName,drawCanvasName,x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上画星星  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('star_') == 0:    
                NameSplitArray = ShepTagName.partition('star_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("star_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash[0],dash[1]]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,outlinecolor,outlinewidth,dash[0],dash[1],None,'',None,'']    
    DoCanvasRecord(drawCanvas,'star',x1,y1,x2,y2,color,outlinecolor,outlinewidth,dash1=dash[0],dash2=dash[1],newImage=None,text='',textFont = None,textColor='',shapeTag=shapeTag)
    return shapeTag    
def DrawText(uiName,drawCanvasName,x,y,text,textFont=None,color='#FFFFFF',anchor='nw',shapeTag=''):   
    PrintFunctionInfo(DrawText,[uiName,drawCanvasName,x,y,text,textFont,color,anchor,shapeTag])
    #在画布上写字  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('text_') == 0:    
                NameSplitArray = ShepTagName.partition('text_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("text_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['text',x,y,x,y,text,textFont,color]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[color,color,0,0,0,None,text,textFont,color]    
    drawCanvas.create_text(x, y,fill=color,text=text,font = textFont,anchor=anchor,tag=shapeTag)
    return shapeTag    
def DrawImage(uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag=''):  
    PrintFunctionInfo(DrawImage,[uiName,drawCanvasName,x1,y1,x2,y2,imagefile,shapeTag])
    #在画布上显示图片  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    if drawCanvasName not in G_CanvasShapeDictionary[uiName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
    newImage = None    
    hasGIFAnimation = False    
    w = x2 - x1    
    h = y2 - y1    
    if uiName and uiName in G_CanvasImageDictionary:    
        if drawCanvasName and drawCanvasName in G_CanvasImageDictionary[uiName]:    
            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:    
                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :    
                    newImage = ImageInfo[1]    
                    break    
    else:    
        return    
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('image_') == 0:    
                NameSplitArray = ShepTagName.partition('image_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("image_%d"%Index)
    if newImage == None:    
        resourPath = imagefile    
        imagefile_Lower = imagefile.lower()
        if imagefile_Lower in G_ResourcesFileList:    
            resourPath = G_ResourcesFileList[imagefile_Lower]    
        if type(resourPath) == type(""):    
            if os.path.exists(resourPath) == True:    
                try:    
                    if imagefile.find('.gif') >= 0:    
                        GifData = Image.open(resourPath)
                        seq = []    
                        try:    
                            while 1:    
                                imageRGBA = GifData.copy().convert('RGBA')
                                resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                newImage = ImageTk.PhotoImage(resizeImage)
                                seq.append(newImage)
                                GifData.seek(len(seq))
                        except EOFError:    
                            pass    
                        delay = 100    
                        try:    
                            delay = GifData.info['duration']    
                        except KeyError:    
                            delay = 100    
                        if delay == 0:    
                            delay = 100    
                        newImage = [seq,delay,0]    
                        hasGIFAnimation = True    
                    else:    
                        imageRGBA = Image.open(resourPath).convert('RGBA')
                        resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                        newImage = ImageTk.PhotoImage(resizeImage)
                    if drawCanvasName not in G_CanvasImageDictionary[uiName]:    
                        G_CanvasImageDictionary[uiName][drawCanvasName] = []    
                    G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                except:    
                    return     
        elif type(imagefile) == type(Image):    
            imageRGBA = imagefile    
            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
            newImage = ImageTk.PhotoImage(resizeImage)
            if drawCanvasName not in G_CanvasImageDictionary[uiName]:    
                G_CanvasImageDictionary[uiName][drawCanvasName] = []    
            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
    if newImage:    
        if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['image',x1,y1,x2,y2,newImage,imagefile]    
        if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
            G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=['#FFFFFF','#FFFFFF',0,0,0,newImage,'',None,'#FFFFFF']    
        DoCanvasRecord(drawCanvas,'image',x1,y1,x2,y2,'#FFFFFF','#FFFFFF',0,dash1=0,dash2=0,newImage=newImage,text='',textFont = None,textColor='',shapeTag=shapeTag)
        if hasGIFAnimation == True:    
            drawCanvas.after(100,lambda: updateGIFFrame(uiName,drawCanvasName))
def DrawButton(uiName,drawCanvasName,x1,y1,x2,y2,text='',textcolor='#000000',textFont = None,fillcolor='#FFFFFF',outlinecolor='#FFFFFF',outlinewidth=0,dash=(0,0),shapeTag=''):    
    PrintFunctionInfo(DrawButton,[uiName,drawCanvasName,x1,y1,x2,y2,text,textcolor,textFont,fillcolor,outlinecolor,outlinewidth,dash,shapeTag])
    #在画布上显示圆角按钮  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    center_x = (x1 + x2)/2    
    center_y = (y1 + y2)/2    
    oval_rx = 20    
    dash1=dash[0],dash2=dash[1]    
    OutLineTag = shapeTag+"_outline"    
    half_width = int((outlinewidth+1)/2)
    if shapeTag == '':    
        Index = 0    
        for ShepTagName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            if ShepTagName.find('button_') == 0:    
                NameSplitArray = ShepTagName.partition('button_')
                if NameSplitArray[2].isdigit() == True:    
                    Number = int(NameSplitArray[2])
                    if Number > Index:    
                        Index = Number    
        Index = Index + 1    
        shapeTag = str("button_%d"%Index)
    if shapeTag not in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=['button',x1,y1,x2,y2,text,textcolor,textFont,fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None]    
    if drawCanvasName not in G_CanvasParamDictionary[uiName]:    
        G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
    G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fillcolor,outlinecolor,outlinewidth,dash[0],dash[1],None,text,textFont,textcolor]    
    if  dash1 > 0 :    
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2),width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor,dash=(dash1,dash2), width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    else:    
        drawCanvas.create_oval(x1,y1,x1+2*oval_rx,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_oval(x2-2*oval_rx,y1,x2,y2,fill=fillcolor,outline=outlinecolor,width = outlinewidth,tag=shapeTag)
        drawCanvas.create_rectangle(x1+oval_rx, y1, x2-oval_rx, y2,fill=fillcolor,outline=outlinecolor, width = outlinewidth,tag=shapeTag)
        drawCanvas.create_line(x1+oval_rx, y1+half_width, x1+oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
        drawCanvas.create_line(x2-oval_rx, y1+half_width, x2-oval_rx, y2-half_width,fill=fillcolor,width = outlinewidth,tag=OutLineTag)
    if len(text) > 0:    
        drawCanvas.create_text(center_x, center_y,text=text,fill=textcolor,anchor='center',tag=shapeTag+"_text")
def EraserCanvas(uiName,drawCanvasName,x1,y1,x2,y2): 
    PrintFunctionInfo(EraserCanvas,[uiName,drawCanvasName,x1,y1,x2,y2])
    #在画布上檫去区域  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    bgcolor = drawCanvas.cget('bg')
    DoCanvasRecord(drawCanvas,'eraser',x1,y1,x2,y2,bgcolor,bgcolor,0,dash1=0,dash2=0,newImage=None,text='',textFont = None,textColor='',shapeTag='')
def SetCanvasGridBG(uiName,drawCanvasName,bgcolor='#888888',tile_width=20,tile_height=20):  
    PrintFunctionInfo(SetCanvasGridBG,[uiName,drawCanvasName,bgcolor,tile_width,tile_height])
    #设置画布背景格子  
    drawCanvas = GetElement(uiName,drawCanvasName)
    if drawCanvas is None:    
        return    
    canvasWidth = drawCanvas.winfo_width()
    canvasHeight = drawCanvas.winfo_height()
    DoCanvasRecord(drawCanvas,'grid',0,0,canvasWidth,canvasHeight,bgcolor,bgcolor,0,dash1=tile_width,dash2=tile_height,newImage=None,text='',textFont = None,textColor='',shapeTag='grid_bg')
 
def checkPtInRect(x,y,left,right,top,bottom):    
    if x < left:return 0    
    if x > right:return 0    
    if y < top:return 0    
    if y > bottom:return 0    
    return 1    
def Shape_MouseEvent(event,uiName,canvasName,shapeTag,eventName): 
    PrintFunctionInfo(Shape_MouseEvent,[event,uiName,canvasName,shapeTag,eventName])
    if eventName == 'MouseLeave':    
        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
        if type(x1) == type(1.0):    
            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
        if type(y1) == type(1.0):    
            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
        if type(x2) == type(1.0):    
            if x2 <= 1.0:    
                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
            else:    
                x2 = x1 + int(x2)
        if type(y2) == type(1.0):    
            if y2 <= 1.0:    
                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
            else:    
                y2 = y1 + int(y2)
        borderwidth = 0    
        if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':    
            borderwidth = 1 + G_CanvasShapeDictionary[uiName][canvasName][shapeTag][10]    
        if checkPtInRect(event.x,event.y,x1+borderwidth,x2-borderwidth,y1+borderwidth,y2-borderwidth) == 1:    
            return     
    if shapeTag not in G_CanvasEventDictionary[uiName][canvasName]:    
        return    
    if eventName not in G_CanvasEventDictionary[uiName][canvasName][shapeTag]:    
        return    
    for actionInfo in G_CanvasEventDictionary[uiName][canvasName][shapeTag][eventName]:    
        if actionInfo[0] == "SetShapeRect":    
            SetShapeRect(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3],actionInfo[4],actionInfo[5])
        elif actionInfo[0] == "SetFillColor":    
            SetShapeFillColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "SetOutlineColor":    
            SetShapeOutlineColor(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeImage":    
            SetShapeImage(uiName ,canvasName,actionInfo[1],actionInfo[2])
        elif actionInfo[0] == "ChangeText":    
            SetShapeText(uiName ,canvasName,actionInfo[1],actionInfo[2],actionInfo[3])
        elif actionInfo[0] == "JumpToUI":    
            UIPath, UIFile = os.path.split(actionInfo[2])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:    
                import sys    
                sys.path.append(UIPath)
            GoToUIDialog(uiName,UIName)
            return 
        elif actionInfo[0] == "LoadUI":    
            WidgetName = actionInfo[2]    
            UIPath, UIFile = os.path.split(actionInfo[3])
            UIName, extension = os.path.splitext(UIFile)
            if len(UIPath) > 0:    
                import sys    
                sys.path.append(UIPath)
            if WidgetName == "Form_1":    
                WidgetName == "root"    
            LoadUIDialog(uiName,WidgetName,UIName)
            return 
        elif actionInfo[0] == "DeleteShape":    
            DeleteShape(uiName ,canvasName,actionInfo[1])
        elif actionInfo[0] == "OnSwitch":    
            OnSwitch(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "OnExpandOrShrink":    
            OnExpandOrShrink(uiName ,canvasName,actionInfo[1],actionInfo)
        elif actionInfo[0] == "CallFunction":    
            if actionInfo[1]:    
                if actionInfo[2]:    
                    actionInfo[1](event,uiName,canvasName,actionInfo[2])
                else:    
                    actionInfo[1](event,uiName,canvasName)
def updateGIFFrame(uiName,elementName):    
    #更新GIF动画  
    Control = GetElement(uiName,elementName)
    if elementName in G_CanvasShapeDictionary[uiName].keys():    
        for shapeTag in G_CanvasShapeDictionary[uiName][elementName]:    
            ShapeInfo = G_CanvasShapeDictionary[uiName][elementName][shapeTag]    
            if ShapeInfo[0] == 'image':    
                if type(ShapeInfo[5]) == type([]):    
                    FrameIndex = ShapeInfo[5][2]    
                    FrameImages = ShapeInfo[5][0]    
                    x = ShapeInfo[1]    
                    y = ShapeInfo[2]    
                    newImage = FrameImages[FrameIndex]    
                    Control.delete(shapeTag)
                    Control.create_image(x, y,image=newImage,anchor='nw',tag=shapeTag)
                    FrameIndex = FrameIndex + 1    
                    if FrameIndex == len(FrameImages):    
                            FrameIndex = 0    
                    ShapeInfo[5][2] = FrameIndex    
    if uiName in G_CanvasImageDictionary:    
        if elementName in G_CanvasImageDictionary[uiName].keys():    
            if hasattr(Control,"GetEntry") == True:    
                Control = Control.GetEntry()
            if Control != None:    
                for imageInfo in G_CanvasImageDictionary[uiName][elementName]:    
                    if type(imageInfo[1]) == type([]):    
                        GifData = imageInfo[1]    
                        FrameSequ = GifData[0]    
                        FrameIndex = GifData[2]    
                        if elementName.find('Text_') >= 0:    
                            if GifData[3]:    
                                Control.delete(GifData[3])
                                GifData[3] = Control.image_create(tkinter.END, image=FrameSequ[FrameIndex])
                            else:    
                                GifData[3] = Control.image_create(tkinter.END, image=FrameSequ[FrameIndex])
                        elif elementName.find('Label_') >= 0 or elementName.find('Button_') >= 0 or elementName.find('RadioButton_') >= 0 or elementName.find('CheckButton_') >= 0:    
                            Control.configure(image = FrameSequ[FrameIndex])
                        FrameIndex = FrameIndex + 1    
                        if FrameIndex == len(FrameSequ):    
                            FrameIndex = 0    
                        GifData[2] = FrameIndex    
    if Control:    
        Control.after(100,lambda: updateGIFFrame(uiName,elementName)) 
def LoadCanvasRecord(uiName,UIScale=1.0):   
    PrintFunctionInfo(LoadCanvasRecord,[uiName,UIScale])
    #读取画板动作记录  
    global G_ExeDir    
    global G_ResDir   
    global G_PrintFunctionMode
    drawCanvasName = None    
    drawCanvas = None    
    drawCanvas_width = 0    
    drawCanvas_height = 0    
    hasGIFAnimation = False    
    canvasFile = os.path.join(G_ResDir,uiName + ".cav")
    if os.path.exists(canvasFile) == False:    
        file_path = os.path.abspath(__file__)  
        checkExeDir = os.path.dirname(file_path)  
        checkResDir = os.path.join(checkExeDir,"Resources")  
        canvasFile = os.path.join(G_ResDir,uiName + ".cav")  
        if os.path.exists(canvasFile) == False:     
            if uiName.find("_") > 0:      
                endIndex = uiName.rfind("_")  
                originalName = uiName[0:endIndex]      
                canvasFile = os.path.join(G_ResDir,originalName + ".cav")  
                if os.path.exists(canvasFile) == False:    
                    file_path = os.getcwd()  
                    checkExeDir = os.path.dirname(file_path)  
                    checkResDir = os.path.join(checkExeDir,"Resources")  
                    if os.path.exists(checkResDir) == False:      
                        return
                    canvasFile = os.path.join(checkResDir,originalName + ".cav")  
    if os.path.exists(canvasFile) == False:  
        if G_PrintFunctionMode == True:
            print(uiName+"没有界面图形")
    else:
        if G_PrintFunctionMode == True:
            print(uiName+"加载:"+canvasFile)
        f = open(canvasFile,encoding='utf-8')
        line =""     
        while True:    
            line = f.readline()
            if not line:    
                break    
            text = line.strip()
            if not text:    
                continue    
            if text.find('Canvas:') >= 0:    
                splitArray = text.split(':')
                drawCanvasName = splitArray[1].strip()
                drawCanvas = GetElement(uiName,drawCanvasName)
                if drawCanvas is None:    
                    drawCanvasName = "PyMe_"+drawCanvasName    
                    drawCanvas = GetElement(uiName,drawCanvasName)
                if drawCanvas is None:    
                    break    
                drawCanvas_width = drawCanvas.winfo_width()
                drawCanvas_height = drawCanvas.winfo_height()
                if drawCanvasName == "Form_1":    
                    root = GetElement(uiName,"root")
                    drawCanvas_width = root.winfo_width()
                    drawCanvas_height = root.winfo_height()
                G_CanvasSizeDictionary[uiName][drawCanvasName] = [drawCanvas_width,drawCanvas_height]    
                G_CanvasShapeDictionary[uiName][drawCanvasName] = {}    
                G_CanvasParamDictionary[uiName][drawCanvasName] = {}    
                G_CanvasFontDictionary[uiName][drawCanvasName] = []    
                G_CanvasImageDictionary[uiName][drawCanvasName] = []    
                G_CanvasPointDictionary[uiName][drawCanvasName] = {}    
                G_CanvasEventDictionary[uiName][drawCanvasName] = {}    
                continue    
            elif text.find(',') >= 0:    
                if drawCanvas != None:    
                    splitArray = text.split(',')
                    splitCount = len(splitArray)
                    ShapeType = splitArray[0]    
                    if ShapeType == 'image':    
                        if splitArray[1].find('.') > 0:    
                            x1 = float(splitArray[1])
                        else:    
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:    
                            y1 = float(splitArray[2])
                        else:    
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:    
                            x2 = float(splitArray[3])
                        else:    
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:    
                            y2 = float(splitArray[4])
                        else:    
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * drawCanvas_width    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * drawCanvas_height    
                        fill = splitArray[5]    
                        outline = splitArray[6]    
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = splitArray[10]    
                        newImage = None    
                        newtext = ''    
                        textFont = None    
                        textColor=''    
                        shapeTag = ''    
                        if len(splitArray) > 12:    
                            shapeTag = splitArray[11]    
                        for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:    
                            if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :    
                                newImage = ImageInfo[1]    
                                continue    
                        if newImage == None:    
                            imagefile_Lower = imagefile.lower()
                            if imagefile_Lower in G_ResourcesFileList:    
                                resourPath = G_ResourcesFileList[imagefile_Lower]    
                                if os.path.exists(resourPath) == True:    
                                    try:    
                                        if imagefile.find('.gif') >= 0:    
                                            GifData = Image.open(resourPath)
                                            seq = []    
                                            try:    
                                                while 1:    
                                                    imageRGBA = GifData.copy().convert('RGBA')
                                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                                    newImage = ImageTk.PhotoImage(resizeImage)
                                                    seq.append(newImage)
                                                    GifData.seek(len(seq))
                                            except EOFError:    
                                                pass    
                                            delay = 100    
                                            try:    
                                                delay = GifData.info['duration']    
                                            except KeyError:    
                                                delay = 100    
                                            if delay == 0:    
                                                delay = 100    
                                            newImage = [seq,delay,0]    
                                            hasGIFAnimation = True    
                                        else:    
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                    except:    
                                        pass    
                            G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,imagefile]    
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'text':    
                        if splitArray[1].find('.') > 0:    
                            x1 = float(splitArray[1])
                        else:    
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:    
                            y1 = float(splitArray[2])
                        else:    
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:    
                            x2 = float(splitArray[3])
                        else:    
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:    
                            y2 = float(splitArray[4])
                        else:    
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * drawCanvas_width    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * drawCanvas_height    
                        fill = splitArray[5]    
                        outline = splitArray[6]    
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        imagefile = ''    
                        newImage = None    
                        shapeTag = ''    
                        newtext = splitArray[10]    
                        for i in range(11,splitCount-8):    
                            newtext = newtext + ","+splitArray[i]                    
                        familytext = splitArray[-8]    
                        sizetext = int(int(splitArray[-7]) * UIScale)
                        sizetext = str(sizetext)
                        weighttext = splitArray[-6]    
                        slanttext = splitArray[-5]    
                        underlinetext = splitArray[-4]    
                        overstriketext = splitArray[-3]    
                        textColor=''    
                        textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                        shapeTag = splitArray[-2]    
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textFont,fill]    
                        #字体    
                        fontFind = False    
                        for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:    
                            if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:    
                                fontFind = True    
                                continue    
                        if fontFind == False:    
                            G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'button':    
                        if splitArray[1].find('.') > 0:    
                            x1 = float(splitArray[1])
                        else:    
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:    
                            y1 = float(splitArray[2])
                        else:    
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:    
                            x2 = float(splitArray[3])
                        else:    
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:    
                            y2 = float(splitArray[4])
                        else:    
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * drawCanvas_width    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * drawCanvas_height    
                        fill = splitArray[5]    
                        outline = splitArray[6]    
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        shapeTag = ''    
                        newtext = splitArray[10]    
                        for i in range(11,splitCount-11):    
                            newtext = newtext + ","+splitArray[i]             
                        familytext = splitArray[-11]    
                        sizetext = int(int(splitArray[-10]) * UIScale)
                        sizetext = str(sizetext)
                        weighttext = splitArray[-9]    
                        slanttext = splitArray[-8]    
                        underlinetext = splitArray[-7]    
                        overstriketext = splitArray[-6]    
                        textColor = splitArray[-5]    
                        textFont = None    
                        if len(familytext) > 0:    
                            textFont = tkinter.font.Font(family=familytext, size=sizetext,weight=weighttext,slant=slanttext,underline=underlinetext,overstrike=overstriketext)
                            #字体    
                            fontFind = False    
                            for fontInfo in G_CanvasFontDictionary[uiName][drawCanvasName]:    
                                if fontInfo[1] == familytext and fontInfo[2] == sizetext and fontInfo[3] == weighttext and fontInfo[4] == slanttext and fontInfo[5] == underlinetext and fontInfo[6] == overstriketext:    
                                    fontFind = True    
                                    continue    
                            if fontFind == False:    
                                G_CanvasFontDictionary[uiName][drawCanvasName].append([textFont,familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                        imagefile = splitArray[-4]    
                        newImage = None    
                        if imagefile != "":    
                            for ImageInfo in G_CanvasImageDictionary[uiName][drawCanvasName]:    
                                if ImageInfo[0] == imagefile and ImageInfo[2] == w and ImageInfo[3] == h :    
                                    newImage = ImageInfo[1]    
                                    continue    
                            if newImage == None:    
                                imagefile_Lower = imagefile.lower()
                                if imagefile_Lower in G_ResourcesFileList:    
                                    resourPath = G_ResourcesFileList[imagefile_Lower]    
                                    if os.path.exists(resourPath) == True:    
                                        try:    
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                        except:    
                                            return     
                                G_CanvasImageDictionary[uiName][drawCanvasName].append([imagefile,newImage,w,h])
                        shapeTag = splitArray[-2]    
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newtext,textColor,textFont,fill,outline,width,dashx,dashy,newImage]    
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'roundrect':    
                        if len(splitArray) > 11:    
                            if splitArray[1].find('.') > 0:    
                                x1 = float(splitArray[1])
                            else:    
                                x1 = int(splitArray[1])
                                x1 = int(x1 * UIScale)
                            if splitArray[2].find('.') > 0:    
                                y1 = float(splitArray[2])
                            else:    
                                y1 = int(splitArray[2])
                                y1 = int(y1 * UIScale)
                            if splitArray[3].find('.') > 0:    
                                x2 = float(splitArray[3])
                            else:    
                                x2 = int(splitArray[3])
                                x2 = int(x2 * UIScale)
                            if splitArray[4].find('.') > 0:    
                                y2 = float(splitArray[4])
                            else:    
                                y2 = int(splitArray[4])
                                y2 = int(y2 * UIScale)
                            w = x2 - x1    
                            if isinstance(w,float) == True:    
                                w = w * drawCanvas_width    
                            h = y2 - y1    
                            if isinstance(h,float) == True:    
                                h = h * drawCanvas_height    
                            fill = splitArray[5]    
                            outline = splitArray[6]    
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = int(splitArray[10])
                            newImage = imagefile    
                            newtext = ''    
                            textFont = None    
                            textColor = ''    
                            shapeTag = splitArray[11]    
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]    
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'point':    
                        if splitArray[1].find('.') > 0:    
                            x1 = float(splitArray[1])
                        else:    
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:    
                            y1 = float(splitArray[2])
                        else:    
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:    
                            x2 = float(splitArray[3])
                        else:    
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:    
                            y2 = float(splitArray[4])
                        else:    
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * drawCanvas_width    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * drawCanvas_height    
                        fill = splitArray[5]    
                        outline = splitArray[6]    
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        parentShapeTag = splitArray[10]    
                        imagefile = ''    
                        newImage = None    
                        newtext = ''    
                        textFont = None    
                        textColor = ''    
                        shapeTag = ''    
                        centerX = (x1 + x2)*0.5    
                        if centerX  > 1.0:    
                            centerX = int(centerX)                 
                        centerY = (y1 + y2)*0.5    
                        if centerY  > 1.0:    
                            centerY = int(centerY)      
                        if len(splitArray) > 12:    
                            shapeTag = splitArray[11]    
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=(ShapeType,x1,y1,x2,y2)
                        if parentShapeTag not in G_CanvasPointDictionary[uiName][drawCanvasName]:    
                            G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag] = {}    
                        G_CanvasPointDictionary[uiName][drawCanvasName][parentShapeTag][shapeTag] = [centerX,centerY]    
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
#                     elif ShapeType == 'listmenu':    
#                         shapeTag = splitArray[-2]    
#                         LockFlag = splitArray[-1]    
#                         if splitArray[1].find('.') > 0:    
#                             x1 = float(splitArray[1])
#                         else:    
#                             x1 = int(splitArray[1])
#                         if splitArray[2].find('.') > 0:    
#                             y1 = float(splitArray[2])
#                         else:    
#                             y1 = int(splitArray[2])
#                         if splitArray[3].find('.') > 0:    
#                             x2 = float(splitArray[3])
#                         else:    
#                             x2 = int(splitArray[3])
#                         if splitArray[4].find('.') > 0:    
#                             y2 = float(splitArray[4])
#                         else:    
#                             y2 = int(splitArray[4])
#                         w  = x2 - x1    
#                         h  = y2 - y1    
#                         fill = splitArray[5]    
#                         outline = splitArray[6]    
#                         width = int(splitArray[7])
#                         dashx = int(splitArray[8])
#                         dashy = int(splitArray[9])
#                         menuInfo_Begin = text.find('{')
#                         menuInfo_End = text.rfind('}')
#                         menuInfo = text[menuInfo_Begin :menuInfo_End+1]    
#                         menuInfo = menuInfo.replace("'",'"')
#                         menu_dict = json.loads(menuInfo)
#                         imagefile = ''    
#                         newImage = menu_dict    
#                         newtext = ''    
#                         textFont = None    
#                         textColor = ''    
#                         G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,menu_dict]    
#                         for subMesh in menu_dict['SubMenus']:    
#                             subMeshTag = shapeTag + "_" + subMesh[0]    
#                             if subMeshTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:                         
#                                 G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag] = {}       
#                             EventName = "ButtonDown"     
#                             if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag]:                 
#                                 G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag][EventName] = []       
#                             actionInfo = ["OnExpandOrShrink",subMeshTag,True]                          
#                             G_CanvasEventDictionary[uiName][drawCanvasName][subMeshTag][EventName].append(actionInfo) 
#                         G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
#                         DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'table':    
                        shapeTag = splitArray[-2]    
                        LockFlag = splitArray[-1]    
                        if splitArray[1].find('.') > 0:    
                            x1 = float(splitArray[1])
                        else:    
                            x1 = int(splitArray[1])
                            x1 = int(x1 * UIScale)
                        if splitArray[2].find('.') > 0:    
                            y1 = float(splitArray[2])
                        else:    
                            y1 = int(splitArray[2])
                            y1 = int(y1 * UIScale)
                        if splitArray[3].find('.') > 0:    
                            x2 = float(splitArray[3])
                        else:    
                            x2 = int(splitArray[3])
                            x2 = int(x2 * UIScale)
                        if splitArray[4].find('.') > 0:    
                            y2 = float(splitArray[4])
                        else:    
                            y2 = int(splitArray[4])
                            y2 = int(y2 * UIScale)
                        w  = x2 - x1    
                        h  = y2 - y1    
                        fill = splitArray[5]    
                        outline = splitArray[6]    
                        width = int(splitArray[7])
                        dashx = int(splitArray[8])
                        dashy = int(splitArray[9])
                        tableInfo_Begin = text.find('{')
                        tableInfo_End = text.rfind('}')
                        tableInfo_Text = text[tableInfo_Begin :tableInfo_End+1]    
                        table_dict = {}    
                        table_dict['font'] = []    
                        table_dict['font'].append(['System','12'])
                        table_dict['style'] = []    
                        table_dict['style'].append(['',0,'center','',0,''])
                        table_dict['style'].append(['',0,'center','',1,''])
                        table_dict['style'].append(['#EEEEEE',0,'center','',1,''])
                        table_dict['cows'] = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]    
                        table_dict['rows'] = []    
                        table_dict['merge'] = []    
                        try:    
                            table_dict = eval(tableInfo_Text)
                        except Exception as ex:    
                            MessageBox('表格加载错误'+':'+str(ex))
                        imagefile = ''    
                        newImage = table_dict    
                        if UIScale < 1.0:    
                            for FontInfo in table_dict['font']:    
                                FontInfo[1] = int(int(FontInfo[1]) * UIScale)
                                FontInfo[1] = str(FontInfo[1])
                        newtext = ''    
                        textFont = None    
                        textColor = ''    
                        G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,table_dict]    
                        G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'SetShapeRect':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        if splitArray[4].find('.') > 0:    
                            x = float(splitArray[4])
                        else:    
                            x = int(splitArray[4])
                            x = int(x * UIScale)
                        if splitArray[5].find('.') > 0:    
                            y = float(splitArray[5])
                        else:    
                            y = int(splitArray[5])
                            y = int(y * UIScale)
                        if splitArray[6].find('.') > 0:    
                            w = float(splitArray[6])
                        else:    
                            w = int(splitArray[6])
                            w = int(w * UIScale)
                        if splitArray[7].find('.') > 0:    
                            h = float(splitArray[7])
                        else:    
                            h = int(splitArray[7])
                            h = int(h * UIScale)
                        actionInfo = ["SetShapeRect",TargetShapeTag,x,y,w,h]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetFillColor':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        Color = splitArray[4]       
                        actionInfo = ["SetFillColor",TargetShapeTag,Color]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'SetOutlineColor':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        Color = splitArray[4]       
                        actionInfo = ["SetOutlineColor",TargetShapeTag,Color]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeImage':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        ImageFile = splitArray[4]    
                        actionInfo = ["ChangeImage",TargetShapeTag,ImageFile]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'ChangeText':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        Text = splitArray[4]    
                        TextColor = splitArray[5]    
                        actionInfo = ["ChangeText",TargetShapeTag,Text,TextColor]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'JumpToUI':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetUIName = splitArray[3]    
                        actionInfo = ["JumpToUI",shapeTag,TargetUIName]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'LoadUI':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        WidgetName = splitArray[3]    
                        TargetUIName = splitArray[4]    
                        actionInfo = ["LoadUI",shapeTag,WidgetName,TargetUIName]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'DeleteShape':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = splitArray[3]    
                        actionInfo = ["DeleteShape",TargetShapeTag]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'OnSwitch':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        TargetShapeTag = shapeTag    
                        actionInfo = ["OnSwitch",TargetShapeTag,True]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    elif ShapeType == 'CallFunction':    
                        shapeTag = splitArray[1]    
                        EventName = splitArray[2]    
                        FunctionName = drawCanvasName+"_"+shapeTag+"_on"+EventName    
                        CallBackFunc = None    
                        if hasattr(G_UICommandDictionary[uiName],FunctionName) == True:    
                            CallBackFunc = getattr(G_UICommandDictionary[uiName],FunctionName)
                        actionInfo = ["CallFunction",CallBackFunc,None]    
                        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
                        if EventName not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
                            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName] = []    
                        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][EventName].append(actionInfo)
                    else:    
                        if len(splitArray) > 11:    
                            if splitArray[1].find('.') > 0:    
                                x1 = float(splitArray[1])
                            else:    
                                x1 = int(splitArray[1])
                                x1 = int(x1 * UIScale)
                            if splitArray[2].find('.') > 0:    
                                y1 = float(splitArray[2])
                            else:    
                                y1 = int(splitArray[2])
                                y1 = int(y1 * UIScale)
                            if splitArray[3].find('.') > 0:    
                                x2 = float(splitArray[3])
                            else:    
                                x2 = int(splitArray[3])
                                x2 = int(x2 * UIScale)
                            if splitArray[4].find('.') > 0:    
                                y2 = float(splitArray[4])
                            else:    
                                y2 = int(splitArray[4])
                                y2 = int(y2 * UIScale)
                            w = x2 - x1    
                            if isinstance(w,float) == True:    
                                w = w * drawCanvas_width    
                            h = y2 - y1    
                            if isinstance(h,float) == True:    
                                h = h * drawCanvas_height    
                            fill = splitArray[5]    
                            outline = splitArray[6]    
                            width = int(splitArray[7])
                            dashx = int(splitArray[8])
                            dashy = int(splitArray[9])
                            imagefile = ''    
                            newImage = None    
                            newtext = ''    
                            textFont = None    
                            textColor = ''    
                            shapeTag = splitArray[10]    
                            G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy]    
                            G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                continue    
        f.close() 
        if hasGIFAnimation == True:    
            drawCanvas.after(100,updateGIFFrame(uiName,drawCanvasName))
        if uiName in G_CanvasEventDictionary:     
            for drawCanvasName in G_CanvasEventDictionary[uiName].keys():    
                drawCanvas = GetElement(uiName,drawCanvasName)
                for shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName].keys():    
                    for EventName in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:   
                        print(drawCanvasName + "tag_bind:"+shapeTag+"+>"+EventName) 
                        if EventName == "MouseEnter":    
                            drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
                        elif EventName == "MouseLeave":    
                            drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
                        elif EventName == "ButtonDown":    
                            drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
                        elif EventName == "ButtonMotion":    
                            drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
                        elif EventName == "ButtonUp":    
                            drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
                        elif EventName == "DoubleClick":    
                            drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
                            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName] and G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                                TextTag = shapeTag+"_text"    
                                drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
 
def GetShapePoint(uiName,drawCanvasName,shapeTag='',pointTag='',absoluteMode=True):  
    PrintFunctionInfo(GetShapePoint,[uiName,drawCanvasName,shapeTag,pointTag,absoluteMode])
    #获取绑定点位置  
    if uiName not in G_CanvasShapeDictionary:    
        return None    
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
            if shapeTag in G_CanvasPointDictionary[uiName][drawCanvasName]:      
                parentX1,parentY1,parentX2,parentY2 = GetShapeRect(uiName,drawCanvasName,shapeTag) 
                if pointTag in G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag]:     
                    shapeX = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][0]     
                    shapeY = G_CanvasPointDictionary[uiName][drawCanvasName][shapeTag][pointTag][1]     
                    if type(shapeX) == type(1.0):     
                        shapeX = int(shapeX * (parentX2-parentX1)) 
                    if type(shapeY) == type(1.0):     
                        shapeY = int(shapeY * (parentX2-parentX1)) 
                    if absoluteMode == True:     
                        shapeX = shapeX + parentX1     
                        shapeY = shapeY + parentY1     
                    return (shapeX,shapeY) 
    return None   
 
def SetShapeRect(uiName,canvasName,shapeTag,x1,y1,x2,y2): 
    PrintFunctionInfo(SetShapeRect,[uiName,canvasName,shapeTag,x1,y1,x2,y2]) 
    #设置矩形位置大小  
    if uiName in G_CanvasShapeDictionary:    
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                if shapeTag.find('text_') >= 0:    
                    drawCanvas.coords(shapeTag, x1,y1) 
                else:    
                    try:    
                        drawCanvas.coords(shapeTag, x1,y1,x2,y2) 
                    except:    
                        drawCanvas.coords(shapeTag, x1,y1) 
#               drawCanvas.itemconfig(shapeTag,width=x2-x1,height=y2-y1) 
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1] = x1    
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2] = y1    
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3] = x2    
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4] = y2    
def GetShapeRect(uiName,canvasName,shapeTag):  
    PrintFunctionInfo(GetShapeRect,[uiName,canvasName,shapeTag]) 
    #取得画布图形矩形位置大小  
    if uiName in G_CanvasShapeDictionary:    
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                if type(x1) == type(1.0):    
                    x1 = round(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                if type(y1) == type(1.0):    
                    y1 = round(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                if type(x2) == type(1.0):    
                    x2 = round(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                if type(y2) == type(1.0):    
                    y2 = round(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                return (x1,y1,x2,y2)
    return None   
 
def SetShapeFillColor(uiName,canvasName,shapeTag,color): 
    PrintFunctionInfo(SetShapeFillColor,[uiName,canvasName,shapeTag,color]) 
    #设置图形填充颜色  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':    
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:    
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, fill=color)
#                         OutlineTag = shapeTag+"_outline"    
#                         drawCanvas.itemconfig(OutlineTag, fill=color)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color    
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'text':    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color    
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][8]=color    
                else:    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][0]=color    
def GetShapeFillColor(uiName,canvasName,shapeTag):  
    PrintFunctionInfo(GetShapeFillColor,[uiName,canvasName,shapeTag]) 
    #取得画布图形颜色  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]    
    return None  
 
def SetShapeOutlineColor(uiName,canvasName,shapeTag,color): 
    PrintFunctionInfo(SetShapeOutlineColor,[uiName,canvasName,shapeTag,color]) 
    #设置图形边框颜色  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'cylinder':    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    OutlineTag = shapeTag+"_outline"    
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color    
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':    
                    OutlineTag = shapeTag+"_outline"    
                    ArcTag = shapeTag+"_arc"    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, fill=color)
                    drawCanvas.itemconfig(ArcTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color    
                else:    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, outline=color)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][1]=color    

def GetShapeOutlineColor(uiName,canvasName,shapeTag): 
    PrintFunctionInfo(GetShapeOutlineColor,[uiName,canvasName,shapeTag]) 
    #取得画布图形边框颜色  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]    
        return None   
 
def SetShapeLineWidth(uiName,canvasName,shapeTag,width):  
    PrintFunctionInfo(SetShapeLineWidth,[uiName,canvasName,shapeTag,width]) 
    #设置图形线条宽度  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'button':    
                    if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][-1] == None:    
                        drawCanvas = GetElement(uiName,canvasName)
                        drawCanvas.itemconfig(shapeTag, width=width)
                        G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width    
                elif G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'roundrect':    
                    OutlineTag = shapeTag+"_outline"    
                    ArcTag = shapeTag+"_arc"    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(OutlineTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width    
                else:    
                    drawCanvas = GetElement(uiName,canvasName)
                    drawCanvas.itemconfig(shapeTag, width=width)
                    G_CanvasParamDictionary[uiName][canvasName][shapeTag][2]=width    
 
def SetShapeImage(uiName,canvasName,shapeTag,imageFile,angle=0): 
    PrintFunctionInfo(SetShapeImage,[uiName,canvasName,shapeTag,imageFile,angle]) 
    #更换图片文件  
    if uiName in G_CanvasShapeDictionary:    
        drawCanvas = GetElement(uiName,canvasName)
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:     
                x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                w = x2 - x1    
                h = y2 - y1    
                newImage = None    
                if isinstance(imageFile,str) == True:    
                    for ImageInfo in G_CanvasImageDictionary[uiName][canvasName]:    
                        if ImageInfo[0] == imageFile and ImageInfo[2] == w and ImageInfo[3] == h :    
                            newImage = ImageInfo[1]    
                            continue    
                    if newImage == None:    
                        imageFile_Lower = imageFile.lower()
                        if imageFile_Lower in G_ResourcesFileList:    
                            resourPath = G_ResourcesFileList[imageFile_Lower]    
                            if os.path.exists(resourPath) == True:    
                                try:    
                                    imageRGBA = Image.open(resourPath).convert('RGBA')
                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                    newImage = ImageTk.PhotoImage(resizeImage.rotate(angle))
                                except:    
                                    return     
                        G_CanvasImageDictionary[uiName][canvasName].append([imageFile,newImage,w,h])
                elif imageFile:    
                    resizeImage = imageFile.resize((w, h),Image.LANCZOS)
                    newImage = ImageTk.PhotoImage(resizeImage.rotate(angle))
                    imageFile = ''    
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage    
                G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6] = imageFile    
                drawCanvas.itemconfig(shapeTag, image=newImage)
def GetShapeImage(uiName,canvasName,shapeTag):   
    PrintFunctionInfo(GetShapeImage,[uiName,canvasName,shapeTag]) 
    #取得画布图形图片文件  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:     
                return G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]    
    return None    
def PasteImageToShapeImage(uiName,canvasName,shapeTag,imageFileName,x1,x2,y1,y2,angle):  
    PrintFunctionInfo(PasteImageToShapeImage,[uiName,canvasName,shapeTag,imageFileName,x1,x2,y1,y2,angle]) 
    #将图片粘贴到画布的图片图形上  
    if uiName in G_CanvasShapeDictionary:    
        if canvasName in G_CanvasShapeDictionary[uiName]:    
            drawCanvas = GetElement(uiName,canvasName)
            if shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:     
                if G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0] == 'image':    
                    image_x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                    image_y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                    image_x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                    image_y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                    if type(image_x1) == type(1.0):    
                        image_x1 = int(image_x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                    if type(image_y1) == type(1.0):    
                        image_y1 = int(image_y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                    if type(image_x2) == type(1.0):    
                        if image_x2 <= 1.0:    
                            image_x2 = int(image_x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        else:    
                            image_x2 = image_x1 + int(image_x2)
                    if type(image_y2) == type(1.0):    
                        if image_y2 <= 1.0:    
                            image_y2 = int(image_y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        else:    
                            image_y2 = image_y1 + int(image_y2)
                    image_w = image_x2 - image_x1    
                    image_h = image_y2 - image_y1    
                    imageFile = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]    
                    imageFile_Lower = imageFile.lower()
                    if imageFile_Lower in G_ResourcesFileList:    
                        resourPath = G_ResourcesFileList[imageFile_Lower]    
                        if os.path.exists(resourPath) == True:    
                            try:    
                                imageRGBA = Image.open(resourPath).convert('RGBA')
                                bigImage = imageRGBA.resize((image_w, image_h),Image.LANCZOS)
                                imageFileName_Lower = imageFileName.lower()
                                if imageFileName_Lower in G_ResourcesFileList:    
                                    resourPath = G_ResourcesFileList[imageFileName_Lower]    
                                else:    
                                    resourPath = imageFileName    
                                    if os.path.exists(resourPath) == True:    
                                        try:    
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            w = x2 - x1    
                                            h = y2 - y1    
                                            smallImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            smallImage = smallImage.rotate(angle)
                                            bigImage.paste(smallImage, (x1,y1), mask=smallImage)
                                            newImage = ImageTk.PhotoImage(bigImage)
                                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage    
                                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6] = imageFile    
                                            drawCanvas.itemconfig(shapeTag, image=newImage) 
                                        except:    
                                            return     
                            except:    
                                return     

 
def SetShapeText(uiName,drawCanvasName,shapeTag,text,color = None):    
    PrintFunctionInfo(SetShapeText,[uiName,drawCanvasName,shapeTag,text,color]) 
    #设置画布文字及颜色  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5] = text     
                shapeTextTag = shapeTag     
                textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][7]     
                if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                    shapeTextTag = shapeTag+"_text"     
                    textcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]     
                if color:     
                    textcolor = color       
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6] = text    
                G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8] = textcolor    
                drawCanvas.itemconfigure(shapeTextTag,text=text)
                drawCanvas.itemconfigure(shapeTextTag,fill=textcolor)
def GetShapeText(uiName,drawCanvasName,shapeTag): 
    PrintFunctionInfo(GetShapeText,[uiName,drawCanvasName,shapeTag]) 
    #取得画布图形文字与颜色  
    if uiName not in G_CanvasShapeDictionary:    
        return None    
    if drawCanvasName in G_CanvasParamDictionary[uiName]:    
        if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]:     
            text = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][6]    
            textColor = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag][8]    
            return (text,textColor)
    return None    

def SetCanvasTableCellBGColor(uiName,drawCanvasName,shapeTag,row=0,col=0,bgColor='#FFFFFF'): 
    PrintFunctionInfo(SetCanvasTableCellBGColor,[uiName,drawCanvasName,shapeTag,row,col,bgColor]) 
    #设置单元格背景色  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        styleIndex = mergeInfo[3]    
                        StyleList = TableInfo['style']    
                        StyleInfo = StyleList[styleIndex]    
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[0] = bgColor    
                        if NewStyleInfo in TableInfo['style']:    
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:    
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                        Params[5] = TableInfo    
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if CowIndex == col and RowIndex == row:    
                            styleIndex = rowInfo[1]    
                            StyleList = TableInfo['style']    
                            StyleInfo = StyleList[styleIndex]    
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[0] = bgColor    
                            if NewStyleInfo in TableInfo['style']:    
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:    
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                            Params[5] = TableInfo    
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
def SetCanvasTableCellText(uiName,drawCanvasName,shapeTag,row=0,col=0,cellText=''): 
    PrintFunctionInfo(SetCanvasTableCellText,[uiName,drawCanvasName,shapeTag,row,col,cellText]) 
    #设置单元格文字,字符┇作为分隔符,可斜线分割单元格  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        mergeInfo[2] = str(cellText)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                        Params[5] = TableInfo    
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if CowIndex == col and RowIndex == row:    
                            rowInfo[0] = str(cellText)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                            Params[5] = TableInfo    
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
def SetCanvasTableCellTextColor(uiName,drawCanvasName,shapeTag,row=0,col=0,textColor='#000000'):  
    PrintFunctionInfo(SetCanvasTableCellTextColor,[uiName,drawCanvasName,shapeTag,row,col,textColor]) 
    #设置单元格文字颜色  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        styleIndex = mergeInfo[3]    
                        StyleList = TableInfo['style']    
                        StyleInfo = StyleList[styleIndex]    
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[3] = textColor    
                        if NewStyleInfo in TableInfo['style']:    
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:    
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                        Params[5] = TableInfo    
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if CowIndex == col and RowIndex == row:    
                            styleIndex = rowInfo[1]    
                            StyleList = TableInfo['style']    
                            StyleInfo = StyleList[styleIndex]    
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[3] = textColor    
                            if NewStyleInfo in TableInfo['style']:    
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:    
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                            Params[5] = TableInfo    
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
def SetCanvasTableCellTextFont(uiName,drawCanvasName,shapeTag,row=0,col=0,font='TkDefaultFont'):  
    PrintFunctionInfo(SetCanvasTableCellTextFont,[uiName,drawCanvasName,shapeTag,row,col,font]) 
    #设置单元格文字字体  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                #字体信息    
                familytext = font.actual('family')
                sizetext = font.actual('size')
                weighttext = font.actual('weight')
                slanttext = font.actual('slant')
                underlinetext = font.actual('underline')
                overstriketext = font.actual('overstrike')
                CellTextFontIndex = -1    
                FontIndex = 0    
                for FontInfo in TableInfo['font']:    
                    if FontInfo[0] == familytext and FontInfo[1] == sizetext and FontInfo[2] == weighttext and FontInfo[3] == slanttext and FontInfo[4] == underlinetext and FontInfo[5] == overstriketext:    
                        CellTextFontIndex = FontIndex    
                        break    
                    FontIndex = FontIndex + 1    
                if CellTextFontIndex < 0:    
                    CellTextFontIndex = len(TableInfo['font'])
                    TableInfo['font'].append([familytext,sizetext,weighttext,slanttext,underlinetext,overstriketext])
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        styleIndex = mergeInfo[3]    
                        StyleList = TableInfo['style']    
                        StyleInfo = StyleList[styleIndex]    
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[1] = CellTextFontIndex    
                        if NewStyleInfo in TableInfo['style']:    
                            mergeInfo[1] = TableInfo['style'].index(NewStyleInfo)
                        else:    
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[1] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                        Params[5] = TableInfo    
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if CowIndex == col and RowIndex == row:    
                            styleIndex = rowInfo[1]    
                            StyleList = TableInfo['style']    
                            StyleInfo = StyleList[styleIndex]    
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[1] = CellTextFontIndex    
                            if NewStyleInfo in TableInfo['style']:    
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:    
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                            Params[5] = TableInfo    
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
def SetCanvasTableCellTextAnchor(uiName,drawCanvasName,shapeTag,row=0,col=0,anchor='center'): 
    PrintFunctionInfo(SetCanvasTableCellTextAnchor,[uiName,drawCanvasName,shapeTag,row,col,anchor]) 
    #设置单元格文字对齐方式  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        styleIndex = mergeInfo[3]    
                        StyleList = TableInfo['style']    
                        StyleInfo = StyleList[styleIndex]    
                        NewStyleInfo = copy.deepcopy(StyleInfo)
                        NewStyleInfo[2] = anchor    
                        if NewStyleInfo in TableInfo['style']:    
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        else:    
                            TableInfo['style'].append(NewStyleInfo)
                            mergeInfo[3] = TableInfo['style'].index(NewStyleInfo)
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                        Params[5] = TableInfo    
                        DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                        return    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if CowIndex == col and RowIndex == row:    
                            styleIndex = rowInfo[1]    
                            StyleList = TableInfo['style']    
                            StyleInfo = StyleList[styleIndex]    
                            NewStyleInfo = copy.deepcopy(StyleInfo)
                            NewStyleInfo[2] = anchor    
                            if NewStyleInfo in TableInfo['style']:    
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            else:    
                                TableInfo['style'].append(NewStyleInfo)
                                rowInfo[1] = TableInfo['style'].index(NewStyleInfo)
                            drawCanvas.delete(shapeTag)
                            Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                            Params[5] = TableInfo    
                            DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                            return    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
def SetCanvasTableCellMerge(uiName,drawCanvasName,shapeTag,BeginRow=0,BeginCow=0,EndRow=0,EndCow=0):   
    PrintFunctionInfo(SetCanvasTableCellMerge,[uiName,drawCanvasName,shapeTag,BeginRow,BeginCow,EndRow,EndCow]) 
    #合并单元格  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                RowIndex = 0    
                for rowInfoLine in TableInfo['rows']:    
                    CowIndex = 0    
                    for rowInfo in rowInfoLine:    
                        if checkPtInRect(CowIndex,RowIndex,BeginCow,EndCow,BeginRow,EndRow) == True:    
                            rowInfo[1] = 0    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
                TableInfo['merge'].append([(BeginRow,BeginCow),(EndRow,EndCow),'',1])
                drawCanvas.delete(shapeTag)
                Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                Params[5] = TableInfo    
                DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
def SetCanvasTableCellSplit(uiName,drawCanvasName,shapeTag,row=0,col=0):  
    PrintFunctionInfo(SetCanvasTableCellSplit,[uiName,drawCanvasName,shapeTag,row,col]) 
    #拆分单元格  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                for mergeInfo in TableInfo['merge']:    
                    MergeBeginRow = mergeInfo[0][0]    
                    MergeBeginCow = mergeInfo[0][1]    
                    MergeEndRow = mergeInfo[1][0]    
                    MergeEndCow = mergeInfo[1][1]    
                    if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                        TableInfo['merge'].remove(mergeInfo)
                    RowIndex = 0    
                    for rowInfoLine in TableInfo['rows']:    
                        CowIndex = 0    
                        for rowInfo in rowInfoLine:    
                            if checkPtInRect(CowIndex,RowIndex,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                                rowInfo[1] = 1    
                        CowIndex = CowIndex + 1    
                    RowIndex = RowIndex + 1    
                drawCanvas.delete(shapeTag)
                Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                Params[5] = TableInfo    
                DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
def SetCanvasTableRowTextList(uiName,drawCanvasName,shapeTag,row=0,textList=[]): 
    PrintFunctionInfo(SetCanvasTableRowTextList,[uiName,drawCanvasName,shapeTag,row,textList]) 
    #使用列表填充表格整行文字  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:     
                drawCanvas = GetElement(uiName,drawCanvasName)
                x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
                y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
                x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
                y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
                if type(x1) == type(1.0):    
                    x1 = int(x1 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                if type(y1) == type(1.0):    
                    y1 = int(y1 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                if type(x2) == type(1.0):    
                    if x2 <= 1.0:    
                        x2 = int(x2 * G_CanvasSizeDictionary[uiName][drawCanvasName][0])
                    else:    
                        x2 = x1 + int(x2)
                if type(y2) == type(1.0):    
                    if y2 <= 1.0:    
                        y2 = int(y2 * G_CanvasSizeDictionary[uiName][drawCanvasName][1])
                    else:    
                        y2 = y1 + int(y2)
                TableInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][10]    
                if row < len(TableInfo['rows']):    
                    col = 0    
                    for cellText in textList:    
                        CellInfo = TableInfo['rows'][row][col]    
                        CellInfo[0] = str(cellText)
                        for mergeInfo in TableInfo['merge']:    
                            MergeBeginRow = mergeInfo[0][0]    
                            MergeBeginCow = mergeInfo[0][1]    
                            MergeEndRow = mergeInfo[1][0]    
                            MergeEndCow = mergeInfo[1][1]    
                            if checkPtInRect(col,row,MergeBeginCow,MergeEndCow,MergeBeginRow,MergeEndRow) == True:    
                                mergeInfo[2] = str(cellText)
                        col = col + 1    
                    drawCanvas.delete(shapeTag)
                    Params = G_CanvasParamDictionary[uiName][drawCanvasName][shapeTag]    
                    Params[5] = TableInfo    
                    DoCanvasRecord(drawCanvas,'table',x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
 
def BindShapeEvent_SetShapeRect(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,x,y,w,h):
    PrintFunctionInfo(BindShapeEvent_SetShapeRect,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,x,y,w,h])
    #绑定事件-设置图形位置与大小  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["SetShapeRect",targetShapeTag,x,y,w,h]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetFillColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):  
    PrintFunctionInfo(BindShapeEvent_SetFillColor,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color])
    #绑定事件-设置图形颜色  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["SetFillColor",targetShapeTag,color]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_SetOutlineColor(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color):   
    PrintFunctionInfo(BindShapeEvent_SetOutlineColor,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,color])
    #绑定事件-设置图形边框颜色  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["SetOutlineColor",targetShapeTag,color]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeImage(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,ImageFile):  
    PrintFunctionInfo(BindShapeEvent_ChangeImage,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,ImageFile])
    #绑定事件-更换图形图片  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:       
                actionInfo = ["ChangeImage",targetShapeTag,ImageFile]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_ChangeText(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,Text,TextColor):  
    PrintFunctionInfo(BindShapeEvent_ChangeText,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,Text,TextColor])
    #绑定事件-设置图形文字  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:       
                actionInfo = ["ChangeText",targetShapeTag,Text,TextColor]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_JumpToUI(uiName,drawCanvasName,shapeTag,bindEvent,targetUIName):  
    PrintFunctionInfo(BindShapeEvent_JumpToUI,[uiName,drawCanvasName,shapeTag,bindEvent,targetUIName])
    #绑定事件-跳转其它界面  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["JumpToUI",shapeTag,targetUIName]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_LoadUI(uiName,drawCanvasName,shapeTag,bindEvent,widgetName,targetUIName):   
    PrintFunctionInfo(BindShapeEvent_LoadUI,[uiName,drawCanvasName,shapeTag,bindEvent,widgetName,targetUIName])
    #绑定事件-嵌入界面  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["LoadUI",shapeTag,widgetName,targetUIName]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_DeleteShape(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag):   
    PrintFunctionInfo(BindShapeEvent_DeleteShape,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag])
    #绑定事件-删除图形  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["DeleteShape",targetShapeTag]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeEvent_CallFunction(uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,callBackFuncton,param = None):  
    PrintFunctionInfo(BindShapeEvent_CallFunction,[uiName,drawCanvasName,shapeTag,bindEvent,targetShapeTag,callBackFuncton,param])
    #绑定事件-调用函数  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                actionInfo = ["CallFunction",callBackFuncton,param]    
                BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo)
def BindShapeMouseEvent(uiName,drawCanvasName,shapeTag,bindEvent,actionInfo): 
    PrintFunctionInfo(BindShapeMouseEvent,[uiName,drawCanvasName,shapeTag,bindEvent,actionInfo])
    #对绑定事件进行处理  
    if uiName in G_CanvasShapeDictionary:    
        if shapeTag not in G_CanvasEventDictionary[uiName][drawCanvasName]:    
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag] = {}    
        if bindEvent not in G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag]:    
            G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent] = []    
        G_CanvasEventDictionary[uiName][drawCanvasName][shapeTag][bindEvent].append(actionInfo)
        drawCanvas = GetElement(uiName,drawCanvasName)
 
        if bindEvent == "MouseEnter":
            drawCanvas.tag_bind(shapeTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Any-Enter>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseEnter"))
        elif bindEvent == "MouseLeave": 
            drawCanvas.tag_bind(shapeTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"  
                drawCanvas.tag_bind(TextTag, "<Any-Leave>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="MouseLeave"))
        elif bindEvent == "ButtonDown": 
            drawCanvas.tag_bind(shapeTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown")) 
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonDown"))
        elif bindEvent == "ButtonMotion": 
            drawCanvas.tag_bind(shapeTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"
                drawCanvas.tag_bind(TextTag, "<B1-Motion>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonMotion"))
        elif bindEvent == "ButtonUp":   
            drawCanvas.tag_bind(shapeTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"    
                drawCanvas.tag_bind(TextTag, "<ButtonRelease-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="ButtonUp"))
        elif bindEvent == "DoubleClick": 
            drawCanvas.tag_bind(shapeTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
            if G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][0] == 'button':    
                TextTag = shapeTag+"_text"    
                drawCanvas.tag_bind(TextTag, "<Double-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=shapeTag,eventName="DoubleClick"))
 
def OnSwitch(uiName,drawCanvasName,shapeTag,actionInfo):  
    PrintFunctionInfo(OnSwitch,[uiName,drawCanvasName,shapeTag,actionInfo]) 
    #切换开关  
    if uiName not in G_CanvasShapeDictionary:    
        return None    
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
        if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete(shapeTag)
            x1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][1]    
            y1 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][2]    
            x2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][3]    
            y2 = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][4]    
            SwitchWidth = x2 - x1    
            SwitchHeight = y2 - y1    
            Switch_radius = int(SwitchHeight/2)
            fillcolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][5]    
            outlinecolor = G_CanvasShapeDictionary[uiName][drawCanvasName][shapeTag][6]    
            if actionInfo[2] == False:    
                fillcolor = '#777777'    
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+2, y1+2, x1+(SwitchHeight-3), y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+(SwitchWidth-int(1.0*SwitchHeight)), y1+int(SwitchHeight/2), text="Off",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = True    
            else:    
                drawCanvas.create_oval(x1, y1, x1+SwitchHeight, y1+SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight), y1, x1+SwitchWidth,y1+ SwitchHeight-1,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_rectangle(x1+Switch_radius,y1,x1+(SwitchWidth-Switch_radius),y1+SwitchHeight,fill=fillcolor,outline=outlinecolor,width=0, tag=shapeTag)
                drawCanvas.create_oval(x1+(SwitchWidth-SwitchHeight)-2, y1+2, x1+SwitchWidth-3, y1+(SwitchHeight-3),fill=outlinecolor,width=0,tag=shapeTag)
                drawCanvas.create_text(x1+int(0.8*SwitchHeight), y1+int(SwitchHeight/2), text="On",font = ("System",int(SwitchHeight/2)),anchor='center',fill=outlinecolor,width=0,tag=shapeTag)
                actionInfo[2] = False    
 
def OnExpandOrShrink(uiName,drawCanvasName,shapeTag,actionInfo):  
    PrintFunctionInfo(OnExpandOrShrink,[uiName,drawCanvasName,shapeTag,actionInfo]) 
    #展开或收缩菜单  
    if uiName not in G_CanvasShapeDictionary:    
        return None    
    if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
        listmenuNameIndex = shapeTag.rfind('_')
        listmenuName = shapeTag[0:listmenuNameIndex]    
        if listmenuName in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
            drawCanvas = GetElement(uiName,drawCanvasName)
            drawCanvas.delete('drawing_shape')
            drawInfo = G_CanvasShapeDictionary[uiName][drawCanvasName][listmenuName]    
            MenuInfo = drawInfo[10]    
            SubMenus = MenuInfo['SubMenus']    
            x1 = drawInfo[1]    
            y1 = drawInfo[2]    
            x2 = drawInfo[3]    
            y2 = drawInfo[4]    
            fillcolor = drawInfo[5]    
            outlinecolor = drawInfo[6]    
            fillwidth = int(drawInfo[7])
            dashx = int(drawInfo[8])
            dashy = int(drawInfo[9])
            for subMenu in SubMenus:    
                titleText = subMenu[0]    
                bgImgFile = subMenu[1]    
                itemList = subMenu[2]    
                subMenuTag = listmenuName +"_"+titleText    
                drawCanvas.delete(subMenuTag)
                if shapeTag == subMenuTag:    
                    if subMenu[3] == True:    
                        subMenu[3] = False    
                    else:    
                        subMenu[3] = True    
            DoCanvasRecord(drawCanvas,"listmenu",x1,y1,x2,y2,fillcolor,outlinecolor,fillwidth,dash1=0,dash2=0,newImage=MenuInfo,text='',textFont = None,textColor='',shapeTag=listmenuName)
            for subMenu in SubMenus:    
                titleText = subMenu[0]    
                subMenuTag = listmenuName +"_"+titleText    
                drawCanvas.tag_bind(subMenuTag, "<Button-1>",EventFunction_Adaptor(Shape_MouseEvent,uiName = uiName,canvasName = drawCanvasName,shapeTag=subMenuTag,eventName="ButtonDown"))
 
def DeleteShape(uiName,drawCanvasName,shapeTag):   
    PrintFunctionInfo(DeleteShape,[uiName,drawCanvasName,shapeTag])
    #删除画布中的画形  
    if uiName in G_CanvasShapeDictionary:    
        if drawCanvasName in G_CanvasShapeDictionary[uiName]:    
            if shapeTag in G_CanvasShapeDictionary[uiName][drawCanvasName]:    
                drawCanvas = GetElement(uiName,drawCanvasName)
                drawCanvas.delete(shapeTag)
                OutLineTag = shapeTag+"_outline"    
                drawCanvas.delete(OutLineTag)
                G_CanvasShapeDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasEventDictionary[uiName]:    
                    if shapeTag in G_CanvasEventDictionary[uiName][drawCanvasName]:    
                        G_CanvasEventDictionary[uiName][drawCanvasName].pop(shapeTag)
                if drawCanvasName in G_CanvasParamDictionary[uiName]:    
                    if shapeTag in G_CanvasParamDictionary[uiName][drawCanvasName]:    
                        G_CanvasParamDictionary[uiName][drawCanvasName].pop(shapeTag)
 
def ReDrawCanvasShape(uiName,canvasName):  
    PrintFunctionInfo(ReDrawCanvasShape,[uiName,canvasName])
    #重绘界面指定画布。参数1:界面类名,参数2:画布名称  
    hasGIFAnimation = False       
    drawCanvas = GetElement(uiName,canvasName)
    if uiName in G_UIElementAliasDictionary.keys() and canvasName in G_UIElementAliasDictionary[uiName].keys():    
        canvasName = G_UIElementAliasDictionary[uiName][canvasName]    
    if drawCanvas:    
        if uiName in G_CanvasSizeDictionary:    
            if  canvasName in G_CanvasSizeDictionary[uiName]:    
                for shapeTag in G_CanvasShapeDictionary[uiName][canvasName]:    
                    ShapeType = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][0]    
                    if ShapeType == 'image':    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        image_handle = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5]    
                        image_filename = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][6]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        if w == 1 and h == 1:    
                            continue    
                        newImage = None    
                        if newImage == None:    
                            image_filename_Lower = image_filename.lower()
                            if image_filename_Lower in G_ResourcesFileList:    
                                resourPath = G_ResourcesFileList[image_filename_Lower]    
                                if os.path.exists(resourPath) == True:    
                                    try:    
                                        if image_filename.find('.gif') >= 0:    
                                            GifData = Image.open(resourPath)
                                            seq = []    
                                            try:    
                                                while 1:    
                                                    imageRGBA = GifData.copy().convert('RGBA')
                                                    resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                                    newImage = ImageTk.PhotoImage(resizeImage)
                                                    seq.append(newImage)
                                                    GifData.seek(len(seq))
                                            except EOFError:    
                                                pass    
                                            delay = 100    
                                            try:    
                                                delay = GifData.info['duration']    
                                            except KeyError:    
                                                delay = 100    
                                            if delay == 0:    
                                                delay = 100    
                                            newImage = [seq,delay,0]    
                                            hasGIFAnimation = True    
                                        else:    
                                            imageRGBA = Image.open(resourPath).convert('RGBA')
                                            resizeImage = imageRGBA.resize((w, h),Image.LANCZOS)
                                            newImage = ImageTk.PhotoImage(resizeImage)
                                    except Exception as Ex:    
                                        OutputText = resourPath + ":"+str(Ex)
                                        print(OutputText)
                                        return     
                                else:    
                                    print("找不到"+resourPath)
                            else:    
                                print("Resources目录找不到"+image_filename)
                            #G_CanvasImageDictionary[uiName][canvasName].append([imagefile,newImage,w,h])
                            #G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,newImage,image_filename]    
                            G_CanvasShapeDictionary[uiName][canvasName][shapeTag][5] = newImage    
                            G_CanvasParamDictionary[uiName][canvasName][shapeTag][5] = newImage       
                            drawCanvas.delete(shapeTag)   
                            Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                            DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'text':    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'button':    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'point':    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
                    elif ShapeType == 'table':    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
#                     elif ShapeType == 'listmenu':    
#                         shapeTag = splitArray[-2]    
#                         LockFlag = splitArray[-1]    
#                         if splitArray[1].find('.') > 0:    
#                             x1 = float(splitArray[1])
#                         else:    
#                             x1 = int(splitArray[1])
#                         if splitArray[2].find('.') > 0:    
#                             y1 = float(splitArray[2])
#                         else:    
#                             y1 = int(splitArray[2])
#                         if splitArray[3].find('.') > 0:    
#                             x2 = float(splitArray[3])
#                         else:    
#                             x2 = int(splitArray[3])
#                         if splitArray[4].find('.') > 0:    
#                             y2 = float(splitArray[4])
#                         else:    
#                             y2 = int(splitArray[4])
#                         w  = x2 - x1    
#                         h  = y2 - y1    
#                         fill = splitArray[5]    
#                         outline = splitArray[6]    
#                         width = int(splitArray[7])
#                         dashx = int(splitArray[8])
#                         dashy = int(splitArray[9])
#                         menuInfo_Begin = text.find('{')
#                         menuInfo_End = text.rfind('}')
#                         menuInfo = text[menuInfo_Begin :menuInfo_End+1]    
#                         menuInfo = menuInfo.replace("'",'"')
#                         menu_dict = json.loads(menuInfo)
#                         imagefile = ''    
#                         newImage = menu_dict    
#                         newtext = ''    
#                         textFont = None    
#                         textColor = ''    
#                         G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,menu_dict]    
#                         for subMesh in menu_dict['SubMenus']:    
#                             subMeshTag = shapeTag + "_" + subMesh[0]    
#                             if subMeshTag not in G_CanvasEventDictionary[uiName][canvasName]:    
#                                 G_CanvasEventDictionary[uiName][canvasName][subMeshTag] = {}    
#                             EventName = "ButtonDown"    
#                             if EventName not in G_CanvasEventDictionary[uiName][canvasName][subMeshTag]:    
#                                 G_CanvasEventDictionary[uiName][canvasName][subMeshTag][EventName] = []    
#                             actionInfo = ["OnExpandOrShrink",subMeshTag,True]    
#                             G_CanvasEventDictionary[uiName][canvasName][subMeshTag][EventName].append(actionInfo)
#                         G_CanvasParamDictionary[uiName][canvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
#                         DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
#                     elif ShapeType == 'table':    
#                         shapeTag = splitArray[-2]    
#                         LockFlag = splitArray[-1]    
#                         if splitArray[1].find('.') > 0:    
#                             x1 = float(splitArray[1])
#                         else:    
#                             x1 = int(splitArray[1])
#                         if splitArray[2].find('.') > 0:    
#                             y1 = float(splitArray[2])
#                         else:    
#                             y1 = int(splitArray[2])
#                         if splitArray[3].find('.') > 0:    
#                             x2 = float(splitArray[3])
#                         else:    
#                             x2 = int(splitArray[3])
#                         if splitArray[4].find('.') > 0:    
#                             y2 = float(splitArray[4])
#                         else:    
#                             y2 = int(splitArray[4])
#                         w  = x2 - x1    
#                         h  = y2 - y1    
#                         fill = splitArray[5]    
#                         outline = splitArray[6]    
#                         width = int(splitArray[7])
#                         dashx = int(splitArray[8])
#                         dashy = int(splitArray[9])
#                         tableInfo_Begin = text.find('{')
#                         tableInfo_End = text.rfind('}')
#                         tableInfo = text[tableInfo_Begin :tableInfo_End+1]    
#                         tableInfo = tableInfo.replace("'",'"')
#                         table_dict = json.loads(tableInfo)
#                         imagefile = ''    
#                         newImage = table_dict    
#                         newtext = ''    
#                         textFont = None    
#                         textColor = ''    
#                         G_CanvasShapeDictionary[uiName][canvasName][shapeTag]=[ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,table_dict]    
#                         G_CanvasParamDictionary[uiName][canvasName][shapeTag]=[fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor]    
#                         DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,fill,outline,width,dashx,dashy,newImage,newtext,textFont,textColor,shapeTag)
                    elif ShapeType == 'SetShapeRect':    
                        pass    
                    elif ShapeType == 'SetFillColor':    
                        pass    
                    elif ShapeType == 'SetOutlineColor':    
                        pass    
                    elif ShapeType == 'ChangeImage':    
                        pass    
                    elif ShapeType == 'ChangeText':    
                        pass    
                    elif ShapeType == 'JumpToUI':    
                        pass    
                    elif ShapeType == 'LoadUI':    
                        pass    
                    elif ShapeType == 'DeleteShape':    
                        pass    
                    elif ShapeType == 'OnSwitch':    
                        pass    
                    elif ShapeType == 'CallFunction':    
                        pass    
                    else:    
                        x1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][1]    
                        y1 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][2]    
                        x2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][3]    
                        y2 = G_CanvasShapeDictionary[uiName][canvasName][shapeTag][4]    
                        if type(x1) == type(1.0):    
                            x1 = int(x1 * G_CanvasSizeDictionary[uiName][canvasName][0])
                        if type(y1) == type(1.0):    
                            y1 = int(y1 * G_CanvasSizeDictionary[uiName][canvasName][1])
                        if type(x2) == type(1.0):    
                            if x2 <= 1.0:    
                                x2 = int(x2 * G_CanvasSizeDictionary[uiName][canvasName][0])
                            else:    
                                x2 = x1 + int(x2)
                        if type(y2) == type(1.0):    
                            if y2 <= 1.0:    
                                y2 = int(y2 * G_CanvasSizeDictionary[uiName][canvasName][1])
                            else:    
                                y2 = y1 + int(y2)
                        w = x2 - x1    
                        if isinstance(w,float) == True:    
                            w = w * G_CanvasSizeDictionary[uiName][canvasName][0]    
                        h = y2 - y1    
                        if isinstance(h,float) == True:    
                            h = h * G_CanvasSizeDictionary[uiName][canvasName][1]    
                        drawCanvas.delete(shapeTag)
                        Params = G_CanvasParamDictionary[uiName][canvasName][shapeTag]    
                        DoCanvasRecord(drawCanvas,ShapeType,x1,y1,x2,y2,Params[0],Params[1],Params[2],Params[3],Params[4],Params[5],Params[6],Params[7],Params[8],shapeTag)
        drawCanvas.update()
        if hasGIFAnimation == True:    
            drawCanvas.after(100,updateGIFFrame(uiName,canvasName))
def ReDrawCanvasRecord(uiName,ForceReDraw=False): 
    PrintFunctionInfo(ReDrawCanvasRecord,[uiName,ForceReDraw])
    #重绘界面所有画布。参数1:界面类名,参数2:是否强制更新  
    ReDraw = False    
    if uiName in G_CanvasSizeDictionary:    
        for canvasName in G_CanvasSizeDictionary[uiName]:    
            drawCanvas = GetElement(uiName,canvasName) 
            drawCanvas_width = drawCanvas.winfo_width()
            drawCanvas_height = drawCanvas.winfo_height()
            if canvasName == "Form_1":    
                root = GetElement(uiName,"root")
                drawCanvas_width = root.winfo_width()
                drawCanvas_height = root.winfo_height()
            if ForceReDraw == True or G_CanvasSizeDictionary[uiName][canvasName][0] != drawCanvas_width or G_CanvasSizeDictionary[uiName][canvasName][1] != drawCanvas_height:    
                ReDraw = True    
            G_CanvasSizeDictionary[uiName][canvasName] = [drawCanvas_width,drawCanvas_height]    
    if ReDraw == True:    
        if G_CanvasSizeDictionary[uiName][canvasName][0] == 1 and G_CanvasSizeDictionary[uiName][canvasName][1] == 1:    
            return     
        print("ReDrawCanvasRecord")
        if uiName in G_CanvasShapeDictionary:    
            for canvasName in G_CanvasSizeDictionary[uiName]:    
                ReDrawCanvasShape(uiName,canvasName)
    if uiName in G_UIElementRoundRectangleDictionary:    
        for elementName in G_UIElementRoundRectangleDictionary[uiName]:    
            Control = G_UIElementDictionary[uiName][elementName]    
            if Control:    
                RRInfo = G_UIElementRoundRectangleDictionary[uiName][elementName]    
                ShowRoundedRectangle(Control,RRInfo[0],RRInfo[1])
def ResizeAllChart(uiName,forceRedraw=False):   
    PrintFunctionInfo(ResizeAllChart,[uiName,forceRedraw])
    #更新图表  
    if uiName in G_UIElementUserDataArray.keys():    
        for elementName in G_UIElementUserDataArray[uiName]:    
            ChartReady = 0    
            for EBData in G_UIElementUserDataArray[uiName][elementName]:    
                if EBData[0] == 'ChartReady':    
                    ChartReady = EBData[2]    
                if EBData[0] == 'ChartCanvas' and (ChartReady == 1 or forceRedraw == True):    
                    theChart = EBData[2]    
                    theChartCanvas = theChart.get_tk_widget()
                    w = theChartCanvas.winfo_width()
                    h = theChartCanvas.winfo_height()
                    if w == 1 and h == 1:    
                        parentWidget = theChartCanvas._nametowidget(theChartCanvas.winfo_parent())
                        if "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:    
                            w = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]    
                            w = int(w * parentWidget.winfo_width())
                        else:    
                            w = G_UIElementPlaceDictionary[uiName][elementName]["width"]    
                        if "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:    
                            h = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]    
                            h = int(h * parentWidget.winfo_width())
                        else:    
                            h = G_UIElementPlaceDictionary[uiName][elementName]["height"]    
                    else:    
                        oldw = W    
                        oldh = h    
                        parentWidget = theChartCanvas._nametowidget(theChartCanvas.winfo_parent())
                        if "relwidth" in G_UIElementPlaceDictionary[uiName][elementName]:    
                            oldw = G_UIElementPlaceDictionary[uiName][elementName]["relwidth"]    
                            oldw = int(oldw * parentWidget.winfo_width())
                        else:    
                            oldw = G_UIElementPlaceDictionary[uiName][elementName]["width"]    
                        if "relheight" in G_UIElementPlaceDictionary[uiName][elementName]:    
                            oldh = G_UIElementPlaceDictionary[uiName][elementName]["relheight"]    
                            oldh = int(oldh * parentWidget.winfo_height())
                        else:    
                            oldh = G_UIElementPlaceDictionary[uiName][elementName]["height"]    
                        if forceRedraw == False and w == oldw and h == oldh:    
                            continue    
                    event = ChartEvent(w,h,theChartCanvas)
                    theChart.resize(event)
                    theChartCanvas.update()  
 
PyMeStyleRadioGroup = {}    
def OnRadioButtonClick1(uiName,elementName,groupid,radio_value,keepselected=False):   
    PrintFunctionInfo(OnRadioButtonClick1,[groupid,radio_value])
    GroupName = G_UIGroupDictionary[uiName][elementName]
    if groupid in PyMeStyleRadioGroup.keys():    
        for RadioInfo in PyMeStyleRadioGroup[groupid]:
            RadioButtonName = RadioInfo["name"]  
            OriBGColor = '#EFEFEF'
            OriFGColor = '#000000'
            BGColor = '#EFEFEF'
            FGColor = '#000000'
            if RadioButtonName in G_UIRadioButtonGroupArray[uiName][GroupName]:
                OriBGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][0][0]    
                OriFGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][0][1]   
                BGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][1][0]
                FGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][1][1]
            if RadioInfo["var"] == radio_value:    
                RadioInfo["radio"].select()
                RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_yes"])
                if keepselected == False:
                    bgColor = RadioInfo["radio"].cget("activebackground")
                    RadioInfo["icon"].configure(bg = bgColor)
                    RadioInfo["radio"].configure(bg = bgColor)
                    RadioInfo["radio"].configure(fg = FGColor)
                else:
                    RadioInfo["icon"].configure(bg = BGColor)
                    RadioInfo["radio"].configure(bg = BGColor)
                    RadioInfo["radio"].configure(fg = FGColor)
            else:    
                RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_no"])
                RadioInfo["icon"].configure(bg = OriBGColor)
                RadioInfo["radio"].configure(bg = OriBGColor)
                RadioInfo["radio"].configure(fg = OriFGColor)
def OnRadioButtonClick2(uiName,elementName,groupid,radio_value):  
    PrintFunctionInfo(OnRadioButtonClick2,[groupid,radio_value])
    GroupName = G_UIGroupDictionary[uiName][elementName]
    if groupid in PyMeStyleRadioGroup.keys():    
        for RadioInfo in PyMeStyleRadioGroup[groupid]:
            RadioButtonName = RadioInfo["name"]  
            if RadioInfo["var"] == radio_value:   
                OriBGColor = '#EFEFEF'
                OriFGColor = '#000000'
                BGColor = '#EFEFEF'
                FGColor = '#000000'
                if RadioButtonName in G_UIRadioButtonGroupArray[uiName][GroupName]:
                    OriBGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][0][0]    
                    OriFGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][0][1]   
                    BGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][1][0]
                    FGColor = G_UIRadioButtonGroupArray[uiName][GroupName][RadioButtonName][1][1]
                RadioInfo["radio"].select()
                RadioInfo["icon"].itemconfig("icon_image", image=RadioInfo["tkimage_yes"])
                RadioInfo["icon"].configure(bg = BGColor)
                RadioInfo["radio"].configure(bg = BGColor)
                RadioInfo["radio"].configure(fg = FGColor)
                return 

def OnRadioButtonConfigure(event):   
    PrintFunctionInfo(OnRadioButtonConfigure,[event])
    for groupid in PyMeStyleRadioGroup.keys():    
        for RadioInfo in PyMeStyleRadioGroup[groupid]:    
            if RadioInfo["radio"] is event.widget:    
                radio_x = event.widget.winfo_x()
                radio_y = event.widget.winfo_y()
                radio_height = event.widget.winfo_height()
                radio_req_height = event.widget.winfo_reqheight()
                radio_circle_size = int(radio_req_height*0.8)
                if radio_circle_size < 26:    
                    radio_circle_size = 26    
                RadioInfo["icon"](x=radio_x + 4 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)
def SetRadioButtonPyMeStyle(uiName,elementName,radiovalue,oval_color,over_select_color,visible = True):  
    PrintFunctionInfo(SetRadioButtonPyMeStyle,[uiName,elementName,radiovalue,oval_color,over_select_color,visible])
    global PyMeStyleRadioGroup 
    if elementName in G_UIGroupDictionary[uiName]:     
        GroupName = G_UIGroupDictionary[uiName][elementName]    
        if GroupName.find("Group_") == 0:    
            GroupText = GroupName[6:]     
            GroupID = int(GroupText)  
            Control = GetElement(uiName,elementName)
            if Control :    
                text = Control.cget("text")
                font = Control.cget("font")
                if type(font) == type('TkDefaultFont'):
                    font = tkinter.font.Font(font=font)
                spacechar_width = font.measure(' ')
                parentinfo = Control.winfo_parent()
                parentwidget = Control._nametowidget(parentinfo)
                Control.bind("<Button-1>", lambda event: OnRadioButtonClick1(uiName,elementName,GroupID,radiovalue))
                Control.bind("<ButtonRelease-1>", lambda event: OnRadioButtonClick2(uiName,elementName,GroupID,radiovalue))
                Control.bind("<Configure>", OnRadioButtonConfigure)
                radio_x = Control.winfo_x()
                radio_y = Control.winfo_y()
                radio_bg = Control.cget('bg')
                radio_height = Control.winfo_height()
                radio_req_height = Control.winfo_reqheight()
                radio_circle_size = int(radio_req_height*0.8)
                if radio_circle_size < 26:    
                    radio_circle_size = 26    
                small_radio_icon = tkinter.Canvas(parentwidget,bg=radio_bg,highlightthickness=0,bd=0)
                image_no = Image.new('RGBA', (radio_circle_size, radio_circle_size), '#00000000')
                draw = aggdraw.Draw(image_no)
                border_p = aggdraw.Pen(oval_color,2)
                draw.ellipse((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
                draw.flush()
                tkimage_no = ImageTk.PhotoImage(image_no)
                image_yes = Image.new('RGBA', (radio_circle_size, radio_circle_size), '#00000000')
                draw = aggdraw.Draw(image_yes)
                border_p = aggdraw.Pen(over_select_color,2)
                draw.ellipse((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
                center_b = aggdraw.Brush(over_select_color)
                draw.ellipse((8,8,radio_circle_size-8,radio_circle_size-8), center_b)
                draw.flush()
                tkimage_yes = ImageTk.PhotoImage(image_yes)
                small_radio_icon.create_image(0, 0,image=tkimage_no,anchor='nw',tag="icon_image")
                small_radio_icon.place(x=radio_x + 4 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)
                small_radio_icon.bind("<Button-1>", lambda event: OnRadioButtonClick1(uiName,elementName,GroupID,radiovalue))
                small_radio_icon.bind("<ButtonRelease-1>", lambda event: OnRadioButtonClick2(uiName,elementName,GroupID,radiovalue))
                if GroupID not in PyMeStyleRadioGroup:    
                    PyMeStyleRadioGroup[GroupID] = []    
                NewRadioInfo = {"name":elementName,"radio":Control,"var":radiovalue,"icon":small_radio_icon,"border_color":oval_color,"image_no":image_no,"image_yes":image_yes,"tkimage_no":tkimage_no,"tkimage_yes":tkimage_yes}    
                PyMeStyleRadioGroup[GroupID].append(NewRadioInfo)
                
                #计算需要前面补几个空格可以给自绘图留出合适宽度
                space_count = len(text) - len(text.lstrip())
                if space_count >= 2:
                    space_count -= 2
                space_count += 2
                text = ' ' * space_count + text.lstrip()
                Control.configure(text = text)
                if visible == False:
                    small_radio_icon.place_forget()
PyMeStyleCheckButton = {}    
def OnCheckButtonClick1(event,uiName,elementName):   
    PrintFunctionInfo(OnCheckButtonClick1,[event,uiName,elementName])
    global PyMeStyleCheckButton    
    print("OnCheckButtonClick1")
    if uiName in PyMeStyleCheckButton.keys():    
        for CheckInfo in PyMeStyleCheckButton[uiName]:    
            if CheckInfo["checkbutton"] is event.widget or CheckInfo["icon"] is event.widget:    
                CheckValue = GetCurrentValue(uiName,elementName)
                print("Value:"+str(CheckValue))
                if CheckValue == 0:    
                    CheckInfo["icon"].itemconfig("icon_image", image=CheckInfo["tkimage_yes"])
                    if CheckInfo["icon"] is event.widget:    
                        #SetCurrentValue(uiName,elementName,1)
                        CheckInfo["checkbutton"].select()
                    if elementName in G_UIRadioButtonGroupArray[uiName]:
                        BGColor = G_UIRadioButtonGroupArray[uiName][elementName][1][0]    
                        FGColor = G_UIRadioButtonGroupArray[uiName][elementName][1][1]   
                        
                        CheckInfo["checkbutton"].configure(bg=BGColor)
                        CheckInfo["checkbutton"].configure(fg=FGColor)
                        if CheckInfo["checkbutton"] is event.widget:    
                            bgColor = CheckInfo["checkbutton"].cget("activebackground") 
                            CheckInfo["icon"].configure(bg = bgColor) 
                        else:
                            CheckInfo["icon"].configure(bg = BGColor) 

                else:    
                    CheckInfo["icon"].itemconfig("icon_image", image=CheckInfo["tkimage_no"])
                    if CheckInfo["icon"] is event.widget:    
                        #SetCurrentValue(uiName,elementName,0)
                        CheckInfo["checkbutton"].deselect()
                    if elementName in G_UIRadioButtonGroupArray[uiName]:
                        OriBGColor = G_UIRadioButtonGroupArray[uiName][elementName][0][0]    
                        OriFGColor = G_UIRadioButtonGroupArray[uiName][elementName][0][1]    
                        bgColor = CheckInfo["checkbutton"].cget("activebackground") 
                        CheckInfo["icon"].configure(bg = bgColor) 
                        CheckInfo["checkbutton"].configure(bg=bgColor)
                        CheckInfo["checkbutton"].configure(fg=bgColor)
                return 

def OnCheckButtonClick2(event,uiName,elementName):
    PrintFunctionInfo(OnCheckButtonClick2,[event,uiName,elementName])
    global PyMeStyleCheckButton    
    if uiName in PyMeStyleCheckButton.keys():    
        for CheckInfo in PyMeStyleCheckButton[uiName]:    
            if CheckInfo["checkbutton"] is event.widget or CheckInfo["icon"] is event.widget:    
                if elementName in G_UIRadioButtonGroupArray[uiName]:
                    CheckValue = GetCurrentValue(uiName,elementName)
                    OriBGColor = G_UIRadioButtonGroupArray[uiName][elementName][0][0]    
                    OriFGColor = G_UIRadioButtonGroupArray[uiName][elementName][0][1]   
                    BGColor = G_UIRadioButtonGroupArray[uiName][elementName][1][0]    
                    FGColor = G_UIRadioButtonGroupArray[uiName][elementName][1][1] 
                    if CheckValue == 0: 
                        CheckInfo["icon"].configure(bg = OriBGColor) 
                        CheckInfo["checkbutton"].configure(bg=OriBGColor)
                        CheckInfo["checkbutton"].configure(fg=OriFGColor)
                    else:
                        CheckInfo["icon"].configure(bg = OriBGColor) 
                        CheckInfo["checkbutton"].configure(bg=OriBGColor)
                        CheckInfo["checkbutton"].configure(fg=OriFGColor)

def OnCheckButtonConfigure(event):   
    PrintFunctionInfo(OnCheckButtonConfigure,[event])
    global PyMeStyleCheckButton    
    for uiName in PyMeStyleCheckButton.keys():    
        for CheckInfo in PyMeStyleCheckButton[uiName]:    
            if CheckInfo["checkbutton"] is event.widget:    
                radio_x = event.widget.winfo_x()
                radio_y = event.widget.winfo_y()
                radio_height = event.widget.winfo_height()
                radio_req_height = event.widget.winfo_reqheight()
                radio_circle_size = int(radio_req_height*0.8)
                if radio_circle_size < 26:    
                    radio_circle_size = 26    
                CheckInfo["icon"].place(x=radio_x + 4 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)

def SetCheckButtonPyMeStyle(uiName,elementName,checkbutton_value,oval_color,over_select_color,visible = True):  
    PrintFunctionInfo(SetCheckButtonPyMeStyle,[uiName,elementName,checkbutton_value,oval_color,over_select_color,visible])
    global PyMeStyleCheckButton    
    Control = GetElement(uiName,elementName)
    if Control :   
        text = Control.cget("text")
        font = Control.cget("font")
        if type(font) == type('TkDefaultFont'):
            font = tkinter.font.Font(font=font)
        spacechar_width = font.measure(' ')
        parentinfo = Control.winfo_parent()
        parentwidget = Control._nametowidget(parentinfo)
        Control.bind("<Button-1>", lambda event: OnCheckButtonClick1(event,uiName,elementName))
        Control.bind("<ButtonRelease-1>", lambda event: OnCheckButtonClick2(event,uiName,elementName))
        Control.bind("<Configure>", OnCheckButtonConfigure)
        radio_x = Control.winfo_x()
        radio_y = Control.winfo_y()
        radio_bg = Control.cget('bg')
        radio_height = Control.winfo_height()
        radio_req_height = Control.winfo_reqheight()
        radio_circle_size = int(radio_req_height*0.8)
        if radio_circle_size < 26:    
            radio_circle_size = 26    
        small_radio_icon = tkinter.Canvas(parentwidget,bg=radio_bg,highlightthickness=0,bd=0)
        image_no = Image.new('RGBA', (radio_circle_size, radio_circle_size), '#00000000')
        draw = aggdraw.Draw(image_no)
        border_p = aggdraw.Pen(oval_color,2)
        draw.rectangle((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        draw.flush()
        tkimage_no = ImageTk.PhotoImage(image_no)
        image_yes = Image.new('RGBA', (radio_circle_size, radio_circle_size), '#00000000')
        draw = aggdraw.Draw(image_yes)
        border_p = aggdraw.Pen(over_select_color,2)
        draw.rectangle((4,4,radio_circle_size-4,radio_circle_size-4), border_p)
        center_b = aggdraw.Brush(over_select_color)
        draw.rectangle((8,8,radio_circle_size-8,radio_circle_size-8), center_b)
        draw.flush()
        tkimage_yes = ImageTk.PhotoImage(image_yes)
        if checkbutton_value == True:    
            small_radio_icon.create_image(0, 0,image=tkimage_yes,anchor='nw',tag="icon_image")
        else:    
            small_radio_icon.create_image(0, 0,image=tkimage_no,anchor='nw',tag="icon_image")
        small_radio_icon.place(x=radio_x + 4 ,y = radio_y + radio_height//2 - radio_circle_size//2,width=radio_circle_size, height=radio_circle_size)
        small_radio_icon.bind("<Button-1>", lambda event: OnCheckButtonClick1(event,uiName,elementName))
        small_radio_icon.bind("<ButtonRelease-1>", lambda event: OnCheckButtonClick2(event,uiName,elementName))
        if uiName not in PyMeStyleCheckButton:    
            PyMeStyleCheckButton[uiName] = []    
        NewCheckButtonInfo = {"checkbutton":Control,"icon":small_radio_icon,"border_color":oval_color,"image_no":image_no,"image_yes":image_yes,"tkimage_no":tkimage_no,"tkimage_yes":tkimage_yes}    
        PyMeStyleCheckButton[uiName].append(NewCheckButtonInfo)
        #计算需要前面补几个空格可以给自绘图留出合适宽度
        space_count = len(text) - len(text.lstrip())
        if space_count >= 2:
            space_count -= 2
        space_count += 2
        text = ' ' * space_count + text.lstrip()
        Control.configure(text = text)
        if visible == False:
            small_radio_icon.place_forget()
 
def CtrlCCopy_CallBack(event):    
    currIndex = event.widget.curselection()
    currIndexCount = len(currIndex)
    if currIndexCount > 0:    
        import pyperclip    
        if currIndexCount == 1:    
            currText = event.widget.get(currIndex[0])
        else:    
            currText = ""    
            for i in range(currIndexCount):    
                currText = currText + event.widget.get(currIndex[i]) + "\n"    
        pyperclip.copy(currText)
def KeyUpDown_CallBack(event):    
    if event.keysym == "Up":    
        currIndex = event.widget.curselection()
        if currIndex[0] > 0:    
            event.widget.selection_clear(0, "end")
            event.widget.selection_set(currIndex[0]-1)
            event.widget.see(currIndex[0] - 1)
    elif event.keysym == "Down":    
        currIndex = event.widget.curselection()
        if currIndex[0] < event.widget.size() - 1:    
            event.widget.selection_clear(0, "end")
            event.widget.selection_set(currIndex[0]+1)
            event.widget.see(currIndex[0] + 1)
def EnableCtrlCCopyContent(uiName,elementName):    
    Control = GetElement(uiName,elementName)
    if Control :    
        Control.bind("<Control-c>",CtrlCCopy_CallBack)
        Control.bind("<Up>",KeyUpDown_CallBack)
        Control.bind("<Down>",KeyUpDown_CallBack)  

def ListView_CtrlCCopy_CallBack(event):  
    item = event.widget.selection()
    item_text = event.widget.item(item, "values")
    import pyperclip
    pyperclip.copy(str(item_text))
def ListView_EnableCtrlCCopyContent(uiName,elementName):    
    Control = GetElement(uiName,elementName)
    if Control :    
        Control.bind("<Control-c>",ListView_CtrlCCopy_CallBack)
 
class FrameDraggable():    
    #定义一个可拖拽的子窗口类  
    def __init__(self,FrameInst,EmbedUI):    
        if EmbedUI:    
            self.root = FrameInst
            ChildWidgetList = EmbedUI.root.children    
            for childKey in ChildWidgetList.keys():    
                Form_1 = ChildWidgetList[childKey]    
                Form_1.bind('<Button-1>',self.BeginDrag)
                Form_1.bind('<ButtonRelease-1>',self.EndDrag)
                Form_1.bind('<B1-Motion>',self.Draging)
        else:    
            self.root = FrameInst    
            self.root.bind('<Button-1>',self.BeginDrag)
            self.root.bind('<ButtonRelease-1>',self.EndDrag)
            self.root.bind('<B1-Motion>',self.Draging)
    def BeginDrag(self,event):    
        self.beginx = event.x_root    
        self.beginy = event.y_root    
    def Draging(self,event):    
        offsetx = event.x_root - self.beginx     
        offsety = event.y_root - self.beginy    
        oldX = self.root.winfo_x() 
        oldY = self.root.winfo_y() 
        x = oldX + offsetx    
        y = oldY + offsety    
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        for uiName in G_UIElementPlaceDictionary:    
            for elementName in G_UIElementPlaceDictionary[uiName]:    
                Control = G_UIElementDictionary[uiName][elementName]    
                if Control == self.root:    
                    SetControlPlace(uiName,elementName,x,y,w,h)
                    break    
        self.beginx = event.x_root    
        self.beginy = event.y_root    
    def EndDrag(self,event):    
        self.beginx = event.x_root    
        self.beginy = event.y_root    
class WindowDraggable():    
    #定义一个可拖拽移动和拖拽边框大小的窗口类。  
    def __init__(self,widget,dragmove=False,bordersize = 6,bordercolor = '#444444'):    
        global G_WindowDraggable    
        G_WindowDraggable = self    
        self.widget = widget    
        if dragmove == True:    
            if bordersize > 0:    
                widget.bind('<Enter>',self.Enter)
                widget.bind('<Motion>',self.Motion)
                widget.bind('<Leave>',self.Leave)
# 暂时在InitElementData中处理了
# f.write("            widget.bind('<ButtonPress-1>',self.StartDrag)
# f.write("            widget.bind('<ButtonRelease-1>',self.StopDrag)
# f.write("            widget.bind('<B1-Motion>',self.MoveDragPos)
            widget.after(10, lambda: self.ShowWindowIcoToBar(widget))
        self.bordersize = bordersize    
        self.bordercolor = bordercolor    
        self.x = None    
        self.y = None    
        self.formw = self.widget.winfo_width()
        self.formh = self.widget.winfo_height()
        self.top_drag = None    
        self.left_drag = None    
        self.right_drag = None    
        self.bottom_drag = None    
        self.topleft_drag = None    
        self.bottomleft_drag = None    
        self.topright_drag = None    
        self.bottomright_drag = None    
    def GetWidget(self):    
        return self.widget    
    def ShowWindowIcoToBar(self,widget):    
        GWL_EXSTYLE=-20    
        WS_EX_APPWINDOW=0x00040000    
        WS_EX_TOOLWINDOW=0x00000080    
        hwnd = windll.user32.GetParent(widget.winfo_id())
        _winlib = windll.user32    
        try :    
            style = _winlib.GetWindowLongPtrW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW    
            style = style | WS_EX_APPWINDOW    
            res =_winlib.SetWindowLongPtrW(hwnd, GWL_EXSTYLE, style)
        except :    
            try :    
                style = _winlib.GetWindowLongA(hwnd, GWL_EXSTYLE)
                style = style & ~WS_EX_TOOLWINDOW    
                style = style | WS_EX_APPWINDOW    
                _winlib.SetWindowLongA(hwnd, GWL_EXSTYLE, style)
            except :    
                pass    
    def Enter(self,event):    
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":    
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
#             self.formw = self.widget.winfo_width() 
#             self.formh = self.widget.winfo_height()
    def Motion(self,event):    
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":    
            formx = self.widget.winfo_x() 
            formy = self.widget.winfo_y() 
            formw = self.widget.winfo_width() 
            formh = self.widget.winfo_height()
            x = event.x_root - formx    
            y = event.y_root - formy    
            if ((x >= 0) and (x <= self.bordersize) and (y >= 0) and (y <= self.bordersize)):    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((y >= 0) and (y <= self.bordersize)):    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_V1)
                self.top_drag.bind('<Motion>',self.MotionDragBorder)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.configure(bg = self.bordercolor)
            if ((y >= (formh - self.bordersize)) and (y <= formh)):    
                if self.bottom_drag == None:    
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_V2)
                self.bottom_drag.bind('<Motion>',self.MotionDragBorder)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder)
                self.bottom_drag.place(x = 0,y = (formh - self.bordersize),width = formw,height = self.bordersize)
                self.bottom_drag.configure(bg = self.bordercolor)
            if ((x >= 0 ) and (x <= self.bordersize)):    
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_H1)
                self.left_drag.bind('<Motion>',self.MotionDragBorder)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.configure(bg = self.bordercolor)
            if ((x >= (formw - self.bordersize)) and (x <= formw)):    
                if self.right_drag == None:    
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_H2)
                self.right_drag.bind('<Motion>',self.MotionDragBorder)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder)
                self.right_drag.place(x = (formw - self.bordersize),y = 0,width = self.bordersize,height = formh)
                self.right_drag.configure(bg = self.bordercolor)
    def Leave(self,event):    
        if self.widget == event.widget or event.widget.winfo_class() =="Canvas":    
            pass    
    def StartDrag(self,event):    
        state = self.widget.state()
        if state == "normal":    
            self.x = event.x_root    
            self.y = event.y_root    
            self.formw = self.widget.winfo_width()
            self.formh = self.widget.winfo_height()
    def StopDrag(self,event):    
        self.x = None    
        self.y = None    
        self.widget.configure(cursor='arrow')
    def MoveDragPos(self,event):    
        state = self.widget.state()
        if state == "normal":    
            if self.widget == event.widget or event.widget.winfo_class() =="Canvas" or event.widget.winfo_class() =="Label" or event.widget.winfo_class() =="Frame"  or event.widget.winfo_class() =="Labelframe":    
                formx = self.widget.winfo_x() 
                formy = self.widget.winfo_y() 
                if self.x and self.y:    
                    deltaX = event.x_root - self.x    
                    deltaY = event.y_root - self.y    
                    newX = formx + deltaX    
                    newY = formy + deltaY    
                    WindowMaster = win32gui.GetParent(self.widget.winfo_id())
                    if self.widget.overrideredirect() == True:    
                        win32gui.MoveWindow(WindowMaster,newX,newY,self.formw,self.formh,False)
                    else:    
                        geoinfo = str('%dx%d+%d+%d'%(self.formw,self.formh,newX,newY))
                        self.widget.geometry(geoinfo)
                self.x = event.x_root    
                self.y = event.y_root    
                return "break"    
    def MoveDragSize_H1(self,event):    
        deltaX = event.x_root - self.x    
        newX = self.widget.winfo_x() + deltaX    
        newY = self.widget.winfo_y()
        newW = self.formw - deltaX    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,self.formh,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,self.formh,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.widget.winfo_height())
        self.x = event.x_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
    def MoveDragSize_H2(self,event):    
        deltaX = event.x_root - self.x    
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newW = self.formw + deltaX    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,self.formh,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,self.formh,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = formh)
        self.x = event.x_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
    def MoveDragSize_V1(self,event):    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y() + deltaY    
        newH = self.formh - deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,self.formw,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(self.formw,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.top_drag.place(x = 0,y = 0,width = self.formw,height = self.bordersize)
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formh = newH    
    def MoveDragSize_V2(self,event):    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newH = self.formh + deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,self.formh,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(self.formw,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.bottom_drag.place(x = 0,y = (newH - self.bordersize),width = self.formw,height = self.bordersize)
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formh = newH    
    def MotionDragBorder(self,event):    
        formx = self.widget.winfo_x() 
        formy = self.widget.winfo_y() 
        formw = self.widget.winfo_width() 
        formh = self.widget.winfo_height() 
        x = event.x_root - formx    
        y = event.y_root - formy    
        if event.widget == self.left_drag:    
            if y >=0 and y <= self.bordersize:    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if y >=(formh-self.bordersize) and y <= formh:    
                if self.bottom_drag == None:    
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
        if event.widget == self.right_drag:    
            if y >=0 and y <= self.bordersize:    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.place(x = 0,y = 0,width = formw,height = self.bordersize)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:    
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
            if y >=(formh-self.bordersize) and y <= formh:    
                if self.bottom_drag == None:    
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.place(x = 0,y = formh-self.bordersize,width = formw,height = self.bordersize)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)
                if self.right_drag == None:    
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
        if event.widget == self.top_drag:    
            if x >=0 and x <= self.bordersize:    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TL)
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_TL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_TL)
            if x >=(formw-self.bordersize) and x <= formw:    
                if self.top_drag == None:    
                    self.top_drag = tkinter.Label(self.widget)
                self.top_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.top_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.top_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.top_drag.bind('<Leave>',self.LeaveDragBorder_TR)
                if self.right_drag == None:    
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_TR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_TR)
        if event.widget == self.bottom_drag:    
            if x >=0 and x <= self.bordersize:    
                if self.bottom_drag == None:    
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BL)
                if self.left_drag == None:    
                    self.left_drag = tkinter.Label(self.widget)
                self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = formh)
                self.left_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.left_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.left_drag.bind('<B1-Motion>',self.MoveDragSize_BL)
                self.left_drag.bind('<Leave>',self.LeaveDragBorder_BL)
            if x >=(formw-self.bordersize) and x <= formw:    
                if self.bottom_drag == None:    
                    self.bottom_drag = tkinter.Label(self.widget)
                self.bottom_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.bottom_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.bottom_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.bottom_drag.bind('<Leave>',self.LeaveDragBorder_BR)  
                if self.right_drag == None:    
                    self.right_drag = tkinter.Label(self.widget)
                self.right_drag.place(x = formw-self.bordersize,y = 0,width = self.bordersize,height = formh)
                self.right_drag.bind('<ButtonPress-1>',self.StartDrag)
                self.right_drag.bind('<ButtonRelease-1>',self.StopDrag)
                self.right_drag.bind('<B1-Motion>',self.MoveDragSize_BR)
                self.right_drag.bind('<Leave>',self.LeaveDragBorder_BR)
    def LeaveDragBorder(self,event):    
        event.widget.place_forget()
    def MoveDragSize_TL(self,event):    
        deltaX = event.x_root - self.x    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x() + deltaX    
        newY = self.widget.winfo_y() + deltaY    
        newW = self.formw - deltaX    
        newH = self.formh - deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = self.newH)
        self.top_drag.place(x = 0,y = 0,width = newW,height = self.bordersize)
        self.x = event.x_root    
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
        self.formh = newH    
    def LeaveDragBorder_TL(self,event):    
        self.left_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_TR(self,event):    
        deltaX = event.x_root - self.x    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y() + deltaY    
        newW = self.widget.winfo_width() + deltaX    
        newH = self.widget.winfo_height() - deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = newH)
        self.top_drag.place(x = 0,y = 0,width = newW,height = self.bordersize)
        self.x = event.x_root    
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
        self.formh = newH    
    def LeaveDragBorder_TR(self,event):    
        self.right_drag.place_forget()
        self.top_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BL(self,event):    
        deltaX = event.x_root - self.x    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x() + deltaX    
        newY = self.widget.winfo_y()
        newW = self.widget.winfo_width() - deltaX    
        newH = self.widget.winfo_height() + deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.left_drag.place(x = 0,y = 0,width = self.bordersize,height = newH)
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = newW,height = self.bordersize)
        self.x = event.x_root    
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
        self.formh = newH    
    def LeaveDragBorder_BL(self,event):    
        self.left_drag.place_forget()
        self.bottom_drag.place_forget()
        self.widget.configure(cursor='arrow')
    def MoveDragSize_BR(self,event):    
        deltaX = event.x_root - self.x    
        deltaY = event.y_root - self.y    
        newX = self.widget.winfo_x()
        newY = self.widget.winfo_y()
        newW = self.widget.winfo_width() + deltaX    
        newH = self.widget.winfo_height() + deltaY    
        WindowMaster = win32gui.GetParent(self.widget.winfo_id())
        if self.widget.overrideredirect() == True:    
            win32gui.MoveWindow(WindowMaster,newX,newY,newW,newH,False)
        else:    
            geoinfo = str('%dx%d+%d+%d'%(newW,newH,newX,newY))
            self.widget.geometry(geoinfo)
        self.right_drag.place(x = newW-self.bordersize,y = 0,width = self.bordersize,height = newH)
        self.bottom_drag.place(x = 0,y = newH-self.bordersize,width = newW,height = self.bordersize)
        self.x = event.x_root    
        self.y = event.y_root    
        self.widget.configure(cursor='plus')
        self.formw = newW    
        self.formh = newH    
    def LeaveDragBorder_BR(self,event):    
        self.right_drag.place_forget()
        self.bottom_drag.place_forget() 
        self.widget.configure(cursor='arrow')

 
ToolTipClick_X = 0    
ToolTipClick_Y = 0    
#提示类    
class ToolTip(object):    
    def __init__(self, widget,bgColor = '#CCCCCC',fgColor='#000000'):    
        self.widget = widget    
        self.tipwindow = None    
        self.bgColor = bgColor    
        self.fgColor = fgColor    
        self.id = None    
        self.x = 0    
        self.y = 0    
        self.font = tkinter.font.Font(family="System", size=12,weight='normal',slant='roman',underline=0,overstrike=0)
    #显示提示    
    def showtip(self, text ,x ,y):    
        global ToolTipClick_X    
        global ToolTipClick_Y    
        if self.tipwindow or not text:    
            return    
        if ToolTipClick_X == x  and ToolTipClick_Y == y:    
            return     
        self.tipwindow = tkinter.Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(1)
        self.tipwindow.wm_attributes("-topmost", 1)
        maxwidth = 0    
        maxheight = 24    
        #label = tkinter.Label(self.tipwindow, text=self.text, justify=tkinter.LEFT,background=g_Scheme_FG2,fg=g_Scheme_BG2, relief=tkinter.SOLID, borderwidth=2,font=("Roman", "12", "normal"))
        if type(text) == type([]):    
            self.text = ""    
            TextLineArray = text    
            for TextLine in TextLineArray:    
                maxwidth = max(int(self.font.measure(TextLine)),maxwidth)
                self.text = self.text + TextLine     
                maxheight = maxheight + 24    
        else:     
            self.text = text    
            maxwidth = max(int(self.font.measure(text)),maxwidth)
        maxwidth = maxwidth + 24    
        geoinfo = str('%dx%d+%d+%d'%(maxwidth,maxheight,x-int(maxwidth/2), y-30))
        self.tipwindow.wm_geometry(geoinfo)
        if type(text) == type([]):    
            self.Text = tkinter.Text(self.tipwindow, width=maxwidth,background=self.bgColor,fg=self.fgColor, relief=tkinter.SOLID, borderwidth=2,font=self.font)
            self.Text.pack(ipadx=1)
            self.Text.bind('<Button-1>',self.clicktip)
            TextLineArray = text    
            for TextLine in TextLineArray:    
                self.Text.insert(tkinter.END,TextLine,'tag0')    
        else:     
            maxwidth = max(self.font.measure(text),maxwidth)
            self.label = tkinter.Message(self.tipwindow, text=self.text, anchor=tkinter.W,width=maxwidth,background=self.bgColor,fg=self.fgColor, relief=tkinter.SOLID, borderwidth=2,font=self.font)
            self.label.pack(ipadx=1)
            self.label.bind('<Button-1>',self.clicktip)
    #点击隐藏提示    
    def clicktip(self,event):    
        global ToolTipClick_X    
        global ToolTipClick_Y    
        ToolTipClick_X = event.x    
        ToolTipClick_Y = event.y    
        self.hidetip()
    #隐藏提示    
    def hidetip(self):    
        tw = self.tipwindow    
        self.tipwindow = None    
        if tw:    
            tw.destroy()
#创建提示    
def CreateToolTip(uiName,elementName,tipText,bgColor = '#CCCCCC',fgColor='#000000'):    
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return    
    if hasattr(Control,"GetEntry") == True:    
        Control = Control.GetEntry()
    elif hasattr(Control,"GetWidget") == True:    
        Control = Control.GetWidget()
    toolTip = ToolTip(Control,bgColor,fgColor)
    def enter(event):    
        toolTip.showtip(tipText,event.x_root,event.y_root)
    def leave(event):    
        toolTip.hidetip()
    def click(event):    
        toolTip.hidetip()
    Control.bind('<Enter>', enter,add=True)
    Control.bind('<Leave>', leave,add=True)
#f.write("    Control.bind('<Button-1>',click)
 
def PlayAction_MoveTo(uiName,elementName,targetX,targetY,duration = 1.0,fps = 50):    
    #控件移动到指定位置  
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return    
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    Delay = int(1000 / fps)
    def MovingLoop():    
        CurrTime = time.time() - InitTime    
        Progress = CurrTime / duration     
        if Progress > 1.0:    
            CurrX = targetX    
            CurrY = targetY    
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:    
            CurrX = InitX + (targetX - InitX) * Progress     
            CurrY = InitY + (targetY - InitY) * Progress     
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_MoveBy(uiName,elementName,moveX=0,moveY=0,duration = 1.0,fps = 50):    
    #控件移动一定距离  
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return    
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    targetX = InitX + moveX    
    targetY = InitY + moveY    
    Delay = int(1000 / fps)
    def MovingLoop():    
        CurrTime = time.time() - InitTime    
        Progress = CurrTime / duration     
        if Progress > 1.0:    
            CurrX = targetX    
            CurrY = targetY    
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
        else:    
            CurrX = InitX + (targetX - InitX) * Progress     
            CurrY = InitY + (targetY - InitY) * Progress     
            Control.place(x=int(CurrX),y=int(CurrY),width=InitW,height=InitH)
            Control.after(Delay,MovingLoop)
    Control.after(Delay,MovingLoop)
def PlayAction_ScaleTo(uiName,elementName,anchor = "center",scaleW=1.0,scaleH=1.0,duration = 1.0,fps = 50):    
    #控件缩放到指定大小  
    Control = GetElement(uiName,elementName)
    if Control is None:    
        return    
    InitTime = time.time()
    InitX = Control.winfo_x()
    InitY = Control.winfo_y()
    InitW = Control.winfo_width()
    InitH = Control.winfo_height()
    CenterX = InitX + InitW * 0.5    
    CenterY = InitY + InitH * 0.5    
    targetW = InitW * scaleW    
    targetH = InitH * scaleH    
    if anchor == "nw":    
        targetX = InitX    
        targetY = InitY    
    elif anchor == "n":    
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY    
    elif anchor == "ne":    
        targetX = InitX + InitW - targetW    
        targetY = InitY    
    elif anchor == "w":    
        targetX = InitX    
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "e":    
        targetX = InitX + InitW - targetW    
        targetY = int(CenterY-targetH * 0.5)
    elif anchor == "sw":    
        targetX = InitX    
        targetY = InitY + InitH - targetH    
    elif anchor == "s":    
        targetX = int(CenterX-targetW * 0.5)
        targetY = InitY + InitH - targetH    
    elif anchor == "se":    
        targetX = InitX + InitW - targetW    
        targetY = InitY + InitH - targetH    
    else:    
        targetX = int(CenterX - targetW*0.5)
        targetY = int(CenterY - targetH*0.5)
    Delay = int(1000 / fps)
    def ScalingLoop():    
        CurrTime = time.time() - InitTime    
        Progress = CurrTime / duration     
        if Progress > 1.0:    
            Control.place(x=targetX,y=targetY,width=targetW,height=targetH)
        else:    
            CurrX = InitX + (targetX - InitX) * Progress     
            CurrY = InitY + (targetY - InitY) * Progress     
            CurrW = InitW + (targetW - InitW) * Progress     
            CurrH = InitH + (targetH - InitH) * Progress     
            Control.place(x=int(CurrX),y=int(CurrY),width=CurrW,height=CurrH)
            Control.after(Delay,ScalingLoop)
    Control.after(Delay,ScalingLoop)
# def PlayAction_FadeIn(uiName,duration = 1.0,fps = 50):    
#     #界面渐显弹出  
# def PlayAction_FadeOut(uiName,duration = 1.0,fps = 50):      
#     #界面渐隐消失  
# def PlayAction_Popup(uiName,duration = 1.0,fps = 50):    
#     #界面渐显弹出  
# def PlayAction_Shrink(uiName,duration = 1.0,fps = 50):      
#     #界面渐隐消失  
 
def SetRootRoundRectangle(canvas,hastitlebar,x1, y1, x2, y2, radius=25,**kwargs): 
    #使用TKinter方式设置窗口圆角, 支持跨平台。参数1:Canvas控件,参数2:左上x位置,参数3:左上y位置,参数4 :右下x位置,参数5:右下y位置,参数6:圆角半径。  
    rootinfo = canvas.winfo_parent()
    root = canvas._nametowidget(rootinfo)
    DwmApi = ctypes.windll.dwmapi    
    DwmSetWindowAttribute = DwmApi.DwmSetWindowAttribute    
    WindowMaster = win32gui.GetParent(root.winfo_id())
    RoundValue = ctypes.c_int(4)
    DwmSetWindowAttribute(WindowMaster,33,ctypes.byref(RoundValue),ctypes.sizeof(RoundValue))
#     canvas.create_rectangle(x1, y1, x2, y2, fill=kwargs['outline'])
#     if hastitlebar == True:    
#         points = [x1, y1,    
#               x1, y1,    
#               x2, y1,    
#               x2, y1,    
#               x2, y1,    
#               x2, y1,    
#               x2, y1,    
#               x2, y2-radius,    
#               x2, y2-radius,    
#               x2, y2,    
#               x2-radius, y2,    
#               x2-radius, y2,    
#               x1+radius, y2,    
#               x1+radius, y2,    
#               x1, y2,    
#               x1, y2-radius,    
#               x1, y2-radius,    
#               x1, y1,    
#               x1, y1,    
#               x1, y1]    
#     else:    
#         points = [x1+radius, y1,    
#               x1+radius, y1,    
#               x2-radius, y1,    
#               x2-radius, y1,    
#               x2, y1,    
#               x2, y1+radius,    
#               x2, y1+radius,    
#               x2, y2-radius,    
#               x2, y2-radius,    
#               x2, y2,    
#               x2-radius, y2,    
#               x2-radius, y2,    
#               x1+radius, y2,    
#               x1+radius, y2,    
#               x1, y2,    
#               x1, y2-radius,    
#               x1, y2-radius,    
#               x1, y1+radius,    
#               x1, y1+radius,    
#               x1, y1]    
#     return canvas.create_polygon(points, smooth=True, **kwargs)
   
def ReadFromFile(filePath,encoding='utf-8',autoEval=False):    
    PrintFunctionInfo(ReadFromFile,[filePath,encoding,autoEval])
    #从一个文件中读取内容。参数1 :文件路径 。  
    content = None    
    if filePath != None:    
        if os.path.exists(filePath) == True:     
            f = open(filePath,mode='r',encoding=encoding)
            if f != None:    
                content = f.read()
                if autoEval == True:    
                    content = eval(content)
                f.close()
    return content    
def OpenFile(title="Open Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = ''):  
    PrintFunctionInfo(OpenFile,[title,filetypes,initDir])
    #调用打开文件框  
    import tkinter.filedialog    
    import inspect    
    parent = None    
    calling_frame = inspect.currentframe().f_back    
    if "uiName" in calling_frame.f_locals:    
        uiName = calling_frame.f_locals["uiName"]    
        parent = GetElement(uiName,"Form_1")
    openPath = tkinter.filedialog.askopenfilename(initialdir=initDir,title=title,filetypes=filetypes,parent=parent)
    return openPath    

def WriteToFile(filePath,content,encoding='utf-8',append=False):  
    PrintFunctionInfo(WriteToFile,[filePath,content,encoding,append])
    #将内容写入到一个文件中。参数1 :文件路径,参数2 :写入的内容 。   
    if filePath != None:    
        f = None    
        if append == True:    
            f = open(filePath,mode='a',encoding=encoding)
        else:    
            f = open(filePath,mode='w',encoding=encoding)
        if f != None:    
            if content != None:    
                f.write(str(content))
            f.close()
            return True    
    return False    
def SaveFile(title="Save Python File",filetypes=[('Python File','*.py'),('All files','*')],initDir = '',defaultextension='py'):   
    PrintFunctionInfo(SaveFile,[title,filetypes,initDir,defaultextension])
    #调用保存文件框  
    import tkinter.filedialog    
    import inspect    
    parent = None    
    calling_frame = inspect.currentframe().f_back    
    if "uiName" in calling_frame.f_locals:    
        uiName = calling_frame.f_locals["uiName"]    
        parent = GetElement(uiName,"Form_1")
    savePath = tkinter.filedialog.asksaveasfilename(initialdir=initDir,title=title,filetypes=filetypes,defaultextension=defaultextension,parent=parent)
    return savePath  
 
def ReadStyleFile(filePath):
    PrintFunctionInfo(ReadStyleFile,[filePath])  
    #读取样式定义文件,返回样式列表。参数1 :文件路径 。  
    global G_ExeDir    
    StyleArray = {}    
    if len(filePath)==0 :    
        return StyleArray    
    if os.path.exists(filePath) == False:    
        PathName, FileName = os.path.split(filePath)
        filePath = os.path.join(G_ExeDir,FileName)
        if os.path.exists(filePath) == False:    
            return StyleArray    
    f = open(filePath,encoding='utf-8')
    line =""    
    while True:    
        line = f.readline()
        if not line:    
            break    
        text = line.strip()
        if not text:    
            continue    
        if text.find('style = tkinter.ttk.Style()') >= 0:    
            continue    
        if text.find('style.configure(') >= 0:    
            splitarray1 = text.partition('style.configure(')
            stylename = None    
            splitarray2 = None    
            if splitarray1[2].find(',') >= 0:    
                splitarray2 = splitarray1[2].partition(',')
                stylename = splitarray2[0].replace('"','')
            else:    
                splitarray2 = splitarray1[2].partition(')')
                stylename = splitarray2[0].replace('"','')
            sytleValueText = splitarray2[2]    
            fontindex_begin = sytleValueText.find('font=(')
            fontindex_end = fontindex_begin    
            StyleArray[stylename] = {}    
            othertext = sytleValueText    
            if fontindex_begin >= 0:    
                fontindex_end = sytleValueText.find(')')
                fonttext = sytleValueText[fontindex_begin+6:fontindex_end]    
                fontsplitarray = fonttext.split(',')
                StyleArray[stylename]['font'] = tkinter.font.Font(family=fontsplitarray[0].replace('"','').strip(), size=int(fontsplitarray[1].replace('"','').strip()),weight=fontsplitarray[2].replace('"','').strip())
                othertext = sytleValueText[0:fontindex_begin] + sytleValueText[fontindex_end+1:-1]    
            else:    
                splitarray4 = sytleValueText.partition(')')
                othertext = splitarray4[0]    
            splitarray3 = othertext.split(',')
            for stylecfgtext in splitarray3:    
                if stylecfgtext.find('=') > 0:    
                    splitarray4 = stylecfgtext.partition('=')
                    key = splitarray4[0].replace('"','').strip()
                    value = splitarray4[2].replace('"','').strip()
                    StyleArray[stylename][key] = value    
            continue    
        if text.find('style.map(') >= 0:    
            continue    
    f.close()
    return StyleArray     
ResourFileList = WalkAllResFiles(G_ResDir,True)
for FilePath in ResourFileList:
    PathName, FileName = os.path.split(FilePath)
    FileName_Lower = FileName.lower()
    G_ResourcesFileList[FileName_Lower] = FilePath
    shotname, extension = os.path.splitext(FileName)
    extension_lower = extension.lower()
    if extension_lower == ".ttf" or extension_lower == ".otf":
        TTFFontPath = FilePath
        TTFFontPathBuf = create_unicode_buffer(TTFFontPath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
        numFontsAdded = AddFontResourceEx(byref(TTFFontPathBuf), 0, 0)
def GetResourcePath(FileName):
    """查询一个资源文件的路径"""
    global G_ResourcesFileList
    FileName_Lower = FileName.lower()
    if FileName_Lower in G_ResourcesFileList:
        return G_ResourcesFileList[FileName_Lower]
    return None
 
#下载进度对话框    
class   DownLoadFileProgressDialog:    
    def __init__(self,uiName,showDialog = True,title='"+Language.G_Language[3240]+"',bgColor='#EFEFEF',fgColor='#000000'):    
        self.FinishFlag = False    
        self.LocalSaveFile = ""    
        self.showDialog = showDialog    
        if self.showDialog == True:    
            self.root = GetElement(uiName,"root")
            self.Dialog = tkinter.Toplevel()
            self.Dialog.attributes("-toolwindow", 1)
            self.Dialog.resizable(0,0) 
            self.Dialog.wm_attributes("-topmost", 1)
            self.Title = title    
            self.bgColor = bgColor    
            self.fgColor = fgColor    
            self.Dialog.title(self.Title)
            self.Form = tkinter.Canvas(self.Dialog,width = 280,height=140,bg = bgColor)
            self.Form.place(x=0, y=0,width=280,height=140)
            self.ShowDownLoadProgressDialog()
    #取得当前窗口句柄    
    def GetWindHandle(self):    
        _handle = None    
        if self.showDialog == True:    
            import win32gui    
            _handle = win32gui.FindWindow(None,self.Title)
        return _handle    
    def downloadFileFromURL(self,url,saveToDir=None,ReDownLoadIfExist = True,autoExtractZip = False,progressCallBack = None,finishCallBack = None,errorCallBack = None):    
        #多线程下载单文件,url为远端文件网址,saveToDir为本地保存位置,None指项目所在目录,ReDownLoadIfExist为如果存在是否重新下载，progressCallBack进度函数:参数1：本地文件，参数2:进度值,finishCallBack完成函数，参数1：本地文件,errorCallBack错误函数，参数1：网址或本地文件，参数2：错误原因:1:文件下载失败 2:本地解压失败  
        global G_ResDir    
        self.URLFile = url    
        self.LocalDir = saveToDir    
        self.autoExtractZip = autoExtractZip    
        self.progressCallBack = progressCallBack    
        self.errorCallBack = errorCallBack    
        self.finishCallBack = finishCallBack    
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        WebSite, FileName = os.path.split(self.URLFile)
        if self.LocalDir:    
            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
        else:    
            self.LocalSaveFile = os.path.join(projpath,FileName)
        IsZipFile = False    
        if FileName.find(".zip") > 0 :    
            IsZipFile = True    
        if os.path.exists(self.LocalSaveFile) == True:    
            if ReDownLoadIfExist == True:    
                os.remove(self.LocalSaveFile)
            else:    
                if IsZipFile == True and self.autoExtractZip == True:    
                    if self.LocalDir:    
                        LocalDir, LocalFile = os.path.split(self.LocalDir)
                        self.extractZipFile(self.LocalSaveFile,LocalDir)
                    else:    
                        self.extractZipFile(self.LocalSaveFile,projpath)
                return     
        try:    
            resp = requests.get(self.URLFile,stream=True)
            total_length = int(resp.headers.get('content-length',0))
            def handle_ThreadDownload(theResp,theTotallength):    
                if resp.status_code == 404:    
                    if self.showDialog == True:    
                        MessageBox('文件异常,无法下载.',_handle)
                    if self.errorCallBack:    
                        self.errorCallBack(self.URLFile,1)
                    self.cancle()
                else:    
                    step = int(theTotallength / 100)
                    if step < 320:    
                        step = 320    
                    maximum = int (theTotallength/step)
                    if maximum == 0:    
                        maximum = 1    
                    if self.showDialog == True:    
                        self.ProgressBar['maximum'] = maximum    
                    self.FinishFlag = False    
                    if os.path.exists(self.LocalSaveFile) == False:    
                        with open(self.LocalSaveFile, 'wb') as f:    
                            progress = 0    
                            for i in theResp.iter_content(chunk_size=step):      
                                f.write(i)
                                progress = progress + 1    
                                if progress <= maximum:    
                                    if self.showDialog == True:    
                                        self.ProgressBar['value'] = progress    
                                        self.TitleLabel.configure(text='正在下载压缩包' + str("(%d%%)"%progress))
                                    if self.progressCallBack:    
                                        self.progressCallBack(self.LocalSaveFile,progress)
                        #下载完毕后解压，并删除ZIP文件    
                        if IsZipFile == True and self.autoExtractZip == True:    
                            if self.showDialog == True:    
                                self.TitleLabel.configure(text='下载完成,准备解压缩文件')
                            if self.LocalDir:    
                                self.extractZipFile(self.LocalSaveFile,self.LocalDir)
                            else:    
                                self.extractZipFile(self.LocalSaveFile,projpath)
                        else:    
                            self.FinishFlag = True     
                            if self.showDialog == True:    
                                self.TitleLabel.configure(text='下载完成')
                                self.OKButton.configure(text='确定')
                            if self.finishCallBack:    
                                self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownload, args=[resp,total_length])
            self.run_thread_download.Daemon = True    
            self.run_thread_download.start() 
        except Exception as Ex:    
            if self.errorCallBack:    
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:    
                MessageBox(str(Ex),_handle)
    def downloadFilesFromURLList(self,urllist,saveToDir,ReDownLoadIfExist = True,progressCallBack = None,finishCallBack = None,errorCallBack = None):    
        #多线程下载多文件,urllist为远端文件网址列表,saveToDir为本地保存位置,None指项目所在目录,ReDownLoadIfExist为如果存在是否重新下载，progressCallBack进度函数:参数1：本地文件，参数2:进度值,finishCallBack完成函数，参数1：本地文件,errorCallBack错误函数，参数1：网址或本地文件，参数2：错误原因:1:文件下载失败 2:本地解压失败  
        global G_ResDir    
        self.URLFileList = urllist    
        self.URLFile = ""    
        self.LocalDir = saveToDir    
        self.progressCallBack = progressCallBack    
        self.errorCallBack = errorCallBack    
        self.finishCallBack = finishCallBack    
        self.FinishFlag = False    
        projpath, resdirname = os.path.split(G_ResDir)
        _handle = self.GetWindHandle()
        if self.showDialog == True:    
            self.ProgressBar['maximum'] = len(urllist)
        try:    
            def handle_ThreadDownloadFiles():    
                progress = 0    
                for url in self.URLFileList:    
                    self.URLFile = url    
                    resp = requests.get(self.URLFile,stream=True)
                    total_length = int(resp.headers.get('content-length',0))
                    if resp.status_code == 404:    
                        if self.showDialog == True:    
                            MessageBox(self.URLFile+'文件异常,无法下载.',_handle)
                        if self.errorCallBack:    
                            self.errorCallBack(self.URLFile,1)
                    else:    
                        WebSite, FileName = os.path.split(self.URLFile)
                        if self.LocalDir:    
                            self.LocalSaveFile = os.path.join(self.LocalDir,FileName)
                        else:    
                            self.LocalSaveFile = os.path.join(projpath,FileName)
                        if os.path.exists(self.LocalSaveFile) == True:    
                            if ReDownLoadIfExist == True:    
                                    os.remove(self.LocalSaveFile)
                        if os.path.exists(self.LocalSaveFile) == False:    
                            step = 1024       
                            with open(self.LocalSaveFile, 'wb') as f:    
                                for i in resp.iter_content(chunk_size=step):    
                                    f.write(i)
                        progress = progress + 1    
                        if self.showDialog == True:    
                            self.ProgressBar['value'] = progress    
                            self.TitleLabel.configure(text='正在下载文件' + str("(%d%%)"%progress))
                        if self.progressCallBack:    
                            self.progressCallBack(self.LocalSaveFile,progress)

                self.FinishFlag = True     
                if self.showDialog == True:    
                    self.TitleLabel.configure(text='下载完成')
                    self.OKButton.configure(text='确定')
                if self.finishCallBack:    
                    self.finishCallBack(self.LocalSaveFile)
            self.run_thread_download = threading.Thread(target=handle_ThreadDownloadFiles, args=[])
            self.run_thread_download.Daemon = True    
            self.run_thread_download.start() 
        except Exception as Ex:    
            if self.errorCallBack:    
                self.errorCallBack(self.URLFile,1)
            if self.showDialog == True:    
                MessageBox(str(Ex),_handle)
    #解压    
    def extractZipFile(self,ZipFile,ExtractDir):    
        _handle = self.GetWindHandle()
        try:    
            block_size = 8192    
            z = zipfile.ZipFile(ZipFile)
            namecount = len(z.namelist())
            if self.showDialog == True:    
                self.ProgressBar['maximum'] = namecount    
            nameindex = 0    
            for zip_file in z.namelist():    
                old_dir,old_fileName = os.path.split(zip_file)
                file_name = zip_file    
                file_name_utf8 = file_name.encode('cp437').decode('gbk') 
#                 try:    
#                     file_name_utf8 = file_name.encode('cp437').decode('gbk') 
#                 except:    
#                     file_name_utf8 = filename.encode('utf-8').decode('utf-8')
#                new_dir,new_fileName = os.path.split(file_name_utf8)
                progress = int(nameindex / namecount * 100)
                if self.showDialog == True:    
                    self.TitleLabel.configure(text='正在解压缩文件' + str("(%d%%)"%progress))
                entry_info = z.getinfo(file_name)
                i = z.open(file_name)
                print(file_name)
                if file_name[-1] != '/':    
                    o = open(f"{ExtractDir}/{file_name_utf8}", "wb")
                    offset = 0    
                    while True:    
                        b = i.read(block_size)
                        offset += len(b)
                        if b == b'':    
                            break    
                        o.write(b)
                    o.close()
                else:    
                    dir_name = os.path.dirname(file_name_utf8)
                    p = Path(f"{ExtractDir}/{file_name_utf8}")
                    p.mkdir(parents=True, exist_ok=True)
                i.close()
                nameindex = nameindex + 1    
                if self.showDialog == True:    
                    self.ProgressBar['value'] = nameindex    
            z.close()
            if self.autoExtractZip == True:    
                os.remove(ZipFile)
            self.FinishFlag = True      
            if self.showDialog == True:    
                self.TitleLabel.configure(text='完成解压缩')
                self.OKButton.configure(text='确定')
            if self.finishCallBack:    
                self.finishCallBack(ExtractDir)
            return True    
        except Exception as Ex:    
            try:    
                zip_1 = zipfile.ZipFile(ZipFile,'r')
                zip_1.extractall(path=ExtractDir)
                zip_1.close()
                os.remove(ZipFile)
                self.FinishFlag = True      
                if self.showDialog == True:    
                    self.TitleLabel.configure(text='完成解压缩')
                    self.OKButton.configure(text='确定')
                if self.finishCallBack:    
                    self.finishCallBack(ExtractDir)
                return True    
            except Exception as Ex:    
                if self.showDialog == True:    
                    MessageBox(str(Ex),_handle)
                if self.errorCallBack:    
                    self.errorCallBack(self.LocalSaveFile,2)
                return False    
    #确定TitleLabel    
    def submit(self):    
        if self.showDialog == True:    
            _handle = self.GetWindHandle()
            if self.FinishFlag == False:    
                if  AskBox('正在下载，确定退出？',_handle) == False:    
                    return     
                if self.LocalSaveFile:    
                    if os.path.exists(self.LocalSaveFile) == True:    
                        os.remove(self.LocalSaveFile)
            self.Dialog.destroy()
    #取消    
    def cancle(self):    
        if self.showDialog == True:    
            self.Dialog.destroy()
    #显示设置列表    
    def ShowDownLoadProgressDialog(self):    
        if self.showDialog == True:    
            self.TitleFont =tkinter.font.Font(family="System", size=10,weight='normal',slant='roman',underline=0,overstrike=0)
            self.TitleLabel = tkinter.Label(self.Form,anchor = tkinter.W,bg=self.bgColor,fg=self.fgColor,font = self.TitleFont,text=self.Title,width = 100,height = 1)
            self.TitleLabel.place(x = 10,y = 10,width = 260,height = 24)
            self.ProgressBar = tkinter.ttk.Progressbar(self.Form, length=200, mode='determinate',style="TProgressbar", orient=tkinter.HORIZONTAL)
            self.ProgressBar.place(x=10,y=40,width=260,height=15)
            self.ProgressBar['maximum'] = 100    
            self.ProgressBar['value'] = 0    
            self.OKButton = tkinter.Button(self.Form,anchor = tkinter.CENTER,text='取消',width = 100,height = 1,bg=self.bgColor,fg=self.fgColor,command=self.submit)
            self.OKButton.place(x = 180,y = 70,width = 80,height = 24) 
            #居中显示    
            sx = self.root.winfo_x()
            sy = self.root.winfo_y()
            sw = self.root.winfo_width()
            sh = self.root.winfo_height()
            nx = sx + (sw - 280)/2    
            ny = sy + (sh - 110)/2    
            geoinfo = str('%dx%d+%d+%d'%(280,110,nx,ny))
            self.Dialog.geometry(geoinfo)   

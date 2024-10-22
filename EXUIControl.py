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

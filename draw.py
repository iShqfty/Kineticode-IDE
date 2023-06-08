import tkinter as tk
import const as c
import threading as th

# All Subs Of Draw
import windraw as wd
import tabheader as tb
import directory as dir
import texteditor as txt
import highlight as hlt
import settingseditor as sedit
"""

Draw is the class that inherits from all other sub-draws for all their methods

Used to compile into 1 method (FinalDraw()) to be called during loader

"""


class Draw(wd.WinDraw, tb.TabHeader, dir.Directory, txt.TextEditor,
           hlt.Highlight, sedit.SettingsEditor):

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def FinalDraw(self):
    self.WinDrawAll()
    self.TabHeaderAll()
    self.DirectoryAll()
    self.TextEditorAll()
    self.SettingsAll()
    self.TimedLoop()

  def TimedLoop(self):
    if c.c.threadAllowed:
      th.Timer(1.0, self.TimedLoop).start()
      self.highlightKeywords()

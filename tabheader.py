import tkinter as tk
import const as c
import winfnc as wfc
import kmBox as km
"""

Tab bar right below custom dragging header for running, saving, new files, etc.

"""


class TabHeader:

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def TabBar(self):
    tabbar = tk.Frame(self.tk,
                      width=c.c.w,
                      height=int(c.c.TabHeaderTabBarHeight),
                      bg=c.c.dtc,
                      border=0,
                      borderwidth=0)
    tabbar.pack()
    tabbar.place(x=0,y=c.c.WinDrawDragHeaderHeight)

  def TabOptions(self):
    newf = tk.Button(self.tk,
                     bg=c.c.dtc,
                     fg=c.c.fg,
                     text=">>  New File",
                     width=c.c.TabHeaderButtonWidth,
                     border=0,
                     borderwidth=0,
                     highlightthickness=0,
                     command=lambda:km.AskString(self.tk, "New File", "Name Of New File + Extension")
                    )
    newf.pack()
    newf.place(x=c.c.spacing, y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

    runf = tk.Button(self.tk,
                     bg=c.c.dtc,
                     fg=c.c.fg,
                     text=">>  Run File",
                     width=c.c.TabHeaderButtonWidth,
                     border=0,
                     borderwidth=0,
                     highlightthickness=0,
                     command=lambda: wfc.runCommand(f"python {c.c.currOpen}"))
    runf.pack()
    runf.place(x=c.c.spacing * 3 + c.c.TabHeaderButtonWidth * 1 * 10,
               y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

    savef = tk.Button(
      self.tk,
      bg=c.c.dtc,
      fg=c.c.fg,
      text=">>  Save File",
      width=c.c.TabHeaderButtonWidth,
      border=0,
      borderwidth=0,
      highlightthickness=0,
      command=lambda:wfc.saveFile()
    )
    savef.pack()
    savef.place(x=c.c.spacing * 5 + c.c.TabHeaderButtonWidth * 2 * 10,
                y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

    delf = tk.Button(
      self.tk,
      bg=c.c.dtc,
      fg=c.c.fg,
      text=">>  Delete File",
      width=c.c.TabHeaderButtonWidth,
      border=0,
      borderwidth=0,
      highlightthickness=0,
      command=lambda:wfc.delFile(self.tk)
    )
    delf.pack()
    delf.place(x=c.c.spacing * 7 + c.c.TabHeaderButtonWidth * 3 * 10,
                y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

    clrf = tk.Button(
      self.tk,
      bg=c.c.dtc,
      fg=c.c.fg,
      text=">>  Clear File",
      width=c.c.TabHeaderButtonWidth,
      border=0,
      borderwidth=0,
      highlightthickness=0,
      command=lambda: c.c.gbtxt.delete("1.0", "end-1c")
    )
    clrf.pack()
    clrf.place(x=c.c.spacing * 9 + c.c.TabHeaderButtonWidth * 4 * 10,
                y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

    clrc = tk.Button(
      self.tk,
      bg=c.c.dtc,
      fg=c.c.fg,
      text=">>  Clear CMD",
      width=c.c.TabHeaderButtonWidth,
      border=0,
      borderwidth=0,
      highlightthickness=0,
      command=lambda: wfc.runCommand("clear")
    )
    clrc.pack()
    clrc.place(x=c.c.spacing * 11 + c.c.TabHeaderButtonWidth * 5 * 10,
                y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

  def TabHeaderAll(self):
    self.TabBar()
    self.TabOptions()

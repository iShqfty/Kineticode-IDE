import tkinter as tk
import const as c
import draw as d
"""

Initializer of entire program to be called in main

"""


class Loader:

  def __init__(self):
    self.tk = tk.Tk()
    self.dr = d.Draw(self.tk)

  def initWindow(self):
    self.tk.geometry(str(c.c.w) + "x" + str(c.c.h))
    self.tk.title = c.c.title
    self.tk.configure(bg=c.c.bg)

  def destroyWindow(self):
    loc = self.tk.winfo_children()
    for i in loc:
      if i.winfo_children():
        loc.extend(i.winfo_children())
    for item in loc:
      item.destroy()

  def changeThemeRedraw(self, lbg, bg, ltc, dtc, fg, dfg):
    c.c.lbg = lbg
    c.c.bg = bg
    c.c.ltc = ltc
    c.c.dtc = dtc
    c.c.fg = fg
    c.c.dfg = dfg
    
    self.destroyWindow()
    self.dr.FinalDraw()

  def mainLoop(self):
    self.initWindow()
    self.dr.FinalDraw()
    self.tk.mainloop()

ld = Loader()

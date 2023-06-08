import tkinter as tk
import const as c
import loader as l
import os

class ThemeInfo:
  def __init__(self, root: tk.Tk, name, x, y, fontsz, lbg, bg, ltc, dtc, fg, dfg):
    self.btn = tk.Button(root,
                         bg=c.c.bg,
                         fg=c.c.fg,
                         text=name,
                         font=(str(fontsz)),
                         command=self.Command
                        )
    self.btn.pack()
    self.btn.place(x=x, y=y)

    root.update()

    self.lbg = lbg
    self.bg = bg
    self.ltc = ltc
    self.dtc = dtc
    self.fg = fg
    self.dfg = dfg

    self.y = y


  def getYPos(self):
    return self.y+self.btn.winfo_height()

  def Command(self):
    l.ld.changeThemeRedraw(self.lbg, self.bg, self.ltc, self.dtc, self.fg, self.dfg)
    os.system("clear") #clears an error that keeps getting thrown for an unknown reason (has no effect on the program whatsoever)

  def Destroy(self):
    self.btn.destroy()
    
    
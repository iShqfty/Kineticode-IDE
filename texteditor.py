import tkinter as tk
import const as c
import winfnc as wfc


class TextEditor:

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def InnerTextBox(self):
    frm = tk.Frame(self.tk,
                   bg=c.c.lbg,
                   width=c.c.w * c.c.mainRatio - (c.c.spacing * 2) + 1,
                   height=33)
    frm.pack()
    frm.place(
      x=(c.c.spacing * 2) + (c.c.directoryRatio * c.c.w - c.c.spacing) - 1,
      y=c.c.WinDrawDragHeaderHeight + c.c.TabHeaderTabBarHeight + c.c.spacing)

    c.c.gbtxt = tk.Text(
      self.tk,
      bg=c.c.bg,
      fg=c.c.fg,
      width=108,  # Again, had to guess. Pixels are just not valid
      font=("20"),
      border=0,
      borderwidth=0,
      highlightthickness=0,
      height=35)
    c.c.gbtxt.pack()
    c.c.gbtxt.place(x=(c.c.spacing * 2) +
                    (c.c.directoryRatio * c.c.w - c.c.spacing) - 1,
                    y=c.c.WinDrawDragHeaderHeight + c.c.TabHeaderTabBarHeight +
                    (c.c.spacing * 2) + 33)

    exfrm = tk.Frame(self.tk,
                     bg=c.c.lbg,
                     width=c.c.w * c.c.mainRatio - (c.c.spacing * 2) + 1,
                     height=34 - c.c.spacing)
    exfrm.pack()
    exfrm.place(x=(c.c.spacing * 2) +
                (c.c.directoryRatio * c.c.w - c.c.spacing) - 1,
                y=c.c.GlobalBottomPos - c.c.spacing)

    self.tk.update()

    cmdl = tk.Entry(self.tk,
                    bg=c.c.bg, 
                    fg=c.c.dfg, 
                    highlightthickness=0,
                    border=0,
                    borderwidth=0,
                    width=120
                   )
    cmdl.pack()
    cmdl.place(x=exfrm.winfo_x()+c.c.spacing, y=exfrm.winfo_y()+c.c.spacing+1)
    cmdl.insert("insert", "Run Command Line...")

    self.tk.update()

    rcmdl = tk.Button(self.tk,
                      text="Run CMD >> ",
                      bg =c.c.dtc,
                      fg=c.c.fg,
                      border=0,
                      borderwidth=0,
                      highlightthickness=0,
                      command = lambda: wfc.runCommand(cmdl.get())
                     )
    rcmdl.pack()
    rcmdl.place(x=cmdl.winfo_x()+cmdl.winfo_width()+c.c.spacing, y=cmdl.winfo_y()-4)

  def TextEditorAll(self):
    self.InnerTextBox()

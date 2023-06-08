import tkinter as tk
import const as c
import sys


class WinDraw:

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def DragHeader(self):
    self.tk.overrideredirect(True)
    header = tk.Frame(self.tk,
                      bg=c.c.ltc,
                      relief='raised',
                      bd=1,
                      width=c.c.w,
                      height=c.c.WinDrawDragHeaderHeight,
                      border=0,
                      borderwidth=0)
    header.pack(fill='x')

    ## ------------------------------------ ##

    header.bind("<ButtonPress-1>", self.StartMoveHeader)
    header.bind("<ButtonRelease-1>", self.StopMoveHeader)
    header.bind("<B1-Motion>", self.MoveHeader)

    header.place(x=0,y=0)

  ## ------------------------------------ ##
  ## Thank you for the custom dragging window -> https://stackoverflow.com/questions/4055267/tkinter-mouse-drag-a-window-without-borders-eg-overridedirect1

  def TitleBar(self):
    titlebar = tk.Label(self.tk,
                        text=c.c.title,
                        bg=c.c.ltc,
                        fg=c.c.fg,
                        font=("20"))
    titlebar.pack()
    titlebar.place(x=5, y=5)

    exitbtn = tk.Button(self.tk,
                        text="x",
                        bg=c.c.ltc,
                        fg=c.c.fg,
                        border=0,
                        borderwidth=0,
                        highlightthickness=0,
                        font=("30"),
                        command=self.Exit)
    exitbtn.pack()
    exitbtn.place(x=c.c.w - 33, y=0)

  ## ----------- Functionals ------------ ##

  def StartMoveHeader(self, event):
    self.x = event.x
    self.y = event.y

  def StopMoveHeader(self, event):
    self.x = None
    self.y = None

  def MoveHeader(self, event):
    dtax = event.x - self.x
    dtay = event.y - self.y
    x = self.tk.winfo_x() + dtax
    y = self.tk.winfo_y() + dtay
    self.tk.geometry(f"+{x}+{y}")

  def Exit(self):
    c.c.threadAllowed = False # Thread Becomes Main 
    self.tk.quit()
    exit(c.c.exitmsg)

  ## ------------------------------------ ##
  def WinDrawAll(self):
    self.DragHeader()
    self.TitleBar()

  ## ------------------------------------ ##
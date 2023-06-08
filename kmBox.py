"""

Custom Message Box

Made this b/c Tkinter's messagebox does not render even though it loads (upon pressing enter after prompting it takes input)

"""

import tkinter as tk
import const as c
import winfnc as wfc


def AskString(root: tk.Tk, title: str, message: str, isReturn = False, Return = ""):
  if isReturn:
    c.c.AskStringReturn = Return
    wfc.newFile(root, c.c.AskStringReturn)
    return
  coverup = tk.Frame(root, width=c.c.w, height=c.c.h, bg=c.c.kmBoxCoverUpColor)
  coverup.pack()
  coverup.place(x=0, y=c.c.WinDrawDragHeaderHeight)

  main = tk.Frame(root,
                  width=c.c.kmBoxMainWidth,
                  height=c.c.kmBoxMainHeight,
                  bg=c.c.lbg)
  main.pack()
  main.place(x=int(c.c.w / 2) - int(c.c.kmBoxMainWidth / 2),
             y=int(c.c.h / 2) - int(c.c.kmBoxMainHeight / 2))

  mlbl = tk.Label(root, bg=c.c.ltc, fg=c.c.fg, text=title, width=31)
  mlbl.pack()
  mlbl.place(x=int(c.c.w / 2) - int(c.c.kmBoxMainWidth / 2) - 1,
             y=int(c.c.h / 2) - int(c.c.kmBoxMainHeight / 2))

  minfo = tk.Label(root, bg=c.c.lbg, fg=c.c.fg, text=message)
  minfo.pack()
  minfo.place(x=int(c.c.w / 2) - int(c.c.kmBoxMainWidth / 2) + 2,
              y=int(c.c.h / 2) - int(c.c.kmBoxMainHeight / 2) + 30)

  mtext = tk.Entry(root, bd=0, bg=c.c.bg, fg=c.c.fg, width=30)
  mtext.pack()
  mtext.place(x=int(c.c.w / 2) - int(c.c.kmBoxMainWidth / 2) + 3,
              y=int(c.c.h / 2) - int(c.c.kmBoxMainHeight / 2) + 50)

  rtrn = tk.Button(root,
                   bg=c.c.dtc,
                   fg=c.c.fg,
                   text="Enter",
                   width=28,
                   bd=0,
                   command=lambda: ReturnCall())
  rtrn.pack()
  rtrn.place(x=int(c.c.w / 2) - int(c.c.kmBoxMainWidth / 2),
             y=int(c.c.h / 2) - int(c.c.kmBoxMainHeight / 2) + 80)

  def ReturnCall():
    return DestroyAll()

  def DestroyAll() -> str:
    coverup.destroy()
    main.destroy()
    mlbl.destroy()
    minfo.destroy()
    #get before destruction
    ret = mtext.get()
    mtext.destroy()
    rtrn.destroy()
    AskString(root, title, message, True, ret)
import tkinter as tk
import const as c
import winfnc as wfc
"""

Side directory-display to be able to open new files

"""


class Directory:

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def DirectoryFrame(self):
    back = tk.Frame(self.tk,
                    bg=c.c.lbg,
                    width=c.c.directoryRatio * c.c.w - c.c.spacing,
                    height=c.c.h - (c.c.spacing * 2) -
                    (c.c.TabHeaderTabBarHeight + c.c.WinDrawDragHeaderHeight))
    back.pack()
    back.place(x=c.c.spacing,
               y=c.c.TabHeaderTabBarHeight + c.c.WinDrawDragHeaderHeight +
               c.c.spacing)

  def InnerDirectory(self):
    title = tk.Label(self.tk,
                     bg=c.c.lbg,
                     fg=c.c.fg,
                     text="All Files",
                     font=("20"))
    title.pack()
    self.tk.update(
    )  # << Update Here So Root Is Able To Draw And Calculate Size For Title Label (Needed for calculation below)
    title.place(x=c.c.spacing + int(
      (c.c.directoryRatio * c.c.w - c.c.spacing) / 2) -
                int(title.winfo_width() / 2),
                y=c.c.TabHeaderTabBarHeight + c.c.WinDrawDragHeaderHeight +
                (c.c.spacing * 2))

    spl = tk.Frame(self.tk,
                   bg=c.c.bg,
                   width=c.c.directoryRatio * c.c.w - c.c.spacing,
                   height=c.c.spacing)
    spl.pack()
    spl.place(x=c.c.spacing,
              y=c.c.TabHeaderTabBarHeight + c.c.WinDrawDragHeaderHeight +
              (c.c.spacing * 3) + title.winfo_height())

    self.tk.update(
    )  # << Update Here So Root Is Able To Draw And Calculate Size For Title Label (Needed for calculation below)

    cdir = tk.Label(self.tk,
                    bg=c.c.lbg,
                    fg=c.c.fg,
                    text=f"Directory: {wfc.getCurrentDirectory()}")
    cdir.pack()
    self.tk.update(
    )  # << Update Here So Root Is Able To Draw And Calculate Size For Title Label (Needed for calculation below)
    cdir.place(x=c.c.spacing + int(
      (c.c.directoryRatio * c.c.w - c.c.spacing) / 2) -
               int(cdir.winfo_width() / 2),
               y=c.c.h - (c.c.spacing * 2) - cdir.winfo_height())

    self.tk.update()
    c.c.GlobalBottomPos = cdir.winfo_y()
    spl2 = tk.Frame(self.tk,
                    bg=c.c.bg,
                    width=c.c.directoryRatio * c.c.w - c.c.spacing,
                    height=c.c.spacing)
    spl2.pack()
    self.tk.update(
    )  # << Update Here So Root Is Able To Draw And Calculate Size For Title Label (Needed for calculation below)
    spl2.place(x=c.c.spacing,
               y=cdir.winfo_y() - spl2.winfo_height() - c.c.spacing)

    dir = wfc.getSafeDirectoryNames()
    for i in range(len(dir)):
      file = tk.Button(
        self.tk,
        text=dir[i],
        bg=c.c.lbg,
        fg=c.c.dfg,
        border=0,
        borderwidth=0,
        highlightthickness=0,
        font=("7"),
        width=
        26  # I HAD to guess on this variable, width is not pixels inside of buttons and labels for some reason (very illogical in my opinion)
      )
      file.pack()
      self.tk.update(
      )  # << Update Here So Root Is Able To Draw And Calculate Size For Title Label (Needed for calculation below)
      file.place(x=c.c.spacing,
                 y=spl.winfo_y() + spl.winfo_height() +
                 (file.winfo_height() * i))
      file.bind("<ButtonPress-1>", lambda event, arg=i: wfc.openFile(arg, self.tk))

  def DirectoryAll(self):
    self.DirectoryFrame()
    self.InnerDirectory()

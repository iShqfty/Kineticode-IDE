import const as c
import tkinter as tk
import loader as l
import themeinfo as ti


class SettingsEditor:

  def __init__(self, tk: tk.Tk):
    self.tk = tk

  def Settings(self):
    sbtn = tk.Button(self.tk,
                     bg=c.c.dtc,
                     fg=c.c.fg,
                     text="⚙️",
                     font=("30"),
                     border=0,
                     borderwidth=0,
                     highlightthickness=0,
                     command=self.SettingsEditor)
    sbtn.pack()
    self.tk.update()
    sbtn.place(x=c.c.w - c.c.spacing - sbtn.winfo_width(),
               y=c.c.WinDrawDragHeaderHeight + c.c.spacing * 2)

  def SettingsEditor(self):
    bdrop = tk.Frame(self.tk, bg=c.c.bg, width=c.c.w, height=c.c.h)
    bdrop.pack()
    bdrop.place(x=0, y=c.c.WinDrawDragHeaderHeight)

    retrn = tk.Button(self.tk,
                      bg=c.c.dtc,
                      fg=c.c.fg,
                      text="<< Back",
                      border=0,
                      borderwidth=0,
                      highlightthickness=0,
                      command=lambda: ReturnCall())
    retrn.pack()
    retrn.place(x=c.c.spacing, y=c.c.WinDrawDragHeaderHeight + c.c.spacing)

    titleTS = tk.Label(self.tk,
                       bg=c.c.bg,
                       fg=c.c.fg,
                       text="Theme Settings",
                       font=("30"))
    titleTS.pack()
    self.tk.update()
    titleTS.place(x=c.c.spacing,
                  y=retrn.winfo_y() + retrn.winfo_height() + c.c.spacing)

    self.tk.update()
    hpnk = ti.ThemeInfo(
      self.tk, "Hot Pink", c.c.spacing,
      titleTS.winfo_y() + titleTS.winfo_height() + c.c.spacing, 20, "#FF7A7B",
      "#FF7A7B", "#FDBDBC", "#FC9C9D", "#FFDBDB", "#FFCFCF")
    drkgrn = ti.ThemeInfo(self.tk, "Emerald", c.c.spacing,
                          hpnk.getYPos() + c.c.spacing, 20, '#41916C',
                          '#2E6A50', '#74C79D', '#51B788', '#B7E4C7',
                          '#95D5B2')
    blck = ti.ThemeInfo(self.tk, "Monotone", c.c.spacing,
                        drkgrn.getYPos() + c.c.spacing, 20, "#414141",
                        "#333333", "#777777", "#565656", "#CFCFCF", "#A8A8A8")
    dflt = ti.ThemeInfo(self.tk, "Default", c.c.spacing,
                        blck.getYPos() + c.c.spacing, 20, '#1B222C',
                        '#12151C', '#661B1C', '#531516', '#FFFFFF', '#EBEBE4')

    lstofthemes = [hpnk, drkgrn, blck, dflt]

    def ReturnCall():
      c.c.title = "Kineticode IDE"
      l.ld.dr.DragHeader()
      l.ld.dr.TitleBar()
      bdrop.destroy()
      titleTS.destroy()
      for i in lstofthemes:
        i.Destroy()

      retrn.destroy()  # Last

  def SettingsAll(self):
    self.Settings()

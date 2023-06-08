import math as m
import tkinter as tki
"""

Constants to be used throughout the program

I would have defined macros but this is python and you can only do that with custom libs

(Not sure why I put it inside of a class, I dont need multiple instances of it)

"""


class Consts:

  def __init__(self):
    # Window Info
    self.w = m.floor(1150 * 1.2)
    self.h = m.floor(750 * 1.1)
    self.title = "Kineticode IDE"
    self.threadAllowed = True  # Only stored to stop all recursions once false, so erros aren't thrown upon closing. Errors are caused with constant recursion because thread isnt in main

    # GUI
    self.spacing = 5  # Between Elements / Widgets
    self.directoryRatio = .21  # Width Ratio Of Window For Directory Display
    self.mainRatio = 1 - self.directoryRatio  # Remainder For Main IDE Code Viewer

    # Colors
    self.lbg = '#1B222C'  # Light Background (Directory Display)
    self.bg = '#12151C'  # Background (Navy-Ish)
    self.ltc = '#661B1C'  # Light Theme Color
    self.dtc = '#531516'  # Darker Theme Color
    self.fg = '#FFFFFF'  # Default Foreground (White)
    self.dfg = '#EBEBE4'  # Disabled Foreground (Same as HTML [Gray-Ish {You Can't Tell Me Its 'Grey', They Both Refer To The Same Color 😂}])

    # Class-Specific Vars
    self.WinDrawDragHeaderHeight = 30
    self.TabHeaderTabBarHeight = int(self.WinDrawDragHeaderHeight * 1.5)
    self.TabHeaderButtonWidth = 10
    self.kmBoxCoverUpColor = self.bg
    self.kmBoxMainWidth = 250
    self.kmBoxMainHeight = 200
    self.WindowsDirectoryRestricted = ["venv"]
    self.WindowsDirectoryRestrictedExtensions = ["png"]
    self.HighlightKWP = ["True", "False", "await", "if", "elif", "else", "None", "pass", "import", "except", "try", "finally", "break", "raise", "return", "lambda", "for", "while", "continue", "def", "async"]
    self.HighlightKWPC = '#A78CFA'
    self.HighlightSPEC = ["nonlocal", "global", "del", "assert", "yield", "self"]
    self.HighlightSPECC = '#F78B6C'
    self.HighlightKWB = ["class", "in", "is", "and", "or", "from", "with", "as", "not"]
    self.HighlightKWBC = '#6394EC'
    self.GlobalBottomPos = 0

    # Inner Text Globals (Needs to be put here so its a global and can be edited by multiple files)
    self.gbtxt = tki.Text
    self.currOpen = ""
    self.firstIter = True
    self.currDisp = None

    # Miscellaneous
    self.exitmsg = f"Thank You For Using {self.title}"
    self.AskStringReturn = ""
    

  def ReloadCurrentOpen(self, tk: tki.Tk):
    if self.firstIter:
      self.currDisp = tki.Label(tk,
                                bg=self.lbg,
                                fg=self.fg,
                                font=("20"),
                                text=f"Opened File: {self.currOpen}")
      self.currDisp.pack()
      self.currDisp.place(x=(self.spacing * 2) +
                          (self.directoryRatio * self.w - self.spacing) + 2,
                          y=self.WinDrawDragHeaderHeight +
                          self.TabHeaderTabBarHeight + (self.spacing * 2))
      self.firstIter = False
      return
    self.currDisp.destroy()

    self.currDisp = tki.Label(tk,
                              bg=self.lbg,
                              fg=self.fg,
                              font=("20"),
                              text=f"Opened File: {self.currOpen}")
    self.currDisp.pack()
    self.currDisp.place(
      x=(self.spacing * 2) + (self.directoryRatio * self.w - self.spacing) + 2,
      y=self.WinDrawDragHeaderHeight + self.TabHeaderTabBarHeight +
      (self.spacing * 2))


c = Consts()

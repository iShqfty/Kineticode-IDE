import tkinter as tk
import const as c

class Highlight:
  def __init__(self, tk : tk.Tk):
    self.tk = tk

  def highlighter(self, tag, x, y, fg):
    c.c.gbtxt.tag_add(tag, x, y)
    c.c.gbtxt.tag_config(tag, foreground=fg)

  def highlightKeywords(self):
    lines = c.c.gbtxt.get("1.0", "end-1c").splitlines()
    for line in range(len(lines)):
      split = lines[line].split()
      for word in split:
        clr = None
        if "(" in word and ")" in word:
          clr = 'yellow'
        elif word in c.c.HighlightKWB:
          clr = c.c.HighlightKWBC
        elif word in c.c.HighlightKWP:
          clr = c.c.HighlightKWPC
        elif word in c.c.HighlightSPEC:
          clr = c.c.HighlightSPECC
        lpos = lines[line].find(word)
        endpos = 0
        if clr == 'yellow':
          if not lines[line].find(".") == -1:
            lpos = lines[line].find(".")
          endpos = lpos + (lines[line].find("(") - lpos)
        else:
          endpos = lpos + len(word)
        x = f"{line+1}.{lpos}"
        y = f"{line+1}.{endpos}"
        self.highlighter(word, x, y, clr)
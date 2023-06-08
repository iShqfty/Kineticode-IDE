"""

Windows functions or similar abstractable, non file-specific functions (usually system/os related)

"""

import os
import const as c
import loader as l


def getCurrentDirectory():
  return os.getcwd()


def getDirectoryNames():
  return os.listdir()


def runCommand(cmd):
  os.system(cmd)


def getSafeDirectoryNames():
  pot = getDirectoryNames()  # 'pot'ential names but not all are safe
  ret = []
  for i in range(len(pot)):
    if pot[i][0] == '.' or pot[i][0:2] == "__" or pot[
        i] in c.c.WindowsDirectoryRestricted:
      continue
    elif not pot[i].find(".") == -1:
      if pot[i][pot[i].find(".") +
                1:len(pot[i])] in c.c.WindowsDirectoryRestrictedExtensions:
        continue
    ret.append(pot[i])
  return ret


def openFile(i, tk):
  c.c.gbtxt.delete("1.0", "end-1c")
  dir = getSafeDirectoryNames()
  with open(dir[i], 'r') as f:
    for j in f.readlines():
      c.c.gbtxt.insert('insert', j)
  c.c.currOpen = dir[i]
  c.c.ReloadCurrentOpen(tk)

def newFile(root, name):
  if not name in getDirectoryNames():
    with open(f"{c.c.AskStringReturn}", 'w') as f:
      print(f)
  c.c.currOpen = name
  c.c.ReloadCurrentOpen(root)
  l.ld.dr.DirectoryAll()

def saveFile():
  with open(c.c.currOpen, 'w') as f:
    f.writelines(c.c.gbtxt.get("1.0", "end-1c"))

def delFile(root):
  os.remove(c.c.currOpen)
  openFile(len(getSafeDirectoryNames())-1, root)
  l.ld.dr.DirectoryAll()
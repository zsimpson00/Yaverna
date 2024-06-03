import random
from tkinter import *
import time
import math
pName = ""
companions = ["Ellie","Charlie","Nick","Emma"]
classTypes = ["Healer","Warrior","Mage",
              "Archer","Knight","Assassin"]
races = ["Human","Elf","Half-Elf"]
buildTypes = ["Skinny","Average","Chubby","Fat"]
companion = -1
companionInfo = ["Name","Race","Class","Build","HP"]
health = str(100)
companionStats = ([[companions[0],races[2],classTypes[0],buildTypes[2],health],
                   [companions[1],races[0],classTypes[1],buildTypes[1],health],
                   [companions[2],races[0],classTypes[3],buildTypes[2],health],
                   [companions[3],races[1],classTypes[2],buildTypes[1],health]])


def starLine(numRows,numSleep):
    sLine = "*" * 10
    for i in range(numRows):
        print(sLine)
    time.sleep(numSleep)


def companionList():
    starLine(1, 0)
    for i in range(len(companions)):
        for j in range(len(companionStats[i])):
            print(companionInfo[j] + ":",companionStats[i][j])
        starLine(1,1)

companionList()
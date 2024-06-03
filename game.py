import random
from tkinter import *
import time
import math

root = Tk()
root.title("Yaverna")
root.iconbitmap("YavernaIcon.ico")
pName = ""
companions = ["Ellie","Charlie","Nick","Emma"]
classTypes = ["Healer","Warrior","Mage",
              "Archer","Knight","Assassin"]
races = ["Human","Elf","Half-Elf","Yavernian"]
buildTypes = ["Skinny","Average","Chubby","Fat"]
companion = ""
companionInfo = ["Name","Race","Class","Build","HP"]
health = str(100)
hp = int(health)
startMessage = "Enter Your Name, Traveler"
companionQuestion = ("Choose a companion for your journey. "
                     "Your companion of choice has a major "
                     "impact on the story.")
e = Entry(root, width=50)
companionPrompt = Label(root, text=companionQuestion, padx=10, pady=10)
startLabel = Label(root, text=startMessage, padx=10, pady=10)
companionStats = ([[companions[0],races[2],classTypes[0],buildTypes[2],health],
                   [companions[1],races[0],classTypes[1],buildTypes[1],health],
                   [companions[2],races[0],classTypes[3],buildTypes[2],health],
                   [companions[3],races[1],classTypes[2],buildTypes[1],health]])


def starLine(numRows,numSleep):
    sLine = "*" * 10
    for i in range(numRows):
        print(sLine)
    time.sleep(numSleep)


def onEnterClick():
    global pName
    pName = e.get()
    e.destroy()
    startLabel.destroy()
    startButton.destroy()
    companionPrompt.pack()
    companionButton1.pack()
    companionButton2.pack()
    companionButton3.pack()
    companionButton4.pack()


def objectBreak(build):
    if build > 2:
        canSupportWeight = False
    else:
        canSupportWeight = True
    print(canSupportWeight)


def companionList():
    starLine(1, 0)
    for i in range(len(companions)):
        for j in range(len(companionStats[i])):
            print(companionInfo[j] + ":",companionStats[i][j])
        starLine(1,1)


companionButton1 = Button(root, text="ELLIE", command=lambda: companionChoose(1))
companionButton2 = Button(root, text="CHARLIE", command=lambda: companionChoose(2))
companionButton3 = Button(root, text="NICK", command=lambda: companionChoose(3))
companionButton4 = Button(root, text="EMMA", command=lambda: companionChoose(4))


def companionChoose(number):
    global companion
    global pName
    if number == 1:
        companion = companions[0]
        print(companion)
    elif number == 2:
        companion = companions[1]
        print(companion)
    elif number == 3:
        companion = companions[2]
        print(companion)
    elif number == 4:
        companion = companions[3]
        print(companion)
    time.sleep(1)
    companionButton1.destroy()
    companionButton2.destroy()
    companionButton3.destroy()
    companionButton4.destroy()
    companionPrompt.destroy()


startButton = Button(root, text="Enter", command=onEnterClick)
startLabel.pack()
e.pack()
startButton.pack()


root.mainloop()

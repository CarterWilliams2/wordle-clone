import tkinter as tk
import random

def main():
    #set up main window
    mainWindow()


def mainWindow():   
    #make main window
    mainWindow = tk.Tk()
    mainWindow.title('Main Window')
    mainWindow.geometry('500x500')
    playButton = tk.Button(mainWindow, text='Play', command=lambda: [play(), mainWindow.destroy()])
    playButton.pack()
    seeStatsButton = tk.Button(mainWindow, text = 'See stats')
    seeStatsButton.pack()
    mainWindow.mainloop()


def play():
    #make game window
    gameWindow = tk.Tk()
    gameWindow.title('Game Window')
    gameWindow.geometry('500x500')

    #generate word to play with
    wordLine = random.randint(0, 2314)
    answersFile = open("/Users/carterwilliams/Coding_Projects/Wordle_Clone/wordle-clone/answers.txt", "r")
    word = answersFile.readline()
    for x in range(wordLine):
        word = answersFile.readline()
    label = tk.Label(gameWindow, text=word)
    label.pack()
    
    


main()


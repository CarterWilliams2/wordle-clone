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

    #create layout for game board
    r0c0 = tk.LabelFrame(gameWindow, height='40', width='40')
    r0c0.grid(row=0, column=0, padx='10', pady='10')
    r0c1 = tk.LabelFrame(gameWindow, height='40', width='40')
    r0c1.grid(row=0, column=1)
    r0c2 = tk.LabelFrame(gameWindow, height='40', width='40')
    r0c2.grid(row=0, column=2, padx='10', pady='10')
    r0c3 = tk.LabelFrame(gameWindow, height='40', width='40')
    r0c3.grid(row=0, column=3)
    r0c4 = tk.LabelFrame(gameWindow, height='40', width='40')
    r0c4.grid(row=0, column=4)
    r1c0 = tk.LabelFrame(gameWindow, height='40', width='40')
    r1c0.grid(row=1, column=0)
    r1c1 = tk.LabelFrame(gameWindow, height='40', width='40')
    r1c1.grid(row=1, column=1)
    r1c2 = tk.LabelFrame(gameWindow, height='40', width='40')
    r1c2.grid(row=1, column=2)
    r1c3 = tk.LabelFrame(gameWindow, height='40', width='40')
    r1c3.grid(row=1, column=3)
    r1c4 = tk.LabelFrame(gameWindow, height='40', width='40')
    r1c4.grid(row=1, column=4)
    r2c0 = tk.LabelFrame(gameWindow, height='40', width= '40')
    r2c0.grid(row=2, column=0, padx='10', pady='10')
    r2c1 = tk.LabelFrame(gameWindow, height='40', width='40')
    r2c1.grid(row=2, column=1)
    r2c2 = tk.LabelFrame(gameWindow, height='40', width='40')
    r2c2.grid(row=2, column=2)
    r2c3 = tk.LabelFrame(gameWindow, height='40', width='40')
    r2c3.grid(row=2, column=3)
    r2c4 = tk.LabelFrame(gameWindow, height='40', width='40')
    r2c4.grid(row=2, column=4)
    r3c0 = tk.LabelFrame(gameWindow, height='40', width='40')
    r3c0.grid(row=3, column=0)
    r3c1 = tk.LabelFrame(gameWindow, height='40', width='40')
    r3c1.grid(row=3, column=1)
    r3c2 = tk.LabelFrame(gameWindow, height='40', width='40')
    r3c2.grid(row=3, column=2)
    r3c3 = tk.LabelFrame(gameWindow, height='40', width='40')
    r3c3.grid(row=3, column=3)
    r3c4 = tk.LabelFrame(gameWindow, height='40', width='40')
    r3c4.grid(row=3, column=4)
    r4c0 = tk.LabelFrame(gameWindow, height='40', width='40')
    r4c0.grid(row=4, column=0, padx='10', pady='10')
    r4c1 = tk.LabelFrame(gameWindow, height='40', width='40')
    r4c1.grid(row=4, column=1)
    r4c2 = tk.LabelFrame(gameWindow, height='40', width='40')
    r4c2.grid(row=4, column=2)
    r4c3 = tk.LabelFrame(gameWindow, height='40', width='40')
    r4c3.grid(row=4, column=3)
    r4c4 = tk.LabelFrame(gameWindow, height='40', width='40')
    r4c4.grid(row=4, column=4, padx='10', pady='10')

    
    


main()


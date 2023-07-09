import tkinter as tk

def main():
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
    
    


main()


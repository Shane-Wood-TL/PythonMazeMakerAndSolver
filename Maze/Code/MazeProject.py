#project part 1 Shane Wood
# allows user to make a maze (blue start, red end)
# allows user to save a maze to a file "maze.dat"
# allows user to set start and end pos (just uses last and first var in ButtonList)
# all with a questionable gui built with tkinter


import tkinter
import os

tempButton = None
save = None

ButtonList = list()
ObuttonList = list()


def updateFile():
    with open("maze.dat", "w") as outfile:
        for sublist in ButtonList:
            outfile.write(f"{sublist}\n")


def maze_builder():
    window = tkinter.Tk()
    pos = 0
    for i in range(1,22):
        for ii in range(1,22):
            tempButton= tkinter.Button(window, text=f"XX", bg="white") #"
            tempButton.grid(row=i, column=ii)
            tempButton["command"] = lambda \
                                    button = tempButton, \
                                    gridPos = [i,ii] : \
                                    test(gridPos, button)

    save = tkinter.Button(window, text=f"Save File", command=updateFile)
    save.grid(row = 23,column = 1, columnspan=22)
    window.mainloop()
 
def test(pos, button):
            #both of there if/else control the buttons in the list
    if  (button in ObuttonList):
        
        button["bg"] = "white"
        button["text"] = "XX"
        ButtonList.remove(pos)
        ObuttonList.remove(button)
        #updateFile()
      
    else:
        ButtonList.append(pos)
        print(pos)
        ObuttonList.append(button)
        #updateFile()
        
        #this is a little cursed, but it works (makes every button green in the list)
    for i in range(1, len(ObuttonList)):
        temp = ObuttonList[i]
        temp["bg"] = "green"
        temp["text"] = "OO"

#this makes the first and last buttons blue and red
    try:
        start = ObuttonList[0]
        start["bg"] = "blue"
        start["text"] = "OO"
        end = ObuttonList[len(ObuttonList)-1]
        end["bg"] = "red"
        end["text"] = "OO"
    except:
        pass

maze_builder()
    


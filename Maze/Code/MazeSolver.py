# MazeSolver
# project part 2 Shane Wood
# allows bot to solve a maze (maze format not standard, points list)
# writes positons it took to a list
# for some reason x and y are flipped, but its the same flipped as the builder 
# all with a questionable gui built with tkinter
# path green, maze white, blue is start and end

import tkinter
import os

done = False

def checkDone(current, endPos, moves):
    if current == endPos:
        #print(moves)
        return True
    
    else:
        False

def get_maze():
    with open("maze.dat", 'r') as infile:
        table = [ ]
        string_in = infile.readline()
        while (string_in):
            list_of_strings = string_in.strip('[').strip(']\n').split(',')
            good_list = [int(x) for x in list_of_strings]
            table.append(good_list)
            string_in = infile.readline()
    return(table)

def solve_maze(list_of_lists):
    global done
    points_list = list_of_lists
    #print("it got to 2nd function")

    startPos = points_list[0]
    endPointPos = len(points_list)
    endPos = points_list[endPointPos-1]

    #print(f'{startPos}, {endPos}')

    moves = 0
    currentPos = startPos

    path = list()
    path.append(currentPos)
    rotation = 0
    leftFree = False
    forwardFree = False
    rightFree = False

    totalMoves = 0



    while(moves != currentPos):
        #print("in while")
        #left wall following
        while rotation == 0: #facing up
            #print("facing up")
            leftFree = False
            forwardFree = False
            rightFree = False
            for points in list_of_lists: 
                if points == ([(currentPos[0]), currentPos[1]-1]): #checking to the left (left)
                    leftFree = True
                elif points == ([(currentPos[0] -1), currentPos[1]]): #checking to the forward (up)
                    forwardFree = True
                elif points == ([(currentPos[0]), currentPos[1]+1]): #checking to the right (right)
                    rightFree = True

   
            if (leftFree == True):
                currentPos = ([(currentPos[0]), currentPos[1]-1])
                path.append(currentPos)
                moves = moves + 1
                rotation = 90       
                #rotate left
                #move left
                break
            elif (leftFree == False) and (forwardFree == True):
                #go forward
                #keep rot the same
                currentPos = ([(currentPos[0] -1), currentPos[1]])
                path.append(currentPos)
                moves = moves + 1
                break
            elif (leftFree == False) and (forwardFree == False) and (rightFree == True):
                #change rotation to right
                currentPos = ([(currentPos[0]), currentPos[1]+1])
                path.append(currentPos)
                moves = moves + 1
                rotation = 270
                break
            elif (leftFree == True) and (forwardFree == True) and (rightFree == True):
                currentPos = ([(currentPos[0]), currentPos[1]-1])
                path.append(currentPos)
                moves = moves + 1
                rotation = 90  
                break             

            else:
                #rotation = opposite of current
                rotation = 180
                break
        if checkDone(currentPos, endPos, moves):
            done = True
            return path

  
        while rotation == 90: #facing left
            #print("facing left")
            leftFree = False
            forwardFree = False 
            rightFree = False  
            for points in list_of_lists:
                  

                if points == ([(currentPos[0]+1), currentPos[1]]): #checking to the left (down)
                    leftFree = True
                elif points == ([(currentPos[0]), currentPos[1]-1]): #checking to the foward (left)
                    forwardFree = True 
                elif points == ([(currentPos[0]-1), currentPos[1]]): #checking to the right (up)
                    rightFree = True

            if (leftFree == True):
                currentPos = ([(currentPos[0]+1), currentPos[1]])
                path.append(currentPos)
                moves = moves + 1
                rotation = 180
                #rotate left
                #move left
                break
            elif (leftFree == False) and (forwardFree == True):
                moves = moves + 1
                #go forward
                #keep rot the same
                currentPos = ([(currentPos[0]), currentPos[1]-1])
                path.append(currentPos)
                break
            elif (leftFree == False and forwardFree == False and rightFree == True):
                #change rotation to right
                moves = moves + 1
                currentPos = ([(currentPos[0]-1), currentPos[1]])
                path.append(currentPos)
                rotation = 0
                break
            elif (leftFree == True and forwardFree == True and rightFree == True):
                currentPos = ([(currentPos[0]+1), currentPos[1]])
                path.append(currentPos)
                moves = moves + 1
                rotation = 180
                #rotate left
                #move left    
                break            
            else:
                #rotation = opposite of current
                rotation = 270
                break
        if checkDone(currentPos, endPos, moves):
            done = True
            return path
                     

        while rotation == 180: #facing down
            #print("facing down")
            leftFree = False
            forwardFree = False 
            rightFree = False
            for points in list_of_lists:
  

                if points == ([(currentPos[0]), currentPos[1]+1]): #checking to the left (right)
                    leftFree = True
                elif points == ([(currentPos[0]+1), currentPos[1]]): #checking to the forward (down)
                    forwardFree = True
                elif points == ([(currentPos[0]), currentPos[1]-1]): #checking to the right (left)
                    rightFree = True


            if (leftFree == True):
                currentPos = ([(currentPos[0]), currentPos[1]+1])
                moves = moves + 1
                path.append(currentPos)
                rotation = 270
                #rotate left
                #move left
                break
            elif (leftFree == False) and (forwardFree == True):
                #go forward
                #keep rot the same
                currentPos = ([(currentPos[0] +1), currentPos[1]])
                path.append(currentPos)
                moves = moves + 1
                break
            elif (leftFree == False) and (forwardFree == False) and (rightFree == True):
                moves = moves + 1 
                currentPos = ([(currentPos[0]), currentPos[1]-1])
                path.append(currentPos)
                #change rotation to right
                rotation = 90
                break
            elif (leftFree == True) and (forwardFree == True) and (rightFree == True):
                currentPos = ([(currentPos[0]), currentPos[1]+1])
                moves = moves + 1
                path.append(currentPos)
                rotation = 270
                #rotate left
                #move left     
                break           
            else:
                #rotation = opposite of current
                rotation = 0
                break
        if checkDone(currentPos, endPos, moves):
            done = True
            return path

        while rotation == 270: #facing right
            #print("facing right")
            leftFree = False
            forwardFree = False 
            rightFree = False  
            
            for points in list_of_lists:
                  

                if points == ([(currentPos[0] -1), currentPos[1]]): #checking to the left (up)
                    leftFree = True
                elif points == ([(currentPos[0]), currentPos[1]+1]): #checking to the forward (right)
                    forwardFree = True
                elif points == ([(currentPos[0] +1), currentPos[1]]): #checking to the right (down)
                    rightFree = True


            if (leftFree == True):
                currentPos = ([(currentPos[0] -1), currentPos[1]])
                moves = moves + 1
                path.append(currentPos)
                rotation = 0
                #rotate left
                #move left
                break
            elif (leftFree == False) and (forwardFree == True):
                #go forward
                #keep rot the same
                moves = moves + 1
                currentPos = ([(currentPos[0]), currentPos[1]+1])
                path.append(currentPos)
                break
            elif (leftFree == False) and (forwardFree == False) and (rightFree == True):
                moves = moves + 1
                currentPos = ([(currentPos[0] +1), currentPos[1]])
                path.append(currentPos)
                #change rotation to right
                rotation = 180
                break
            elif (leftFree == True) and (forwardFree == True) and (rightFree == True):
                currentPos = ([(currentPos[0] -1), currentPos[1]])
                moves = moves + 1
                path.append(currentPos)
                rotation = 0
                #rotate left
                #move left              
                break  
            else:
                #rotation = opposite of current
                rotation = 90
                break       
        if checkDone(currentPos, endPos, moves):
            done = True
            return path

            
   
        moves = moves + 1
        if moves > 399: #if it doesnt get in it 400 moves, its probably not going to, without modifing the search list
            #(moves var is not based on it actually moving, just how many times the loop runs)
            #print("Fail with left")
            for i in range(len(path)-1):
                try:
                    workingPos = path[i]
                    #print(points_list)
                    #print(workingPos)
                    points_list.remove(workingPos)
                    break 
                except:
                    pass
            totalMoves = totalMoves + 400
            moves = 0
        
        if(totalMoves > 8000):
            #this is the point of utter failure
            #gives up, makes bg red
            return path




def display_maze(pointsListin, list_of_lists):
    pointsList = list()
    for i in pointsListin: #tk inter is very unhappy unless this removes duplicates
        if i not in pointsList:
            pointsList.append(i)

    global done
    #print("Got to displaying")
    
    window = tkinter.Tk()

    for i in range(1,22):
        for ii in range(1,22):
            pos = tkinter.Label(window, text = "     ")
            pos.grid(row = i, column=ii)
            if done == True:
                pos['bg']= "black"
            else:
                pos['bg']= "red" #only happens in the maze fails
    
    for points in list_of_lists:
        posX = tkinter.Label(window, text = "     ")
        posX['bg'] = "white"
        posX.grid(row = int(points[0]), column=int(points[1])) #overall maze

    
         

    for points in pointsList:
            posX = tkinter.Label(window, text = "     ")
            posX['bg'] = "green"
            posX.grid(row = int(points[0]), column=int(points[1])) #path
    #print(f"{points[0]} {points[1]}")

    startPosb = pointsList[0]
    startPosBox = tkinter.Label(window, text= "     ")
    startPosBox['bg'] = "blue"
    startPosBox.grid(row = int(startPosb[0]), column=int(startPosb[1])) #start

    endPosb = pointsList[len(pointsList)-1]
    endPosBox = tkinter.Label(window, text= "     ")
    endPosBox['bg'] = "blue" 
    endPosBox.grid(row=int(endPosb[0]), column=int(endPosb[1])) #stop tile

    window.mainloop()

    

list_of_lists = get_maze()
solved_list_of_lists = solve_maze(list_of_lists)
display_maze(solved_list_of_lists, list_of_lists)




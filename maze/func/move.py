#checks if player can go down 
def down(maze,column,row):
    position=maze[row,column]
    len_maze=len(maze)-1
    #checks if player is in the last row
    if row==len_maze:
        return ""
    else:
        ...
    if position==0:
        row+=1
        number=maze[row,column]
        if number == 1:
            return ""
        else:
            return "down"
    else:
        return ""
#checks if player can go up  
def up(maze,column,row):
    position=maze[row,column]
    if position==0:
        row-=1
        number=maze[row,column]
        if number == 1:
            return ""
        else:
            return "up"
    else:
        return "Enter right position"
#checks if player can go right   
def right(maze,column,row):
    position=maze[row,column]
    len_row=len(maze)-1
    #checks if player is in the last column
    
    if column == len_row:
        return""
    else:
        ...
    if position==0:
        column+=1
        number=maze[row,column]
        print(number)
        if number == 1:
            return ""
        else:
            return "right"
    else:
        return ""
    
#checks if player can go left
def left(maze,column,row):
    position=maze[row,column]
    if position==0:
        column-=1
        number=maze[row,column]
        if number == 1:
            return ""
        else:
            return "left"
    else:
        return ""
#moves players position
def movement(maze,move,column,row):
    number = None
    if move == "down":
        row+=1
        number = maze[row,column]
    elif move == "up":
        row-=1
        number = maze[row,column]
    elif move == "left":
        column-=1
        number = maze[row,column]
    elif move == "right":
        column+=1
        number = maze[row,column]
    else:
        return "Choose one of the options"
    if number == 0:
        print(maze)
        return f"Your new position:{number}\nRow:{row}\nColumn:{column}"
    elif number==2:
        print(number)
        return "You won!!!"
    else: 
        return "You cannot go there,there is a wall" 
import random
import numpy as np


def create_matrix(columns,rows):
    maze=[]
    for row in range(rows):
        numbers=[]
        for column in range(columns):
            numbers.append(random.randint(0,1))
        maze.append(numbers)
    return maze


def spawn(maze):
    row_num = 0
    col_num = 0
    row = maze[row_num]
    while 0 not in row:
        row_num += 1
        row = maze[row_num]
        if 0 in row:
            break
    number=maze[row_num,col_num]
    
    if number==1:
        while number:
            col_num += 1
            number = maze[row_num,col_num]
            if number == 0:
                return f"your starting position:{number}\nRow:{row_num+1}\nColumn:{col_num+1}"
            else:
                ...
    else:
        return f"Your starting position:{number}\nRow:{row_num+1}\nColumn:{col_num+1}"
    
    
    
def movement(maze,move,column,row):
    row_num = row
    col_num = column
    number = None
    if move == "down":
        row_num+=1
        number = maze[row_num,col_num]
    elif move == "up":
        row_num-=1
        number = maze[row_num,col_num]
    elif move == "left":
        col_num-=1
        number = maze[row_num,col_num]
    elif move == "right":
        col_num+=1
        number = maze[row_num,col_num]
    else:
        return "Choose one of the options"
    print(number)
    if number == 1:
        return "You cannot go there,there is a wall"
    else: 
        print(maze)
        return f"your new position:{number}\nRow:{row_num+1}\nColumn:{col_num+1}" 




rows = int(input("Enter number of rows"))
columns = int(input("Enter number of columns"))
matrix = create_matrix(rows,columns)
maze = np.matrix(matrix)
print(maze)
spawn_position=spawn(maze)
print(spawn_position)
while True:
    col=int(input("Enter you column"))
    row=int(input("Enter you row"))
    move=input("Enter your move:\ndown\nup\nleft\nright")
    move_resp=movement(maze,row=row,column=col,move=move)
    print(move_resp)


    

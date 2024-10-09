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
                break
            else:
                ...
    else:
        ...
    row_end=-1
    col_end=-1
    row = maze[row_end]
    while 0 not in row:
        row_end-=1
        row = maze[row_end]
        if 0 in row:
            break
    num_end=maze[row_end,col_end]
    if num_end==1:
        while num_end:
            col_end-=1
            num_end=maze[row_end,col_end]
            if num_end == 0:
                return f"Start:\nRow:{row_num}\nColumn:{col_num}\nFinish:\nRow:{row_end}\nColumn:{col_end}"
            else:
                ...
    else:
        return f"Start:\nRow:{row_num}\nColumn:{col_num}\nFinish:\nRow:{row_end}\nColumn:{col_end}"
    




    




    
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
    print(number)
    if number == 0:
        print(maze)
        return f"Your new position:{number}\nRow:{row}\nColumn:{column}"
    else: 
        return "You cannot go there,there is a wall" 




rows = int(input("Enter number of rows"))
columns = int(input("Enter number of columns"))
matrix = create_matrix(rows,columns)
maze = np.matrix(matrix)
print(maze)
spawn_position=spawn(maze)

print(spawn_position)

while True:
    col=int(input("Enter your column"))
    row=int(input("Enter your row"))
    move=input("Enter your move:\ndown\nup\nleft\nright")
    move_resp=movement(maze,row=row,column=col,move=move)
    print(move_resp)


    

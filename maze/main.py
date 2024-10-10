import numpy as np
from func import up,down,right,left,movement,create_start_and_finish


#dict of matrix
matrixs={1:"0 0 1 1;1 0 1 1;0 0 0 1;1 1 0 2",
         2:"1 1 0 1 1 1;1 0 0 0 1 1;1 0 1 0 1 1;1 0 1 0 0 1;1 0 0 1 0 0;1 1 1 1 1 2",
         3:"0 1 1 1 1 0 0 1;0 0 0 0 0 0 1 1;1 0 1 1 0 1 1 1;1 0 1 1 0 1 0 1;0 0 1 0 0 0 0 1;1 1 1 0 1 0 1 1;1 0 0 0 1 0 0 2;1 1 1 1 1 1 1 1",
         4:"0 1 0 1 1 0 1 1 0 1;0 1 1 1 1 1 1 0 0 1;0 0 0 0 0 1 1 0 1 1;0 1 1 1 1 0 0 0 0 1;0 0 0 1 1 0 1 1 0 1;1 1 0 0 0 0 1 1 0 0;0 0 0 1 1 1 0 0 0 1;0 1 1 1 0 0 0 1 1 1;1 1 1 1 1 1 0 1 1 2;1 1 1 1 1 1 0 0 0 0"}

print("Welcome to maze-game!")
choice = int(input("Enter your choice:\n1->4x4\n2->6x6\n3->8x8\n4->10x10\n"))
matrix=matrixs.get(choice)
#transforms matrix
maze=np.matrix(matrix)
print(maze)
print("1 is wall,0 is path and 2 is end")
start_finish=create_start_and_finish(maze)
print(start_finish)

while True:
    col=int(input("Enter your column\n"))
    row=int(input("Enter your row\n"))
    move_up=up(maze,column=col,row=row)
    move_down=down(maze,column=col,row=row)
    move_right=right(maze,column=col,row=row)
    move_left=left(maze,column=col,row=row)
    while move_up=="Enter right position":
        print(move_up)
        col=int(input("Enter your column"))
        row=int(input("Enter your row"))
        move_up=up(maze,column=col,row=row)
        move_down=down(maze,column=col,row=row)
        move_right=right(maze,column=col,row=row)
        move_left=left(maze,column=col,row=row)
        if move_up != "Enter right position":
            move=input(f"Enter your move:\n{move_up}\n{move_down}\n{move_right}\n{move_left}")
            move_resp=movement(maze,row=row,column=col,move=move)
            print(move_resp)
        else:
            ...
    move=input(f"Enter your move:\n{move_up}\n{move_down}\n{move_right}\n{move_left}\n")
    move_resp=movement(maze,row=row,column=col,move=move)
    print(move_resp)
    if move_resp=="You won!!!":
        break


    

#creates start position for player and finish
def create_start_and_finish(maze):
    #default start position
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
    #default finish position
    row_end=-1
    col_end=-1
    row = maze[row_end]
    while 2 not in row:
        row_end-=1
        row = maze[row_end]
        if 2 in row:
            break
    num_end=maze[row_end,col_end]
    if num_end==2:
        return f"Start:\nRow:{row_num}\nColumn:{col_num}\nFinish:{num_end}\nRow:{row_end}\nColumn:{col_end}"
    else:
        while num_end:
            col_end-=1
            num_end=maze[row_end,col_end]
            if num_end == 0:
                return f"Start:\nRow:{row_num}\nColumn:{col_num}\nFinish:{num_end}\nRow:{row_end}\nColumn:{col_end}"
            else:
                ...
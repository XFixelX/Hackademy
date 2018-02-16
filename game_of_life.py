def generate_row(num_of_elements):
    my_list = []
    for i in range(num_of_elements):
        random_number = random.randint(0,1)
        if random_number == 1:
            my_list.append('X')
        else:
            my_list.append('-')
    return my_list


def generate_matrix(num_of_elements):
    my_list = []
    for i in range(num_of_elements):
        my_list.append(generate_row(num_of_elements))
    return my_list

current_board = generate_matrix(8)


def neighbors(row,column,board):
    n = []
    n.append(board[row-1][column-1])
    n.append(board[row-1][column])
    n.append(board[row-1][column+1])
    n.append(board[row][column-1])
    n.append(board[row][column+1])
    n.append(board[row+1][column-1])
    n.append(board[row+1][column])
    n.append(board[row+1][column+1])
    return n


def count_alive(a_list):
    counter = 0
    for each_cell in a_list:
        if each_cell == 'X':
            counter = counter + 1
    return counter


def count_alive_neighbors(row,column,board):
    return count_alive(neighbors(row,column,board))


def is_cell_alive(row,column, board):
    return board[row][column] == 'X'


def is_future_cell_alive(row,column,board):
    alive_neigh = count_alive_neighbors(row,column,board)
    alive_cell = is_cell_alive(row,column,board)

    if alive_cell:
        if alive_neigh >= 2 and alive_neigh <= 3:
            return True
        else:
            return False
    else:
        if alive_neigh == 3:
            return True
        else:
            return False

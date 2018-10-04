
"""
N queen problem
https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

"""
total_cnt = 0


def solve_nqueen(board, col, n, m, queen):

    # if all queens are placed, return True
    if col == m:        # or queen == 0:
        global total_cnt
        total_cnt += 1
        print_position(board)
        print("")
        return True

    # consider this column and try placing this queen one by one in rows.
    res = False
    for row in range(n):
        if board[row][col] != '#':

            # check if it is safe to place the queen on this row, col
            if is_safe(board, row, col, n):
                # place the queen on board[row][col]
                board[row][col] = 1

                # recurse and place rest of the queens
                # if solve_nqueen(board, col+1, n, m, queen-1):       # pending queens
                #     global total_cnt
                #     total_cnt += 1
                #     board[row][col] = '.'

                res = solve_nqueen(board, col+1, n, m, queen-1) or res


                # this is the key to back track. if palcing the queen on row,
                # col doesn't lead to solution later in the stage.
                # then remove this queen from board[row][col]
                # else:
                #     board[row][col] = '.'

                board[row][col] = '.'
        # if the queen can not be placed in any row in this column
        # then return False to the calling function so that the calling function
        # can then travserse in pending rows to accomodate a new position for its own
        # queen and thereby a new posn for this queen as well.

    return res



"""
A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1. So we need to check only left side for attacking queens
"""
"""

# jsut checks if there is any queen
1. on the left in same row
2. on left diagonally(up and down)


"""


def is_safe(board, row, col, n):

    # check this row on left side
    for c in range(col):
        if board[row][c] == "#":   # if found first then return True b/c this is a
            #  good place to place queen
            return True

        if board[row][c] == 1:
            return False            # else if found this first then return not a place

    # check upper diagonal on left
    for r,c in zip(list(range(row, -1, -1)), list(range(col, -1, -1))):  # runs in zip and goes up the way to upper left corner
        if board[r][c] == "#":
            return True

        if board[r][c] == 1:
            return False

    # check lower diagonal on left
    for r,c in zip(list(range(row, n)), list(range(col, -1, -1))):  # runs in zip and goes down the way to lower left corner
        if board[r][c] == "#":
            return True

        if board[r][c] == 1:
            return False

    # if found a safe position return true for this position
    return True


def print_position(board):
    for row in board:
        print(row)


def solve():
    board = [['.', '#', '.'],
             ['.', '#', '.'],
             ['.', '.', '#']]
    n = len(board)          # row
    m = len(board[0])       # col
    print((n, m))

    solve_nqueen(board, col=0, n=n, m=m, queen=n)


solve()
print(total_cnt)

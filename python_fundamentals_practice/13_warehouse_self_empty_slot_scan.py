def find_empty_slot(grid):

    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            if grid[row][col] == 0:
                return(row,col)
            col += 1
        row += 1
    return None
print(find_empty_slot([[5, 3, 0], [2, 4, 6]]))
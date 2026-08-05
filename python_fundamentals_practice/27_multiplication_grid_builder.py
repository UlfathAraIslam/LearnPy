def multiplication_grid(n):
    grid = []
    for i in range(1,n+1):
        row = []
        for j in range(1,n+1):
            row.append(i * j)
        grid.append(row)
    return grid

print(multiplication_grid(3))
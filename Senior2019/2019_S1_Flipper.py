# Complete!


grid = [[1, 2], [3, 4]]
inp = input()


def h_swap(grid):
    index_0 = grid[0]
    grid[0] = grid[1]
    grid[1] = index_0
    return grid


def v_swap(grid):
    grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
    return grid


for i in inp:
    if i == 'H':
        grid = h_swap(grid)
    if i == 'V':
        grid = v_swap(grid)


print(str(grid[0][0]), str(grid[0][1]))
print(str(grid[1][0]), str(grid[1][1]))

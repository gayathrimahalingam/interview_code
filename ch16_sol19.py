# Given a matrix representation of plot of land, 
# find the sizes of all the ponds in the matrix
# 0 indicates water. Pond is the region of water connected vertically, horizontally, or diagonaly

def pond_region(grid, x, y):
    print(x,y)
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return 0

    # no water
    if grid[x][y] != 0:
        return 0

    # this x,y has been checked so mark as visited
    grid[x][y] = -1
    print(x, y)
    print(grid)
    size = 1
    for row in range(x-1, x+2):
        for col in range(y-1, y+2):
            if x != row or y != col:
                size += pond_region(grid, row, col)
                print(size)
    return size 

def find_ponds(grid):
    result = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                result.append(pond_region(grid, i, j))

    return result

if __name__=="__main__":
    grid = [[0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]]
    pond_sizes = find_ponds(grid)
    print ', '.join(map(str, pond_sizes))
M = 8
N = 8
def floodFillUtil(screen, x, y, precC, newC):

    if x <0 or x >= M or y < 0 or y >= N or screen[x][y] != precC or screen[x][y] == newC:
        return
    screen[x][y] = newC
    floodFillUtil(screen, x+1, y, precC, newC)
    floodFillUtil(screen, x, y+1, precC, newC)
    floodFillUtil(screen, x-1, y, precC, newC)
    floodFillUtil(screen, x, y-1, precC, newC)

def floodFill(screen, x, y, newC):
    precC = screen[x][y]
    floodFillUtil(screen, x, y, precC, newC)

screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

newC = 3
x = 4
y = 4
floodFill(screen, x, y, newC)

print ("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end = ' ')
    print()

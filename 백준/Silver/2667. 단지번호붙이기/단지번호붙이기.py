N = int(input())

grid = []
for i in range(N):
    row = input()
    line = []
    for j in range(N):
        line.append(int(row[j]))
    grid.append(line)

visited = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(0)
    visited.append(row)

sizes = []

def dfs(i, j):
    stack = []
    stack.append([i, j])
    count = 0

    while len(stack) > 0:
        cur = stack.pop()
        x = cur[0]
        y = cur[1]

        if visited[x][y] == 1:
            continue

        visited[x][y] = 1
        count += 1

        if x > 0 and grid[x-1][y] == 1 and visited[x-1][y] == 0:
            stack.append([x-1, y])
        if x < N-1 and grid[x+1][y] == 1 and visited[x+1][y] == 0:
            stack.append([x+1, y])
        if y > 0 and grid[x][y-1] == 1 and visited[x][y-1] == 0:
            stack.append([x, y-1])
        if y < N-1 and grid[x][y+1] == 1 and visited[x][y+1] == 0:
            stack.append([x, y+1])

    return count


for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and visited[i][j] == 0:
            size = dfs(i, j)
            sizes.append(size)

sizes.sort()

print(len(sizes))
for i in range(len(sizes)):
    print(sizes[i])
N = int(input())
M = int(input())

x, y = N//2, N//2

lst = []
for i in range(N):
    a = []
    for j in range(N):
        a.append(0)
    lst.append(a)

lst[y][x] = 1

count = 0
num = 1
coords = [1,1]

while True:
    for i in range(1+count):
        if num == M:
            coords = [y+1,x+1]
        num += 1
        y -= 1
        lst[y][x] = num
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        break
    for i in range(1+count):
        if num == M:
            coords = [y+1,x+1]
        num += 1
        x += 1
        lst[y][x] = num
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        break
    for i in range(2+count):
        if num == M:
            coords = [y+1,x+1]
        num += 1
        y += 1
        lst[y][x] = num
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        break
    for i in range(2+count):
        if num == M:
            coords = [y+1,x+1]
        num += 1
        x -= 1
        lst[y][x] = num
        if x == 0 and y == 0:
            break
    count += 2


for i in range(N):
    for j in range(N):
        print(lst[i][j],end=" ")
    print()

print(coords[0], end= " ")
print(coords[1])
Papercount = int(input())
#lst = [ [0] * 100 for _ in range(100) ]
lst = [] 
for i in range(100) : 
  lst.append( [0] * 100 )

for i in range(Papercount):
  paper = list(map(int,input().split()))
  for j in range(10):
    for k in range(10):
      pos1 = paper[0]+j
      pos2 = paper[1]+k
      lst[pos1][pos2] = 1

cnt = 0
for i in range(100):
  for j in range(100):
    cnt += lst[i][j]
print(cnt)
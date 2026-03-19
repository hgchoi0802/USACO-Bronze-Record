r = int(input())
rooms = []
total = 0 
for i in range(r):
  room  = int(input())
  total += room
  rooms.append(room)

mindist = 10**9

for i in range(r):
  dist= 0 
  temp = total - rooms[i] 
  for j in range(i+1,r+i):
    dist += temp
    temp -= rooms[j%r]
    
  mindist = min(dist,mindist)

print(mindist)
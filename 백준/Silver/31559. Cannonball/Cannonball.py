N, S = map(int,input().split())
q = []
v = []
for i in range(N):
  a,b = map(int,input().split())
  q.append(a)
  v.append(b)

pos = S-1
dir = 1
pow = 1
broken = [0]*N
cnt = 0
visited = set()
while True:
  state = (pos,dir,pow)
  if state in visited:
    break
  visited.add(state)
  if q[pos] == 1:
    if broken[pos] == 0 and pow >= v[pos]:
      broken[pos] = 1
      cnt += 1
  else:
    pow += v[pos]
    dir *= -1
  pos = pos + dir*pow
  if pos < 0 or pos >= N:
    break
print(cnt)
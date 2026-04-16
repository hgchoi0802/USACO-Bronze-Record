def check(start,dir) : # left -> dir >> -1 / right -> dir >> +1  
  #이동한 위치 , 지금 내가 있는 위치 
  prev = start 
  r = 1 

  while -1 < prev < N  : #범위를 벗어나지 않을 때까지 
    next = prev 
    while (-1 < next + dir  <N) and (abs(pos[prev] - pos[next + dir])<=r) :  #더 이상 터트릴 수 없을 때까지 
        next += dir 
    if prev == next : 
      break 
    prev = next 
    r += 1 
      
  return  prev #최대로 갈 수 있었던 index 리턴 


N = int(input()) 
pos = sorted([ int(input()) for _ in range(N) ]) 
ans = 0 

for i in range(N) : 
  left = check(i,-1) 
  right = check(i,1) 
  ans = max(ans, right - left + 1 )

print(ans) 
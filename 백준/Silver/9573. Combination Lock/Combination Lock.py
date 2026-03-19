def check(c1,c2) : 
  for i in range(3):
    diff = abs(c1[i] - c2[i])
    if 2 < diff  < N-2 : return False 
  return True 

N = int(input())
lock1 = list(map(int,input().split()))
lock2 = list(map(int,input().split()))

count = 0 

for i in range(1,N+1) : 
  for j in range(1,N+1) : 
    for k in range(1,N+1): 
      if check([i,j,k], lock1) or check([i,j,k], lock2) : 
        count += 1 

print(count) 
N, M = map(int, input().split())
s = input()
a = list(map(int, input().split()))
ans = 0 

for i in range(N) : 
  ans += a[i] 
  if (s[i] == "R" and s[(i+1)%N] == "L") :  # RRRRLLLLL
    total = 0
    j = (i-1+N) % N 
    while s[j] == "R" : 
      total += a[j]
      j = (j-1+N) % N 
    ans -= min(M,total)  
    total = 0
    j = (i+2) % N 
    while s[j] == "L":
      total += a[j]
      j = (j+1) % N
    ans -= min(M,total)
    

print(ans)
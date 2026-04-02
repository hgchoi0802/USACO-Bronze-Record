X,Y = map(int,input().split()) 
ans = 0 

for digit in range(3,18) :  #길이
  for i in range(10): #채울 숫자  #[1,0,0,0,0,0,0,0]
    interesting = [str(i)] * digit #["1","1","2"...]
    #하나 바꿀 숫자 고르기 
    for j in range(digit): 
      for k in range(10):
        if i == k:
          continue
        interesting[j] = str(k)
        if interesting[0] == "0" : 
          continue
        num = int("".join(interesting))
        if num >= X and num <= Y:
          ans += 1
        interesting[j] = str(i)

print(ans)
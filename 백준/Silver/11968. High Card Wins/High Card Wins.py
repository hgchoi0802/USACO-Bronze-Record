#https://www.acmicpc.net/problem/11968 

N = int(input())
count = [0]*2*N
E = []
B = []
for i in range(N):
  card = int(input())
  E.append(card)
  count[card-1] = 1
for i in range(2*N):
  if count[i] == 0:
    B.append(i+1)
    
E.sort() 
i = 0
j = 0
cnt = 0
while i != N:
  if B[i] > E[j]:
    i+= 1
    j+=1
    cnt+=1
  else:
    i+=1
print(cnt)

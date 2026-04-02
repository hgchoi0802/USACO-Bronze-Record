#https://www.acmicpc.net/problem/24981
#한명 기준 
N = int(input())
statements = []
for i in range(N):
  statement = input().split()
  statement[1] = int(statement[1])
  statements.append(statement)

ans = float("inf")

for i in range(N) : 
  pos = statements[i][1]
  cnt = 0
  for j in range(N): 
    if i == j : continue
    if statements[j][0] == "G" and statements[j][1] > pos  : 
      cnt += 1 
    elif statements[j][0] == "L" and statements[j][1] < pos  : 
      cnt += 1 
  ans = min(ans,cnt)

print(ans) 

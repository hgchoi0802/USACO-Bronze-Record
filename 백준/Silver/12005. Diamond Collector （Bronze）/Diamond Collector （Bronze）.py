N,K = map(int,input().split())
dias = []
for i in range(N):
  dias.append(int(input()))
dias.sort()
maxi = -1
for i in range(N):
  cnt = 0
  j = i
  while  j < N and (dias[j]-dias[i])<= K:
    cnt += 1
    j += 1
  maxi = max(cnt,maxi)

print(maxi)
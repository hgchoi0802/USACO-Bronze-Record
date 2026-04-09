T = int(input())
for i in range(T):
  profit = 0
  N = int(input())
  stocks = list(map(int,input().split()))
  maxi = stocks[-1]
  for j in range(N-2, -1, -1):
    if stocks[j] < maxi:
      profit += maxi - stocks[j]
    else:
      maxi = stocks[j]
  print(profit)
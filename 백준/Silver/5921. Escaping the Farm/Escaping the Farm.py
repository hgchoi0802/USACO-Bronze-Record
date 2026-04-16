#https://www.acmicpc.net/problem/5921 
from itertools import combinations
# combinations(리스트, 몇 개)
N = int(input())
cows = []
for i in range(N):
  cow = input()
  cows.append(cow)

for i in range(N):
  for combis in combinations(cows,N-i): 
    digits = [0]*10
    for comb in combis: 
      length = len(comb)
      for k in range(length):
        digits[length-k] += int(comb[k])
    f = True
    for j in range(9):
      if digits[j] >= 10:
        f = False
    if f:
      print(len(combis))
      exit() 
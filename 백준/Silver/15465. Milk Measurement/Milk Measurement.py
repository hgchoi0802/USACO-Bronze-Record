N = int(input())
measures = []
#EMB
cows = [7]*3
top = 7
cnt = 0
for i in range(N):
  measure = input().split()
  measure[0] = int(measure[0])
  measure[2] = int(measure[2])
  measures.append(measure)

measures.sort()

toplst = [True,True,True]


for i in range(N):
  newlst = [False,False,False]
  index = 2
  if measures[i][1] == "Elsie":
    index = 0
  elif measures[i][1] == "Mildred":
    index = 1
  cows[index] += measures[i][2]
  
  if max(cows) > top: 
    top = max(cows)
    for j in range(3):
      if cows[j] == top:
        newlst[j] = True
  else:
    top = max(cows)
    for j in range(3):
      if cows[j] == top:
        newlst[j] = True
  if newlst != toplst:
    cnt += 1
  toplst = newlst
print(cnt)
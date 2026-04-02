barn1 = list(map(int,input().split()))
barn2 = list(map(int,input().split()))
change = set()
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        if (i == k) or (j == l):
          continue
        result = 1000 - barn1[i] + barn2[j] - barn1[k] + barn2[l]
        change.add(result)
for i in range(10):
  for j in range(10):
    result = 1000 - barn1[i] + barn2[j]
    change.add(result)
change.add(1000)

print(len(change))
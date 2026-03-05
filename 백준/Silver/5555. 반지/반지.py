wanted = input()
rings = int(input())
lst= []
cnt = 0
for i in range(rings):
  ring = input()
  ring = ring+ring
  lst.append(ring)
for i in range(rings):
  if wanted in lst[i]:
    cnt += 1
print(cnt)
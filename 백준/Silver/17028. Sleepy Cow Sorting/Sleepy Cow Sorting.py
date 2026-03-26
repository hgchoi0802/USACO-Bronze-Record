N = int(input().strip())
p = list(map(int, input().split()))

i = N - 1

while i > 0 and p[i-1] < p[i]:
    i -= 1

print(i)
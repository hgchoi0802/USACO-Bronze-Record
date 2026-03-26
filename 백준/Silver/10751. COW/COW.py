N = int(input())
s = input()

c_count = 0
co_count = 0
cow_count = 0

for i in range(N):
    if s[i] == 'C':
        c_count += 1
    elif s[i] == 'O':
        co_count += c_count
    elif s[i] == 'W':
        cow_count += co_count

print(cow_count)
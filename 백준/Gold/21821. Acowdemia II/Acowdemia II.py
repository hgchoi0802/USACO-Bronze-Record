K, N = map(int,input().split())
names = input().split()
table = []
for i in range(N):
    table.append(["?"]*N)
    table[i][i] = "B"

for i in range(K):
    paper = input().split()
    index = []

    for j in range(N):
        for k in range(N):
            if paper[j] == names[k]:
                index.append(k)
        
    for j in range(N-1):
        if paper[j] <= paper[j+1]:
            continue
        for k in range(j+1):
            for l in range(j+1,N):
                table[index[k]][index[l]] = "0"
                table[index[l]][index[k]] = "1"


for i in range(N):
    print(*table[i],sep="")

N, M, D, S = map(int, input().split())

p = []
m = []
t = []

for i in range(D):
    a, b, c = map(int, input().split())
    p.append(a)
    m.append(b)
    t.append(c)

sp = []
st = []

for i in range(S):
    a, b = map(int, input().split())
    sp.append(a)
    st.append(b)

ans = 0

for i in range(1, M + 1):

    ok = True

    for j in range(S):

        person = sp[j]
        sick_time = st[j]

        drank = False

        for k in range(D):
            if p[k] == person and m[k] == i and t[k] < sick_time:
                drank = True

        if drank == False:
            ok = False

    if ok:

        used = [0] * (N + 1)

        for j in range(D):
            if m[j] == i:
                used[p[j]] = 1

        cnt = 0
        for j in range(1, N + 1):
            if used[j] == 1:
                cnt += 1

        if cnt > ans:
            ans = cnt

print(ans)
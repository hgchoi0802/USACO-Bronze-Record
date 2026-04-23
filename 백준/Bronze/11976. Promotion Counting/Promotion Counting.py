b1, b2 = map(int,input().split())
s1, s2 = map(int,input().split())
g1, g2 = map(int,input().split())
p1, p2 = map(int,input().split())
gtop = p2-p1
stog = g2-g1+gtop
btos = s2-s1+stog
print(btos)
print(stog)
print(gtop)
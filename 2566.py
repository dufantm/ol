l = []
for i in range(9):
    t = list(map(int,input().split()))
    l.append(t)
m = 0
h = 0
a = 0
for i in range(9):
    for j in range(9):
        if m < l[i][j]:
            m = l[i][j]
            h =i
            a =j
print(m)
print(h,a)
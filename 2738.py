n,m = list(int,input.split())
a,b= [],[]
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    b.append(list(map(int,input().split())))

for j in range(n):
    for i in range(m):
        print(a[j][i]+b[j][i],end=" ")
    print()

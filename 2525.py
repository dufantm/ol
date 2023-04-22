x,y = input().split()
z = int(input())
x = int(x)
y = int(y)
m=x*60+y+z
a = m//60
b = m%60
print(a,b)
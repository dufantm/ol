x,y = input().split()
x = int(x)
y = int(y)
if y>=45:
    y=y-45
elif x==0:
    x=x+23
    y=y+15
else:
    x=x-1
    y=y+15
print(x,y)
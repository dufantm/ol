x,y = input().split()
x = int(x)
y = int(y)
if y>=45:
    y=y-45
else:
    x=x-1
    y=y+15
print(x,y)

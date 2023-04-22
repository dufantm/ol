x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x== y == z:
    print(x*1000+10000)
elif x==y:
    print(x*100+1000)
elif y==z:
    print(y*100+1000)
elif x==z:
    print(z*100+1000)

else:
    print(max(x,y,z)*100)
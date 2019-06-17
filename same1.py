a=int(input())
b=[]
x=''
for i in range(a):
    c=input()
    b.append(c)
for i in range(a-1):
    d=b[i]
    e=b[i+1]
    for y in range(len(min(b,key=len))):
        if d[y]==e[y]:
            x+=d[y]
        else:
            break
    b.pop(i)
    b.insert(0,x)
    x=''
print(b[0])

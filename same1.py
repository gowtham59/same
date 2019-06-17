a1=int(input())
b2=[]
x3=''
for i in range(a1):
    c=input()
    b2.append(c)
for i in range(a1-1):
    d=b2[i]
    e=b2[i+1]
    for y in range(len(min(b2,key=len))):
        if d[y]==e[y]:
            x3+=d[y]
        else:
            break
    b2.pop(i)
    b2.insert(0,x3)
    x3=''
print(b2[0])

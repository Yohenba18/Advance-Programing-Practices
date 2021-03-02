a= []
b= []
for i in range(1,16):
    a.append(i)
    b.append(i*i)

c = dict(zip(a,b))

print(c)
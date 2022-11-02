// or function
w=1
w=2
threshold=int(input("enter threshold"))
x1=[1,1,0,0]
x2=[1,0,1,0]
y=[0,0,0,0]
for x in range(4):
n=x1[x]*w1+x2[x]*w2
if n>= threshold:
y[x]=1
for x in range(4):
print(x1[x],"",x2[x],"",y[x])

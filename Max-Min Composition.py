import numpy as np
# Max-Min Composition
def maxMin(x,y):
  Z=[]
  for x1 in x:
    for y1 in y:
      z.append(max(np.miimum(x1,y1)))
      return np.array(z.reshape(x.shape[0],y.shape[1]))
    #MAx-product composition
    def maxProduct(x,y):
      z=[]
      for x1 in x:
for y1 in y.T:
z.append(max(np.multiply(x1,y1)))
return np.array(z).reshape((x.shape,y.shape[1]))

#3 arrays for the example
r1 = np.array([[1,0,.7],[.3,.2,0],[0,.5,1]])
r2 = np.array([[.6,.6,0],[0,.6,.1],[0,.1,0]])
r3 = np.array([[1,0,.7],[0,1,0],[.7,0,1]])

print("R1oR2=> Max - MIn :\n"+ str(maxMin(r1,r2))+ "\n")
print("R1oR2=> Max product :\n"+ str(maxProduct(r1,r2))+ "\n\n")

print("R1oR3=> Max - MIn :\n"+ str(maxMin(r1,r3))+ "\n")
print("R1oR3=> Max product :\n"+ str(maxProduct(r1,r3))+ "\n\n")

print("R1oR2oR3=> Max - MIn :\n"+ str(maxMin(r1,maxMin(r1,r2)))+ "\n")
print("R1oR2=> Max product :\n"+ str(maxProduct(r1,maxProduct(r1,r2)))+ "\n\n")

# importing python library
import numpy as np
# define unit step funtion
def unitStep(v):
if v>=0:
  return 1
else:
  retrun -1
 # DEfine Preceptron Model1
def preceptron(x,w,b):
  v=np.dot(w,x)+b
  y=unitStep(v)
  return y
# AND Logic function
#w1 =1, w2 =1, b= -1.5
def AND_logicFunction(x):
w= np.array([1,1])
b= -1.5
return perceptronModel(x,w,b)
# testing the perceptron Model
test1 = np.array([-1,1])
test2 = np.array([1,1])
test3 = np.array([-1,-1])
test4 = np.array([1,-1])

print("AND({},{}) = {}".format(-1,1, AND_logicFuntion(test1)))
print("AND({},{}) = {}".format(1,1, AND_logicFuntion(test2)))
print("AND({},{}) = {}".format(-1,-1, AND_logicFuntion(test3)))
print("AND({},{}) = {}".format(1,-1, AND_logicFuntion(test4)))

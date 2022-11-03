#Union operator:
A=dic()
B=dic()
Y=dic()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}
B={"a":0.9,"b":0.9,"c":0.4,"d":0.5}

print('The First Fuzzy set is :', A)
print('The Second Fuzzy set is :', B)

for A_key, B_key in zip(A,B):
A_value =A[A_key]
B_value =B[B_key]

if A_value > B_value:
  Y[A_key]= A_value
  else:
    Y[B_key]=B_value
 print('Fuzzy set union is :',Y)

#Intersection Operator:
A=dic()
B=dic()
Y=dic()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}
B={"a":0.9,"b":0.9,"c":0.4,"d":0.5}

print('The First Fuzzy set is :', A)
print('The Second Fuzzy set is :', B)

for A_key, B_key in zip(A,B):
A_value =A[A_key]
B_value =B[B_key]

if A_value < B_value:
  Y[A_key]= A_value
  else:
    Y[B_key]=B_value
 print('Fuzzy set intersection is :',Y)

#Complement Operator for A
A=dic()
Y=dic()

A={"a":0.2,"b":0.3,"c":0.6,"d":0.6}

print('The Fuzzy set is :', A)

for A_key in A:
Y[A_key]=1-A[A_key]

print('The fuzzy set complement is:'Y)

  

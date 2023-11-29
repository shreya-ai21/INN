import sys
import numpy as np
import matplotlib
import sympy as sym

def sigmoid(x):
  y=1/(1+np.exp(-x))
  return y

inputs=[1,2,3,2.5]
weights=[[0.2,0.8,-0.5,1.0],[0.5,-0.91,0.26,-0.5],[-0.26,-0.27,0.17,0.87]]
bias=[2,3,0.5]

output=[]
sigmoid_op=[]
i=0
while(i<len(weights)):
    ans=0
    for j,k in zip(inputs,weights[i]):
        ans+=j*k
    ans+=bias[i]
    output.append(ans)
    sigmoid_op.append(sigmoid(ans))
    i+=1
print(output)
print(sigmoid_op)


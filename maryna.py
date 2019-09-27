import numpy as np
import scipy.io as sio

A=np.array([[1,2,3],[-2,3,0],[5,1,4]])
print(A)

B=np.array([[1,2,3],[2,4,6],[3,7,2]])
print(B)

'''v=np.array([[-4],[1],[1]])
print(v)

u=np.array([[3],[2],[10]])
print(u)

C=np.random.random((100,100))
print(C)

w=np.random.random((100,1))
print(w)'''

'''print(A+B)
print(A.dot(B))
print(A.dot(A).dot(A))
print(A.dot(B).dot(A))
print(np.dot(v.T,A.T).dot(u+2*v))
print(u.dot(v))
print(C.dot(w)))
print(w.T.dot(C)'''


sum=(A[A>0].sum()+B[B>0].sum())
print(sum)

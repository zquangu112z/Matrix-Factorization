#nhan 2 matrix
import numpy

a = [[2.0,3,1/5],[1/3,1,1/7],[5,7,1]]
a = numpy.array(a, dtype='f')

b = [[2.0,3,1/5],[1/3,1,1/7],[5,7,1]]
b = numpy.array(b,dtype='f')
def multiply(matrix1,matrix2):
	return numpy.dot(matrix1,matrix2)
# print(c)


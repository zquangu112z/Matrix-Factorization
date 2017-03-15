import numpy as np
import numpy.linalg as linalg


a = np.array([[1.0, 0.5, 3],
              [2, 1, 4],
              [0.3333, 0.25, 1]])

# D, V = linalg.eig(a)
# print(D)
# [ 2.  1.  3.]
count = 0
def eigen_value(a):
    # print(++count)
    old_eigen_value = np.array([0.0 , 0, 0])
    while True:
        a = np.dot(a, a)
        print('----', a)

        eigen_value = np.array([0.0 , 0, 0] )

        for i in range(len(a)):
            for j in range(len(a[0])):
                eigen_value[i] += a[i][j]
        print("eigen_value" , eigen_value)
        sum = 0;

        for i in range(len(eigen_value)):
            sum+= eigen_value[i]
        print("sum", sum)
        cnt = False

        for i in range(len(eigen_value)):
            eigen_value[i] = eigen_value[i] / sum
            print(i , eigen_value[i])
            #kiem tra chenh lech
            if(abs((eigen_value[i] - old_eigen_value[i])) > 0.0001):
                cnt = True
            old_eigen_value[i] = eigen_value[i]

        if cnt == False:
            return eigen_value
v = eigen_value(a)

# print(v)



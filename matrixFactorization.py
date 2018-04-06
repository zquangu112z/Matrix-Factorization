'''Tutorial:
http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/
'''
import numpy


def matrix_factorization(R, P, Q, K, steps=4, alpha=0.0002, beta=0.02):

    Q = Q.T

    for step in xrange(steps):

        for i in xrange(len(R)):

            for j in xrange(len(R[i])):

                if R[i][j] > 0:

                    # tich co huong: hang i X cot j
                    eij = R[i][j] - numpy.dot(P[i, :], Q[:, j])

                    for k in xrange(K):  # update

                        P[i][k] = P[i][k] + alpha * \
                            (2 * eij * Q[k][j] - beta * P[i][k])

                        Q[k][j] = Q[k][j] + alpha * \
                            (2 * eij * P[i][k] - beta * Q[k][j])

        # check the overall error, if it's good enough -> break ^^
        # eR = numpy.dot(P,Q)
        # print(eR)

        e = 0

        for i in xrange(len(R)):

            for j in xrange(len(R[i])):

                if R[i][j] > 0:

                    e = e + pow(R[i][j] - numpy.dot(P[i, :], Q[:, j]), 2)

                    for k in xrange(K):

                        e = e + (beta / 2) * \
                            (pow(P[i][k], 2) + pow(Q[k][j], 2))

        if e < 0.001:

            break

    return P, Q.T


R = [
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [1, 0, 0, 4],
    [0, 1, 5, 4]
]
R = numpy.array(R)
N = len(R)
M = len(R[0])
K = 2
P = numpy.random.rand(N, K)
Q = numpy.random.rand(M, K)

nP, nQ = matrix_factorization(R, P, Q, K, 5000)
nR = numpy.dot(nP, nQ.T)
print(nR)

# chua fix bug truong hop 2 doi tuong ko tuong dong nhau


import numpy
from math import sqrt

R = [
    [1.00,4,5,0,3],
    [5,1,0,5,2],
    [4,1,2,5,0],
    [0,3,4,0,4]
]
R = numpy.array(R)

# kich co ma tran R: MxN
M = len(R)
N = len(R[0])

#tinh do tuong dong
SIM = numpy.ndarray((M, M))
for i in xrange(M):
    for j in xrange(i,M):
        tu = 0
        mau1 = 0
        mau2 =0

        # chua fix bug truong hop 2 doi tuong ko tuong dong nhau
        for n in xrange(N):
            if R[i][n] > 0 and R[j][n] >0:
                tu = tu + R[i][n]*R[j][n]
                mau1 = mau1 + pow(R[i][n],2)
                mau2 = mau2 + pow(R[j][n],2)
        SIM[i][j] = SIM[j][i]= tu *1.00/ (sqrt(mau1) * sqrt(mau2) )
print(SIM)

#du doan
def duDoan(R):
    M = len(R)
    N = len(R[0])
    for u in xrange(M):
        for i in xrange(N):
            if R[u][i] == 0:
                rui_tu = 0
                rui_mau = 0
                for u_phay in xrange(M):
                    if u_phay != u:
                        rui_tu = rui_tu + SIM[u, u_phay] * R[u_phay, i]
                        rui_mau = rui_mau + abs(SIM[u, u_phay])
                print(rui_tu / rui_mau)
                R[u][i] = rui_tu / rui_mau
    return R


nR = duDoan(R)
print(nR)

# rui_tu = 0
# rui_mau = 0
# for u_phay in xrange(M):
#     if u_phay != u:
#         rui_tu = rui_tu + SIM[u, u_phay] * R[u_phay, i]
#         rui_mau = rui_mau + abs(SIM[u, u_phay] )
#
# print(rui_tu/rui_mau)











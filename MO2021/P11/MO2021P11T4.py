# coding: utf-8
from sympy import *

def MO2021P11T4():

    N=1000

    print('-------------------(x,y,z,w)=(n1,n1,n2,n2)')
    n0, n1, n2, n3, n4 = symbols('n0 n1 n2 n3 n4', integer=True)

    Sc3 = (6) * summation(summation((n1*n1+n2*n2) - (n1*n2+n1*n2), (n2, n1+1, n0))
                    , (n1, 1, n0-1))
    S0 = factor(Sc3)
    print(S0)
    print("Sc3=", S0.subs([(n0,N)]))

    print('-------------------(x,y,z,w)=(n1,n1,n2,n3),(n1,n2,n2,n3),(n1,n2,n3,n3)')
    Sc4 =  (12) * summation(summation(summation( ((n1*n1+n2*n3) - (n1*n3+n1*n2))
                  + ((n1*n2+n2*n3) - (n1*n3+n2*n2))
                  + ((n1*n2+n3*n3) -(n1*n3+n2*n3)), (n3, n2+1,n0))
                    , (n2, n1+1, n0-1))
                    , (n1, 1, n0-2))
    S0 = factor(Sc4)
    print(S0)
    print("Sc4=", S0.subs([(n0,N)]))


    print('-------------------(x,y,z,w)=(n1,n2,n3,n4)')
    Sc5 =  (24) * summation(summation(summation(summation((n1*n2+n3*n4)- (n1*n4+n2*n3),(n4, n3+1, n0))
                , (n3, n2+1,n0-1))
                , (n2, n1+1, n0-2))
                , (n1, 1, n0-3))
    S0 = factor(Sc5)
    print(S0)
    print("Sc5=", S0.subs([(n0, N)]))

    print('==============================')
    S = factor(Sc3 + Sc4 + Sc5)
    print(S)
    print("S=", S.subs([(n0, N)]))


if __name__ == '__main__':
    MO2021P11T4()

"""
N=10000
-------------------(x,y,z,w)=(n1,n1,n2,n2)
n0**2*(n0 - 1)*(n0 + 1)/2
Sc3= 499999500000
-------------------(x,y,z,w)=(n1,n1,n2,n3),(n1,n2,n2,n3),(n1,n2,n3,n3)
n0*(n0 - 2)*(n0 - 1)*(n0 + 1)*(7*n0 + 4)/10
Sc4= 698998501000800
-------------------(x,y,z,w)=(n1,n2,n3,n4)
n0*(n0 - 3)*(n0 - 2)*(n0 - 1)*(n0 + 1)*(5*n0 + 4)/30
Sc5= 165966834832999200
==============================
n0**2*(n0 - 1)**2*(n0 + 1)**2/6
S= 166666333333500000

"""
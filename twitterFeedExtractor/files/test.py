# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:54:07 2016

@author: Ramanuja
"""
from fractions import Fraction
# your code here
def linearEq(m):
    ans = []
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            try:
                r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            except:
                return [-1,-1]# # N0 Solution, will use rank method later
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    #now backsolve by substitution

    m.reverse() #makes it easier to backsolve
    for sol in range(len(m)):
            if sol == 0:
                try:
                    ans.append(m[sol][-1] / m[sol][-2])
                except:
                    return [-1,-1]# N0 Solution, will use rank method later
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                #the equation is now reduced to ax + b = c form
                #solve with (c - b) / a
                try:
                    ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
                except:
                    return [-1,-1]# N0 Solution, will use rank method later
    ans.reverse()
    isNegative = any(n<0 for n in ans)
    if isNegative:
        ans = [-1,-1]
    return ans
#print linearEq([[7.0,5.0,-3.0,16.0],
#               [3.0,-5.0,2.0,-8.0],
#               [5.0,3.0,-7.0,0.0]])
# input matrix for p*x+q*y+r*z=a will be
#[[p,q,r,a]]
# so for n input matrix will be (n+1)*n
    
def matrix(pegs):
    pegs = map(float,pegs)
    n = len(pegs)
    a = []#eqn matrix
    for i in range(len(pegs)):
        temp = [0.0]*(n+1)
        a.append(temp)
    for i in range(len(pegs)-1):#ignoring the last row
        # variable coefficient assignment
        a[i][i] = 1.0
        a[i][i+1] = 1.0
        #constant term assignment
        a[i][n] = pegs[i+1] - pegs[i]
    a[n-1][0] = 1.0
    a[n-1][n-1] = -2.0
    return a 
      
def location(solution):
    if (solution == [-1,-1]):
        answer = solution
    elif(solution[0]<1):
        answer = [-1,-1]
    else:
       answer = [int(Fraction((solution[0])).limit_denominator()._numerator),int(Fraction((solution[0])).limit_denominator()
._denominator)]
    return answer
#if __name__ == "__main__":
    
    #print matrix([4,30,50])
    #print location(linearEq(matrix([8,60,10])))
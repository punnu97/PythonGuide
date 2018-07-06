'''
Created on Jul 6, 2018
Program to reverse a number
@author: purnima
'''
n = int(input())
d = 0
while n>0 :
    d = d*10+(n%10)
    n = int(n/10)
    
print(d) 
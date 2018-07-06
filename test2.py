'''
Created on Jul 6, 2018
Program to print Average of n numbers
@author: purnima
'''
n = int(input())
i=0 
s=0
for i in range(n):
    x = int(input())
    s+=x 
print(s/n) 
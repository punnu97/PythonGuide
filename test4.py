'''
Created on Jul 6, 2018

@author:     Purnima
Program to print all integers that are not divisible by either 2 or 3 and lies between 1 and 50
'''
i=1 ;
for i in range(51) :
    if i%2!=0 or i%3!=0 :
        print(i)
'''
Created on Jul 7, 2018

@author: purnima
Program to Put Even and Odd elements in a given List into Two Different Lists
'''
n = int(input())
list_even = []
list_odd = [] 
i=0
for i in range(n):
    x = int(input())
    if x%2==0 :
        list_even.append(x)
    else :
        list_odd.append(x)
print("Even list : ",list_even)
print("Odd list :",list_odd)
        
    
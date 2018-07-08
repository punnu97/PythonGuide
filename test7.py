'''
Created on Jul 8, 2018

@author: purnima
Program to Count the Number of Vowels in a String
'''
c=0
i=0
string = input()
for i in string :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
        c=c+1
print("Number of vowels in the string are: ",c)

'''
Created on Jul 8, 2018

@author: purnima
Python Program to Read a List of Words and Return the Longest One
'''
n = int(input())
i=0 
maxi_len=0
maxi_word=""
for i in range(n) :
    word = input()
    if len(word) > maxi_len :
        maxi_len = len(word)
        maxi_word = word
print("Longest word is ",maxi_word," with length of ",maxi_len)
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:35:49 2018

@author: Vishvajeet Singh
"""

def dice():
    print("-----")
    if(num==1):
        print("     ")
        print("  *  ")
        print("     ")
    if(num==2):
        print("     ")
        print("*   *")
        print("     ")
    if(num==3):
        print("*    ")
        print("  * ")
        print("    *")
    if(num==4):
        print("*   *")
        print("     ")
        print("*   *")
    if(num==5):
        print("*   *")
        print("  *  ")
        print("*   *")
    if(num==6):
        print("*   *")
        print("*   *")
        print("*   *")
    print("-----")
from random import randint as r
print("My first Game DIE 1.0\n")
d1 = r(1,6)
num = d1
dice()
d2 = r(1,6)
num = d2 
dice()
a = d1+d2
print("\nyou throw :",a)

d3 = r(1,6)
num = d3
dice()
d4 = r(1,6)
num = d4 
dice()
b = d3+d4
print("\nopponant throw :",b)

if(a==b):
    print("\n****Draw****")
elif(a>b):
    print("\n****You Won****")
else:
    print("\n****opponant Won****")

        
    

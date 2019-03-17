# -*- coding: utf-8 -*-
a=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,0,0,1]]

b=[[1,1,1,1],
   [1,0,0,1],
   [1,1,1,1],
   [1,0,0,1],
   [1,1,1,1]]

c=[[1,1,1,1],
   [1,0,0,0],
   [1,0,0,0],
   [1,0,0,0],
   [1,1,1,1]]

def print_star(word):
    for i in range(len(word)):
        for j in range(len(word[0])):
            if(word[i][j]==1):
                print("*",end='')
            else:
                print(" ",end='')
        print("")
        
        
print_star(a)
print_star(c)
print_star(b)

#!/bin/python3

#code for static input 

import time,sys,subprocess
code=[12,10,15,20,25]
sum=0
for i in code:
    sum=sum+i           
    time.sleep(1)
    print("Element",i,"is added")
print(sum)

#!/bin/python3

#code for dynamic input !! 
#for example :- python3 dynamic.py  10 20 30

import time,sys,subprocess
sum=0

for i in sys.argv[1:]:
    sum=sum+int(i)           
    time.sleep(1)
    print("Element",i,"is added")
print(sum)

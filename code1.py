#!/bin/python3
#calculate even & odd count!!

value=(1,2,3,4,5,6,7,8,9)
print(value)
even=0
odd=0
for x in value:
    if x%2 == 0:
        even+=1
    else:
        odd+=1
print("total number of even : ",even)
print("total number of odd: ",odd) 

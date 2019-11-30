#!/bin/python3

#selection of month which has 30 or 31 days.

x=int(input("Enter the month : "))
if x < 1 or x > 12:
    print("Invalid month selection :")
else:
    if x==2:
        print("Month of Feb : ")
    elif x in (4,6,9,11):
        print("This month is 30 days")
    else:
        print("This month is 31 days")

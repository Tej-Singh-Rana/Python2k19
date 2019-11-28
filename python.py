#!/bin/python3


value=input("What is your value: ")

print(value)

data=input("Enter your exact bid: ")

print(data)

number=input("Enter your last guessing value: ")
print (number)
if value == data:
  print("sucessfully added value")

elif value == number:
    print("Value different from bid: ")
else:
    print("Again try")


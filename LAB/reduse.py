#Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce


def add(num, num2):
    return num+num2

lst=[1,2,3,4,5]

lst2=reduce(add,lst)
print(lst2)
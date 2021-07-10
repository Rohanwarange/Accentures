# # -*- coding: utf-8 -*-
# """
# Created on Sat Jun 26 09:02:43 2021

# @author: ROHAN
# """

# Problem: Write a program in C to display the table of a number and print the sum of all the multiples in it.

# Test Cases:

# Test Case 1:
# Input:
# 5
# Expected Result Value:
# 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
# 275

# Test Case 2:
# Input:
# 12
# Expected Result Value:
# 12, 24, 36, 48, 60, 72, 84, 96, 108, 120
# 660

def summultipke(n):
    total=0
    for i in range(1,11):
        total+=i*n
    return total
print(summultipke(12))

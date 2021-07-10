# # -*- coding: utf-8 -*-
# """
# Created on Sat Jun 26 08:00:55 2021

# @author: ROHAN
# """

# Problem Statement

# You are given a function,

# Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

# The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

# Assumption: String Contains only lower-case alphabetical letters.

# Note:

# Return null if string is null.
# If both characters are not present in string or both of them are same , then return the string unchanged.
# Example:

# Input:
# Str: apples
# ch1:a
# ch2:p
# Output:
# Paales
# Explanation:

# ‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales

def ReplaceCharacter(string,n,char1,char2):
    result=""
    for i in string:
        if i==char1:
            result+=char2
        if i==char2:
            result+=char1
        else:
            result+=i


    return result
string=input()
n=len(string)
char1=input("Enter the char 1 : ")
char2=input("Enter the char 2 : ")

print(ReplaceCharacter(string,n,char1,char2))

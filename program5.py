# # -*- coding: utf-8 -*-
# """
# Created on Fri Jun 25 11:30:20 2021

# @author: ROHAN
# """

# Implement the following functions.a

# char*MoveHyphen(char str[],int n);

# The function accepts a string “str” of length ‘n’, that contains alphabets 
# and hyphens (-). Implement the function to move all hyphens(.) in the string 
# to the front of the given string.

# NOTE:- Return null if str is null.

# Example :-

# Input:
# str.Move-Hyphens-to-Front
# Output:
# -MoveHyphenstoFront
# Explanation:-

# The string “Move-Hyphens -to-front” has 3 hyphens (.), which are moved to
 # the front of the string, this output is “— MoveHyphen”

# Sample Input

# Str: String-Compare
# Sample Output-

# -StringCompare
def MoveHyphen(n,m):
    a=m.count(n)
    return a*n+m.replace(n,"")
m=input()
n="-"
print(MoveHyphen(n, m))          
           
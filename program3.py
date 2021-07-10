# # -*- coding: utf-8 -*-
# """
# Created on Fri Jun 25 09:47:55 2021

# @author: ROHAN
# """

# Implement the following Function

# def ProductSmallestPair(sum, arr)

# The function accepts an integers sum and an integer array arr of size n. Implement the function to find the pair, (arr[j], arr[k]) where j!=k, Such that arr[j] and arr[k] are the least two elements of array (arr[j] + arr[k] <= sum) and return the product of element of this pair

# NOTE

# Return -1 if array is empty or if n<2
# Return 0, if no such pairs found
# All computed values lie within integer range
# Example

# Input

# sum:9

# Arr:5 2 4 3 9 7 1

# Output

# 2

# Explanation

# Pair of least two element is (2, 1) 2 + 1 = 3 < 9, Product of (2, 1) 2*1 = 2. Thus, output is 2

# Sample Input

# sum:4

# Arr:9 8 3 -7 3 9

# Sample Output

# -21
arr=[4,2,4,3,9,7,1]

def ProductSmallestPair(sum,arr):
    if len(arr)<2:
        return 0
    else:
        total=0
        for i in arr:
            for j in arr:
                if i+j<=sum:
                   total+=1
                   p=i*j
    return f"their are {total} sums and product is {p}"
print(ProductSmallestPair(9,arr))           
           
            
        
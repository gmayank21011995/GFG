"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
"""

def funt(l):
    
    n = len(l) + 1
    desired_sum = (n*(n+1))//2
    print(desired_sum)
    
    sum1 = 0
    for i in l:
        sum1 = sum1 + i
    
    print(desired_sum - sum1)
    

funt([1,2,4,6,5])
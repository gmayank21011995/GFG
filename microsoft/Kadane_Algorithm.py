"""
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) 
which has the maximum sum and return its sum.
Example 1:

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
"""

"""def max_sum_cont_arr(l):
    max_sum = -9999
    for i in range(0,len(l)):
        sum1 = l[i]
        for j in range(i+1,len(l)):
            sum1 = sum1 + l[j]
            if max_sum < 0:
                max_sum = 0
            if max_sum < sum1:
                max_sum = sum1
        
        print(max_sum)
    
    print("output : ",max_sum)"""


def max_sum_cont_arr(l):
    max_sum = -9999
    sum1 = 0

    for i in range(0,len(l)):
        sum1 = sum1 + l[i]
        if sum1 > max_sum:
            max_sum = sum1
        
        if sum1 < 0:
            sum1 = 0
        
    print(max_sum)

l = [1,2,3,-2,5]
l = [-2,-3,4,-1,-2,1,5,-3]
l = [-1,-2,-3,-4]

max_sum_cont_arr(l)
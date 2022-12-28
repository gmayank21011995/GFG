"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example 1:
Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
"""

def sort_arr(l):
    # code here
    temp = [0,1,2]
    copy_l = l.copy()
    k = 0
    for i in temp:
        count = 0
        for j in copy_l:
            if i == j:
                count = count + 1
                l[k] = i
                k = k + 1
    print(l)

l = [0, 2, 1, 2, 0]
sort_arr(l)
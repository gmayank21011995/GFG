"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears more than N/2 times
in the array.

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
"""


def funt(l):
    n = len(l)
    d = {}
    for i in l:
        try:
            d[i] = d[i] + 1
        except Exception as e:
            d[i] = 1

    # print(d)

    f = 0
    num = 0
    for i in d:
        if d[i] > n // 2:
            # print(i)
            f = 1
            num = i
            break

    if f == 1:
        print(num)
    else:
        print(-1)


funt([1, 2, 3, 3])

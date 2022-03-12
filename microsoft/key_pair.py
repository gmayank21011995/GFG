"""
Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

Example 1:

Input:
N = 6, X = 16
Arr[] = {1, 4, 45, 6, 10, 8}
Output: Yes
Explanation: Arr[3] + Arr[4] = 6 + 10 = 16

"""


def funt(l, sum1):
    d = {}
    flag = 0
    for i in l:
        temp = sum1 - i
        d[temp] = i

    for i in l:
        try:
            # print(d[i])
            d[i]
            flag = 1
            break
        except Exception as e:
            pass
            # print("handled the excpetion")

    if flag == 1:
        print("number is ", i, d[i])
    else:
        print("no pair found..")


l = [1, 4, 45, 6, 10, 8]
givensum = 499
funt(l, givensum)

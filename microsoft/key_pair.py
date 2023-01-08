"""
Given an array Arr of N positive integers and another number X.
Determine whether or not there exist two elements in Arr whose sum is exactly X.
Example 1:

Input:
N = 6, X = 16
Arr[] = {1, 4, 45, 6, 10, 8}
Output: Yes
Explanation: Arr[3] + Arr[4] = 6 + 10 = 16

"""


def funt(l, sum1):
    """d = {}
    flag = 0
    for i in l:
        temp = sum1 - i
        d[i] = temp
    
    print(d)"""

    hashmap = {}
    for i in range(0, len(l)):
        temp = sum1-l[i]
        print(temp, hashmap)
        if (temp in hashmap):
            print('Yes')
            return
        hashmap[l[i]] = i
    
    print(hashmap)
    print("No")

"""
working, using set time complexity > O(n)
  
hashset = set()
for i in range(0, len(l)):
    temp = sum1 - l[i]
    if temp in hashset:
        print('Yes')
        return
    hashset.add(l[i])
print("No")

"""


l = [1, 4, 45, 6, 8, 8]
givensum = 16
funt(l, givensum)

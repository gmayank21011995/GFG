"""
Given a binary number, Find, if given binary number is a multiple of 3. The given number can be big upto 2^10000. It is recommended to finish the task using one traversal of input binary string.

Example 1:

Input: S = "011"
Output: 1
Explanation: "011" decimal equivalent
is 3, which is divisible by 3.
"""

s = "100100000111111101010010010011010101110110"

j = 0
sum1 = 0
for i in range(len(s)-1,-1,-1):
    #print(s[i])
    if s[i] == '1':
        sum1 = sum1 + 2**j
    
    j = j + 1

#sum1 = str(sum1)
print(sum1)

if sum1 % 3 == 0:
    print("0")
else:
    print("1")
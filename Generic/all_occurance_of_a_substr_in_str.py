# find All occurrences of substring in string

# initializing string
s = "GeeksforGeeks G is best for Geeks"
 
# initializing substring
s1 = "Geeks"

for i in range(len(s)):
    if s.startswith(s1,i):
        print(i)

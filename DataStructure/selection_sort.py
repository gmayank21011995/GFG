"""
pick the min element and swap it with 0th index
do it for remaining unsorted array
n^2 is the complexity
"""
def sele_sort(l):
    print("unsorted", l)

    for i in range(len(l)):
        min1 = min(l[i:])
        min1_index = l.index(min1, i) # l.index(min1, i) you use it when no duplicates r there
        l[i], l [min1_index] = l[min1_index], l[i]
    
    print("sorted", l)

l = [23,2,13,45,17,29]
l = [23,2,13,45,17,29,23,45,13,13,13]
sele_sort(l)
def quick_sort(l):
    if len(l) <= 1:
        return l

    pivot = l[0]
    left = [x for x in l[1:] if x < pivot]
    right = [x for x in l[1:] if x >= pivot]
    print(pivot, left, right)
    return quick_sort(left) + [pivot] + quick_sort(right)

l = [34,2,33,12,1,23,79,33,19,9,8,7,6,5]
print(quick_sort(l))
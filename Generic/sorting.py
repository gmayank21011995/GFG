# bubble sort

def sort_list(l):
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    print(l)

l = [23,3,11,45,33,14]
sort_list(l)
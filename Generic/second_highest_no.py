l = [100000,2,300,400,5,6]

def find_sec_highest(l):

    max1 = 0
    sec_max = 0
    for i in l:
        if max1 < i:
            sec_max = max1
            max1 = i
        else:
            sec_max = max(sec_max, i)
    
    print(max1, sec_max)

find_sec_highest(l)
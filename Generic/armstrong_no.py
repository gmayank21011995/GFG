

def check_armstrong(num):
    num = str(num)
    length = len(num)
    sum1 = 0
    for i in num:
        sum1 = sum1 + (int(i)**length)
    
    print(sum1)
    if sum1 == int(num):
        print("yes")
    else:
        print("no")

num = 16341
check_armstrong(num)
def print_series(n):
    a = 0
    b = 1

    if n < 1:
        print("invalid input")
    
    elif n == 1:
        print(a, end = " ")
    else:
        print(a, end = " ")
        print(b, end = " ")

        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(c, end = " ")

print_series(2)

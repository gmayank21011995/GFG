
def check_prime(num):
    if num >= 1:
        f = 1
        for i in range(2, num//2):
            if num % i == 0:
                f = 0
                print("not a prime no")
                break
        
        if f != 0:
            print("yes it is a prime no")
    
    else:
        print("not prime no")

check_prime(79)
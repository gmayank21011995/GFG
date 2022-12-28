
def check_pallindrome(num):
    num = str(num)
    print(num[::-1])

    if num == num[::-1]:
        print("yess pallindomre")
    else:
        print("no pallindome")

num = 123456789
check_pallindrome(num)
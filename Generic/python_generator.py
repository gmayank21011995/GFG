# https://towardsdatascience.com/6-examples-to-master-python-generators-28f4c614ed45

############################################ ex 1 ############################################

def my_gen(n):
    for i in range(1,n,2):
        yield i**3


for i in my_gen(10):
    print(i)

############################################ ex2 ############################################


my_gen2 = (i**3 for i in range(1,10,2))

for i in my_gen2:
    print(i)


############################################ ex3 ############################################

# using next keyword,
print("using next keyword...")

def my_gen3(n):
    for i in range(1,n):
        yield i*10

obj = my_gen3(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

############################################ ex4 ############################################

# use of iter in python
print("use of iter in python...")

s = "mayank"
obj = iter(s)

print(next(obj))
print(next(obj))
print(next(obj))
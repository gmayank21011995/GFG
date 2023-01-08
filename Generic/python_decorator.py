def decorate(funt):
    # logic to add extra functionality
    def inner():
        print("decorating funt function...")
        funt()
        print("decoration completed...")
    
    return inner

@decorate
def funt():
    print("function without decorator..")

#obj = decorate(funt)
#obj()
funt()

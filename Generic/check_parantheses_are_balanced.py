
def funt(s):
    f = 1
    while True:
        print(s)
        if "{}" in s:
            s = s.replace("{}","")
        elif "()" in s:
            s = s.replace("()","")
        elif "[]" in s:
            s = s.replace("[]","")
        elif s == "":
            return True
        else:
            return False


s = "(()){}{}{[[]]}}"

print(funt(s))

# O(n) is the complexity of replace function.
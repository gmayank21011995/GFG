s = "Geeks"

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
    print("--------")

list_compr = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
print(list_compr)
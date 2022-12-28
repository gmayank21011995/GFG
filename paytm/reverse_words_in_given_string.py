s = "i.like.this.program.very.much"
s = "pqr.mno"

def reverse(s):
    l = s.split(".")
    l1= []
    for i in range(len(l)-1,-1,-1):
        #print(l[i])
        l1.append(l[i])
    
    print(".".join(l1))
    
reverse(s)
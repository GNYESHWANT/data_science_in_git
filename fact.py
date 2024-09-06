def rec(a):
    if(a==0):
        return 1
    else:
        return a*rec(a-1)

def permutation(n,r):
     c= rec(n)/rec(n-r)
     print("permutation of%d,%d is %d"%(n,r,c))
def combination(n,r):
    d=rec(n)
    e=rec(r)*rec(n-r)
    f=d/e
    print("the combination of %d ,%d is %d"%(n,r,f))
b=int(input("1 for factorial\n2 for permutation\n3 for combination"))
if(b==1):
    z=int(input("Enter z value:"))
    print("the factorial of %d is",rec(z)%(z))
elif(b==2):
    s=int(input("enter n value:"))
    t=int(input("enter r value:"))
    permutation(s,t)
elif(b==3):
    s=int(input("enter n value:"))
    t=int(input("enter r value:"))
    combination(s,t)
else:
    print("wrong input")

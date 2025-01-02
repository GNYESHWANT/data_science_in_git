from functools import lru_cache
@lru_cache
def rec(a):
     return 1 if a==0 else a*rec(a-1)
@lru_cache
def permutation(n,r):
     c= rec(n)/rec(n-r)
     print(f"permutation of {n},{r} is {c}")
@lru_cache
def combination(n,r):
    f=rec(n)/(rec(r)*rec(n-r))
    print(f"the combination of {n},{r} is {f}")

b=int(input("1 for factorial\n2 for permutation\n3 for combination\nEnter your choice:"))
if(b==1):
    z=int(input("Enter z value:"))
    print(f"the factorial of {z} is {rec(z)}")
elif(b==2):
    permutation(int(input("enter n value:")),int(input("enter r value:")))
elif(b==3):
    combination(int(input("enter n value:")),int(input("enter r value:")))
else:
    print("wrong input")

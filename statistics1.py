import statistics 
from statistics import*
import math
n=int(input("enter the total no of items in a data set:"))
a=[n]
print("enter elements of list")
for i in range(n):
    c=int(input())
    a.append(c)
b=[n]
print("enter the total no of items in a data set:")
for i in range(n):
   d= int(input())
   b.append(d)
    

def cov(x,y):
    e=statistics.mean(x)
    f=statistics.mean(y)
    n1=0
    for i in x:
        for j in y:
            n=(int(i)-int(e))*(int(j)-int(f))
            n1=n1+n
    return n1/(len(x)-1)
def cor(x,y):
    e=statistics.mean(x)
    f=statistics.mean(y)
    n1=0
    n3=0
    for i in x:
        for j in y:
            n=(int(i)-int(e))**2
            n2=(int(j)-int(f))**2
            n1=n1+n
            n3=n3+n2
    z=math.sqrt(n1)
    w=math.sqrt(n3)
    covar=cov(x,y)/(z*w)
       
print("mean :",statistics.mean(a))
print("median:",statistics.median(a))
print("mode",statistics.mode(a))
print("population standard deviation:",statistics.pstdev(a))
print("sample standard deviation:",statistics.stdev(a))
print("the covariance of the data:",cov(a,b))
print("correlation of data:",cor(a,b))

import statistics as st
from statistics import*
import math
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
b = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
def cov(x,y):
    e=st.mean(x)
    f=st.mean(y)
    n1=0
    for i in x:
        for j in y:
            n=(int(i)-int(e))*(int(j)-int(f))
            n1=n1+n
    return n1/(len(x)-1)
Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage)
percentile10 = np.percentile(Calorie_burnage, 10)
print(percentile10)
print("mean :",st.mean(Calorie_burnage ))
print("median:",st.median(Calorie_burnage ))
print("mode",st.mode(Calorie_burnage ))
print("population standard deviation:",st.pstdev(Calorie_burnage ))
print("sample standard deviation:",st.stdev(Calorie_burnage ))
print("the covariance of the data:",cov(Calorie_burnage ,b))
print("correlation of data:",round(Calorie_burnage.corr(),2))
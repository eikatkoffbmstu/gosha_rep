# ВВЕДЕННАЯ ФУНКЦИЯ
def treug(a,b,c):
    if ((a+b)>c) and ((a+c)>b) and ((c+b)>a):
        return 1
    else:
        return 0
    
def f(x,A):
    return (treug(x,10,20)<=(not(max(x,8)>24))) == (not(treug(3,A,x)))

for A in range(1000):
    if all(f(x,A)==1 for x in range(1000)):
        print(A)
# ПЛОСКОСТИ
for A in range(300,1,-1):
    counter_of_dots=0
    for x in range(0,300):
        for y in range(0,300):
            if ((x<=9)<=(x**2<=A)) and ((y**2<=A) <= ( y<=9)):
                counter_of_dots+=1
    if counter_of_dots==90_000:
        print(A)
        break
# ОТРЕЗКИ 
P = [int(i) for i in range(10,30)]
Q = [int(i) for i in range(30,68)]
A = [int(i) for i in range(10,68)] # A - берется по большему из числовых отрезков

for x in range(1,100):
    if (((x in A)<= (x in P)) or (x in Q))==0:
        A.remove(x)
print(len(A)-1)
# ПОБИТОВАЯ КОНЪЮНКИЦИЯ
for A in range(0,100):
    flag = True
    for x in range(0,100):
        if (((x&52!=0) and (x&36==0))<= (x&A==4))==0:
            flag = False
    if flag==True:
        print(A)
        break

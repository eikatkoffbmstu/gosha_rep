def f(n):
    s=""
    while n>0:
        s+=str(n%3)
        n=n//3
    return s[::-1]
for n in range (999):
    b=f(n)
    if n%2==0:
        b="1"+b+"00"
    if n%2!=0:
        summ=b.count("2")*2
        summ+=b.count("1")
        b= b+ f(summ)
    r = int(b,3)
    if r>168:
        print(n)

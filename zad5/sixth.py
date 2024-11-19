def sixth(n):
    s=''
    while n>0:
        s+=str(n%6)
        n=n//6
    return s[::-1]
print(sixth(36))

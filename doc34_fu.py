def uc(l):
    i=0
    m=0
    m2=0
    while i<len(n):
        if n[i]>m:
            m=n[i]
        if m>n[i]>m2:
            m2=n[i]  
        i=i+1
    print(m,"+",m2,"=",m+m2)
n=[50,40,23,70,56,12,5,10,7]
uc(n)
n=[10, 14, 2, 23, 19]
uc(n)
n=[99, 2, 2, 23, 19]
uc(n)
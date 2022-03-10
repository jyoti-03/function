def expo(num):
    i=0
    l=[]
    while i<=num:
        s=''
        s+="2"+"^"+str(i)
        l.append(s)
        i+=1
    print(l)
n=int(input("Enter number-: "))
expo(n)

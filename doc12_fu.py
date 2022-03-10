def zero(num):
    d=0
    nm=0
    while num>=0:
        d=num%10
        nm=num
        num//=10
        if d>0:
            break
    print(nm)
n=int(input("Enter number-: "))
zero(n)
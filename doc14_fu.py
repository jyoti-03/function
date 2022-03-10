def prime(num):
    i=2
    f=0
    while i<=num:
        if n%i==0:
            f+=1
        i+=1
    if f==1:
        print("prime number",num)
    else:
        print("not prime number",num)
n=int(input("Enter a number-: "))
prime(n)
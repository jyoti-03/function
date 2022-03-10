def miltiples(n):
    i=1
    sum=0
    while i<=n:
        if i%3==0 or i%5==0:
            sum+=i
        i+=1
    print(sum)
num=int(input("enter range number-: "))
miltiples(num)
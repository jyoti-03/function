def perfect(n):
    while n<= 1000:
        i=1
        sum=0
        while i<n:
            if n % i == 0:
                sum+=i
            i+=1
        if sum == n:
            print(n,"perfect number")
        n+=1
num=1
perfect(num)
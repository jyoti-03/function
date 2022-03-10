def multi(limit):
    i=1
    while i<=10:
        print(i,"*",limit,"=",i*limit)
        i+=1
n=int(input("a number for table-: "))
multi(n)
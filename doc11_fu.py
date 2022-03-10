def gr(start,stop,step):
    if start<stop and step>0:
        while start <= stop:
            print(start)
            start+=step
    else:
        print("invalid input")
s1=int(input("Enter start-: "))
s2=int(input("Enter stop-: "))
s3=int(input("Enter step-: "))
gr(s1,s2,s3)
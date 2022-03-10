def max(l):
    i=0
    m=0
    while i<len(l):
        if l[i]>m:
            m=l[i]
        i+=1
    print(m,"big  number")
num=[3,5,7,34,2,89,2,5]
max(num)
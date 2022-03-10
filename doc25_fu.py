def np(l):
    i=0
    nc=0
    pc=0
    while i<len(l):
        if l[i]>0:
            pc+=1
        elif l[i]<0:
            nc+=1
        i+=1
    print("positive",pc)
    print("negative",nc)
li=[2, -7, 5, -64, -14]
np(li)
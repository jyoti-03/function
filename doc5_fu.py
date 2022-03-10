def new(l):
    i=0
    ul=[]
    while i<len(l):
        if l[i] not in ul:
            ul.append(l[i])
        i+=1
    print(ul)
li=[1,2,3,3,3,3,4,5]
new(li)
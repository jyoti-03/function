def new(l):
    i=0
    ul=[]
    while i<len(l):
        if l[i]%2 ==0:
            ul.append(l[i])
        i+=1
    print(ul)
li=[1, 2, 3, 4, 5, 6, 7, 8, 9]
new(li)
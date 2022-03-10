def le(l):
    i=0
    m,s=0,0
    c=0
    b=len(l[i]) 
    while i<len(l):
        if len(l[i])>m:
            m=len(l[i])
            c=i
        if len(l[i])<b:
            b=len(l[i])
            s=i
        i+=1
    print(m,l[c])
    print(b,l[s])
li=[[0,3], [1, 3], [5, 7], [9, 11,12], [13, 15, 17,18]]
le(li)
def stri(l):
    i=0
    while i<len(l):
        if len(l[i])>=2:
            if l[i][0] == l[i][-1]:
                print(l[i])
        i+=1
li=['abc', 'xyz', 'aba', '1221']
stri(li)
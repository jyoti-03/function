def ele(i,e1):
    t=5
    e2=e1
    sl=[]
    el=[]
    while i<=t:
        sl.append(i**2)
        i+=1
    e1=e1-t+1
    while e1<=e2:
        el.append(e1**2)
        e1+=1
    print((sl,el))
s=int(input("enter start number-: "))
e=int(input("enter end number-: "))
ele(s,e)
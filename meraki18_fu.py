def st(st1,st2):
    sl=len(s1)
    sl2=len(s2)
    if sl == sl2:
        print(s1,s2)
    elif sl < sl2:
        print(s2)
    else:
        print(s1)
s1=input("ur name-: ")
s2=input("ur frnd name-: ")
st(s1,s2)
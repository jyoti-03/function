def rev(stri):
    i=len(stri)-1
    sum=""
    while i >= 0:
        sum+=stri[i]
        i-=1
    print(sum)
st="1234abcd"
rev(st)
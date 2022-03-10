def count(ul):
    uc=0
    lc=0
    i=0
    while i<len(ul):
        if ul[i] >= "A" and ul[i] <= "Z":
            uc+=1
        if ul[i] >= "a" and ul[i] <= "z":
            lc+=1
        i+=1
    print("number of uppercase-:",uc)
    print("number of lowercase-:",lc)
st='The quick Brow Fox'
count(st)
def vote(age):
    if age < 18:
        print("not able to voteing")
    elif age >= 18:
        print("able to voteing")
a=int(input("Enter ur age-: "))
vote(a)
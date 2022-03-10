def speed(sp):
    if sp < 70:
        print("speed must be 70")
    elif sp > 70 and sp < 120:
        print("per 5 km")
    elif sp > 120:
        print("license suspended")
km=int(input("Enter speed-: "))
speed(km)
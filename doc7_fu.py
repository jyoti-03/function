def bmi(w,h):
    bmi=w/(h**2)
    print(bmi)
    if bmi < 18.5:
        print("Underweight")
    if bmi >= 18.5 and bmi < 24.9:
        print("Normal")
    if bmi >= 24.9 and bmi < 30:
        print("Overweight")
    if bmi >= 30:
        print("Obese")
we=int(input("Enter ur weight-: "))
he=float(input("Enter ur height(in meter)-: "))
bmi(we,he)

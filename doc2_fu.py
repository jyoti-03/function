def bigno(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print("big",num1)
    if num2 > num1 and num2 > num3:
        print("big",num2)
    if num3 > num1 and num3 > num2:
        print("big",num3)
no1=int(input("Enter 1st number-: "))
no2=int(input("Enter 2nd number-: "))
no3=int(input("Enter 3rd number-: "))
bigno(no1,no2,no3)
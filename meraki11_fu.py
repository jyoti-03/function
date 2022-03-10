def add(num1,num2):
    addnum=num1+num2
    return addnum
def sub(num1,num2):
    subnum=num1-num2
    return subnum
def mult(num1,num2):
    multnum=num1*num2
    return multnum
def div(num1,num2):
    divnum=num1//num2
    return divnum
def cal(num1,num2):
    print("add:",(add(no1,no2)))
    print("subtraction:",(sub(no1,no2)))
    print("multiply:",(mult(no1,no2)))
    print("divide:",(div(no1,no2)))
no1=int(input("Enter 1st number-: "))
no2=int(input("Enter 2nd number-: "))
cal(no1,no2)

#another type

def cal(num1,num2):
    if ope == "add" or ope == "+":
        sum=num1+num2
        return sum
    elif ope == "sub" or ope == "-":
        sub=num1-num2
        return sub
    elif ope == "mult" or ope == "*":
        mult=num1*num2
        return mult
    elif ope == "div" or ope == "/":
        div=num1/num2
        return div
    else:
        p="wrong operater"
        return p
no1=int(input("Enter 1st number-: "))
no2=int(input("Enter 2nd number-: "))
ope=input("Enter operater-: ")
print(cal(no1,no2))
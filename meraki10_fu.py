def cal(num1,num2,opt):
    if opt == "add" or opt == "+":
        print(num1+num2)
    elif opt == "sub" or opt == "-":
        print(num1-num2)
    elif opt == "mult" or opt == "*":
        print(num1*num2)
    elif opt == "div" or opt == "/":
        print(num1/num2)
cal(20,25,"add")
cal(40,3,"sub")
cal(10,4,"mult")
cal(40,4,"div")
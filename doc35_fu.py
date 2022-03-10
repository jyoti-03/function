def age(a):
    if a < 14:
        return "drink toddy"
    if a >= 14 and a < 18:
        return "drink coke"
    if a >= 18 and a < 21:
        return "drink beer"
    if a >= 21:
        return "drink whisky"
ag=int(input("Enter ut age-: "))
print(age(ag))
def add(num1,num2):
    i=0
    while i<len(num_li1):
        if num_li1[i]%2==0 and num_li2[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
num_li1=[2,6,18,10,3,75]
num_li2=[6,19,24,12,3,87]
add(num_li1,num_li2)
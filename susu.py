# a="i am in a navgurkul"
# i=0
# b=a.split()
# while i<len(b):
# 	print(b[i])
# 	i=i+1

def perfect():
    i=1
    sum=0
    while i<n:
        if n%i==0:
            sum+=i
        i+=1
    if sum==n:
        print(n,"perfect number")
n=1
def mane():
    global n
    while n<=500:
        perfect()
        n+=1
mane()
 
# i=1
# def f():
#     global i
#     print("hello",i)
#     i+=1
#     f()
# f()
bn = [1, 0, 0, 1, 1, 0, 1, 1]
sum=0
_i=0
i=len(bn)-1
while i>=0:
	sum+=bn[i]*2**i
	i-=1
	_i+=1
print("decimal",sum)

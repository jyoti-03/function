def fun(l):
	i=0
	b=l[i]
	while i<len(l):
		if l[i]<b:
			b=l[i]
		i+=1
	print(b,"small number")
li=[8, 6, 4, 8, 4, 1, 2, 7]
fun(li)
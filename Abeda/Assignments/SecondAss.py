def multiplyEven(*args):
	total=0
	for i in args:
		if i%2!=1:
			total=total*i
	return total


 

print(multiplyEven(1,2,3,4,5,6,7,8,9,10))
mygen = (x*x for x in range(10))

def createGen():
	for i in range(10):
		yield i*i

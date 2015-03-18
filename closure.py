
# Simple closure example


def counter_add():
	i = {}
	i["count"] = 0 
	def count():
		i["count"] = i["count"] + 1
		return i["count"]
	return count 

def make_printer(msg):
	def printer():
		print msg
	return printer

def main():
	printer = make_printer("FOO!!!")
	printer()

	c = counter_add()
	print c()
	print c()
	print c()
	print c()

if __name__ == "__main__":
	main()




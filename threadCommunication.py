""" How to communicate between threads.
Queue has all the necessary locking structures already implemented.
"""
import threading
import time
import Queue

# signal when to terminate communication
# This could be made any object to stop individual threads
_stopToken = object()

def makeANumber(in_q):
	""" makeANumber
	Generates some number.
	"""
	in_q.put(100)
	in_q.put(_stopToken)

def readSomeNumber(out_q):
	""" readSomeNumber
	Reads the number from the Queue and prints it.
	It then looks for stop token.
	"""
	while True:
		val = out_q.get()
		if val is _stopToken:
			break
		print val
		time.sleep(1)

q = Queue.Queue()

t1 = threading.Thread(target=makeANumber, args=(q,))
t2 = threading.Thread(target=readSomeNumber, args=(q,))

t1.start()
t2.start()

t1.join()
t2.join()





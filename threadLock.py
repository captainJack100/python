""" Thread Lock
How to lock a mutable resource with threading.
"""
import threading
import time

class Counter:
	
	_lock = threading.RLock()

	def __init__(self, value=0):
		self._value = value

	def inc(self, delta=1):
		with Counter._lock:
			self._value += delta

	def dec(self, delta=1):
		with Counter._lock:
			self._value -= delta

c1 = Counter()
c2 = Counter()

t1 = threading.Thread(target=c1.inc, args=())
t2 = threading.Thread(target=c2.dec, args=())

t1.start()
t2.start()

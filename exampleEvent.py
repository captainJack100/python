""" exampleEvent.py
How to use C# style event handler in python. Uses events recipe.
"""

from events import Events

class Counter:
    """ Counter. Add some number to total.
    """
    def __init__(self):
        self.total = 0
        self.events = Events()
    def add(self, x):
        self.total += x
        if (self.total > 10):
            self.threshReached()
    def threshReached(self):
        self.events.on_change(self.total)

    def addCallBack(self, fn):
        self.events.on_change += fn

class Program:
    def __init__(self, valueAmount):
        c = Counter()
        c.addCallBack(self.doSomething)
        c.add(valueAmount)

    def doSomething(self, total):
        print "Function that is called back %s" % total

def main():
    p = Program(100)
    p2 = Program(2)
    
if __name__ == "__main__":
    main()



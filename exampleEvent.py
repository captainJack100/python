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
        self.events.on_change()

class Program:
    def __init__(self):
        c = Counter()
        c.events.on_change += self.doSomething
        c.add(100)

    def doSomething(self):
        print "DO SOMETHING"

def main():
    p = Program()

if __name__ == "__main__":
    main()



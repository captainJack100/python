""" varArgs.py
"""

# list
def print_everything(*args):
    print args
    for count, thing in enumerate(args):
        print '{0}, {1}'.format(count, thing)

# hash
def print_everything2(**kwargs):
    for name, value in kwargs.items():
        print '{0}, {1}'.format(name, value)
    print kwargs

def main():
    print_everything(1,2,3,4)
    print_everything2(apple = 'fruit', cabbage = 'vegetable')

if __name__ == "__main__":
    main()


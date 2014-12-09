from IPython.parallel import Client

def f(x):
    return x * x

def main():
    rc = Client()
    print rc.ids
    
    v = rc[:]
    
    with v.sync_imports():
        import time

    print v.map_sync(f, range(1000000))



if __name__ == "__main__":
    main()

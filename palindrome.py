def palindrome(x):
    x = str(x)
    return len(x) < 2 or (x[0] == x[-1] and palindrome(x[1:-1]))

def main():
    x = "abcdcba"
    y = "asdfasdf"
    print palindrome(x)
    print palindrome(y)

if __name__ == "__main__":
    main()


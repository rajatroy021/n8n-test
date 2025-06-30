def print_fibonacci_up_to_1000():
    a, b = 0, 1
    while a <= 1000:
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    print_fibonacci_up_to_1000()

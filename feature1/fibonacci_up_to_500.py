def fibonacci_up_to_500():
    a, b = 0, 1
    while a <= 500:
        print(a)
        a, b = b, a + b

if __name__ == "__main__":
    fibonacci_up_to_500()
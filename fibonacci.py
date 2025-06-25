def fibonacci_upto(limit):
    a, b = 0, 1
    fib_numbers = []

    while a <= limit:
        fib_numbers.append(a)
        a, b = b, a + b

    return fib_numbers

# Print Fibonacci numbers up to 5000
fib_list = fibonacci_upto(5000)
print(fib_list)

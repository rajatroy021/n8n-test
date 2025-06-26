def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def print_primes_up_to(n):
    """Print all prime numbers up to n."""
    for num in range(1, n+1):
        if is_prime(num):
            print(num)


if __name__ == '__main__':
    print_primes_up_to(100)

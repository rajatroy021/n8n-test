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


def print_primes_up_to(limit):
    """Print all prime numbers from 1 up to a given limit."""
    for number in range(1, limit + 1):
        if is_prime(number):
            print(number)


if __name__ == '__main__':
    print_primes_up_to(100)

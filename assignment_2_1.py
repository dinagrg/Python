def main():
    print("Assignment 2: working with prime numbers, Problem 1")
    print("July 21, 2024")
    print("Dina Gurung")
    print()


import math

def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(math.sqrt(num)) + 1
    for divisor in range(3, max_divisor, 2):
        if num % divisor == 0:
            return False
    return True

def find_nth_prime(n):
    """Find the nth prime number and print progress every 50 primes."""
    primes = []
    candidate = 3
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
            if len(primes) % 50 == 0:
                print(f"{len(primes)} prime numbers found so far.")
        candidate += 2  
    return primes[-1]

def main():
    nth_prime = 450
    result = find_nth_prime(nth_prime)
    print(f"\nThe {nth_prime}th prime number is {result}.")
    print("This program was designed to find the 450th prime number.")

if __name__ == "__main__":
    main()

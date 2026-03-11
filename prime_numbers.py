"""
Prime Number Functions
This module contains functions to work with prime numbers:
- Check if a number is prime
- Find all primes up to n
- Find the first n primes
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    """
    Find all prime numbers up to n using Sieve of Eratosthenes.
    
    Args:
        n: Upper limit (inclusive)
        
    Returns:
        List of all prime numbers up to n
    """
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(n + 1) if sieve[i]]


def first_n_primes(n):
    """
    Find the first n prime numbers.
    
    Args:
        n: Count of primes to find
        
    Returns:
        List of the first n prime numbers
    """
    primes = []
    candidate = 2
    
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    
    return primes


def prime_factors(n):
    """
    Find all prime factors of a number.
    
    Args:
        n: Number to factorize
        
    Returns:
        List of prime factors
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    
    if n > 1:
        factors.append(n)
    
    return factors


if __name__ == "__main__":
    # Example usage
    print("Prime Numbers Examples\n")
    
    # Check if numbers are prime
    print("Check if prime:")
    for num in [10, 17, 25, 37]:
        print(f"  {num} is prime: {is_prime(num)}")
    
    # Find primes up to 30
    print(f"\nPrimes up to 30: {primes_up_to(30)}")
    
    # Find first 10 primes
    print(f"\nFirst 10 primes: {first_n_primes(10)}")
    
    # Prime factorization
    print("\nPrime factors:")
    for num in [24, 60, 100]:
        print(f"  {num} = {' × '.join(map(str, prime_factors(num)))}")

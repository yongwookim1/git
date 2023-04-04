# This function implements the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.
def eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as true.
    prime = [True for i in range(n+1)]
    # Start with the first prime number, 2.
    p = 2
    # Loop through all numbers up to the square root of n.
    while p**2 <= n:
        # If prime[p] is still true, then it is a prime number.
        if prime[p]:
            # Update all multiples of p as not prime.
            for i in range(p**2, n+1, p):
                prime[i] = False
        # Move to the next number.
        p += 1
    # Return all prime numbers up to n.
    return [p for p in range(2, n+1) if prime[p]]


# Test the function with n = 100.
print(eratosthenes(100))

import math

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

pi_digits = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

largest_prime = None
for i in range(len(pi_digits) - 4):
    num = int(pi_digits[i:i+5])
    if isPrime(num) and (largest_prime is None or num > largest_prime):
        largest_prime = num

print("Largest 5-digit prime number in the first 100 digits of Pi:", largest_prime)

#Prime Number Check

# Write a Python program to check whether a given integer is prime. Use a loop and break to stop checking as soon as a divisor is found. Numbers less than 2 must be treated as non-prime.


n = int(input("Enter a number: "))

if n < 2:
    print("Not a prime number")
else:
    i = 2
    is_prime = True

    while i < n:
        if n % i == 0:
            is_prime = False
            break

        i = i + 1

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

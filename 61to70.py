print("61. Armstrong Number\n 62. Strong Number\n 63. Perfect Number\n 64. Sum of Digits\n 65. Binary to Decimal Conversion\n 66. Decimal to Binary Conversion\n 67. Prime Factors of a Number\n 68. Number to Words\n 69. LCM of a Range\n 70. Sieve of Eratosthenes")
question = int(input("Enter the question number: "))
print("\n")

if question == 61:
    # Check if an integer is an Armstrong number. For example, 153 is an Armstrong number (1^3 + 5^3 + 3^3 = 153).
    def armstrong():
        num = int(input("Enter a number: "))
        num_str = str(num)
        sum = 0
        for i in num_str:
            x = int(i) ** len(num_str)
            sum += x
        if sum == num:
            print(num, "is an Armstrong number")
        else:
            print(num, "is not an Armstrong number")

    armstrong()

elif question == 62:
    # Check if an integer is a strong number. A strong number is one whose sum of factorials of digits equals the number (e.g., 145 = 1! + 4! + 5!).
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)

    def strong():
        num = int(input("Enter a number: "))
        num_str = str(num)
        sum = 0
        for i in num_str:
            f = fact(int(i))
            sum += f
        if sum == num:
            print(num, "is a strong number")
        else:
            print(num, "is not a strong number")

    strong()

elif question == 63:
    # Check if an integer is a perfect number. A perfect number equals the sum of its proper divisors (e.g., 6 = 1+2+3).
    def perfect():
        num = int(input("Enter a number: "))
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            print(num, "is a perfect number")
        else:
            print(num, "is not a perfect number")

    perfect()

elif question == 64:
    # Compute the sum of digits of an integer using a loop.
    def summ():
        num = int(input("Enter a number: "))
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        print("Sum of digits is:", sum)

    summ()

elif question == 65:
    # Prompt the user for a binary string and convert it to decimal.
    def binary_to_decimal():
        binary = input("Enter a binary number: ")
        decimal = int(binary, 2)
        print("The decimal equivalent is:", decimal)

    binary_to_decimal()

elif question == 66:
    # Prompt the user for a decimal integer and convert it to binary.
    def decimal_to_binary():
        num = int(input("Enter a decimal number: "))
        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
        print("Binary equivalent is:", binary)

    decimal_to_binary()

elif question == 67:
    # Find all prime factors of a given integer (e.g., 12 -> 2, 2, 3).
    def prime_factors():
        num = int(input("Enter a number: "))
        i = 2
        while num > 1:
            if num % i == 0:
                print(i, end=" ")
                num = num // i
            else:
                i += 1

    prime_factors()

elif question == 68:
    # Convert an integer (e.g., 123) to words (e.g., "one two three").
    def int_to_words():
        num = int(input("Enter a number: "))
        nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        num_str = str(num)
        words = ""
        for i in num_str:
            words += nums[int(i)] + " "
        print(words)

    int_to_words()

elif question == 69:
    # Compute the LCM of all numbers in a given range [1..n]
    def lcm_up_to_n(n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1): 
                if num % i == 0:
                    return False
            return True

        def highest_power(p, n):
            power = p
            while power * p <= n:
                power *= p
            return power

        lcm = 1
        for p in range(2, n + 1):
            if is_prime(p):
                lcm *= highest_power(p, n)
        return lcm

    n = int(input("Enter the number: "))
    print("LCM of numbers from 1 to", n, "is:", lcm_up_to_n(n))

elif question == 70:
    # Implement the Sieve of Eratosthenes to find all prime numbers up to n.
    def sieve_of_eratosthenes(n):
        """
        Find all prime numbers up to n using the Sieve of Eratosthenes.

        Parameters:
            n (int): The upper limit (inclusive) to find primes.

        Returns:
            list: A list of prime numbers up to n.
        """
        if n < 2:
            return []

        prime = [True] * (n + 1)
        prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        primes = [i for i, is_prime in enumerate(prime) if is_prime]
        return primes

    n = int(input("Enter the number: "))
    print(f"Prime numbers up to {n}:", sieve_of_eratosthenes(n))
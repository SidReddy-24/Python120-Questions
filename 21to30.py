print("21.	Create a Simple Calculator (Functions)\n 22.	Power Function\n 23.	Count Characters in a String (Function)\n 24.	Check Prime (Function)\n 25.	Fibonacci Series (Function)\n 26.	GCD of Two Numbers\n 27.	LCM of Two Numbers\n 28.	Factorial (Recursive)\n 29.	Tower of Hanoi\n 30.	Count Occurrences of an Element\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 21:
    # Write four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b). Then prompt the user for two numbers and the operation. Use the corresponding function to output the result.
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")

elif question == 22:
    # Write a function power(base, exponent) that returns base^exponent without using the built-in ** operator (use a loop).
    def power(base, exponent):
        result = 1
        for i in range(1, exponent + 1):
            result = result * base
        return result

    b = int(input("Enter the base value: "))
    e = int(input("Enter the exponential value: "))
    print(power(b, e))

elif question == 23:
    # Write a function that accepts a string and returns the number of characters in it.
    def num_char(s):
        return len(s)

    string = input("Enter a string: ")
    print("Number of characters in the string:", num_char(string))

elif question == 24:
    # Write a function is_prime(n) to check if a number n is prime. Test it with user input.
    def is_prime(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return "Not prime"
            return "Prime"
        else:
            return "Not prime"

    num = int(input("Enter a number: "))
    print(is_prime(num))

elif question == 25:
    # Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.
    def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        else:
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[-1] + fib[-2])
            return fib

    a = int(input("Enter the number of terms: "))
    print(fibonacci(a))

elif question == 26:
    # Write a function gcd(a, b) that computes the greatest common divisor of a and b.
    def gcd(a, b):
        c = []
        d = []

        for i in range(1, a + 1):
            if a % i == 0:
                c.append(i)

        for k in range(1, b + 1):
            if b % k == 0:
                d.append(k)

        common = set(c).intersection(set(d))
        return max(common)

    s = int(input("Enter the first number: "))
    h = int(input("Enter the second number: "))
    print(gcd(s, h))

elif question == 27:
    # Write a function lcm(a, b) that finds the least common multiple of a and b. Hint: lcm(a, b) = abs(a*b)/gcd(a,b).
    def lcm(a, b):
        c = []
        d = []

        for i in range(1, a + 1):
            if a % i ==  0:
                c.append(i)

        for k in range(1, b + 1):
            if b % k == 0:
                d.append(k)

        common = set(c).intersection(set(d))
        x = max(common)

        return abs(a * b) // x  # gcd(a,b)

    s = int(input("Enter the first number: "))
    h = int(input("Enter the second number: "))
    print(lcm(s, h))

elif question == 28:
    # Write a recursive function to compute the factorial of a number.
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    s = int(input("Enter the number: "))
    print(factorial(s))

elif question == 29:
    # Write a recursive function to solve the Tower of Hanoi puzzle for n disks.
    def hanoi(n, source, target, auxiliary):
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        
        # Move n-1 disks from source to auxiliary, so they are out of the way
        hanoi(n - 1, source, auxiliary, target)
        
        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")
        
        # Move the n-1 disks that we left on auxiliary to target
        hanoi(n - 1, auxiliary, target, source)

    # Example usage:
    n = int(input("Enter the number of disks: "))
    hanoi(n, 'A', 'C', 'B')

elif question == 30:
    # Write a function count_occurrences(lst, x) that returns how many times x appears in the list lst.
    def count_occurrences(lst, x):
        return lst.count(x)

    n = int(input("Enter how many elements you want to enter: "))
    l = []
    for i in range(n):
        inp = input("Enter the elements of the list: ")
        l.append(inp)
    f = input("Enter the element to find the number of counts: ")
    if f in l:
        print(count_occurrences(l, f))
    else:
        print("Element not found")
print(" 11.    Largest of Three Numbers\n 12.	Leap Year Checker\n 13.	Multiplication Table\n 14.	Sum of N Natural Numbers\n 15.	Factorial of a Number\n 16.	Number Guessing (While Loop)\n 17.	Count Digits of a Number\n 18.	Reverse a Number (While Loop)\n 19.	Sum of Even and Odd Numbers Separately\n 20.	Palindrome Checker (Integer)\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 11:
    # Input three distinct numbers and print the largest.
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a > b and a > c:
        print(a, "is the largest number")
    elif b > a and b > c:
        print(b, "is the largest number")
    elif c > a and c > b:
        print(c, "is the largest number")
    else:
        print("All numbers are equal")

elif question == 12:
    # Input a year and determine if it’s a leap year.
    year = int(input("Enter the year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

elif question == 13:
    # Input a positive integer and print its multiplication table (e.g., 1 to 10).
    num = int(input("Enter the number: "))
    for i in range(1, 11):
        print(num, "X", i, "=", i * num)

elif question == 14:
    # Input a positive integer n. Calculate the sum of the first n natural numbers.
    n = int(input("Enter the number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("The sum is", sum)

elif question == 15:
    # Input a non-negative integer and compute its factorial.
    num = int(input("Enter the number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial is", fact)

elif question == 16:
    # Generate a random number. Prompt the user to guess until they get it right. Give hints (too high/too low).
    import random

    number_to_guess = random.randint(1, 10)

    while True:
        guess = int(input("Guess the number I'm thinking of within 10: "))
        if guess < number_to_guess:
            print("'I think You are ground to Earth !!'\n", "!! TRY AGAIN !!")
        elif guess > number_to_guess:
            print("'Flying high, come down !!'\n", "!! TRY AGAIN !!")
        else:
            print("!! Congratulations !!")
            break

elif question == 17:
    # Input a positive integer and count how many digits it has.
    num = int(input("Enter the number: "))
    count = 0
    while num != 0:
        count += 1
        num //= 10
    print("Number of digits is", count)

elif question == 18:
    # Input a positive integer and reverse its digits (e.g., 123 -> 321).
    num = int(input("Enter the number: "))
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num //= 10
    print("Reversed number is", rev)

elif question == 19:
    # Input a positive integer n. Sum up all even numbers and all odd numbers from 1 to n separately.
    n = int(input("Enter the number: "))
    even_sum = 0
    odd_sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    print("Sum of even numbers is", even_sum)
    print("Sum of odd numbers is", odd_sum)

elif question == 20:
    # Input a positive integer and check if it’s a palindrome (same forwards and backwards).
    num = int(input("Enter the number: "))
    nstr = str(num)
    rev_str = nstr[::-1]
    if nstr == rev_str:
        print("Number is a palindrome")
    else:
        print("Number is not a palindrome")
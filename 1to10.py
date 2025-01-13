print(" 1. Print “Hello, World!”\n 2. Variables and Data Types\n 3. Arithmetic Operations\n 4. Convert Celsius to Fahrenheit\n 5. Swap Two Variables\n 6. Even or Odd\n 7. Check Vowel or Consonant\n 8. Square, Cube, and Square Root\n 9. Area of Circle\n 10. Simple Interest Calculation")
question = int(input("Enter the question number: "))
print("\n")

if question == 1:
    # Print “Hello, World!”
    print("Hello, World!")

elif question == 2:
    # Prompt the user for their name and age. Print them in a sentence (e.g., "Your name is ... and your age is ...").
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print("Your name is", name, "and your age is", age)

elif question == 3:
    # Prompt for two numbers. Compute and display the sum, difference, product, division, and modulus of those two numbers.
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Sum is", a + b)
    print("Difference is", a - b)
    print("Product is", a * b)
    print("Division is", a / b)
    print("Modulus (remainder) is", a % b)

elif question == 4:
    # Take a temperature in Celsius (input from the user) and convert it to Fahrenheit.
    temp = float(input("Enter the temperature in Celsius: "))
    fahren = (temp * 9 / 5) + 32
    print("Temperature in Fahrenheit is", fahren)

elif question == 5:
    # Prompt for two variables and swap their values. Show the results before and after swapping.
    n = input("Enter the first value: ")
    m = input("Enter the second value: ")
    print("Before swapping, first value is", n, "and second value is", m)
    n, m = m, n
    print("After swapping, first value is", n, "and second value is", m)

elif question == 6:
    # Ask the user for a number and determine if it is even or odd.
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif question == 7:
    # Input a letter from the user and check if it’s a vowel or a consonant.
    ch = input("Enter the character: ")
    if ch in 'aeiouAEIOU':
        print("Vowel")
    else:
        print("Consonant")

elif question == 8:
    # Input a number and display its square, cube, and square root.
    num = int(input("Enter the number: "))
    print("Square of number is", num ** 2)
    print("Cube of number is", num ** 3)
    print("Square root of number is", num ** 0.5)

elif question == 9:
    # Input the radius of a circle and compute its area. Use π = 3.14159.
    r = float(input("Enter the radius of the circle: "))
    pi = 3.14159
    area = pi * r ** 2
    print("Area of circle is", area)

elif question == 10:
    # Input principal, rate, and time. Compute the simple interest as SI = (principal * rate * time) / 100.
    p = int(input("Enter the principal amount: "))
    r = int(input("Enter the rate: "))
    t = int(input("Enter the time in years: "))
    si = (p * r * t) / 100
    print("Simple interest is", si)

else:
    # If the user enters any other number, display an error message.
    print("Invalid choice")
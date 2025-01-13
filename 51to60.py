print("51. Reverse a String\n52. Palindrome String Checker\n53. Count Vowels\n54. Check Anagram\n55. Remove Spaces\n56. Longest Word in a Sentence\n57. String Case Conversion\n58. Capitalize Every Word\n59. Count Special Characters\n60. Character Frequency in String\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 51:
    # Reverse a String
    def reverse_string():
        string = input("Please enter a string: ")
        rev = string[::-1]
        print("Reversed string: ", rev)
        return rev

    reverse_string()

elif question == 52:
    # Palindrome String Checker
    def palindrome_checker():
        string = input("Please enter a string: ")
        string = string.lower()
        if string == string[::-1]:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
        return string

    palindrome_checker()

elif question == 53:
    # Count Vowels
    def count_vowels():
        string = input("Please enter a string: ")
        count = 0
        for char in string:
            if char.lower() in 'aeiou':
                count += 1
        print("Number of vowels: ", count)
        return count

    count_vowels()

elif question == 54:
    # Check Anagram
    def check_anagram():
        string1 = input("Please enter the first string: ")
        string2 = input("Please enter the second string: ")
        if len(string1) == len(string2):
            if sorted(string1) == sorted(string2):
                print("The strings are anagrams.")
            else:
                print("The strings are not anagrams.")
        else:
            print("The strings are not anagrams.")

    check_anagram()

elif question == 55:
    # Remove Spaces
    def remove_spaces():
        string = input("Please enter a string: ")
        no_space = string.replace(" ", "")
        print("String without spaces: ", no_space)

    remove_spaces()

elif question == 56:
    # Longest Word in a Sentence
    def longest_word():
        sentence = input("Please enter a sentence: ")
        words = sentence.split()
        longest_word = max(words, key=len)
        print("The longest word is: ", longest_word)

    longest_word()

elif question == 57:
    # String Case Conversion
    def string_case_conversion():
        string = input("Please enter a string: ")
        print("Uppercase: ", string.upper())
        print("Lowercase: ", string.lower())
        print("Title case: ", string.title())

    string_case_conversion()

elif question == 58:
    # Capitalize Every Word
    def capitalize_words():
        string = input("Please enter a string: ")
        print("Title case: ", string.title())

    capitalize_words()

elif question == 59:
    # Count Special Characters
    def count_special_characters():
        string = input("Please enter a string: ")
        count = 0
        for char in string:
            if not char.isalnum() and not char.isspace():
                count += 1
        print("Number of special characters: ", count)

    count_special_characters()

elif question == 60:
    # Character Frequency in String
    def character_frequency():
        string = input("Please enter a string: ")
        char_dict = {}
        for char in string:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        for char, count in char_dict.items():
            print(f"Character count of '{char}' is: {count}")

    character_frequency()

else:
    print("Invalid question number.")
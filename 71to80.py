print(" 71. Write to File\n72. Read from File\n73. Copy File\n74. Count Lines in a File\n75. Count Words in a File\n76. Find Longest Line in a File\n77. Search for a Word in a File\n78. Append to a File\n79. Remove Blank Lines\n80. File Statistics\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 71:
    # Prompt the user for a string and write it to a text file named "output.txt".
    inp = input("Please enter a string: ")
    with open("output.txt", "w+") as file:
        file.write(inp)
        print("The string has been written to 'output.txt'.")

elif question == 72:
    # Read the content of "output.txt" and print it to the console.
    with open("output.txt", "r") as file:
        print(file.read())
        print("The content has been printed.")

elif question == 73:
    # Copy the contents of one text file to another. Handle exceptions if the source file does not exist.
    try:
        with open("source.txt", "r+") as source_file:
            with open("destination.txt", "w+") as destination_file:
                destination_file.write(source_file.read())
                print("The content has been copied.")
    except FileNotFoundError:
        print("The source file does not exist.")
    finally:
        print("The operation is complete.")

elif question == 74:
    # Read a text file and count how many lines it contains.
    with open("output.txt", "r") as file:
        lines = file.readlines()
        print(f"The file contains {len(lines)} lines.")
    print("The operation is complete.")

elif question == 75:
    # Read a text file and count how many words it contains.
    with open("output.txt", "r") as file:
        content = file.read()
        words = content.split()
        print(f"The file contains {len(words)} word(s).")
    print("The operation is complete.")

elif question == 76:
    # Find and print the longest line in a given text file.
    with open("output.txt", "r") as file:
        lines = file.readlines()
        longest_line = max(lines, key=len)
        print(f"The longest line is: {longest_line}")
    print("The operation is complete.")

elif question == 77:
    # Prompt the user for a word and search for it in a file. Return the line number(s) where it appears.
    inp = input("Please enter a word: ")
    with open("output.txt", "r") as file:
        lines = file.readlines()
        line_numbers = [i+1 for i, line in enumerate(lines) if inp in line.strip()]
    if line_numbers:
        print(f"The word '{inp}' appears in the following line(s): {line_numbers}")
    else:
        print(f"The word '{inp}' does not appear in the file.")

elif question == 78:
    # Prompt the user for some text and append it to "output.txt" without overwriting existing content.
    with open("output.txt", "a+") as file:
        inp = input("Please enter some text: ")
        file.write(inp + "\n")
    print("The operation is complete.")

elif question == 79:
    # Read a text file and write its content to a new file, omitting any blank lines.
    with open("output.txt", "r+") as source_file:
        with open("output2.txt", "w+") as destination_file:
            for line in source_file:
                if line.strip():
                    destination_file.write(line)
    print("The operation is complete.")

elif question == 80:
    # Display file statistics such as total characters, total lines, total words, etc.
    with open("output.txt", "r") as file:
        content = file.read()
        total_chars = len(content)
        total_lines = len(content.split("\n"))
        total_words = len(content.split())
        print(f"File statistics:")
        print(f"Total characters: {total_chars}")
        print(f"Total lines: {total_lines}")
        print(f"Total words: {total_words}")
    print("The operation is complete.")

else:
    print("Invalid question number.")
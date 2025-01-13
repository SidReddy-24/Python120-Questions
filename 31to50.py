print("31. List Operations\n 32. Maximum and Minimum in a List\n 33. Second Largest Element\n 34. Sum and Average of a List\n 35. Count Positive, Negative, Zero\n 36. Remove Duplicates from a List\n 37. Concatenate Two Lists\n 38. List Reversal\n 39. Find Common Elements of Two Lists\n 40. Element-wise Sum of Two Lists\n 41. Tuple Creation and Access\n 42. Tuple to List\n 43. Check if Element Exists in Tuple\n 44. Dictionary: Word Count\n 45. Dictionary: Student Grades\n 46. Dictionary: Keys and Values\n 47. Merge Two Dictionaries\n 48. Invert Dictionary\n 49. Set Operations\n 50. Set Membership Testing\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 31:
    # Create a list of integers. Perform append, insert, remove, pop, and display the list at each stage.
    def operations():
        inp = int(input("Enter the number of elements you want to enter in the list: "))
        lst = []
        for i in range(inp):
            inp1 = input("Enter the element: ")
            lst.append(inp1)

        print("What to Perform\n 1. Append\n 2. Insert\n 3. Remove\n 4. Pop\n 5. Display\n 6. Exit")

        while True:
            inp2 = input("Enter your choice: ")
            if inp2 == "1":
                inp3 = input("Enter the element you want to append: ")
                lst.append(inp3)
                print(lst)

            elif inp2 == "2":
                inp3 = input("Enter the element you want to insert: ")
                inp4 = int(input("Enter the position where you want to insert: "))
                lst.insert(inp4, inp3)
                print(lst)

            elif inp2 == "3":
                inp3 = input("Enter the element you want to remove: ")
                if inp3 in lst:
                    lst.remove(inp3)
                    print(lst)
                else:
                    print("Element not found\n")

            elif inp2 == "4":
                inp3 = int(input("Enter the position from where you want to pop: "))
                if inp3 <= len(lst):
                    lst.pop(inp3 - 1)
                    print(lst)
                else:
                    print("Position out of range\n")

            elif inp2 == "5":
                print("The list is: ", lst)

            elif inp2 == "6":
                print("Exiting the program...!! Thank You !!\n")
                break

            else:
                print("INVALID CHOICE...TRY AGAIN...\n")

    operations()

elif question == 32:
    # Take a list of numbers from the user and find the maximum and minimum values.
    def max_min():
        lst = []
        n = int(input("Enter the length of the list: "))
        for i in range(n):
            inp = int(input("Enter the element you want to add: "))
            lst.append(inp)
        print("The list is: ", lst)
        print("The maximum value is: ", max(lst))
        print("The minimum value is: ", min(lst))

    max_min()

elif question == 33:
    # In a list of unique integers, find the second largest element.
    def sec_large():
        lst = []
        n = int(input("Enter the length of the list: "))
        for i in range(n):
            inp = int(input("Enter the element you want to add: "))
            lst.append(inp)
        print("The list is: ", lst)
        lst.sort()
        if len(lst) > 1:
            print("The second largest element is: ", lst[-2])

    sec_large()

elif question == 34:
    # Prompt the user for a list of numbers. Calculate and print the sum and average.
    def sum_avg():
        lst = []
        n = int(input("Enter the total number of the numbers: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst.append(inp)
        print("\nThe numbers you entered are: ", lst)
        print("The sum of the numbers is: ", sum(lst))
        print("The average of the numbers is: ", sum(lst) / n)

    sum_avg()

elif question == 35:
    # In a list of integers, count how many are positive, negative, or zero.
    def count():
        lst = []
        n = int(input("Enter the total number of the numbers: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst.append (inp)
        print("\nThe numbers you entered are: ", lst)
        print("The number of positive numbers is: ", len([i for i in lst if i > 0]))
        print("The number of negative numbers is: ", len([i for i in lst if i < 0]))
        print("The number of zeros is: ", len([i for i in lst if i == 0]))

    count()

elif question == 36:
    # Prompt for a list of integers (possibly with duplicates). Create a new list with duplicates removed.
    def dup():
        lst = []
        n = int(input("Enter the total number of the numbers: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst.append(inp)
        s = list(set(lst))
        print("\nThe elements after the removal of the duplicates are: ", s)

    dup()

elif question == 37:
    # Input two lists from the user and concatenate them.
    def concat():
        lst1 = []
        n = int(input("Enter the total number of the numbers in the first list: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst1.append(inp)
        lst2 = []
        m = int(input("Enter the total number of the numbers in the second list: "))
        for j in range(m):
            inp = int(input("Enter the number: "))
            lst2.append(inp)
        print("\nThe first list is: ", lst1)
        print("The second list is: ", lst2)
        print("The concatenated list is: ", lst1 + lst2)

    concat()

elif question == 38:
    # Write a function to reverse a given list in place.
    def rev():
        lst = []
        n = int(input("Enter the total number of the numbers: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst.append(inp)
        print("\nThe list you entered is: ", lst)
        lst.reverse()
        print("The reversed list is: ", lst)

    rev()

elif question == 39:
    # Given two lists, find the common elements and store them in a new list.
    def common():
        lst1 = []
        n = int(input("Enter the total number of the numbers in the first list: "))
        for i in range(n):
            inp = int(input("Enter the number: "))
            lst1.append(inp)
        lst2 = []
        m = int(input("Enter the total number of the numbers in the second list: "))
        for j in range(m):
            inp = int(input("Enter the number: "))
            lst2.append(inp)
        print("\nThe first list is: ", lst1)
        print("The second list is: ", lst2)
        common_lst = [i for i in lst1 if i in lst2]
        print("The common elements are: ", common_lst)

    common()

elif question == 40:
    # Given two lists of equal length, create a third list that stores the element-wise sum.
    def sum_list():
        lst1 = []
        n = int(input("Enter the total number of the elements in the list: "))
        for i in range(n):
            inp = int(input("Enter the element for list 1: "))
            lst1.append(inp)
        lst2 = []
        for j in range(n):
            inp = int(input("Enter the element for list 2: "))
            lst2.append(inp)
        print("\nThe first list is: ", lst1)
        print("The second list is: ", lst2)
        sum_lst = [lst1[i] + lst2[i] for i in range(n)]
        print("The final sum list is: ", sum_lst)

    sum_list()

elif question == 41:
    # Create a tuple of strings. Prompt the user for an index and print the element at that index.
    def tup():
        mytup = []
        r = int(input("Enter the range of the tuple: "))
        for i in range(r):
            inp = input("Enter the element: ")
            mytup.append(inp)
        t = tuple(mytup)
        ind = int(input("Enter the index value: "))
        print("The element at the index ", ind, " is: ", t[ind - 1])

    tup()

elif question == 42:
    # Convert a user-defined tuple to a list, modify it, and convert it back to a tuple.
    def tup_list():
        mytup = []
        r = int(input("Enter the range of the tuple: "))
        for i in range(r):
            inp = input("Enter the element: ")
            mytup.append (inp)
        print("The original list is: ", mytup)
        t = tuple(mytup)
        print("After the list to tuple conversion: ", t)
        mytup[0] = "Modified"
        t = tuple(mytup)
        print("After modifying and converting back to tuple: ", t)

    tup_list()

elif question == 43:
    # Prompt the user for an element and check if it exists in the tuple.
    def tup_check():
        mytup = []
        r = int(input("Enter the range of the tuple: "))
        for i in range(r):
            inp = input("Enter the element: ")
            mytup.append(inp)
        t = tuple(mytup)
        ele = input("Enter the element to check: ")
        if ele in t:
            print("The element is present in the tuple.")
        else:
            print("The element is not present in the tuple.")

    tup_check()

elif question == 44:
    # Prompt the user for a string and build a dictionary that counts how many times each word appears.
    def word_count():
        s = input("Enter the string: ")
        s = s.upper()
        words = s.split()
        dictt = {}
        for word in words:
            word = word.strip('.,!?"\'')
            dictt[word] = dictt.get(word, 0) + 1
        for word, count in dictt.items():
            print(f"{word}: {count}")

    word_count()

elif question == 45:
    # Create a dictionary with student names as keys and their grades as values. Prompt the user for a name and display the grade.
    def student_grade():
        dictt = {
            "Shiva": 90,
            "Sid": 85,
            "Vijay": 95,
            "Sahil": 80,
            "Swaraj": 92
        }
        name = input("Enter the student name: ")
        if name in dictt:
            print(f"{name}'s grade is: {dictt[name]}")
        else:
            print("Student not found.")

    student_grade()

elif question == 46:
    # Create a dictionary and then print just its keys and just its values separately.
    def key_value():
        dictt = {
            "Shiva": 90,
            "Sid": 85,
            "Vijay": 95,
            "Sahil": 80,
            "Swaraj": 92
        }
        print("Keys: ", dictt.keys())
        print("Values: ", dictt.values())

    key_value()

elif question == 47:
    # Given two dictionaries, merge them into a new dictionary.
    def merge():
        dict1 = {
            "Shiva": 90,
            "Sid": 85,
            "Vijay": 95
        }
        dict2 = {
            "Sahil": 80,
            "Swaraj": 92,
            "Sarthak": 82
        }
        dict3 = {**dict1, **dict2}
        print("Merged Dictionary: ", dict3)

    merge()

elif question == 48:
    # Given a dictionary {key: value}, swap keys and values if all values are unique (produce {value: key}).
    def swap():
        dictt = {
            "Shiva": 90,
            "Sid": 85,
            "Vijay": 95,
            "Sahil": 80,
            "Swaraj": 92
        }
        if len(dictt.values()) == len(set(dictt.values())):
            dictt = {v: k for k, v in dictt.items()}
            print("Swapped Dictionary: ", dictt)
        else:
            print("Values are not unique.")

    swap()

elif question == 49:
    # Prompt the user for two lists, convert them to sets, and then display the union, intersection, and difference of these sets.
    def set_operations():
        mytup = []
        mytup2 = []
        r = int(input("Enter the range of the list 1: "))
        for i in range(r):
            list1 = input("Enter the elements for first list: ")
            mytup.append(list1)

        r2 = int(input("Enter the range of the list 2: "))
        for i in range(r2):
            list2 = input("Enter the elements for second list: ")
            mytup2.append(list2)

        set1 = set(mytup)
        set2 = set(mytup2)

        print("Union: ", set1.union(set2))
        print("Intersection: ", set1.intersection(set2))
        print("Difference: ", set1.difference(set2))

    set_operations()

elif question == 50:
    # Given a set of names, prompt the user for a name. Check if it is in the set or not.
    def check():
        n = int(input("Enter how many names you want to enter: "))
        myset = set()
        for i in range(n):
            name = input("Enter the name: ")
            myset.add(name)
        m = input("Enter the element to be checked: ")
        if m in myset:
            print("The element exists in the set.")
        else:
            print("The element does not exist.")

    check()
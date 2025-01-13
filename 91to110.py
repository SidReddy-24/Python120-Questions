print("91.	Bubble Sort\n 92.	Insertion Sort\n 93.	Selection Sort\n 94.	Merge Sort\n 95.	Quick Sort\n 96.	Binary Search\n 97.	Linear Search\n 98.	Knuth Shuffle (Fisher-Yates Shuffle)\n 99.	Matrix Addition\n 100.	Matrix Multiplication\n 101.	Transposition of a Matrix\n 102.	Check if a Matrix is Symmetric\n 103.	Longest Common Substring\n 104.	Longest Common Subsequence (LCS)\n 105.	Coin Change (Greedy)\n 106.	Coin Change (DP)\n 107.	Knapsack Problem (0/1 DP)\n 108.	Permutations of a List\n 109.	Backtracking: N-Queens\n 110.	Shortest Path in a Grid\n")
question = int(input("Enter the question number: "))
print("\n")

if question == 91:
# Implement bubble sort to sort a list of integers.
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    # Test the function
    print(bubble_sort([64, 34, 25, 12, 22,11, 90, 43, 65, 76]))

elif question == 92:
# Implement insertion sort to sort a list of integers.
    def insertion_sort(arr):
        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):
            key = arr[i]
            # Move elements of arr[0..i-1], that are greater than key,
            # to one position ahead of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    # Test the function
    print(insertion_sort([64, 34, 25, 12, 22,11, 90, 43, 65, 76]))

elif question == 93:
# Implement selection sort to sort a list of integers.
    def selection_sort(arr):
    # Traverse through all elements in the array
        for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
        # Swap the found minimum element with the first element
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    # Test the function
    print(selection_sort([64, 34, 25, 12, 22,11,90, 43, 65, 76]))

elif question == 94:
# Implement merge sort to sort a list of integers.
    def merge_sort(arr):
        if len(arr) > 1:
            # Find the middle point and divide the array into two halves
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursively sort both halves
            merge_sort(left_half)
            merge_sort(right_half)

            # Merge the sorted halves
            i = j = k = 0

            # Copy data to temp arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            # Check if any element was left in left_half
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            # Check if any element was left in right_half
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr
    # Test the function
    print(merge_sort([64, 34, 25, 12, 22,11,90, 43, 65, 76]))

elif question == 95:
# Implement quick sort to sort a list of integers.
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            # Choose a pivot element (here we choose the last element)
            pivot = arr[-1]
            # Partition the array into three parts:
            # 1. Elements less than the pivot
            # 2. Elements equal to the pivot
            # 3. Elements greater than the pivot
            less = [x for x in arr[:-1] if x <= pivot]
            greater = [x for x in arr[:-1] if x > pivot]
            # Recursively apply quick sort to the 'less' and 'greater' lists
            return quick_sort(less) + [pivot] + quick_sort(greater)
    # Test the function
    print(quick_sort([64, 34, 25, 12, 22,11,90, 43, 65, 76]))

elif question == 96:
# Implement binary search on a sorted list to find a given element.
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            # Check if the target is present at mid
            if arr[mid] == target:
                return mid
            # If target is greater, ignore the left half
            elif arr[mid] < target:
                low = mid + 1
            # If target is smaller, ignore the right half
            else:
                high = mid - 1
     # Target is not present in the array
        return -1
        # Test the function
    arr = [2, 5, 8, 12, 16, 23,38, 56, 72, 91]
    target = 23
    result = binary_search(arr, target)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

elif question == 97:
# implement linear search to find an element in a list.
    def linear_search(arr, target):
    # Traverse through all elements in the array
        for i in range(len(arr)):
        # Check if the current element matches the target
            if arr[i] == target:
                return i
    # Target is not present in the array
        return -1
    # Test the function
    arr = [2, 5, 8, 12, 16, 23,38, 56, 72, 91]
    target = 23
    result = linear_search(arr, target)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")

elif question == 98:
# Given a list, shuffle its elements in place uniformly.
    import random
    def shuffle_list(arr):
    # Traverse the list from the end to the beginning
        for i in range(len(arr) - 1, 0, -1):
        # Pick a random index from 0 to i
            j = random.randint(0, i)
        # Swap arr[i] with the element at random index j
            arr[i], arr[j] = arr[j], arr[i]
        return arr
# Test the function# Example list of integers
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Shuffle the list
    shuffled_arr = shuffle_list(arr)
# Output the shuffled list
    print("Shuffled array:", shuffled_arr)

elif question == 99:
# Prompt the user for two matrices (2D lists) of the same dimensions and compute their sum.
    def get_matrix(name, rows, cols):
        print(f"Enter the elements of {name} row by row, with {cols} numbers in each row.")
        matrix = []
        for i in range(rows):
            while True:
                row = input(f"{name} - Enter row {i + 1}: ").strip()
                elements = list(map(int, row.split()))
                if len(elements) == cols:
                    matrix.append(elements)
                    break
                else:
                    print(f"Please enter exactly {cols} numbers.")
        return matrix

    def add_matrices(matrix1, matrix2):
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    def main():
        print("Matrix Addition Program")
    
    # Ask for fixed dimensions
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
    
        print("\nInput Matrix 1:")
        matrix1 = get_matrix("Matrix 1", rows, cols)
    
        print("\nInput Matrix 2:")
        matrix2 = get_matrix("Matrix 2", rows, cols)
    
    # Compute the sum
        print("\nSum of Matrices:")
        result = add_matrices(matrix1, matrix2)
        for row in result:
            print(row)

    if __name__ == "__main__":
        main()

elif question == 100:
# Prompt the user for two matrices and multiply them if their dimensions are compatible.
    def get_matrix(name, rows, cols):
        print(f"Enter the elements of {name} row by row, with {cols} numbers in each row.")
        matrix = []
        for i in range(rows):
            while True:
                row = input(f"{name} - Enter row {i + 1}: ").strip()
                elements = list(map(int, row.split()))
                if len(elements) == cols:
                    matrix.append(elements)
                    break
                else:
                    print(f"Please enter exactly {cols} numbers.")
        return matrix

    def multiply_matrices(matrix1, matrix2):
        # Matrix multiplication (A * B) is possible if A's columns = B's rows
        result = []
        for i in range(len(matrix1)):  # Iterate through rows of matrix1
            result_row = []
            for j in range(len(matrix2[0])):  # Iterate through columns of matrix2
                result_row.append(sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))))
            result.append(result_row)
        return result

    def main():
        print("Matrix Multiplication Program")
    
    # Input dimensions for matrix1
        rows1 = int(input("Enter the number of rows for Matrix 1: "))
        cols1 = int(input("Enter the number of columns for Matrix 1: "))
    
    # Input dimensions for matrix2
        rows2 = int(input("Enter the number of rows for Matrix 2: "))
        cols2 = int(input("Enter the number of columns for Matrix 2: "))
    
    # Check if the matrices are compatible for multiplication
        if cols1 != rows2:
            print("Error: Number of columns of Matrix 1 must be equal to the number of rows of Matrix 2!")
            return
    
        print("\nInput Matrix 1:")
        matrix1 = get_matrix("Matrix 1", rows1, cols1)
    
        print("\nInput Matrix 2:")
        matrix2 = get_matrix("Matrix 2", rows2, cols2)
    
    # Multiply matrices and display the result
        print("\nResult of Matrix Multiplication:")
        result = multiply_matrices(matrix1, matrix2)
        for row in result:
            print(row)

    if __name__ == "__main__":
        main()

elif question==101:
# Compute the transpose of a user-provided matrix.
    def get_matrix(rows, cols):
        print(f"Enter the matrix with {rows} rows and {cols} columns.")
        matrix = []
        for i in range(rows):
            while True:
                row = input(f"Enter row {i + 1}: ").strip()
                elements = list(map(int, row.split()))
                if len(elements) == cols:
                    matrix.append(elements)
                    break
                else:
                    print(f"Please enter exactly {cols} numbers.")
        return matrix

    def transpose_matrix(matrix):
    # The transpose is obtained by flipping rows with columns
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def main():
        print("Matrix Transpose Program")
    
    # Input dimensions
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
    
    # Input matrix
        matrix = get_matrix(rows, cols)
    
    # Transpose the matrix and display the result
        print("\nOriginal Matrix:")
        for row in matrix:
            print(row)
    
        transposed = transpose_matrix(matrix)
        print("\nTransposed Matrix:")
        for row in transposed:
            print(row)
    if __name__ == "__main__":
        main()

elif question==102:
# Determine if a given square matrix is symmetric (equal to its transpose).
    def get_matrix(size):   
        print(f"Enter a {size}x{size} matrix.")
        matrix = []
        for i in range(size):
            while True:
                row = input(f"Enter row {i + 1}: ").strip()
                elements = list(map(int, row.split()))
                if len(elements) == size:
                    matrix.append(elements)
                    break
                else:
                    print(f"Please enter exactly {size} numbers.")
        return matrix

    def is_symmetric(matrix):
    # Check if the matrix is equal to its transpose
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True

    def main():
        print("Symmetry Check for Square Matrix Program")
    
    # Input the size of the square matrix
        size = int(input("Enter the size of the matrix (n for an n x n matrix): "))
    
    # Input the matrix
        matrix = get_matrix(size)
    
    # Check if the matrix is symmetric
        if is_symmetric(matrix):
            print("\nThe matrix is symmetric.")
        else:
            print("\nThe matrix is not symmetric.")

    if __name__ == "__main__":
        main()

elif question==103:
# Find the longest common substring between two given strings.
    def longest_common_substring(str1, str2):
    # Create a 2D table to store lengths of longest common suffixes
    # of substrings
          m, n = len(str1), len(str2)
          dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # To store the length of the longest common substring
          longest_len = 0
          end_pos = 0  # Position of the end of the longest common substring in str1
    
    # Build the dp table
          for i in range(1, m + 1):
              for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1] + 1
                      if dp[i][j] > longest_len:
                          longest_len = dp[i][j]
                          end_pos = i - 1  # end position in str1
                else:
                      dp[i][j] = 0  # No common substring ends here
    
            # The longest common substring is the substring from end_pos - longest_len + 1 to end_pos
                return str1[end_pos - longest_len + 1:end_pos + 1]

    def main():
        # Take input from the user
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
    
        # Find the longest common substring
        result = longest_common_substring(str1, str2)
    
    # Display the result
        print("Longest common substring:", result)

    if __name__ == "__main__":
          main()

elif question==104:
# Implement the LCS algorithm for two sequences.
      def lcs(str1, str2):
    # Create a 2D table to store the length of the longest common subsequence
          m, n = len(str1), len(str2)
          dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table
          for i in range(1, m + 1):
              for j in range(1, n + 1):
                  if str1[i - 1] == str2[j - 1]:
                      dp[i][j] = dp[i - 1][j - 1] + 1
                  else:
                      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the LCS will be in dp[m][n]
          lcs_length = dp[m][n]

    # Reconstruct the LCS from the dp table
          lcs_sequence = []
          i, j = m, n
          while i > 0 and j > 0:
              if str1[i - 1] == str2[j - 1]:
                  lcs_sequence.append(str1[i - 1])
                  i -= 1
                  j -= 1
              elif dp[i - 1][j] > dp[i][j - 1]:
                  i -= 1
              else:
                  j -= 1

    # Since we constructed the LCS from the end, we reverse it
          lcs_sequence.reverse()

          return "".join(lcs_sequence), lcs_length

      def main():
    # Input two sequences (strings or lists)
          str1 = input("Enter the first sequence: ")
          str2 = input("Enter the second sequence: ")

    # Get the LCS and its length
          lcs_result, lcs_length = lcs(str1, str2)

    # Output the results
          print("Longest Common Subsequence:", lcs_result)
          print("Length of LCS:", lcs_length)

      if __name__ == "__main__":
          main()

elif question==105:
# Given a list of coin denominations and a target amount, find the minimum number of coins needed using a greedy approach.
      def min_coins_greedy(denominations, target):
    # Sort the denominations in descending order
          denominations.sort(reverse=True)
    
    # Initialize variables
          coin_count = 0
          remaining_amount = target
    
    # Iterate over the denominations
          for coin in denominations:
              if remaining_amount >= coin:
            # Find how many coins of this denomination are needed
                  coin_count += remaining_amount // coin
                  remaining_amount %= coin
            
        # If the remaining amount is zero, break out of the loop
              if remaining_amount == 0:
                  break
    
    # If the remaining amount is not zero, it means we couldn't make the change
          if remaining_amount > 0:
              return -1  # Return -1 if it's not possible to make the exact change
    
          return coin_count

      def main():
    # Input coin denominations and target amount
          denominations = list(map(int, input("Enter the coin denominations (space-separated): ").split()))
          target = int(input("Enter the target amount: "))
    
    # Find the minimum number of coins using the greedy approach
          result = min_coins_greedy(denominations, target)
    
          if result == -1:
              print("It is not possible to make the exact change with the given denominations.")
          else:
              print(f"Minimum number of coins needed: {result}")

      if __name__ == "__main__":
          main()

elif question==106:
    def coin_change(coins, amount):
    # Create a DP array to store the minimum coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make the amount 0

    # Populate the DP array
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    # Return the result
        return dp[amount] if dp[amount] != float('inf') else -1

# Input: list of coin denominations and the target amount
    coins = [1, 2, 5]  # Example denominations
    amount = 11        # Example target amount

    result = coin_change(coins, amount)

# Output the result
    if result != -1:
        print(f"The minimum number of coins to make {amount} is: {result}")
    else:
        print(f"It is not possible to make {amount} with the given coins.")

elif question==107:
    def knapsack(values, weights, capacity):
        n = len(values)
    # Create a 2D DP table where dp[i][w] is the max value for the first i items with capacity w
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
        for i in range(1, n + 1):  # Loop through items
            for w in range(1, capacity + 1):  # Loop through capacities
                if weights[i - 1] <= w:  # Check if the item can be included
                    dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                else:
                    dp[i][w] = dp[i - 1][w]

    # The maximum value is in dp[n][capacity]
        return dp[n][capacity]

# Input: values, weights, and knapsack capacity
    values = [60, 100, 120]  # Example values
    weights = [10, 20, 30]   # Example weights
    capacity = 50            # Knapsack capacity

# Output the result
    max_value = knapsack(values, weights, capacity)
    print(f"The maximum value that can be obtained is: {max_value}")

elif question==108:
# Generate all permutations of a given list of distinct elements.
      def generate_permutations_backtrack(elements):
          def backtrack(start=0):
        # If start index reaches the end, a permutation is formed
                  if start == len(elements):
                    result.append(elements[:])  # Add a copy of the current permutation
                  for i in range(start, len(elements)):
                    # Swap the current index with the start index
                    elements[start], elements[i] = elements[i], elements[start]
            # Recurse with the next index
                    backtrack(start + 1)
            # Backtrack (restore the previous state)
                    elements[start], elements[i] = elements[i], elements[start]

          result = []
          backtrack()
          return result

      def main():
    # Input the list of distinct elements
          elements = list(map(int, input("Enter the list of distinct elements (space-separated): ").split()))
    
    # Generate permutations using backtracking
          permutations = generate_permutations_backtrack(elements)
    
    # Display the permutations
          print("All permutations:")
          for perm in permutations:
              print(perm)

      if __name__ == "__main__":
          main()

elif question==109:
# implement the N-Queens puzzle using backtracking.
      def is_safe(board, row, col, n):
    # Check column
          for i in range(row):
              if board[i][col] == 1:
                  return False
    
    # Check diagonal (upper left to lower right)
          for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
              if board[i][j] == 1:
                  return False
    
    # Check diagonal (upper right to lower left)
          for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
              if board[i][j] == 1:
                  return False
    
          return True

      def solve_nqueens(board, row, n, solutions):
    # If all queens are placed
          if row == n:
              solution = []
              for r in range(n):
                  row_str = ""
                  for c in range(n):
                      if board[r][c] == 1:
                          row_str += "Q"
                      else:
                          row_str += "."
                  solution.append(row_str)
              solutions.append(solution)
              return
    
    # Try placing a queen in each column of the current row
          for col in range(n):
              if is_safe(board, row, col, n):
                  board[row][col] = 1  # Place queen
                  solve_nqueens(board, row + 1, n, solutions)  # Recur to place the next queen
                  board[row][col] = 0  # Backtrack (remove queen)

      def nqueens(n):
          board = [[0] * n for _ in range(n)]  # Initialize the board with 0s (no queens placed)
          solutions = []  # To store all possible solutions
          solve_nqueens(board, 0, n, solutions)
          return solutions

      def main():
          n = int(input("Enter the value of N for the N-Queens puzzle: "))
          solutions = nqueens(n)
    
    # Display the solutions
          if solutions:
              print(f"Found {len(solutions)} solutions:")
              for idx, solution in enumerate(solutions, 1):
                  print(f"Solution {idx}:")
                  for row in solution:
                      print(row)
                      print()
          else:
              print("No solutions found.")

      if __name__ == "__main__":
          main()

elif question==110:
# Given a 2D grid, find the shortest path from top-left to bottom-right, moving only down or right (use BFS or DFS).
      from collections import deque

      def is_valid_move(grid, visited, row, col):
    # Check if the move is within the grid and the cell is open (0) and not visited
          return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and not visited[row][col]

      def bfs(grid):
    # If the start or end is blocked, return -1 (no path exists)
          if grid[0][0] == 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
              return -1

    # Directions: (down, right)
          directions = [(1, 0), (0, 1)]

    # Initialize BFS
          queue = deque([(0, 0, 0)])  # (row, col, steps)
          visited = [[False] * len(grid[0]) for _ in range(len(grid))]  # Visited cells
          visited[0][0] = True

          while queue:
              row, col, steps = queue.popleft()

        # If we reached the bottom-right corner, return the number of steps
          if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return steps
            # Try moving in both directions (down and right)
          for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, steps + 1))

    # If no path is found, return -1
          return -1

      def main():
    # Input grid size and grid elements
          m = int(input("Enter the number of rows: "))
          n = int(input("Enter the number of columns: "))
    
          grid = []
          print("Enter the grid (0 for open cell, 1 for blocked cell):")
          for _ in range(m):
              row = list(map(int, input().split()))
              grid.append(row)

    # Find the shortest path using BFS
          result = bfs(grid)
    
          if result == -1:
            print("No path exists.")
          else:
              print(f"The shortest path length is: {result}")

      if __name__ == "__main__":
          main()



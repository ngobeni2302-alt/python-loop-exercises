# python-loop-exercises

Author: Ntsako Ngobeni  
Date: March 10, 2026

## Code Descriptions

The main code is in `assessment1.py`, which contains several functions implementing loop-based solutions for common programming problems. Below is a description of each line of code in the file.

### sum_to_n(n)
- Line 6: `def sum_to_n(n):` - Defines the function that takes an integer n.
- Line 7-11: Docstring explaining the function's purpose and example.
- Line 12: `sum = 0` - Initializes a variable to hold the sum.
- Line 13: `for i in range(1, n + 1):` - Loops from 1 to n inclusive.
- Line 14: `sum += i` - Adds each number to the sum.
- Line 15: `return sum` - Returns the calculated sum.

### count_even_numbers(n)
- Line 19: `def count_even_numbers(n):` - Defines the function.
- Line 20-24: Docstring with description and example.
- Line 25: `even_count = 0` - Initializes counter for even numbers.
- Line 26: `for i in range(1, n + 1):` - Loops through numbers 1 to n.
- Line 27: `if i % 2 == 0:` - Checks if the number is even.
- Line 28: `even_count += 1` - Increments the counter if even.
- Line 29: `return even_count` - Returns the count of even numbers.

### factorial(n)
- Line 33: `def factorial(n):` - Defines the function.
- Line 34-38: Docstring explaining factorial calculation.
- Line 39: `fact = 1` - Initializes factorial to 1.
- Line 40: `for i in range(1, n + 1):` - Loops from 1 to n.
- Line 41: `fact *= i` - Multiplies fact by each number.
- Line 42: `return fact` - Returns the factorial.

### multiplication_table(n)
- Line 46: `def multiplication_table(n):` - Defines the function.
- Line 47-52: Docstring with example.
- Line 53: `ls = []` - Initializes an empty list.
- Line 54: `for i in range(1, 11):` - Loops from 1 to 10.
- Line 55: `multiple = i * n` - Calculates the multiple.
- Line 56: `ls.append(multiple)` - Appends to the list.
- Line 57: `return ls` - Returns the list of multiples.

### sum_of_digits(num: int)
- Line 61: `def sum_of_digits(num: int):` - Defines the function with type hint.
- Line 62-66: Docstring.
- Line 67: `sum = 0` - Initializes sum.
- Line 68: `num = str(num)` - Converts number to string.
- Line 69: `for i in num:` - Loops through each character (digit).
- Line 70: `for x in i:` - Unnecessary nested loop (since i is a single char).
- Line 71: `sum += int(x)` - Converts char to int and adds to sum.
- Line 72: `return sum` - Returns the sum of digits.

### count_vowels(text)
- Line 77: `def count_vowels(text):` - Defines the function.
- Line 78-82: Docstring.
- Line 83: `pass` - Placeholder, function not implemented.

### find_primes(n)
- Line 86: `def find_primes(n):` - Defines the function.
- Line 87-91: Docstring.
- Line 92: `ls = [2, 3]` - Initializes list with first primes.
- Line 93: `if n == 2:` - Special case for n=2.
- Line 94: `return [2]` - Returns [2].
- Line 95: `if n == 3:` - Special case for n=3.
- Line 96: `return [2, 3]` - Returns [2,3].
- Line 97: `for i in range(2, n):` - Loops from 2 to n-1.
- Line 98: `if i % 2 != 0 and i % 3 != 0:` - Checks if not divisible by 2 or 3 (incomplete prime check).
- Line 99: `ls.append(i)` - Appends if condition met.
- Line 100: `return ls` - Returns the list.
- Line 101: `print(find_primes(3))` - Test print statement.

### reverse_string(text)
- Line 106: `def reverse_string(text):` - Defines the function.
- Line 107-111: Docstring.
- Line 112: `return text[::-1]` - Uses slicing to reverse the string.

### pyramid_pattern(n)
- Line 115: `def pyramid_pattern(n):` - Defines the function.
- Line 116-124: Docstring with example.
- Line 125: `for i in range(1, n + 1):` - Loops from 1 to n.
- Line 126: `print("*" * i)` - Prints stars for each row.

### multiplication_grid(n)
- Line 130: `def multiplication_grid(n):` - Defines the function.
- Line 131-140: Docstring.
- Line 141: `ls = []` - Initializes list.
- Line 142: `for i in range(1, n + 1):` - Outer loop for rows.
- Line 143: `row = []` - Initializes row list.
- Line 144: `for j in range(1, n + 1):` - Inner loop for columns.
- Line 145: `row.append(i * j)` - Appends product to row.
- Line 146: `ls.append(row)` - Appends row to main list.
- Line 147: `return ls` - Returns the grid.
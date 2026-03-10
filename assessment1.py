# Python Loop Assessment
# Complete each function using loops.

def sum_to_n(n):
    """
    Return the sum of all numbers from 1 to n (inclusive).
    Example:
    sum_to_n(5) -> 15
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum 



def count_even_numbers(n):
    """
    Count how many even numbers exist between 1 and n (inclusive).

    Example:
    count_even_numbers(10) -> 5
    """
    even_count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_count += 1
    return even_count 

def factorial(n):
    """
    Return the factorial of n using a loop.

    Example:
    factorial(5) -> 120
    """
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact  



def multiplication_table(n):
    """
    Return a list containing the multiplication table for n from 1 to 10.

    Example:
    multiplication_table(3)
    -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    """
    ls = []
    for i in range(1, 11):
        multiple = i * n
        ls.append(multiple)
    return ls


def sum_of_digits(num: int):
    """
    Return the sum of the digits in a number.

    Example:
    sum_of_digits(1234) -> 10
    """
    sum = 0
    num = str(num)
    for i in num:
        for x in i:
            sum += int(x)
    return sum 
    


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the given string.

    Example:
    count_vowels("hello") -> 2
    """
    pass

def find_primes(n):
    """
    Return a list of all prime numbers from 2 up to n.

    Example:
    find_primes(10) -> [2, 3, 5, 7]
    """
    ls = [2, 3]
    if n == 2:
        return [2]
    if n == 3:
        return [2, 3]
    for i in range(2, n):
        if i % 2 != 0 and i % 3 != 0:
            ls.append(i)
    return ls
print(find_primes(3))
    
    


def reverse_string(text):
    """
    Reverse a string using a loop.

    Example:
    reverse_string("hello") -> "olleh"
    """
    return text[::-1]

def pyramid_pattern(n):
    """
    Return a list of strings forming a pyramid pattern of stars.

    Example:
    pyramid_pattern(3)
    -> [
        "*",
        "**",
        "***"
       ]
    """
    for i in range(1, n + 1):
        print("*" * i)



def multiplication_grid(n):
    """
    Create an n x n multiplication grid using nested loops.

    Example:
    multiplication_grid(3)
    -> [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
       ]
    """
    ls = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        ls.append(row)
    return ls
    
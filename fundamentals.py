def add_numbers(a, b):
    """
    Problem 1:
    Write a function that takes two numbers (a and b)
    and returns their sum.

    Example:
    >>> add_numbers(2, 3)
    5
    """
    # TODO: Write your code below
    a =  2
    b = 3
    sum = a + b
    print(sum)



def is_even(n):
    """
    Problem 2:
    Return True if the given number 'n' is even, otherwise return False.

    Example:
    >>> is_even(4)
    True
    >>> is_even(5)
    False
    """
    # TODO: Write your code below
    if n%2 == 0:
     return is_even
    else :
 
     return False


def count_vowels(word):
    """
    Problem 3:
    Write a function that counts how many vowels are in a given string.

    Vowels are: a, e, i, o, u (both uppercase and lowercase).

    Example:
    >>> count_vowels("Hello")
    2
    """
    # TODO: Write your code below
    
    for i in word:
        count = 0
print(count_vowels("Hello"))

def find_max(numbers):
    """
    Problem 4:
    Given a list of numbers, return the largest number.

    Example:
    >>> find_max([1, 4, 2, 10])
    10
    """
    # TODO: Write your code below
    for i in range(numbers):
        

print(find_max(10))

def reverse_string(s):
    """
    Problem 5:
    Write a function that returns the reverse of the input string.

    Example:
    >>> reverse_string("cat")
    'tac'
    """
    # TODO: Write your code below
    s = s[::-1]
print(reverse_string("cat"))


def average(numbers):
    """
    Problem 6:
    Given a list of numbers, return their average.
    If the list is empty, return 0.

    Example:
    >>> average([2, 4, 6])
    4.0
    >>> average([])
    0
    """
    # TODO: Write your code below
    average = sum/total_number
    numbers = [ 2,4,6]
    if numbers[2,4,6]:
        return average
    else:

        return 0
print(average(2,4,6))

def word_in_sentence(word, sentence):
    """
    Problem 7:
    Return True if the given word appears in the sentence, otherwise False.

    Example:
    >>> word_in_sentence("cat", "The cat is sleeping")
    True
    >>> word_in_sentence("dog", "The cat is sleeping")
    False
    """
    # TODO: Write your code below
    
    for word in word_in_sentence:
        if word  :
            return True
        else:
            return False
print("cat","The cat is sleeping")        




def factorial(n):
    """
    Problem 8:
    Write a function that returns the factorial of a non-negative integer n.
    The factorial of n (written as n!) is the product of all positive integers up to n.
    If n is 0, return 1.

    Example:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    # TODO: Write your code below
    def factorial(n):
        count = 1
        for i in range(1,n+1):
            count *= i
    print(factorial(5))        

def remove_duplicates(numbers):
    """
    Problem 9:
    Given a list of numbers, return a new list with duplicates removed.
    The order of the first occurrence of each element should be preserved.

    Example:
    >>> remove_duplicates([1, 2, 2, 3, 1])
    [1, 2, 3]
    """
    # TODO: Write your code below
    for i in numbers:
        new = ""
        len(number)= len(set(number))





def fizzbuzz(n):
    """
    Problem 10:
    Write a function that returns a list of numbers from 1 to n,
    but replace:
    - multiples of 3 with "Fizz"
    - multiples of 5 with "Buzz"
    - multiples of both 3 and 5 with "FizzBuzz"

    Example:
    >>> fizzbuzz(5)
    [1, 2, 'Fizz', 4, 'Buzz']
    """
    # TODO: Write your code below
    if n%3 == 0:
        return "Fizz" 
    elif n%5 == 0:
        return "Buzz"
    
    else :n%3 == 0 and n%5 ==0
    return "FizzBuzz"

print(fizzbuzz(24))



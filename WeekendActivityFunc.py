# 1. Write a program to reverse a string.
# Sample data: “1234abcd”
# Expected Output: “dcba4321”

def string(a):
    return a[::-1]


b = string("1234abcd")
print(b)


# 2. 	Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def wordcases(a):
    countupper = 0
    countlower = 0
    for i in a:
        if i.isupper():
            countupper += 1
        elif i.islower():
            countlower += 1
    print("Number of uppercase:", countupper)
    print("Number of lowercase:", countlower)


a = input("Enter any string:")
wordcases(a)


# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique(a):
    b = set(a)
    c = []
    for i in b:
        c.append(i)
    print(b)


unique([1, 20, 3, 4, 5, 67, 7, 7, 8, 9, 9, 9, 2, 2, 2])


# 4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


def hyphensep(s):
    y = s.split("-")
    y.sort()
    print("-".join(s))


z = input("Enter a string with hypen:")
hyphensep(z)


# 5.Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def seq(a):
    a = a.upper()
    return (a)


print(seq("Hello world"))
print(seq("Practice makes perfect"))


# 6.Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def sumtask():
    a = input("Enter 1st number: ")
    b = input("Enter 2nd number: ")
    c = int(a)
    d = int(b)
    result = c + d
    print(result)


sumtask()

# 7.Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

e = input("Enter 1st string: ")
f = input("Enter 2nd string: ")


def work(e, f):
    if len(e) > len(f):
        print(e)
    elif len(e) < len(f):
        print(f)
    else:
        print(e)
        print(f)


work(e, f)


# 8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def sq():
    a = []
    for i in range(1, 21):
        a.append(i * i)
    a = tuple(a)
    print(a)


sq()


# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# Example: If the limit is 3 , it should print:
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
def limit():
    l = int(input("Enter a limit of odd and even: "))
    for i in range(1, l + 1):
        if i % 2 == 0:
            print("EVEN")
        else:
            print("ODD")


limit()

# 10.Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included)

a = filter(lambda x: x % 2 == 0, range(-1, 21))
print(list(a))

# 11.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,
# 4,5,6,7,8,9,10] Hints: Use map() to generate a list. Use filter() to filter elements of a list Use lambda to define
# anonymous functions

b = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, range(1, 11)))
print(list(b))

# 12. 	Write a function to compute 5/0 and use try/except to catch the exceptions

try:
    a = 5 / 0
except:
    print("Not permitted")

# 13. 	Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

import itertools

a = [[1, 2, 3], [4, 5], [6, 7, 8]]
b = list(itertools.chain(*a))
print(b)

#  14.

def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)


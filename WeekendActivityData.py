# WEEKEND ACTIVITY ON DATA STRUCTURES

# 3. Create a list of given structure and run
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

x = [100, 200, 300, 400, 500, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 600, 700, 800]
print("1.", x[5][0:4])
print("2.", x[6:8])
print("3.", x[::2])
print("4", x[::-1])
print("5", x[5][5][0])
print("6.", x[:0])

# 4. 	Create a list of thousand number using range and xrange and see the difference between each other.

b = []
for i in range(1, 1001):
    b.append(i)
print(b)

# 5. 	How Tuple is beneficial as compare to the list?
# Tuple being immutable requires less memory space as compared to a any other list. It is considered to be faster than a List

# 6. 	Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.

a = []
for a in range(1, 101):
    if a % 3 == 0 and a % 2 == 0:
        print(a)


# 7. 	Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

def random(a):
    b = a[::-1]
    print(b)
    for i in b:
        if i in "aeiou":
            print(i, "The index of the vowel is: ", b.index(i))


print(random("consultadd"))


# 8. 	Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

def sent(a):
    a = a.split(' ')
    for i in a:
        if len(i) % 2 == 0:
            print(i)


a = "hello my name is abcde"
sent(a)

# 9. 	Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.
# x=[1,2,3,4,5,6,7,8,9,-1]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
for a in x:
    for b in x:
        if a + b == 8:
            print("First Number:", a, "Second Number: ", b, "Result: ", (a + b))


# 10. 	Write a program in Python to complete the following task:
# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

even_list = []
odd_list = []
while(True):
  x = int(input('Enter any number: '))

  if x%2 == 0:
    even_list.append(x)
  else:
    odd_list.append(x)
  if len(even_list) == 5 and len(odd_list) == 5:
    print('Sum of even list: ', sum(even_list))
    print('Even list maximum number: ', max(even_list))
    print('Sum of odd list: ', sum(odd_list))
    print('Odd list maximum number: ', max(odd_list))
    break
print("Cannot enter anymore numbers")

# 11.Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab
#                       Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

d = "12abcbacbaba344ab "
print("Number of a's: ", d.count("a"))
print("Number of b's: ", d.count("b"))
print("Number of c's: ", d.count("c"))

# 12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
z = []
for i in y:
    if i % 2 == 0:
        z.append(i)
z = tuple(z)
print(z)

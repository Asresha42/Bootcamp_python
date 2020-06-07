# 1.Create a list of the 10 elements of four different types of Data Type like int, string, complex and float.

x = ["Hello", 1, 1.5, (1 + 2j), 4, 6, 7, "World", 6.88, (2 + 5j)]
print("List:", x)

# 2.Create a list of size 5 and execute the slicing structure

x = [1, 2, 3, 4, 5]
print("Length:", len(x))
print('Sliced Values:', x[1:4])

# 3.Write a program to get the sum and multiply of all the items in a given list.

a = [1, 2, 3, 4, 5]
s = 0
multiply = 1
for i in a:
    s = s + i
    multiply = multiply * i
print("Sum:", s)
print("Multiplication:", multiply)

# 4.Find the largest and smallest number from a given list

b = [2, 3, 7, 1, 9, 4]
print("Maximum Value:", max(b), ", Minimum Value:", min(b))

# 5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

c = [3, 7, 2, 8, 44, 51, 31]
for i in c:
    if i % 2 == 0:
        continue
    else:
        print(i)

# 6.Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

d = range(1, 31)
e = []

for i in d[-5:] and d[:5]:
    e = i ** 2
    print("Square values are:", e)

# 7.Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

f = [1, 3, 5, 7, 9, 10]
g = [2, 4, 6, 8]
f[-1] = g
print("List: ", f)

# 8.Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

h = {1: 10, 2: 20}
i = {3: 30, 4: 40}
h.update(i)
print("Dictionary:", h)

# 9.Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
# Sample data (n=5)
# Expected Output: {1:1,2:4,3:9,4:16,5:25}

j = {}
n = eval(input("Enter the range: "))
for i in range(n + 1):
    j = {i: i * i}
    print(j)

# 10.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# The output should be:
# [‘34’,’67’,’55’,’33’,’12’,’98’]
# (‘34’,’67’,’55’,’33’,’12’,’98’)

m = input("Enter numbers: ")
k = []
l = ()

for i in m:
    k = m.split(",")
    l = tuple(k)

print("List:", k, "Tuple:", l)

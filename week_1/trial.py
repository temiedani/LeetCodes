import itertools
import sys
from functools import reduce
from collections import Counter, defaultdict

x = [1, 2, 3, 4, 5]
# list to int
y = [str(i) for i in x]
print(int("".join(y)))


sent = ["lol", "you", "are", "funny", "lol"]

# list to dict
dic = dict(zip([index for index, j in enumerate(sent)],
           [value for index, value in enumerate(sent)]))
print(dic)


fruits = ["Apple", "Pear", "Peach", "Banana"]
prices = [0.35, 0.40, 0.40, 0.28]

# unlimited parameters


def summ(*a):
    s = 0
    for i in a:
        s += i
    return s


print(summ(1, 2, 3))
print(summ(1, 2))

# smple functions


def squares(n: int) -> bool:
    return n**2


def evens(n: int) -> bool:
    return n % 2 == 0


def multiply(x: int, y: int) -> int:
    return x*y


# zip
fruit_dictionary = dict(zip(fruits, prices))

print(fruit_dictionary)

# list comprehension
even = [x for x in range(20) if x % 2 == 0]
print(even)

#print(list(range(0, 20, 2)))
s
# filter
sq = list(map(squares, [1, 2, 3, 4, 5]))
print(sq)

# map
ev = list(filter(evens, [1, 2, 3, 4, 5]))
print(ev)

# reduce -> needs to be imported from functools
product = reduce(multiply, [1, 2, 3, 4, 5])
print(product)

# lampda
print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))

# all and any

# enumerate vs in range
for idx, val in enumerate([1, 2, 3, 4]):
    print(idx, " at ", val, end=", ")
print()

# sort a list
data_list = [3, 4, 5, 6, 9, 4]
# reverse=True for ascending order
# set key for complex list
sorted_data_list = sorted(data_list, reverse=True)
print("sorted in descending order", sorted_data_list)
data = [{"name": "temie", "age": 25},
        {"name": "Iseyas", "age": 39},
        {"name": "Shewit", "age": 27}]
print(sorted(data, key=lambda x: x["age"]))
# sort a


# unique values in list
# converst to set and back to list
mylist = [7, 1, 2, 3, 2, 3, 4, 5, 1]
print(list(set(mylist)))


# generators save memory
my_gen = (i for i in range(1000))
print(sum(my_gen), "  ", sys.getsizeof(my_gen), " bytes")

# user dic.get if key may not exist return None
my_dict = {"name": "temie", "age": 25}
print(my_dict.get("gender", "key does not exist"))
# we can use dict.setdefalult()
my_dict.setdefault("gender", "empty")
# checking result after setting default
print(my_dict.get("gender", "key does not exist"))


# Count hashable object with collections.Counter
xc = [1, 2, 3, 4, 1, 3]
counter = Counter(xc)
print(counter)
print(counter.most_common(1))

# format string with f string
age = 25
name = "temie"
print(f"my name is {name} and i am {age} years old")


# concatinate string with .join
my_sent = ["lol", "you", "are", "crazy"]
print(" ".join(my_sent))


# merge dictionaries

my_dict_1 = {"name": "temie", "age": 25}
my_dict_2 = {"salary": "120k"}
merged_dict = {**my_dict_1, **my_dict_2}
print(merged_dict)

#  cycle itertools
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
skip = 0
for color in itertools.cycle(colors):
    print(color)
    skip += 1
    if skip == 5:
        break

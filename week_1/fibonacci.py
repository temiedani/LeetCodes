# pyhton Generatos yield and next


from itertools import count


def fib(x):
    a, b = 0, 1
    for i in range(x):
        yield(f"{i+1}th fibonacci is {a}")
        a, b = b, a+b


a = fib(5)

# print(next(a), next(a))


for i in count(10, 3):
    print(i)
    if i > 20:
        break

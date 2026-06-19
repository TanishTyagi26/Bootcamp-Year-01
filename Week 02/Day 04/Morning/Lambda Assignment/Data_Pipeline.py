#Use only map() and filter() with lambdas no loops .
#process a list of integers[1-20]:..
#Filter odd no., then square each , then sum the results using reduce()...



from functools import reduce

start = int(input("Enter start: "))
end = int(input("Enter end: "))

result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 != 0, range(start, end + 1))
    ),
    0
)

print("Sum =", result)
numbers = [2, 5, 8, 11, 14, 17, 20]

square = list(map(lambda x: x*x, filter(lambda x: x%2==0, numbers)))

print(square)
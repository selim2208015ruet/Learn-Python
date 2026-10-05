numbers = [2, 5, 8, 11, 14, 17, 20]

result = list(filter(lambda x: x%2==0, numbers))

square = list(map(lambda x: x*x,result))

print(square)
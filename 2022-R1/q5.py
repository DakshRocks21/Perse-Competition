hat = int(input())
scarf = int(input())
glove = int(input())

print('toasty' if (min(1, hat) + min(1, glove//2) + min(1, scarf)) >= 2 else 'cold')

hat = max(0, hat - 1)
scarf = max(0, scarf - 1)
glove = max(0, glove - 2)

print(hat + scarf + glove)

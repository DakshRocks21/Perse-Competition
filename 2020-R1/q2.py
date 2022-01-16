word = input()

z = ['a','e','i','o','u']
for i in word:
    for j in z:
        if i == j:
            print(i)
lemon, sugar = int(input()), int(input())

if lemon >= 20 and sugar >= 3:
    print("A")
elif lemon < 20 and sugar >= 3:
    print("B")
elif lemon >= 20 and sugar < 3:
    print("C")
else:
    print("D")

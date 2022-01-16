mixture = input()
icecream, milk, ice, cream = 0,0,0,0

for i in mixture:
    if i == "I":
        icecream += 1
    elif i == "M":
        milk += 1
    elif i == "C":
        ice += 1
    elif i == "w":
        cream += 1
    else:
        pass

if icecream < 2:
    print("I")
elif milk < 1:
    print("M")
elif ice < 3:
    print("C")
else:
    print("W")

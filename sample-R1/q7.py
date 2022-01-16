current = 1

for _ in range(5):    
    x= input()
    if x == "Ellie":
        if current == 1:
            print("1st")
        elif current == 2:
            print("2nd")
        elif current == 3:
            print("3rd")
        else:
            print(str(current)+"th")
        break
    current += 1



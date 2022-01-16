car_type = input()

if car_type == "electric":
    print("$0")
else:
    size = float(input())    
    index = 0
    prices = [120, 140, 150, 170, 180, 100]
    
    if car_type == "petrol":
        index += 2
    elif car_type == "diesel":
        index += 4     
    
    if size >= 1.8:
        index += 1
        
    print(f"${prices[index]}")
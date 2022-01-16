min_l, max_l = int(input()), int(input())

carrots = []
vaild, invaild = 0, 0

while True:
    x = int(input())
    if x != -1:
        carrots.append(x)    
    else:
        break

for i in carrots:
    if min_l <= i <= max_l:
        vaild += 1
    else:
        invaild += 1
        
print(vaild)
print(invaild)
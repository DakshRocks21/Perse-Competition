current, jump = input(), int(input())

seasons = ["spring", "summer", "autumn", "winter"]

for _ in range(jump):
    num = seasons.index(current)+1
    if num > len(seasons)-1:
        num = 0
    current = seasons[num]
print(current)
fname, lname = input(),input()

a = fname[0].lower()
b = lname[0].lower()
c = lname[-1].lower()
num = str(len(fname))

if a==b or a==c or c==b:
    print(f"{a}{b}{c}{num}x")
else:
    print(f"{a}{b}{c}{num}")

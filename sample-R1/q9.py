a = "<+&><+&>"
b = "+&><+&><"
c = "&><+&><+"
d = "><+&><+&"

start = input()

if start == "<":
    print(a)
elif start == "+":
    print(b)  
elif start == "&":
    print(c)
else:
    print(d)
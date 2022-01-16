word, num = input(), int(input())
poem = "wibble wobble wibble wobble jelly on the plate".split(" ")
first = poem.index(word)
print(" ".join(poem[first+1:first+1+num]))
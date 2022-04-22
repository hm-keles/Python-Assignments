word = input("Please give a word: ")
Left = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
Right = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
word = set(word)
leftcheck = bool(word.intersection(Left))
rightcheck = bool(word.intersection(Right))

result = leftcheck and rightcheck
print(result)
# İlk çözüm...

sentence = input("Please write a sentence: ")

let_char = {}

for i in range(len(sentence)) :
    if sentence[i] not in let_char :
        let_char.update({sentence[i]:1})
    else :
        let_char[sentence[i]] += 1
print(let_char)

# İkinci çözüm

sentence2 = input("Please write a sentence: ")

result = {char:sentence2.count(char) for char in sentence2}
print(result)
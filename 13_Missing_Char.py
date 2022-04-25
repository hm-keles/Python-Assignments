#Given a non-empty string and an int n, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in the original string (i.e. n will be in the range 0....len(str)-1 inclusive).

def missing_char(word, n):
    word2 = ""
    for i in range(len(word)) :
        if i != n :
            word2 += word[i]
        else :
            continue
    return word2

print(missing_char('kitchen', 1))
print(missing_char('kitchen', 0))
print(missing_char('kitchen', 4))
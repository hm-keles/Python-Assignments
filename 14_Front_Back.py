# Given a string, return a new string where the first and last chars have been exchanged

def front_back(word):
    if len(word) == 1 :
        return word
    else :
        return (word[-1] + word[1:len(word)-1] + word[0])
    
print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))
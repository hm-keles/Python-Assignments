fibonacci = [1, 1]

for i in range(8) :  # range(2,55)
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
    #if fibonacci[i] == 55 :
     #   break
print(fibonacci)
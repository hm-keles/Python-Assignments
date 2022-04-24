num = int(input("Please enter a number to print prime numbers are smaller than it: "))
prime_list = []
for i in range(1,num) :
    liste = []
    for j in range(2,num) :
        if i % j == 0 :
            liste.append(j)
    if liste == [i] :
        prime_list.append(i)
print(prime_list)
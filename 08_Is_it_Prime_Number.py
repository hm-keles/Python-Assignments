num = int(input("Please enter a positive int number to check if it is a Prime Number: "))
array =[]
    
for i in range(2, num) :
    if num % i == 0 :
        array.append(i)
if array == list() :
    print(f"{num} is a prime number.")
else :
    print(f"{num} is not a prime number.")
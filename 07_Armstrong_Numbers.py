# solution with "for"

num = input("Please enter a positive integer number: ")

if num.isdigit() :
    n = 0
    sum_powers = 0
    for i in num :
        sum_powers += int(num[n])**len(num)
        n += 1
    if sum_powers == int(num) :
        print(num, "is an Armstrong number")
    else :
        print(num, "is not an Armstrong number")
else :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

# solution with "while"
num = input("Please enter a positive integer number: ")

if num.isdigit() :
    x = int(num)
    n = len(num)
    sum_powers = 0
    num = int(num)
    while num > 0 :
        sum_powers += (num % 10)**n
        num = num // 10
    if sum_powers == x :
        print(x, "is an Armstrong number")
    else :
        print(x, "is not an Armstrong number")
else :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
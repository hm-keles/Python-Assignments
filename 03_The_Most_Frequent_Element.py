numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
frequent_number = max(numbers, key = numbers.count)

times = numbers.count(frequent_number)

print(f"The most frequent number is {frequent_number} and it was {times} times repeated.")
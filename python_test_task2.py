numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]

print("Duplicate Numbers and Their Counts:")
count = {}
for number in numbers:
    x = numbers.count(number)
    if x > 1:
        count[number] = x
    # if number in count:
    #     count[number] += 1
    # else:
    #     count[number] = 1

for number,count_of_number in count.items():
    print(f"{number} appears {count_of_number} times")

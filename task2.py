def func(numbers):
    numbers_greater_than_5 = [number for number in numbers if number > 5]
    return numbers_greater_than_5, sum(numbers_greater_than_5)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

numbers_gt_5, total_sum = func(numbers)
print("Numbers greater than 5:", numbers_gt_5)
print("Sum of numbers greater than 5:", total_sum)



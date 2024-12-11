numbers = [10, -5, 20, -3, 8, -2, 15]

positive_numbers = [num for num in numbers if num >= 0]
print(f"Positive numbers: {positive_numbers}")

max_value = max(positive_numbers)
min_value = min(positive_numbers)
print(f"Maximum: {max_value}, Minimum: {min_value}")

average = sum(positive_numbers) / len(positive_numbers)
print(f"Average: {average}")
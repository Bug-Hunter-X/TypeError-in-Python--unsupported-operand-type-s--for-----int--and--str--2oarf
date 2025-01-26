def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # This will print 0 as expected

my_list = [10, 20, 30, 40, 50] 
average = calculate_average(my_list) 
print(f"The average is: {average}") # This will print 30.0 as expected

my_list = [10, 20, 'a', 40, 50] #This will not throw an error
average = calculate_average(my_list)
print(f"The average is: {average}") # This will print 30.0 as expected
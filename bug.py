def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") # This will print 0 as expected

my_list = [10, 20, 30, 40, 50] 
average = calculate_average(my_list) 
print(f"The average is: {average}") # This will print 30.0 as expected

my_list = [10, 20, 'a', 40, 50] #This will throw an error
average = calculate_average(my_list)
print(f"The average is: {average}")
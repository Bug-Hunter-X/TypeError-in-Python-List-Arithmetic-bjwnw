def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") #This will print 0 which is not an error

my_list_with_zero = [1,0,3,0,5]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}") #This will not raise an error, as it is handled correctly

my_list_with_string = [1,2,"a",4,5]
result = calculate_average(my_list_with_string) #This will raise a TypeError
print(f"The average is: {result}")
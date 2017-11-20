# created by Matthew Walsh
# created for ics3u
# created on nov 2017
# finds the minimum value in an array

from numpy import random

def find_min_value(array = []):
    # finds min value in array
    
    min_number = array[0]
    
    for number in array:
        if min_number > number:
            min_number = number
            
    return min_number

# input
counter = 0
random_numbers = []

while counter < 10:
    number = random.randint(1, 10 + 1)
    print(number)
    random_numbers.append(number)
    counter = counter + 1

# process
smallest_value = find_min_value(random_numbers)

# output
print("\nThe minimum value of the array is " + str(smallest_value) + ".\n")

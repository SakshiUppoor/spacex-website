#Accepting a string of comma-separated binary numbers as input
input_string = input()

#Converting string to a list
binary_list = input_string.split(',')

#Creating a list to store output
output_list = []

#Iterating through all numbers in the list
for number in binary_list:
    b = int(number,2)

    if not b%5:
        #If number is divisible by 5, append it to the output list
        output_list.append(number)

#printing output
print(",".join(output_list))
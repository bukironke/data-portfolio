#declares a function that will take one argument which is expected to be a list 
def find_unique_fruit (input_list):
#initialises an empty list that will store unique strings from the input list
    unique_fruit = []
#initialises a loop that iterates through each element in IL assigning each element to the variable 'string'
    for string in input_list:
#checks if the current string is not already in the UF list
        if string not in unique_fruit:
#if not, it is appended to the list
            unique_fruit.append(string)
#returns the UF list containing only the unique elements from the input list while keeping the order
    return unique_fruit

input_list = ["apple", "banana", "orange", "apple", "kiwi", "strawberry", "lemon", "cucumber"]
output_list = find_unique_fruit(input_list)
print (output_list)

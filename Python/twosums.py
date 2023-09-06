#Defining a method called two_sum, showing that the meth would be working var num and var target
def two_sum(nums, target):
    #defining a dictionary
    num_dict = {}
    #defining loop - i is the index (position) and num is the number - enumerate is to store it
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], i]
            #if no number is found, adds an entry to the dic w num as the key and i as the position
        num_dict[num] = i
    #if nothing is found, return an empty list
    return [] 


nums = [2, 11, 7, 15]
target = 9


result = two_sum(nums, target)

# Print the result
if result:
    print(f"The indices of the two numbers that add up to {target} are {result[0]} and {result[1]}")
else:
    print("No solution found.")

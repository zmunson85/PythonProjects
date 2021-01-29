# Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one,
# from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5, 4, 3, 2, 1, 0]
#

# start = num1(input("starting point for countdown"))
# stop = num2(input("stop cnountdown here"))


def countdown(num):
    newList = []
    print('num is ->', num)
    for i in range(num, -1, -1):
        newList.append(i)

    print(newList)
    return newList


countdown(5)
countdown(15)
countdown(25)

# return newList

# for i in range(0, len(arr), 1):

# for (i = 0; i < arr.length; i++)


# Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.
# Example: print_and_return([1, 2]) should print 1 and return 2

# input is a ([1,2])
def print_return(arr):
    print(arr[0])
    num = arr[1]
    return num


arr = [1, 2]
print(print_return(arr))


# First Plus Length -
# Create a function that accepts a list and returns the sum of the
#  first value in the list plus the list's length.
# Example: first_plus_length([1, 2, 3, 4, 5]) should return 6 (first value: 1 + length: 5)

def firstPluslen(arr):
    length_val = len(arr)
    sum = length_val+arr[0]
    print(sum)
    return(sum)


arr = [1, 2, 3, 4, 5]
firstPluslen(arr)


def ValuesGreater(arr):
    for i in range(len(arr)):
        if arr[1] < arr[i]:

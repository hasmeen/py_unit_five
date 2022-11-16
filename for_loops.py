# #sofia Fall
# import random

# for x in range(10):
#     number = random.randint(1,100)
#     print(number)

# # def count(first, last):
# #     """
# #     This function will create a string of numbers separated by a space. The numbers will start with the
#     first number and end with the second. The second number SHOULD be included as part of the string. If
#     the first number is larger than the second, the numbers should count down, rather than up.
#     count(5, 10) returns "5 6 7 8 9 10 "
#     :param first: The starting number
#     :param second: The final number. Must be included
#     :return: A string containing the numbers
#     """
#     pass # make sure to delete this line when you write your own function


# def main():
#     print(count(0, 6))


# if __name__ == '__main__':
#     main()
def count(first, last, m):
    # Create an empty string
    string_of_numbers = ''
    count_up = True

    # Determine if counting up or down

    # If m is negative
    if m < 0:
    # Don't count up
    #count_up = False
    #Swap first and last using a temp variable
        temp = first
        first = last
        last = temp

    # Call range with start, stop, and step
    for number in range(first, last, m):
        string_of_numbers += str(number) + ' '

    return string_of_numbers


if __name__ == '__main__':
    print(count(1, 10, 2)) # 1 3 5 7 9
    print(count(2, 28, -3)) # 28 25 22 19 16 13 10 7 4
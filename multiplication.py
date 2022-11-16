# def multiplication_table(number):
#     """
#     Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
#     :param number: An integer
#     :return: A string of 12 values representing the mulitiplication table of the parameter number.
#     """
#     pass # Make sure to delete this line when writing your function.

def multiplication_table(number):

    test = " "
    for x in range(12):
        test += str(x * number)+ " "
    print(test)

def main():

       (multiplication_table(9))

main()# def multiplication_table(number):
#     """
#     Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
#     :param number: An integer
#     :return: A string of 12 values representing the mulitiplication table of the parameter number.
#     """
#     pass # Make sure to delete this line when writing your function.

def multipiclation_table(number):

    test = " "
    for x in range(1, 12):
        test += str(x * number)+ " "
    print(test)

def main():

       (multipiclation_table(9))

main()
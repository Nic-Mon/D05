#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        input_number = int(input("Enter an integer: "))

        if(input_number % 2 == 0):
            print(str(input_number) + " is even")
        else:
            print(str(input_number) + " is odd")

    except:
        print("that is not an int")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for tens in range(0,10):
        for ones in range(1,10):
            print('{0:<5}'.format(tens*10 + ones), end='')
        print('{0:<5}'.format(tens*10 + 10))


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    total = 0
    count = 0
    user_input = input("Enter a number: ")

    while user_input != 'done':
        try:
            total += float(user_input)
            count += 1
        except:
            print("That is not a number")
        user_input = input("Enter another number: ")

    return total/count


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())

if __name__ == '__main__':
    main()

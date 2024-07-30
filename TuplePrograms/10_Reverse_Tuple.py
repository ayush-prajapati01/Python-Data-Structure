'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to reverse a tuple.
    
'''


def reverse_tuple(numbers):
    """
    Description: 
        This function used to reverse the tupple
    Parameters:
        numbers: tuple to be reversed
    Return:
        tuple: reversed tuple

    """
    return numbers[::-1]


def main():
    numbers = (1,2,3,4,5,6,7,8)
    print(f"The tuple is {numbers}")
    print(f"The reverse of the string is : {reverse_tuple(numbers)}")


if __name__ == "__main__":
    main()
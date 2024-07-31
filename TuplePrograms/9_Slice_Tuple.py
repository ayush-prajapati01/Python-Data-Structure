'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to slice a tuple.
    
'''


def slice_tuple(number, start, end):
    """
    Description: 
        This function removes an item from a tuple.
    Parameters:
        numbers: the tuple containing numbers
    Return:
        tuple: updated tuple
    """
    return number[start:end]


def main():
    numbers = (1,2,3,4,5,6,7,8)
    print(f"The tuple is {numbers}")

    start = int(input("Enter the starting range for slicing: "))
    end = int(input("Enter the ending range for slicing: "))
    print(slice_tuple(numbers, start, end))


if __name__ == "__main__":
    main()
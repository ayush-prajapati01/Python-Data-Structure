'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to remove an item from a tuple.
    
'''


def remove_item(numbers, remove_num):
    """
    Description: 
        This function removes an item from a tuple.
    Parameters:
        numbers: the tuple containing numbers
    Return:
        tuple: updated tuple
    """
    index = numbers.index(remove_num)

    return numbers[:index] + numbers[index+1:]


def main():
    numbers = (1,2,3,4,5,6,7,8)
    print(f"The tuple is ")

    remove_num = int(input("Enter the number to be removed: "))
    print(remove_item(numbers, remove_num))


if __name__ == "__main__":
    main()
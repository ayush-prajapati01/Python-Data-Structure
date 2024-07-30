'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to multiply all the items in a list.
    
'''


def multiply_list(num_list):
    """
    Description: 
        This function accepts a list and returns its multiplication
    Parameters:
        num_list: list containing integers 
    Return:
        int: multiplication of list
    """
    multiplication = 1
    for num in num_list:
        multiplication *= num

    return multiplication


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list = []

    for index in range(n):
        num_list.append(int(input(f"Enter {index+1}th element: ")))

    print(f"\nThe list entered is : {num_list}")
    print(f"The sum of the list is : {multiply_list(num_list)}")


if __name__ == "__main__":
    main()
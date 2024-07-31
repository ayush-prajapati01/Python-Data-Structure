'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to get the smallest number from a list.
    
'''


def smallest_element(num_list):
    """
    Description: 
        This function accepts a list and returns its multiplication
    Parameters:
        num_list: list containing integers 
    Return:
        int: multiplication of list
    """
    smallest = 2 ** 30
    for num in num_list:
        if num < smallest:
            smallest = num
    
    return smallest


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list = []

    for index in range(n):
        num_list.append(int(input(f"Enter {index+1}th element: ")))

    print(f"\nThe list entered is : {num_list}")
    print(f"The smallest element of the list is : {smallest_element(num_list)}")


if __name__ == "__main__":
    main()
'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to remove duplicates from a list.
    
'''


def remove_duplicates(num_list):
    """
    Description: 
        This function remove duplicates from a list.
    Parameters:
        num_list1: The list containing numbers.
    Return:
        list: updated list
    """
    unique_list = []

    for num in num_list:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list = []

    for index in range(n):
        num_list.append(int(input(f"Enter {index+1}th element: ")))

    print(f"\nThe list entered is : {num_list}")
    print(f"The unique list is : {remove_duplicates(num_list)}")


if __name__ == "__main__":
    main()
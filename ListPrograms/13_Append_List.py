'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to append a list to the second list.
    
'''


def append_list(list1, list2):
    """
    Description: 
        This function to get the append two list
    Parameters:
        list1, list2: The list containing numbers.
    Return:
        list: updated list
    """
    for num in list2:
        list1.append(num)

    return list1


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list1 = []
    num_list2 = []

    for index in range(n):
        num_list1.append(int(input(f"Enter {index+1}th element for list 1: ")))

    print("\nFor list 2: ")
    for index in range(n):
        num_list2.append(int(input(f"Enter {index+1}th element for list 2: ")))
    
    print(f"The appended list is: {append_list(num_list1, num_list2)}")


if __name__ == "__main__":
    main()
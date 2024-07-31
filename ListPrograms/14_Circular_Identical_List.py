'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title : Python program to check whether two lists are circularly identical.
    
'''


def is_circular_list(num_lst1, num_lst2):
    """
    Description: 
        This function checks whether two list are circularly identical.
    Parameters:
        num_list1, num_list2: The list containing numbers.
    Return:
        boolean: whether circularly identical
    """
    if(len(num_lst1) != len(num_lst2)):
        return False
    
    num_lst1 = num_lst1 * 2
    index = 0
    for index in range(len(num_lst2)):
        if num_lst1[index: index+len(num_lst2)] == num_lst2:
            return True

    return False


def main():
    num_list1 = []
    num_list2 = []

    n1 = int(input("Enter number of elements in the list1: "))
    for index in range(n1):
        num_list1.append(int(input(f"Enter {index+1}th element for list 1: ")))

    n2 = int(input("Enter number of elements in the list1: "))
    print("\nFor list 2: ")
    for index in range(n2):
        num_list2.append(int(input(f"Enter {index+1}th element for list 2: ")))
    
    print(f"The entered list {num_list2} is circular list of {num_list1}: {is_circular_list(num_list1, num_list2)}")


if __name__ == "__main__":
    main()
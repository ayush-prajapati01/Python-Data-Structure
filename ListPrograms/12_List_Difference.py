'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to get the difference between the two lists.
    
'''


def list_difference(lst1, lst2):
    """
    Description: 
        This function to get the difference between the two lists.
    Parameters:
        lst1, lst2: The list containing numbers.
    Return:
        list: updated list
    """
    diff_list = []
    for num in lst1:
        if num not in lst2:
            diff_list.append(num)
    
    return diff_list


def main():
    lst1 = int(input("Enter items for the first list (space-separated): ").split())
    lst2 = int(input("Enter items for the second list (space-separated): ")).split()

    print(f"The difference of list is: {list_difference(lst1, lst2)}")


if __name__ == "__main__":
    main()
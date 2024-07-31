'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to remove item(s) from set
    
'''


def remove_items(num_set):
    """
    Description: 
        This function remove the element in the set
    Parameters:
        num_set: The set to be iterated
    Return:
        set: Updated set
    """
    item_to_remove = int(input("Enter the item to remove from the set: "))
    if item_to_remove in num_set:
        num_set.remove(item_to_remove)
        print(f"'{item_to_remove}' has been removed.")
    else:
        print(f"'{item_to_remove}' not found in the set.")
    print(f"\nUpdated set is {num_set}")
    return num_set


def main():
    num_set = {1,2,3,4,5,6,7,8,9}
    print(f"The orignal set is {num_set}")
    n = int(input("Enter number of items to remove: "))
    for _ in range(n):
        remove_items(num_set)


if __name__ == "__main__":
    main()
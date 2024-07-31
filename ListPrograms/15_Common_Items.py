'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title : Python program to find common items from two lists

'''


def find_common_items(list1, list2):
    """
    Description: 
        This function finds common items between two lists without using sets.
    Parameters:
        list1: The first list.
        list2: The second list.
    Return:
        list: A list containing common items.
    """
    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items


def main():
    list1 = input("Enter items for the first list (space-separated): ").split()
    list2 = input("Enter items for the second list (space-separated): ").split()

    common_items = find_common_items(list1, list2)

    if common_items:
        print("Common items:", ", ".join(common_items))
    else:
        print("No common items found.")


if __name__ == "__main__":
    main()
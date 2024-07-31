'''
    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to remove duplicates from a list of lists
'''


def remove_duplicate_lists(list_of_lists):
    """
    Description: 
        This function removes duplicate lists from a list of lists.
    Parameters:
        list_of_lists: A list containing lists.
    Return:
        list: A new list with duplicate lists removed.
    """
    unique_lists = []
    for sublist in list_of_lists:
        if sublist not in unique_lists:
            unique_lists.append(sublist)
    return unique_lists


def main():
    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    
    print("Original list:")
    print(sample_list)

    new_list = remove_duplicate_lists(sample_list)

    print("\nList after removing duplicates:")
    print(new_list)


if __name__ == "__main__":
    main()
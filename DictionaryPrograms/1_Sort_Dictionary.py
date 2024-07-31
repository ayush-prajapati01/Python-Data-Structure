'''
    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python script to sort a dictionary by value (ascending and descending)
    
'''


def sort_dict_by_value(dictionary, reverse=False):
    """
    Description: 
        This function sorts a dictionary by its values.
    Parameters:
        dictionary: The dictionary to be sorted.
        reverse: Boolean to determine sorting order (False for ascending, True for descending).
    Return:
        dict: A new dictionary sorted by values.
    """
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=reverse))


def main():
    my_dict = {'java': 5, 'rust': 2, 'c': 8, 'python': 1, 'c++': 3}
    
    print("Original dictionary:")
    print(my_dict)

    # Sort in ascending order
    ascending_dict = sort_dict_by_value(my_dict)
    print("\nDictionary sorted in ascending order by value:")
    print(ascending_dict)

    # Sort in descending order
    descending_dict = sort_dict_by_value(my_dict, reverse=True)
    print("\nDictionary sorted in descending order by value:")
    print(descending_dict)


if __name__ == "__main__":
    main()
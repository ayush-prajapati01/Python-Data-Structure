'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to count the number of items in dictionary values that are lists.
    
'''


def count_items_in_list_values(my_dict):
    """
    Description: 
        This function counts the number of items in dictionary values that are lists.
    Parameters:
        my_dict: The dictionary with values that may be lists.
    Return:
        int: count of items in all list values.
    """
    count = 0
    for value in my_dict.values():
        if isinstance(value, list):
            count += len(value)
    return count


def main():
    my_dict = {
        'languages': ['Python', 'JavaScript', 'Java', 'C++'],
        'frameworks': ['Django', 'React', 'Spring', 'Flask'],
        'databases': ['PostgreSQL', 'MySQL', 'MongoDB'],
        'tools': ['Git', 'Docker', 'Jenkins']
    }

    total_items = count_items_in_list_values(my_dict)
    print(f"The total number of items in list values is: {total_items}")


if __name__ == "__main__":
    main()

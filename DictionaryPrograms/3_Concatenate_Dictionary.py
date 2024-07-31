'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title : Python program to concatenate a dictionary.
    
'''


def create_dictionary(num_entries):
    """
    Description: 
        This function creates a dictionary
    Parameters:
        num_entries: number of key-value pairs for dictionary
    Return:
        dictionary: new dictionary
    """
    number_dict = {}
    for _ in range(num_entries):
        key = int(input("Enter Key : "))
        value = int(input("Enter value: "))
        number_dict[key] = value
    return number_dict


def concatenate_dict(dict1, dict2, dict3):
    """
    Description: 
        This function concatenates a dictionary
    Parameters:
        dict1, dict2, dict3: dictionary to be concatenated
    Return:
        dictionary: concatenated dictionary
    """
    # dict1.update(dict2)
    # dict1.update(dict3)

    for key, value in dict2.items():
        dict1.update({key: value})

    for key, value in dict3.items():
        dict1.update({key: value})
    
    return dict1


def main():
    num_entries = int(input("Enter the number of key-value pairs for 1st dictionary: "))
    number_dict1 = create_dictionary(num_entries)

    num_entries = int(input("Enter the number of key-value pairs for 2nd dictionary: "))
    number_dict2 = create_dictionary(num_entries)

    num_entries = int(input("Enter the number of key-value pairs for 3rd dictionary: "))
    number_dict3= create_dictionary(num_entries)

    print(f"The concatenated dictionary is: {concatenate_dict(number_dict1, number_dict2, number_dict3)}")


if __name__ == "__main__":
    main()


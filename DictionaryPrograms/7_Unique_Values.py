'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to print all unique values in a dictionary.
    
'''


def unique_values(my_dict):
    """
    Description: 
        This function finds the unique value in the dictionary
    Parameters:
        my_dict: dictionary 
    Return:
        list: Contains unique values
    """
    unique_values = []
    for key, value in my_dict.items():
        if value not in unique_values:
            unique_values.append(value)
    
    return unique_values


def main():
    num_entries = int(input("Enter the number of key-value pairs for dictionary: "))
    my_dict = {}
    for _ in range(num_entries):
        key = int(input("Enter Key : "))
        value = input("Enter value: ")
        my_dict[key] = value

    print(f"\nThe unique values in the dictionary are: {unique_values(my_dict)}")


if __name__ == "__main__":
    main()
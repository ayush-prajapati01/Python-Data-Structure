'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title : Python program to add a key to a dictionary.
    
'''

def add_key(number_dict):
    """
    Description: 
        This function adds a key to dictionary
    Parameters:
        number_dict: Orignal dictionary
    Return:
        dictionary: Updated dictionary
    """
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    number_dict.update({key: value})
    return number_dict


def main():
    num_entries = int(input("Enter the number of key-value pairs: "))
    number_dict = {}
    for _ in range(num_entries):
        key = int(input("Enter Key : "))
        value = int(input("Enter value: "))
        number_dict[key] = value
    
    print(f"The entered dictionary is {number_dict}")
    print("\nAdding a new key")
    number_dict = add_key(number_dict)
    print(f"The update dictionary is {number_dict}")


if __name__ == "__main__":
    main()

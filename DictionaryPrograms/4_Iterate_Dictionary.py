'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title : Python program to iterate over dictionaries using for loops.
    
'''


def iterate_dictionary(my_dict):
    """
    Description: 
        This function iterates a dictionary
    Parameters:
        my_dict: dictionary to be iterated
    Return:
        None
    """
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
    

def main():
    num_entries = int(input("Enter the number of key-value pairs for dictionary: "))
    number_dict = {}
    for _ in range(num_entries):
        key = int(input("Enter Key : "))
        value = int(input("Enter value: "))
        number_dict[key] = value

    print("\nThe dictionary iteration is: \n")
    iterate_dictionary(number_dict)


if __name__ == "__main__":
    main()


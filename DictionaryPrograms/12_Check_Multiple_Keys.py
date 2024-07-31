'''
    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to check if multiple keys exist in a dictionary and list missing keys.
'''


def check_multiple_keys(dictionary, keys):
    """
    Description: 
        This function checks if multiple keys exist in a dictionary.
    Parameters:
        dictionary: The dictionary to check.
        keys: A list of keys to check for.
    Return:
        boolean: all keys exist or not
        list: list of missing keys
    """
    existing_keys = set(dictionary.keys())
    keys_to_check = set(keys)
    missing_keys = keys_to_check.difference(existing_keys)
    return len(missing_keys) == 0, list(missing_keys)


def main():
    my_dict = {
        'name': 'Ayush',
        'age': 21,
        'city': 'Navi Mumbai',
        'occupation': 'Data Engineer'
    }
    
    keys_to_check = ['name', 'age', 'city']

    all_keys_exist, missing_keys = check_multiple_keys(my_dict, keys_to_check)
    
    if all_keys_exist:
        print(f"All keys {keys_to_check} exist in the dictionary.")
    else:
        print(f"Keys missing are: {missing_keys}")

if __name__ == "__main__":
    main()

'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to count the values associated with key in a sdictionary.
    
'''


def count_dict_key_values(my_dict, target_key):
    """
    Description: 
        This function count the values associated with key in a dictionary.
    Parameters:
        my_dict: dictionary
        target_key = key to be search
    Return:
        int: count of value
    """
    count = 0
    for key, value in my_dict.items():
        for ikey, ivalue in value.items():
            if ikey == target_key and ivalue == True:
                count += 1

    return count


def main():
    my_dict = {
        1: {'id': 1, 'success': True, 'name': 'Lary'}, 
        2: {'id': 2, 'success': False, 'name': 'Rabi'}, 
        3: {'id': 3, 'success': True, 'name': 'Alex'},
        4: {'id': 4, 'success': True, 'name': 'Ayush'},
        5: {'id': 5, 'success': True, 'name': 'Deven'}
    }


    key = input("Enter the key whose value needs to be counted: ")
    print(f"\nThe unique values in the dictionary are: {count_dict_key_values(my_dict, key)}")


if __name__ == "__main__":
    main()

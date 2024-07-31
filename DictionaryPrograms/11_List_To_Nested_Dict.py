'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title : Python program to convert a list into a nested dictionary of keys
    
'''


def list_to_nested_dict(word_list):
    """
    Description: 
        This function converts a list into a nested dictionary of keys.
    Parameters:
        word_list: The list to be converted.
    Return:
        dict: A nested dictionary created from the input list.
    """
    result = {}
    current = result
    for item in word_list:
        current[item] = {}
        current = current[item]
        
    return result


def main():
    # Example usage
    word_list = ['a', 'b', 'c', 'd']
    
    print("Original list:")
    print(word_list)

    nested_dict = list_to_nested_dict(word_list)
    
    print("\nNested dictionary:")
    print(nested_dict)

if __name__ == "__main__":
    main()
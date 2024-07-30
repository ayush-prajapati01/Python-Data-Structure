'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to concatenate all elements in a list into a string and return it.
    
'''


def concatenate_list_elements(lst):
    """
    Description:
        This function concatenates all elements in a list into a string.
    Parameters:
        lst: A list of elements to be concatenated.
    Return:
        str: A string of all concatenated elements.
    """
    return ''.join(map(str, lst))


lst = ['a', 'b', 'c', 1, 2, 3]
print("Concatenated string:", concatenate_list_elements(lst))
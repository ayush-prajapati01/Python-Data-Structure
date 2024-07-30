'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to display Documentation of In-built function
    
'''
 

import builtins


def print_doc(func_name):
    """
    Description: 
        This function returns the first and last colors from the given list.
    Parameters:
        color_list: A list containing color names.
    Return:
        tuple: A tuple containing the first and last colors.
    """
    func = getattr(builtins, func_name)
    if callable(func):
        print(func.__doc__)
    else:
        print(f"{func_name} is not a callable built-in function.")
        

def main():
    fun_name = input("Please enter the name of the function: ")
    print(print_doc(fun_name))


if __name__ == "__main__":
    main()
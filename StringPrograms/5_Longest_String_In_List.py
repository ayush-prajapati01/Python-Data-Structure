'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program that takes a list of words and 
            returns the length of the longest one.
    
''' 


def longest_string_length(str_list):
    """
    Description: 
        This function calculates length of longest string in a list
    Parameters:
        str_list: list of strings
    Return:
        int: length of longest string
    """
    len_longest_str = 0
    for str in str_list:
        if len(str) > len_longest_str:
            len_longest_str = len(str)
    
    return len_longest_str


def main():
    n = int(input("Enter number of element in the string list: "))
    str_list = []
    for index in range(n):
        str_list.append(input(f"Enter {index+1}th element: "))
    
    print(f"\nThe string list you entered is : {str_list}")
    print(f"The length of longest element in the above list is : {longest_string_length(str_list)}")


if __name__ == "__main__":
    main()
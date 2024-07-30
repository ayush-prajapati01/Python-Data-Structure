'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program that takes input from the user and 
            displays that input back in upper and lower cases.
    
''' 


def upper_lower_str(str):
    """
    Description: 
        This function return the upper and lower case of a string
    Parameters:
        str: A string
    Return:
        string
    """
    return str.upper(), str.lower()


def main():
    str_entered = input("Enter the value of string: ")

    upper_str, lower_str = upper_lower_str(str_entered)
    print(f"\nThe entered string {str_entered} in Upper case is {upper_str} and in Lower case is {lower_str}")


if __name__ == "__main__":
    main()
'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python Program to reverse a string.
    
''' 


def reverse_string(str):
    """
    Description: 
        This function used to reverse the string
    Parameters:
        str: It specfies the string to be reversed
    Return:
        string: reversed string

    """
    rev_str = ""
    for i in range(len(str)-1, -1, -1):
        rev_str += str[i] 
    
    return rev_str


def main():
    str_entered = input("Enter the value of the string: ")
    print(f"The reverse of the string is : {reverse_string(str_entered)}")


if __name__ == "__main__":
    main()
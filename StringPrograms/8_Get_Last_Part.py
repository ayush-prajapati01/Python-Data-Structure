'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python Program to get the last part of a string before a specified character
    
''' 


def last_part_str(str, char):
    """
    Description: 
        This function return last part of a string before a specified character
    Parameters:
        str: A string
    Return:
        string
    """
    for i in range(len(str)):
        if str[i] == char:
            return str[:i]
    
    return f"Char not found"


def main():
    str_entered = input("Enter the value of the string: ")
    char = input("Enter the char value: ")
    print(last_part_str(str_entered, char))


if __name__ == "__main__":
    main()
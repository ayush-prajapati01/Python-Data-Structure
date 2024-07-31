'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to get a string from a given string where all occurrences of its
            first char have been changed to '$', except the first char itself.
    
''' 


def replace_first_char_occ(str):
    """
    Description: 
        This function accepts a string and replace the first char occurences with '$'
    Parameters:
        str: The string 
    Return:
        string: updated string
    """
    char = str[0]
    updated_str = str[0] + str[1:].replace(char, '$')
    return updated_str


def main():
    str_entered = input("Enter a string value: ")

    print(f"\nThe orignal string is {str_entered}")
    print(f"The update string is {replace_first_char_occ(str_entered)}")


if __name__ == "__main__":
    main()


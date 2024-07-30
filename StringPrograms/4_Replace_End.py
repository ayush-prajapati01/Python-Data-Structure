'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to add 'ing' at the end of a given string. 
            If the given string already ends with 'ing' then add 'ly' instead.
    
''' 


def replace_end_str(str):
    """
    Description: 
        This function add 'ing' or 'ly'(if 'ing' already exist) to the end of the string 
    Parameters:
        str: The string 
    Return:
        string: updated string
    """
    if str.endswith('ing'):
        return str + "ly"
    else:
        return str + "ing"
    

def main():
    str_entered = input("Enter the string value: ")
    if len(str_entered) > 2:
        print(replace_end_str(str_entered))
    else:
        print(str_entered)


if __name__ == "__main__":
    main()

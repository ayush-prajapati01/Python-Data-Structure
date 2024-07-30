'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to calculate the length of a string.
    
'''


def length_of_str(str):
    """
    Description: 
        This function accepts a string and returns its length
    Parameters:
        str: The string 
    Return:
        int: Length of string
    """
    len_str = 0
    for element in str:
        len_str += 1
    
    return len_str


def main():
    str = input("Enter the string: ")

    # Method 1
    # print(f"The length of the string {str} is : {len(str)}") 

    # Method 2
    print(f"The length of the string {str} is : {length_of_str(str)}")


if __name__ == "__main__":
    main()
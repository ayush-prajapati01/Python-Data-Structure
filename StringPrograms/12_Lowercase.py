'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python Program to lowercase first n characters in a string.
    
''' 

def lowecase_first_n(str,n):
    """
    Description: 
        This function used to reverse the string
    Parameters:
        str: It specfies the string to be reversed
    Return:
        string: reversed string

    """
    return str[:n].lower() + str[n:]


def main():
    str_entered = input("Enter the value of the string: ")
    n = int(input("Enter the value of n: "))
    print(f"The reverse of the string is : {lowecase_first_n(str_entered, n)}")


if __name__ == "__main__":
    main()
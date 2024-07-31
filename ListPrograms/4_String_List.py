'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to count the number of strings 
            where the string length is 2 or more and the 
            first and last character are same from a given list of strings.
    
'''


def string_functions(str_list):
    """
    Description: 
        This function accepts a list and returns its sum
    Parameters:
        num_list: list containing integers 
    Return:
        int: sum of list
    """
    count = 0
    for str in str_list:
        if len(str) > 1 and str[0] == str[-1]:
            count += 1
        
    return count


def main():
    n = int(input("Enter number of elements in the list: "))
    str_list = []

    for index in range(n):
        str_list.append(input(f"Enter {index+1}th element: "))

    print(f"\n{string_functions(str_list)}")


if __name__ == "__main__":
    main()
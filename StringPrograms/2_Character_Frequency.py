'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title : Python program to count the character frequency in a string
    
'''


def char_frequency(str):
    """
    Description: 
        This function accepts a string and returns its length
    Parameters:
        str: The string 
    Return:
        int: Length of string
    """
    frequency = {}
    for char in str:
        count = 0
        for index in range(len(str)):
            if char == str[index]:
                count += 1
        
        frequency[char]= count
    
    return frequency


def main():
    str_entered = input("Enter the value of string: ")
    print(f"The character frequency of string {str_entered} is :",
          f"{char_frequency(str_entered)}")


if __name__ == "__main__":
    main()
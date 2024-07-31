'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to create a dictionary from a string.
            Note: Track the count of the letters from the string.
    
'''


def string_to_dict(word):
    """
    Description: 
        This function creates a dictionary from a string.
    Parameters:
        word: string to be converted
    Return:
        dictionary: dictionary from a string
    """
    string_dict = {}
    for char in word:
        if char in string_dict:
            string_dict[char] += 1
        else:
            string_dict[char] = 1

    return string_dict


def main():
    word = input("Enter the word to be converted to dictionary: ")
    print(f"\nThe dictionary for the word {word} is: \n{string_to_dict(word)}")


if __name__ == "__main__":
    main()



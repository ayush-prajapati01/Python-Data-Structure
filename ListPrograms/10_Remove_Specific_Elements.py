'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to print a specified list after removing the 0th, 4th and
            5th elements.

'''


def remove_specified_element(word_list):
    """
    Description: 
        This function returns list after removing the 0th, 4th and
        5th elements.
    Parameters:
        word_list: The list containing words.
    Return:
        list: updated word list
    """
    updated_word_list = []

    for index in range(len(word_list)):
        if(index == 0):
            pass
        elif(index == 4):
            pass
        elif(index == 5):
            pass
        else:
            updated_word_list.append(word_list[index])    

    return updated_word_list
             

def main():
    word_list = input("Enter items for the first list (space-separated): ").split()
    
    print(f"The orignal word list is: {word_list}")
    print(f"The updated word list is: {remove_specified_element(word_list)}")


if __name__ == "__main__":
    main()
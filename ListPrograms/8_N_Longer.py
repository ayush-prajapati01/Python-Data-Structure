'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to find the list of words that are longer than n from a
            given list of words.
    
'''


def n_longer_words(str_list, n):
    """
    Description: 
        This function accepts a list and returns list of words that are longer than n
    Parameters:
        str_list: list containing words
        n: The length of required strings 
    Return:
        list: list of words greater than n
    """
    n_longer_list = []
    for str in str_list:
        if len(str) > n:
            n_longer_list.append(str)
    
    return n_longer_list


def main():
    n = int(input("Enter the length n: "))
    str_list = input("Enter words (space-separated): ").split()
    print(f"The words in the lost longer than {n} are: \n{n_longer_words(str_list, n)}")


if __name__ == "__main__":
    main()

'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024  
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title : Python program to split a list based on first character of word

'''


def split_list_by_first_char(words):
    """
    Description: 
        This function splits a list of words based on their first character.
    Parameters:
        words: A list of words to be split.
    Return:
        dict: A dictionary where keys are first characters and values are lists of words.
    """
    result = {}
    for word in words:
        if word:
            first_char = word[0].lower()
            if first_char in result:
                result[first_char].append(word)
            else:
                result[first_char] = [word]
    return result


def main():
    input_words = input("Enter words (space-separated): ").split()

    split_words = split_list_by_first_char(input_words)
    print(split_words)


if __name__ == "__main__":
    main()

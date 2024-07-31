'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Write a Python program that accepts a comma separated sequence of words as input
            and prints the unique words in sorted form
    
''' 


def sort_list_alphabetically(str_list):
    return sorted(str_list)


def main():
    str_entered = input("Enter the string separated by comma: ")
    str_list = [str.strip() for str in str_entered.split(",")]
    print(sort_list_alphabetically(str_list))


if __name__ == "__main__":
    main()
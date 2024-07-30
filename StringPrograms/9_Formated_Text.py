'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python Program to display formatted text (width=50) as output.
    
''' 


import textwrap


def formatted_text(paragraph):
    """
    Description: 
        This function return formatted text of width 50
    Parameters:
        paragraph: The paragraph to be formatted
    Return:
        string: formatted paragraph
    """
    return textwrap.fill(paragraph, width=50)


def main():
    paragraph = input("Enter a paragraph : \n")
    print(f"\n{formatted_text(paragraph)}")


if __name__ == "__main__":
    main()
    
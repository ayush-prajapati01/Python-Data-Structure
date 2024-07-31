'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to generate and print a dictionary that contains a
            number (between 1 and n) in the form (x, x*x).
    
'''


def n_square_dictionary(n):
    """
    Description: 
        This function generates dictionary based on square of n
    Parameters:
        n: number of elements and square till n
    Return:
        dictionary
    """
    n_square_dict = {}
    for num in range(1, n+1):
        n_square_dict.update({num : num ** 2})

    return n_square_dict


def main():
    n = int(input("Enter a number: "))
    print(f"The generated dictionary for number {n} is {n_square_dictionary(n)}")


if __name__ == "__main__":
    main()
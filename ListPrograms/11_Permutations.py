'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: PPython program to generate all permutations of a list in Python.
    
'''


def list_permutations(num_list):
    """
    Description: 
        This function that gives permutations of the given list
    Parameters:
        num_list: list containing numbers 
    Return:
        none
    """
    for start in range(len(num_list)):
        for end in range(start, len(num_list)+1):
            if start < end:
                print(num_list[start:end])


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list = []

    for index in range(n):
        num_list.append(int(input(f"Enter {index+1}th element: ")))

    print(f"\nThe list entered is : {num_list}")
    print(f"The permutations of the list is : {list_permutations(num_list)}")


if __name__ == "__main__":
    main()

'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to use a Frozen Set
    
'''


def create_frozen_set(num_set):
    """
    Description: 
        This function coverts the set into frozen set
    Parameters:
        set1: The set to clear
    Return:
        set:frozen set
    """
    return frozenset(num_set)


def main():
    num_elements = int(input("Enter the number of elements in the set: "))
    my_set = set()
    for _ in range(num_elements):
        element = input("Enter an element: ")
        my_set.add(element)
    
    print(f"\n{create_frozen_set(my_set)}")


if __name__ == "__main__":
    main()
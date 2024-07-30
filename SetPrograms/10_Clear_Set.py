'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to clear a set.
    
'''


def clear_set(set1):
    """
    Description: 
        This function clears the set
    Parameters:
        set1: The set to clear
    Return:
        set:empty set
    """
    empty_set = ()
    set1 = empty_set
    return set1


def main():
    set1 = {1, 2, 3, 4, 5}
    print(f"The clear set is: {clear_set(set1)}")


if __name__ == "__main__":
    main()
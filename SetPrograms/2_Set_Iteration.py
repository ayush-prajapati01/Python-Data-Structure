'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to iteration over sets.
    
'''


def iterate_set(myset):
    """
    Description: 
        This function iterates a set and prints the element
    Parameters:
        set: The set to be iterated
    Return:
        None
    """
    for element in myset:
        print(element)


def main():
    myset = {'java', 'python', 'javascript', 'c++', 'rust'}
    print(f"The elements in my set are : \n{iterate_set(myset)}")


if __name__ == "__main__":
    main()
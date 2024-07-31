'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to create a set
    
'''


def create_set():
    """
    Description: 
        This function creates a set
    Parameters:
        None
    Return:
        set
    """
    num_elements = int(input("Enter the number of elements in the set: "))
    new_set = set()
    for _ in range(num_elements):
        element = input("Enter an element: ")
        new_set.add(element)
    return new_set


def main():
    # myset = {'java', 'python', 'javascript', 'c++', 'rust'}
    myset = create_set()
    print(f"The set is {myset} and is of type {type(myset)}")


if __name__ == "__main__":
    main()
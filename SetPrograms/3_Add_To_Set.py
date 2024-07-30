'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to add member(s) in a set.
    
'''


def add_member(word_set, add_elements_list):
    """
    Description: 
        This function add the element in the set
    Parameters:
        word_set: The set to be iterated
        add_elements_list: The list of elements to be addded
    Return:
        set: Updated set
    """
    for element in add_elements_list:
        word_set.add(element)
    
    return word_set


def main():
    myset = {'java', 'python', 'javascript', 'c++', 'rust'}
    n = int(input("Enter number of elements to add: "))
    add_elements = []
    for index in range(n):
        add_elements.append(input(f"Enter {index+1}st element to add: "))
    
    print(f"The updated set is {add_member(myset, add_elements)}")


if __name__ == "__main__":
    main()
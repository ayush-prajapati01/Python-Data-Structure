'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to create a symmetric difference.
    
'''


def set_symmetric_difference(set1, set2):
    """
    Description: 
        This function get the set symmetric difference
    Parameters:
        set1, set2: The sets for symmetric difference
    Return:
        set: symmetric difference of two set
    """
    # symmetric_difference_set = set1.symmetric_difference(set2)
    intersection = set()
    symmetric_difference_set = set()
    for num in set1:
        if num in set2:
            intersection.add(num)
    
    for num in set1:
        if num not in intersection:
            symmetric_difference_set.add(num)
  
    for num in set2:
        if num not in intersection:
            symmetric_difference_set.add(num)
  
    return symmetric_difference_set


def main():
    set1 = {1, 2, 3, 4}
    set2 = {1, 2, 5}
    print(f"The symmentric difference of {set1} and {set2} is {set_symmetric_difference(set1,set2)}")


if __name__ == "__main__":
    main()
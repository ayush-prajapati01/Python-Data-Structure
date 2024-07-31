'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to find set difference.
    
'''


def set_difference(set1, set2):
    """
    Description: 
        This function get the set difference
    Parameters:
        set1, set2: The sets for difference
    Return:
        set: difference of set1 and set2
    """
    for num in set2:
        if num in set1:
            set1.remove(num)
    
    return set1


def main():
    set1 = {1, 2, 3, 4}
    set2 = {1, 2, 5}
    print(f"The union of {set1} and {set2} is {set_difference(set1,set2)}")


if __name__ == "__main__":
    main()
'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to create an union of sets.
    
'''


def set_union(set1, set2):
    """
    Description: 
        This function get the set intersection
    Parameters:
        set1, set2: The sets for intersection
    Return:
        set: intersection of two set
    """
    updated_set = set1.union(set2)
    # updated_set = set()
    # for num in set1:
    #     if num in set2:
    #         updated_set.add(num)

    return updated_set


def main():
    set1 = {1, 2, 3, 4}
    set2 = {1, 2, 5}
    print(f"The union of {set1} and {set2} is {set_union(set1,set2)}")


if __name__ == "__main__":
    main()
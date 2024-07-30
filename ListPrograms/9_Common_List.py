'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to check common element present in two list

'''


def common_element(lst1, lst2):
    """
    Description: 
        This function that takes two lists and returns True if they have at
        least one common member.
    Parameters:
        str_list: list containing words
        n: The length of required strings 
    Return:
        list: list of words greater than n
    """
    for num in lst1:
        if num in lst2:
            return True
    
    return False


def main():
    n = int(input("Enter number of elements in the list: "))
    num_list1 = []
    num_list2 = []

    for index in range(n):
        num_list1.append(int(input(f"Enter {index+1}th element for list 1: ")))

    print("For list 2: ")
    for index in range(n):
        num_list2.append(int(input(f"Enter {index+1}th element for list 2: ")))
    
    if common_element(num_list1, num_list2):
        print("Yes, Common Element Exists")
    else:
        print("No, Common Element doesnt Exists")

if __name__ == "__main__":
    main()

'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to reverse the order of the items in the array.
    
'''


import array as arr


def reverse_arr(num_arr):
    """
    Description: 
        This function accepts a array and returns reversed array
    Parameters:
        num_arr: The number array
    Return:
        array: The reversed array
    """
    rev_arr = arr.array('i', [])
    for index in range(len(num_arr)-1, -1, -1):
        rev_arr.append(num_arr[index])

    return rev_arr


def main():
    n = int(input("Enter number of elements in the list: "))
    num_arr = arr.array('i', [])
    for index in range(n):
        num_arr.insert(index, int(input(f"Enter the {index+1}th element: ")))
    
    print(f"\nThe orignal array is: {num_arr}")
    print(f"The reversed array is: {reverse_arr(num_arr)}")
    

if __name__ == "__main__":
    main()
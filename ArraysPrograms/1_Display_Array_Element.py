'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to create an array of integers and display the array items.
    
'''


import array as arr


def display_arr_elements(num_array):
    """
    Description: 
        This function accepts a array and returns the array items
    Parameters:
        num_list: The number listarray
    Return:
        None
    """
    for index in range(len(num_array)):
        print(f"The element at {index}th index is {num_array[index]}")


def main():
    n = int(input("Enter number of elements in the array: "))
    num_array = arr.array('i', [])
    for index in range(n):
        num_array.insert(index, int(input(f"Enter {index+1}th element of the array: ")))
    
    print("")
    display_arr_elements(num_array)


if __name__ == "__main__":
    main()
'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title: Python program to to remove the first occurrence of a specified element from an array
    
'''


import array as arr


def remove_first_occurence(num_arr, element):
    """
    Description: 
        This function remove the first occurrence of a specified element from an array
    Parameters:
        num_arr: The number array
        element: The number to be searched
    Return:
        array: updated array with first occurrence removed
    """
    updated_num_arr = arr.array('i', [])
    count = 0
    for index in range(len(num_arr)):
        if element == num_arr[index] and count == 0:
            count += 1
        else:
            updated_num_arr.append(num_arr[index])

    return updated_num_arr


def main():
    n = int(input("Enter number of elements in the list: "))
    num_arr = arr.array('i', [])
    for index in range(n):
        num_arr.insert(index, int(input(f"Enter the {index+1}th element: ")))
    print(f"\nThe  array entered is: {num_arr}")

    remove_num = int(input("\nEnter the element 1st occurence to be removed: "))
    print(f"The number of occurences of {remove_num} is: {remove_first_occurence(num_arr, remove_num)}")


if __name__ == "__main__":
    main()
    
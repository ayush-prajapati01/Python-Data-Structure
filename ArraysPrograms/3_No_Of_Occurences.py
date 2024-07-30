'''

    @Author: Ayush Prajapati
    @Date: 26-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 26-07-2024 
    @Title : Python program to get the number of occurrences of specified element in an array
    
'''


import array as arr


def no_of_occurences(num_arr, element):
    """
    Description: 
        This function returns number of occurences of a element in an array
    Parameters:
        num_arr: The number array
        element: The number to be searched
    Return:
        count: number of occurences of a element
    """
    count = 0
    for index in range(len(num_arr)):
        if element == num_arr[index]:
            count += 1
    
    return count


def main():
    n = int(input("Enter number of elements in the list: "))
    num_arr = arr.array('i', [])
    for index in range(n):
        num_arr.insert(index, int(input(f"Enter the {index+1}th element: ")))
    print(f"\nThe  array entered is: {num_arr}")

    search_num = int(input("\nEnter the element to searched: "))
    print(f"The number of occurences of {search_num} is: {no_of_occurences(num_arr, search_num)}")


if __name__ == "__main__":
    main()
    
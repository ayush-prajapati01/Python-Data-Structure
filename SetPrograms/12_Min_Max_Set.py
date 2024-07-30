'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to find maximum and the minimum value in a set.
    
'''

def min_max_number(num_set):
    """
    Description: 
        This function finds maximum and minimum value in a set
    Parameters:
        num_set: The set containing int values
    Return:
        int: min and max value
    """
    min = 2 ** 31
    max = 2 ** -31

    for num in num_set:
        if num < min:
            min = num

        if num > max:
            max = num
    
    return min, max


def main():
    num_elements = int(input("Enter the number of elements in the set: "))
    my_set = set()
    for _ in range(num_elements):
        element = int(input("Enter an integer element: "))
        my_set.add(element)

    min_num, max_num = min_max_number(my_set)
    print(f"\nThe set is {my_set}")
    print(f"The minimum number in the set is {min_num} and maximum number in the set is {max_num}")


if __name__ == "__main__":
    main()
    

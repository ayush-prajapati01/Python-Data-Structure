'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024  
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to get a list, sorted in increasing order by the last
            element in each tuple from a given list of non-empty tuples.
    
'''


def sort_list_tuple(num_list):
    """
    Description: 
        This function sortes in increasing order by the last
            element in each tuple from a given list of non-empty tuples.
    Parameters:
        num_list: The list containing numbers.
    Return:
        list: updated num list
    """
    for i in range(len(num_list)-1):
        for j in range(i, len(num_list)):
            if num_list[i][-1] > num_list[j][-1]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp
    
    return num_list


def main():
    num_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(f"Sorted list as per last element of tupple: {sort_list_tuple(num_list)}")


if __name__ == "__main__":
    main()
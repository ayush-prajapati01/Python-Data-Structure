'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to find the repeated items of a tuple.
    
'''

def find_repeated_items(numbers):
    """
    Description: 
        This function finds repeated items in a tuple
    Parameters:
        numbers: the tuple containing numbers
    Return:
        list: A list containing repeated items
    """
    repeated_num = []
    for num in numbers:
        count = 0
        for index in range(len(numbers)):
            if num == numbers[index]:
                count += 1
        
        if count > 1:
            if num not in repeated_num:
                repeated_num.append(num)
    
    return repeated_num


def main():
    numbers = (1,2,1,2,4,6,7)
    print(f"Orignal Tuple: {numbers}")
    print(f"The repeated numbers in the tuple are: {find_repeated_items(numbers)}")


if __name__ == "__main__":
    main()

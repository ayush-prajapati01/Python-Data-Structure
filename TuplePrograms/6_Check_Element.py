'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to check whether an element exists within a tuple.
    
'''

def check_element_exist(numbers, check_num):
    """
    Description: 
        This function to check whether an element exists within a tuple.
    Parameters:
        numbers: the tuple containing numbers
    Return:
        boolean: Exist or not
    """
    for num in numbers:
        if num == check_num:
            return True
    return False



def main():
    numbers = (1,2,1,2,4,6,7)
    num_entered = int(input("Enter number to be checked: "))
    print(f"Orignal Tuple: {numbers}")
    print(f"The number exist in tuple?: {check_element_exist(numbers, num_entered)}")


if __name__ == "__main__":
    main()

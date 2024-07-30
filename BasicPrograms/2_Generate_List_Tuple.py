'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to Generate a list and a tuple with user entered numbers.
    
'''


def generate_list_and_tuple(numbers):
    """
    Description: 
        This function accepts a sequence of numbers and generates a list and a tuple.
    Parameters:
        numbers: A string containing comma-separated numbers.
    Return:
        list: A list of the numbers.
        tuple: A tuple of the numbers.
    """
    num_list = [int(num.strip()) for num in numbers.split(',')]
    num_tuple = tuple(num_list)
    return num_list, num_tuple


def main():
    user_input = input("Enter a sequence of comma-separated numbers: ")
    num_list, num_tuple = generate_list_and_tuple(user_input)
    print(f"List: {num_list}")
    print(f"Tuple: {num_tuple}")


if __name__ == "__main__":
    main()

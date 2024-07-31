'''

    @Author: Ayush Prajapati
    @Date: 30-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 30-07-2024 
    @Title: Python program to generate and print a dictionary that contains a
            number (between 1 and n) in the form (x, x*x).
    
'''


def main():
    num_entries = int(input("Enter the number of key-value pairs for dictionary: "))
    my_dict = {}
    for _ in range(num_entries):
        key = int(input("Enter Key : "))
        value = input("Enter value: ")
        my_dict[key] = value

    print(f"The entered dictionary is: {my_dict}")
    key = int(input("\nEnter the key to deleted from the dictionary: "))
    my_dict.pop(key)
    print(f"\nThe updated dictionary is: {my_dict}")


if __name__ == "__main__":
    main()

     


'''

    @Author: Ayush Prajapati
    @Date: 27-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 27-07-2024 
    @Title: Python program to clone or copy a list.
    
'''

def main():
    n = int(input("Enter number of elements in the list: "))
    num_list = []

    for index in range(n):
        num_list.append(int(input(f"Enter {index+1}th element: ")))

    print(f"\nThe list entered is : {num_list}")

    # cloned_list = num_list[:]
    cloned_list = list(num_list)
    # cloned_list = num_list.copy() 
    print(f"The cloned list is : {cloned_list}")


if __name__ == "__main__":
    main()
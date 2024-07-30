'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to check whether a specified value is contained in a group of values.  
    
'''


def check_in_list(num_list, num):
    for element in num_list:
        if num == element:
            return True
        
    return False


def main():
    n = int(input("Input number of element in the list: "))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f"Enter {i+1}th element: ")))
    
    num = int(input("Enter number to be checked: "))
    
    if check_in_list(num_list, num):
        print(f"\nThe number {num} is present in the list")
    else:
        print(f"\nThe number {num} is Not present in the list")
        

if __name__ == "__main__":
    main()
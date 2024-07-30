'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to display a histogram
    
'''

def create_histogram(integers):
    """
    Description:
        This function creates a histogram from a given list of integers.
    Parameters:
        integers: A list of integers.
    Return:
  
    """
    for i in integers:
        print(f"{'+' * i}")


def main():
    n = int(input("Input number of element in the list: "))
    num_list = []
    for i in range(n):
        num_list.append(int(input(f"Enter {i+1}th element: ")))

    print("Histogram:", create_histogram(num_list))

        

if __name__ == "__main__":
    main()
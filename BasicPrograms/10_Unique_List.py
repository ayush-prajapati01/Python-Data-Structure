'''

    @Author: Ayush Prajapati
    @Date: 25-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to check whether a specified value is contained in a group of values.  
    
'''

def unique_lst(lst1, lst2):
    unique = []
    for element in lst1:
        if element not in lst2:
            unique.append(element)
    
    return unique


def main():
    color_list_1 = set(["White", "Black", "Red"])  
    color_list_2 = set(["Red", "Green"]) 
    
    print(unique_lst(color_list_1, color_list_2))
    

if __name__ == "__main__":
    main()


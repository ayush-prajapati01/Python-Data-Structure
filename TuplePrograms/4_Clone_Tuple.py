'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to create the clone of a tuple.
    
'''

def main():
    my_tuple = ('python', 'ruby', 'c++', 'java', 'rust', 'javascript')

    cloned_tuple = my_tuple[:]

    print(f"The orignal tuple is {my_tuple}")
    print(f"The cloned tuple is {cloned_tuple}")


if __name__ == "__main__":
    main()

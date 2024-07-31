'''

    @Author: Ayush Prajapati
    @Date: 29-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 29-07-2024 
    @Title: Python program to unpack a tuple in several variables.
    
'''

def main():
    fruits = ("Grapes", "banana", "strawberry", "orange")
    (green_fruit, yellow_fruit, red_fruit, orange_fruit) = fruits

    print(f"Unpacking tupple {fruits} values: ")
    print(green_fruit)
    print(yellow_fruit)
    print(red_fruit)
    print(orange_fruit)


if __name__ == "__main__":
    main()



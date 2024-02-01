import os 
import sys 
from Add_Task import AddTask  

if __name__ == "__main__":

    while True:
        print("1. Add Task")
        print("2. Exit")
        choice = int(input("Enter Choice : "))
        if choice == 1: 
            add_obj = AddTask()
            task = input('Enter task description :')
            add_obj.add(task)  
            print(f'{task} added Successfully..') 
        elif choice == 2: 
            sys.exit() 
        
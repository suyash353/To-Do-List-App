import os 
import sys 
import pandas as pd 


class complete_task:
    def __init__(self):
        self.df = pd.read_csv('Task.csv') 

    def list_tasks(self):
        print(self.df['Task_desc'].to_string(index=False))
        
    
    def remove_task(self):
        if self.df.empty :
            print("Task Is not Present !")
        else :
            x = int(input("Enter Number task is present :"))
            if x <= len(self.df):
                df = self.df.drop(x-1)  
                df.to_csv('Task.csv',index=False,index_label=False) 
                print(f'Task {self.df["Task_desc"][x-1]} removed Successfully..')
            else :
                print("Enter invalid input ! ") 
            
        

import os 
import sys 
import pandas as pd 



class AddTask:
    def __init__(self):
        self.task_dict = {'Tasks':[]} 

    def add(self,description):
        self.task_dict['Tasks'].append(description)
        df = pd.DataFrame(self.task_dict) 

        task_file_path = os.path.exists('Task.csv') 
        if task_file_path :
            old_task = pd.read_csv('Task.csv')
            new_task = pd.concat([old_task,df],axis=0)
            new_task.to_csv('Task.csv',index=False) 
        else :
            df.to_csv('Task.csv',index=False) 


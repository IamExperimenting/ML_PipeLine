import pandas as pd, numpy as np 


class Falconheavyfeatengg:
    def __init__(self,train_data,test_data,num_col,cat_col):
        self.train_data = train_data
        self.test_data = test_data
        self.num_col = num_col
        self.cat_col = cat_col
    
    def train_test_data_validation(self):

        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'

        train_copy = self.train_data.values
        test_copy = self.test_data.values
        num_train_stats = {}
        nume_test_stats = {}

        out_of_range = 0
        for n_col in self.num_col:
            min_train_val = train_copy[:,self.train_data.columns.get_loc(n_col)].min()
            max_train_val = train_copy[:,self.train_data.columns.get_loc(n_col)].max()
            min_test_val = test_copy[:,self.test_data.columns.get_loc(n_col)].min()
            max_test_val = test_copy[:,self.test_data.columns.get_loc(n_col)].max()
            if (min_test_val < min_train_val) or (max_test_val > max_train_val):
                print(f"{FAIL}Test column {n_col} is out of range.")
                out_of_range += 1
            
            num_train_stats.update({n_col:{'min':min_train_val,'max':max_train_val}})
            nume_test_stats.update({n_col:{'min':min_test_val,'max':max_test_val}})
        if out_of_range == 0:
            print(f"{OKGREEN} Good to go with all test numerical columns")
        
        print("-------------------------------------------")
        
        higher_cat_value = 0
        for c_col in cat_col:
            train_cat_count = len(set(train_copy[:,self.train_data.columns.get_loc(c_col)]))
            test_cat_count = len(set(test_copy[:,self.test_data.columns.get_loc(c_col)]))

            if test_cat_count > train_cat_count:
                print(f"{FAIL}Test column {c_col} has higher unique value.")
                higher_cat_value += 1
            
        if higher_cat_value==0:
            print(f"{OKGREEN} Good to go with all test categorical columns")


        return num_train_stats,nume_test_stats
    

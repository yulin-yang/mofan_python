import numpy as np
import pandas as pd

action_space = ['name', 'age']
table_data = {'name': ['jack', 'rose', 'tom'], 'age': [12, 13, 14]}

q_table = pd.DataFrame(table_data)

if __name__ == '__main__':

    print(q_table, '\n ---------------------')
    print(q_table.loc[0])

import pandas as pd
import numpy as np
import random

def select_cell_semi_randomly():
    csv_file = "C:/Users/newby/Programming/Bots/randomItemSelctor/data.csv"
    df = pd.read_csv(csv_file)
    probabilities = [0.25, 0.25, 0.2, 0.17, 0.11, 0.01]

    if len(probabilities) != len(df.columns):
        raise ValueError("The number of probabilities must be equal to the number of columns in the CSV file.")

    probabilities = np.array(probabilities) / sum(probabilities)
    choice_column = np.random.choice(df.columns, p=probabilities)
    possible_values = df[choice_column].dropna().tolist()
    
    selected_value = random.choice(possible_values)
    return str(choice_column) + " Item: " + str(selected_value)
    


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Paste print code here:
print(user_data.head(15))

# Paste merge code here:
new_df = pd.merge(user_data, pop_data)

# Paste location code here:
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

print(new_df.head(15))

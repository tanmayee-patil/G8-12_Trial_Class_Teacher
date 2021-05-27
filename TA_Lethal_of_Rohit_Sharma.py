import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("Rohit_truncated_ball_by_ball.csv")
df.head()

# filter the dataset selecting only observation where player_dismissed == "RG Sharma" and assign he resulting dataset to df_Rohit

#group the dataset on ball and assign it to df_Rohit_dismissed. Aggregation for rest of the values should be based on count function

#plot a bar graph showing number of times player was dismissed per ball of an over.

#group the dataset on ball and assign it to df_runs_per_ball. Aggregation for rest of the values should be based on sum function

#plot a bar graph showing runs scored per ball of an over by Rohit Sharma.


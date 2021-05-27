#!/usr/bin/env python
# coding: utf-8

# # DATA ANALYSIS and VISUALIZATION

# ### Data
# 
# _What is **Data**?_<br>
# **Data** is hard facts. These are units of information, often numeric, that are collected through observation.
# 
# The "data gets broadly divided into 2 kinds:
# 1. Qualitative or Categorical data
# 2. Quantitative or Numerical data
# 
# **Categorical data** comprises categories like *overweight*, *underweight*, or *normal* on a BMI scale as categories.<br>
# Similarly, it could be the flavor of ice cream. Categories could be *mango*, *vanilla*, *chocolate*, *pineapple*, *orange*, etc
# 
# **Numerical data** on the other hand is your numeric data like your actual *weight*, *height*, volume of your *ice cream* etc.

# ### Data Analysis
# 
# _What is **Data Analysis**?_<br>
# **Data Analysis** is the process of evaluating data by applying statistical and/or logical techniques.
# *Data Analysis* involves:
# 1. Performing *data cleaning/data wrangling* to improve data quality.
# 2. Getting data into the right format, getting rid of unnecessary data, correcting spelling mistakes, etc.
# 3. *Manipulating* data using tools like Excel or Python etc. This may include plotting the data out, creating pivot tables, and so on.
# 4. *Analyzing* and *interpreting* the data using statistical tools (i.e. finding correlations, trends, outliers, etc.).

# ### Data Visualization
# 
# _What is **Data Visualization**?_<br>
# **Data Visualization** is the representation of data or information in a graph, chart, or other visual formats.
# Understanding of data in the raw form or tables would consume a lot of time and effort of stakeholders, readers, users. Above that it would be extremely hard to interpret the main message in that form.
# 
# Instead, if we choose a graphical representation, we would use charts and graphs and infographics to express those messages, trends.
# 
# ![image.png](attachment:image.png)
# Note: ***USE IMAGE OF SIMILAR TO THIS HERE*** to depict Data visulization
# 
# In above image, even though the data is less, we are easily attracted towards graphic representation of the table. On top of that it is easy to interpret as well.

# ___
# 

# ## Teacher's Activity: Understanding the lethal of Rohit Sharma
# 
# ### We will understand how productive or vulnerable was Rohit Gurunath Sharma on each ball of the over from a given dataset.
# 
# #### Understanding the Dataset
# 
# Dataset consists of 3 columns or `features` namely `ball`, `batsman_runs` and `player_dismissed`.
# 1. `ball` represents the ball of the over.
# 2. `batsman_runs` accounts for the runs attributed to batsman for that particular ball.
# 3. `player_dismissed` provides the name of player who was dismissed on a particular ball.
# 
# 
# #### Understanding the Approach
# 
# 1. Understanding the most vulnerable ball for Rohit Sharma: Here, we will take into account the number of times the player himself was dismissed on any given ball of the over. The columns we will use are: <br>
#     1. `player_dismissed` with entries specific to `RG Sharma`.
#     2. `ball`.
#     
#     _We will `group` the data on `ball` of the over and plot a `bar` graph to interpret the most number of dismissals for a particular ball of over_
#     
#     
# 2. Understanding the most productive ball for Rohit Sharma: Here, we will take into account total runs the player has scored was on any given ball of the over. The columns we will use are: <br>
#     1. `batsman_runs`.
#     2. `ball`.
#     
#     _We will `group` the data on `ball` of the over and plot a `bar` graph to interpret the most runs scored on a particular ball of over_

# #### Importing Packages
# 
# Packages are imported in following manner.<br>
# ```Python
# import package_name
# ```
# 
# In the next cell we have imported the following packages.
# 1. `pandas`. It is the most common library used by data scientists for data manipulation and cleaning
# 2. `numpy`. It adds support for arrays, along with a collection of mathematical functions to operate on these arrays.
# 3. `matplotlib`. It is a plotting library for python. `.pyplot` is a sub-package or set of functions available in matplotlib which we'll be using
# 
# `pd`,`np`,`plt` are all `aliases` for their corresponding packages.
# `Alias` are second name assigned to values or variables.
# 
# `%matplotlib inline` is a "magic function" renders plots

# In[130]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Loading the Dataset
# 
# In the cell below, we have created a new pandas DataFrame by the name `df` and imported the mentioned file. <br>
# We have used `.head()` function to see the first 5 values of the dataset we created.
# 
# `.head()` can show up any number of values based on the parameter given. <br>
# If we want to see more, we can pass value in the function like `df.head(10)` will show first 10 values of the dataset

# In[131]:


df = pd.read_csv("Rohit_truncated_ball_by_ball.csv")
df.head()


# ### 1. Understanding the most vulnerable ball for Rohit Sharma

# #### Reducing the dataset to our need
# 
# In the cell below, we have created a new pandas DataFrame by the name `df_Rohit` and assigned it a filtered version of dataframe `df` such that only those observations are accepted which have `player_dismissed` value as `RG Sharma`. This can be done like:
# ```Python
# df[df["player_dismissed"] == "RG Sharma"]
# ```
# Here, `df["player_dismissed"] == "RG Sharma"`, this value will mark observation True wherever it is.
# Passing that value through `df[]` will filter out the `False` values.
# 
# Then, we have grouped data using `.grouby()` function using various values of `ball` feature/column. The `groupby()` function is then followed by `.count()` to summarize values for other numerical columns in the dataframe. The resulting dataframe is then assigned to dataframe `df_Rohit_dismissed`.

# In[132]:


df_Rohit = df[df["player_dismissed"] == "RG Sharma"]
df_Rohit_dismissed = df_Rohit.groupby("ball").count()


# #### Plotting of information
# 
# `plt.title()` provides the graph or chart with a title. The title we have used is "Number of times player was dismissed on each ball of over".<br>
# `plt.bar()` function is used to plot bar chart. We have plotted bar chart for `df_Rohit_dismissed` dataframe's index value which are, infact, each ball of the over as categories or x-axis of the chart and the dismissals of Rohit Sharma as y-axis.<br>
# `plt.show()` function combines all the elements of charts and shows them in harmony.

# In[133]:


plt.title("Number of times player was dismissed on each ball of over")
plt.bar(df_Rohit_dismissed.index, df_Rohit_dismissed["player_dismissed"])
plt.show()


# ### 2. Understanding the most productive ball for Rohit Sharma

# #### Grouping of data
# 
# we have grouped data using `.grouby()` function using various values of `ball` feature/column. The `groupby()` function is then followed by `.sum()` to summarize values for other numerical columns in the dataframe. The resulting dataframe is then assigned to dataframe `df_runs_per_ball`.

# In[134]:


df_runs_per_ball = df.groupby("ball").sum()


# #### Plotting of information
# 
# `plt.title()` provides the graph or chart with a title.<br>
# `plt.bar()` function is used to plot bar chart. We have plotted bar chart for `df_runs_per_ball` dataframe's index value which are, infact, each ball of the over as categories or x-axis of the chart and the runs scored by Rohit Sharma as y-axis.<br>
# `plt.show()` function combines all the elements of charts and shows them in harmony.

# In[135]:


plt.title("Runs scored for each ball of over")
plt.bar(df_runs_per_ball.index, df_runs_per_ball["batsman_runs"])
plt.show()


# In[ ]:





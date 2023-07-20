#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import violinbox_solution_1


# We'll continue to make use of the fuel economy dataset in this workspace.

# In[2]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# ### Preparatory Step
# The cars in this dataset are categorized into one of five different vehicle classes based on size. Starting from the smallest, they are: `{Minicompact Cars, Subcompact Cars, Compact Cars, Midsize Cars, and Large Cars}`. 
# 
# 
# 
# ### **TO DO**: 
# 1. What is the relationship between the size of a car and the size of its engine? The vehicle classes can be found in the `VClass` column, while the engine sizes are in the `displ` column (in liters). 
# 
# **Hint**: Make sure that the order of vehicle classes makes sense in your plot!

# In[3]:


# Selecting relevant columns from the dataset
data = fuel_econ[['VClass', 'displ']]

# Defining the order of vehicle classes for the plot
class_order = ['Minicompact Cars', 'Subcompact Cars', 'Compact Cars', 'Midsize Cars', 'Large Cars']

# Creating a violin plot with seaborn
plt.figure(figsize=(10, 6))
sb.violinplot(data=data, x='VClass', y='displ', order=class_order, inner='quartile', palette='viridis')
plt.xticks(rotation=15)
plt.xlabel('Vehicle Class')
plt.ylabel('Engine Size (liters)')
plt.title('Relationship between Car Size and Engine Size')
plt.show()


# ### Expected Output

# In[4]:


# run this cell to check your work against ours
violinbox_solution_1()


# In[ ]:





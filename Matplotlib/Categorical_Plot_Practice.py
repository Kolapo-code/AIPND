#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import categorical_solution_1


# We'll continue to make use of the fuel economy dataset in this workspace.

# In[2]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# ###  **TO DO**
# Use a plot to explore whether or not there are differences in recommended fuel type depending on the vehicle class. Only investigate the difference between the two main fuel types found in the 'fuelType' variable: Regular Gasoline and Premium Gasoline. (The other fuel types represented in the dataset are of much lower frequency compared to the main two, that they'll be more distracting than informative.) 
# 
# 
# **Note**: The dataset as provided does not retain any of the sorting of the 'VClass' variable, so you will also need to copy over any code you used previously to sort the category levels.

# In[3]:


# Sort the vehicle class categories
vehicle_class_order = fuel_econ['VClass'].value_counts().index
fuel_econ['VClass'] = pd.Categorical(fuel_econ['VClass'], categories=vehicle_class_order, ordered=True)

# Filter the dataset to include only Regular Gasoline and Premium Gasoline
fuel_econ_filtered = fuel_econ[fuel_econ['fuelType'].isin(['Regular Gasoline', 'Premium Gasoline'])]

# Create the plot
plt.figure(figsize=[12, 6])
sb.countplot(data=fuel_econ_filtered, x='VClass', hue='fuelType')
plt.xticks(rotation=15)
plt.legend(title='Fuel Type')
plt.xlabel('Vehicle Class')
plt.ylabel('Count')
plt.title('Recommended Fuel Type by Vehicle Class')
plt.show()


# ### Expected Output

# In[4]:


# run this cell to check your work against ours
categorical_solution_1()


# In[ ]:





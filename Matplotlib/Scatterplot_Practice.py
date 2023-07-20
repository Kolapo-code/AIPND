#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import scatterplot_solution_1, scatterplot_solution_2


# In this workspace, you'll make use of this data set describing various car attributes, such as fuel efficiency. The cars in this dataset represent about 3900 sedans tested by the EPA from 2013 to 2018. This dataset is a trimmed-down version of the data found [here](https://catalog.data.gov/dataset/fuel-economy-data).

# In[2]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# ### **TO DO 1**: 
# Let's look at the relationship between fuel mileage ratings for city vs. highway driving, as stored in the 'city' and 'highway' variables (in miles per gallon, or mpg). **Use a _scatter plot_ to depict the data.**
# 1. What is the general relationship between these variables? 
# 2. Are there any points that appear unusual against these trends?

# In[9]:


# Scatter plot between city and highway fuel efficiency
plt.figure(figsize=(8, 6))
sb.regplot(data=fuel_econ, x='city', y='highway')
plt.xlabel('City Fuel Efficiency (mpg)')
plt.ylabel('Highway Fuel Efficiency (mpg)')
plt.title('City vs. Highway Fuel Efficiency')
plt.grid(True)
plt.show()


# ### Expected Output

# In[4]:


# run this cell to check your work against ours
scatterplot_solution_1()


# ### **TO DO 2**: 
# Let's look at the relationship between two other numeric variables. How does the engine size relate to a car's CO2 footprint? The 'displ' variable has the former (in liters), while the 'co2' variable has the latter (in grams per mile). **Use a heat map to depict the data.** How strong is this trend?

# In[14]:


# Heat map between engine size and CO2 footprint
plt.figure(figsize=(8, 6))
sb.heatmap(data=fuel_econ[['displ', 'co2']].corr(), annot=True, fmt=".2f", cmap='coolwarm', center=0)
plt.xlabel('Engine Size (liters)')
plt.ylabel('CO2 Footprint (grams per mile)')
plt.title('Engine Size vs. CO2 Footprint')
plt.show()


# ### Expected Output

# In[6]:


# run this cell to check your work against ours
scatterplot_solution_2()


# In[ ]:





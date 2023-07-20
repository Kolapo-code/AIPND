#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_biv import additionalplot_solution_1, additionalplot_solution_2


# We'll continue to make use of the fuel economy dataset in this workspace.

# In[2]:


fuel_econ = pd.read_csv('./data/fuel_econ.csv')
fuel_econ.head()


# ### **Task 1**: 
# Plot the distribution of combined fuel mileage (column 'comb', in miles per gallon) by manufacturer (column 'make'), for all manufacturers with at least eighty cars in the dataset. Consider which manufacturer order will convey the most information when constructing your final plot. 
# 
# **Hint**: Completing this exercise will take multiple steps! Add additional code cells as needed in order to achieve the goal.

# In[3]:


# Step 1: Filter manufacturers with at least 80 cars
car_counts = fuel_econ['make'].value_counts()
manufacturers_with_at_least_80_cars = car_counts[car_counts >= 80].index

# Step 2: Create a sub-dataframe containing only the relevant manufacturers
filtered_fuel_econ = fuel_econ[fuel_econ['make'].isin(manufacturers_with_at_least_80_cars)]

# Step 3: Plot the distribution of combined fuel mileage for each manufacturer
plt.figure(figsize=(12, 6))
sb.violinplot(data=filtered_fuel_econ, x='make', y='comb', inner='quartile')
plt.xticks(rotation=90)
plt.xlabel('Manufacturer')
plt.ylabel('Combined Fuel Mileage (mpg)')
plt.title('Distribution of Combined Fuel Mileage by Manufacturer (with at least 80 cars)')
plt.show()


# In[4]:


# run this cell to check your work against ours
additionalplot_solution_1()


# ### **Task 2**: 
# Continuing on from the previous task, plot the mean fuel efficiency for each manufacturer with at least 80 cars in the dataset.

# In[5]:


# Step 1: Filter manufacturers with at least 80 cars (same as Task 1)
car_counts = fuel_econ['make'].value_counts()
manufacturers_with_at_least_80_cars = car_counts[car_counts >= 80].index

# Step 2: Create a sub-dataframe containing only the relevant manufacturers (same as Task 1)
filtered_fuel_econ = fuel_econ[fuel_econ['make'].isin(manufacturers_with_at_least_80_cars)]

# Step 3: Calculate mean fuel efficiency for each manufacturer
mean_fuel_efficiency = filtered_fuel_econ.groupby('make')['comb'].mean().reset_index()

# Step 4: Plot the mean fuel efficiency for each manufacturer
plt.figure(figsize=(12, 6))
sb.barplot(data=mean_fuel_efficiency, x='make', y='comb')
plt.xticks(rotation=90)
plt.xlabel('Manufacturer')
plt.ylabel('Mean Combined Fuel Mileage (mpg)')
plt.title('Mean Combined Fuel Mileage by Manufacturer (with at least 80 cars)')
plt.show()


# In[6]:


# run this cell to check your work against ours
additionalplot_solution_2()


# In[ ]:





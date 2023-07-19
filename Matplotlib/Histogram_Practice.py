#!/usr/bin/env python
# coding: utf-8

# ### Preparatory Step

# In[1]:


# Prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

# The `solutions_univ.py` is a Python file available in the Notebook server that contains solution to the TO DO tasks.
# The solution to each task is present in a separate function in the `solutions_univ.py` file. 
# Do not refer to the file untill you attempt to write code yourself. 
from solutions_univ import histogram_solution_1


# ### About the Dataset
# We'll continue working with the Pokémon dataset in this workspace. The data was assembled from the database of information found in this [GitHub repository](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv).
# 

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# ### **TO DO Task**
# Pokémon have a number of different statistics that describe their combat capabilities. Here, create a _histogram_ that depicts the distribution of 'special-defense' values taken. 
# 
# **Hint**: Try playing around with different bin width sizes to see what best depicts the data.

# In[3]:


# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(pokemon['special-defense'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Special Defense')
plt.ylabel('Frequency')
plt.title('Distribution of Special Defense Values')
plt.grid(True)
plt.show()


# ### Expected Output
# **Your visualization does not need to be exactly the same as ours, but it should be able to come up with the same conclusions.**

# In[4]:


# run this cell to check your work against ours
histogram_solution_1()


# In[ ]:





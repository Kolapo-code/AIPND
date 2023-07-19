#!/usr/bin/env python
# coding: utf-8

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

from solutions_univ import scales_solution_1, scales_solution_2


# Once again, we make use of the Pokémon data for this exercise.

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# ## TO DO **Task 1**
# There are also variables in the dataset that don't have anything to do with the game mechanics, and are just there for flavor. Try plotting the distribution of Pokémon heights (given in meters). For this exercise, experiment with different axis limits as well as bin widths to see what gives the clearest view of the data.

# In[7]:


# Set up the figure and axes
plt.figure(figsize=(10, 6))
plt.title("Distribution of Pokémon Heights")
plt.xlabel("Height (meters)")
plt.ylabel("Frequency")

# Try different bin widths to see what gives the clearest view of the data
bin_widths = [0.1, 0.2, 0.5, 1.0]

for bin_width in bin_widths:
    # Plot the histogram with the current bin width
    plt.hist(pokemon['height'], bins=np.arange(0, pokemon['height'].max()+bin_width, bin_width), alpha=0.6, label=f"Bin Width = {bin_width}")

plt.legend()
plt.show()


# ## Expected Output: TO DO Task 1

# In[4]:


# run this cell to check your work against ours
scales_solution_1()


# ## TO DO **Task 2**
# In this task, you should plot the distribution of Pokémon weights (given in kilograms). Due to the very large range of values taken, you will probably want to perform an _axis transformation_ as part of your visualization workflow.

# In[8]:


# Set up the figure and axes
plt.figure(figsize=(10, 6))
plt.title("Distribution of Pokémon Weights")
plt.xlabel("Weight (kilograms)")
plt.ylabel("Frequency")

# Use a logarithmic scale for the x-axis (axis transformation) due to the large range of values
plt.xscale('log')

# Try different bin widths to see what gives the clearest view of the data
bin_widths = [1, 5, 10, 25]

for bin_width in bin_widths:
    # Plot the histogram with the current bin width
    plt.hist(pokemon['weight'], bins=np.arange(0, pokemon['weight'].max()+bin_width, bin_width), alpha=0.6, label=f"Bin Width = {bin_width}")

plt.legend()
plt.show()


# ## Expected Output: TO DO Task 2

# In[6]:


# run this cell to check your work against ours
scales_solution_2()


# In[ ]:





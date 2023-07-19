#!/usr/bin/env python
# coding: utf-8

# ## Introduction
# In workspaces like this one, you will be able to practice visualization techniques you've seen in the course materials. In this particular Jupyter Notebook, you'll practice creating single-variable plots for categorical data.
# 
# The cells where you are expected to contribute, are highlighted with **TO DO** markdown. 

# In[1]:


# prerequisite package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

# The `solutions_univ.py` is a Python file available in the Notebook server that contains solution to the TO DO tasks.
# The solution to each task is present in a separate function in the `solutions_univ.py` file. 
# Do not refer to the file untill you attempt to write code yourself. 
from solutions_univ import bar_chart_solution_1, bar_chart_solution_2


# ## About the Dataset
# In this workspace, you'll be working with the dataset comprised of attributes of creatures in the video game series Pokémon. The data was assembled from the database of information found in this [GitHub repository](https://github.com/veekun/pokedex/tree/master/pokedex/data/csv).

# In[2]:


pokemon = pd.read_csv('./data/pokemon.csv')
pokemon.head()


# ### **TO DO Task 1** 
# 1. Explore the `pokemon` dataframe, and try to understand the significance of each of its column.
# 2. There have been quite a few Pokémon introduced over the series' history. Display the count of Pokémon introduced in each generation? Create a _bar chart_ of these frequencies using the 'generation_id' column.

# In[3]:


# Task 1: Create a bar chart of Pokémon count introduced in each generation

# Group the data by 'generation_id' and count the number of occurrences in each group
generation_counts = pokemon['generation_id'].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
sb.barplot(x=generation_counts.index, y=generation_counts.values, palette='viridis')

# Add labels and title
plt.xlabel('Generation ID')
plt.ylabel('Number of Pokémon')
plt.title('Number of Pokémon Introduced in Each Generation')

# Show the plot
plt.show()


# ### Expected Output: TO DO Task 1

# Once you've created your chart, run the cell below to check the output from our solution. **Your visualization does not need to be exactly the same as ours, but it should be able to come up with the same conclusions.**

# In[4]:


# The function below has been defined in the `solutions_univ.py` file, that you can refer only when necessary. 
# This function contains the expected solution. 
bar_chart_solution_1()


# ### **TO DO Task 2** 
# 1. Each Pokémon species has either `type_1`, `type_2` or both `types` that play a part in its offensive and defensive capabilities. The code below creates a new dataframe `pkmn_types` that club the rows of both `type_1` and `type_2`, so that the resulting dataframe has **new** column, `type_level`. 
# 
# **Display, how frequent is each type?**
# 
# 
# 
# The function below will do the following in the pokemon dataframe *out of place*:
# 1. Select the 'id', and 'species' columns from pokemon. 
# 2. Remove the 'type_1', 'type_2' columns from pokemon
# 3. Add a new column 'type_level' that can have a value either 'type_1' or 'type_2'
# 4. Add another column 'type' that will contain the actual value contained in the 'type_1', 'type_2' columns. For example, the first row in the pokemon dataframe having `id=1`	and `species=bulbasaur` will now occur twice in the resulting dataframe after the `melt()` operation. The first occurrence will have `type=grass`, whereas, the second occurrence will have `type=poison`.

# In[5]:


pkmn_types = pokemon.melt(id_vars = ['id','species'], 
                          value_vars = ['type_1', 'type_2'], 
                          var_name = 'type_level', value_name = 'type').dropna()
pkmn_types.head()


# In[6]:


# Task 2: Create a relative frequency plot of Pokémon types

# Calculate the total number of Pokémon
total_pokemon = len(pkmn_types)

# Count the occurrences of each type
type_counts = pkmn_types['type'].value_counts()


# 2. Your task is to use this dataframe to create a _relative frequency_ plot of the proportion of Pokémon with each type, _sorted_ from most frequent to least. **Hint**: The sum across bars should be greater than 100%, since many Pokémon have two types. Keep this in mind when considering a denominator to compute relative frequencies.

# In[7]:


# Calculate the relative frequencies
relative_frequencies = type_counts / total_pokemon

# Sort the types by their relative frequencies in descending order
sorted_types = relative_frequencies.sort_values(ascending=False)

# Create a bar chart
plt.figure(figsize=(12, 6))
sb.barplot(x=sorted_types.index, y=sorted_types.values, palette='pastel')

# Add labels and title
plt.xlabel('Pokémon Type')
plt.ylabel('Relative Frequency')
plt.title('Relative Frequency of Pokémon Types')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()


# ### Expected Output: TO DO Task 2

# In[8]:


# The function below has been defined in the `solutions_univ.py` file, that you can refer only when necessary. 
# This function contains the expected solution. 
bar_chart_solution_2()


# If you're interested in seeing the code used to generate the solution plots, you can find it in the `solutions_univ.py` script in the workspace folder. You can navigate there by clicking on the Jupyter icon in the upper left corner of the workspace. Spoiler warning: the script contains solutions for all of the workspace exercises in this lesson, so take care not to spoil your practice!

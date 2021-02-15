#!/usr/bin/env python
# coding: utf-8

# # Assignment \#8 the Gapminder dataset 2/2
# 
# **Please read carefully all this introduction prior to get into the assignment.**
# 
# There are 4 files for this assignment:
# - `population_total.csv`: total population, per country and per year (1800 to 2018)
# - `life_expectancy_years.csv`: life expectancy, per country and per year (1800 to 2018)
# - `income_per_person.csv`: income per person, per country and per year (1800 to 2018)
# - `countries_total.csv`: countries and regions (Asia, Europe, Africa, Oceania, Americas)
# 
# As usual the files must be along with your notebook and not in a dedicated folder.

# **Important note about the `geo` columns accross the `DataFrame` objects**: 
# - The 3 first files contain a field named `geo` with the names of the different countries. The last file contains also a column with the different countries. It is renamed to `geo` on load to ease the merges that would have to be performed (option `on='geo'` of `merge()` function or `join()` method).
# - The name of the countries have to be processed as is, without trying to homogenize them accross the different files.
# - In order to avoid discrepancies between results, all joins should be performed by using the `how='inner'`option.

# **Hint about the `python_data_science_1` and `python_data_science_2` notebooks**
# 
# - The 7 following questions in parts A and B rely on materials that will be studied in the notebook `python_data_science_1`: 1, 4 and 7 to 11
# - The 8 following questions in parts A and B rely on materials that will be studied in the notebook `python_data_science_2`: 2 to 3, 5 to 6 and 13 to 15

# **Caution**: Questions asking to return a floating point number (ratio, mean, percentage) should round it to 1 decimal place:
# - Such questions are marked with `(°)`
# - For instance, if the variable `result` is a floting point number, e.g. `3.14159265359`
# - The functions should return `round(result, 1)` instead of `result`, e.g. `3.1`
# - Percentages should be returned as floating point numbers (not with the % mark).

# **Last warning:** Do not use the `ìnplace = True` option when doing any manipulations of a `DataFrame`:
# 1. This option is no longer recommended.
# 2. This option might have side effects which may alter your results from one function to another.
# 
# Therefore, instead of <code>df.any_method(inplace=True)</code>, use <code>df = df.any_method()</code>

# #### Questions
# 
# **A. In this part, we will only deal with the data for year 2018 (cont.)**
# 
# - Perform an inner join between the life expectancy and the total population `DataFrame` objects, then an inner join with the result and the country `DataFrame` object. Remember that overlapping columns names are renamed automatically with the `_x` and `_y` suffixes in the left and right side:
# 
# 1) What is the weighted average life expectancy in 2018 (°) (+)?
# 
# 2) What is the largest weighted average life expectancy by region in 2018 (°) (+)?
# 
# 3) What is the smallest weighted average life expectancy by region in 2018 (°) (+)?
# 
# - Perform an inner join between the income per person and the total population `DataFrame` objects, then an inner join with the result and the country `DataFrame` objects. Remember that overlapping columns are renamed automatically with the `_x` and `_y` suffixes in the left and right side:
# 
# 4) What is the weighted average income per person in 2018 (°) (++)?
# 
# 5) Which region has the largest weighted average income per person in 2018 (++)?
# 
# 6) Which region has the smallest weighted average income per person in 2018 (++)?
# 
# (+) The *weighted average life expectancy* is computed with the . It can be computed for all countries in the world or for all countries in each region.
# 
# Hint: weighted average life expectancy $= \frac{\displaystyle\sum_{i} life_{i} \times pop_{i}}{\displaystyle\sum_{i} pop_{i}}$
# 
# (++) The *weighted average income per person* is computed with the sum of the products of income per person by total population of each country divided by the sum of total population of each country. It can be computed for all countries in the world or for all countries in each region.
# 
# Hint: weighted average income per person $= \frac{\displaystyle\sum_{i} income_{i} \times pop_{i}}{\displaystyle\sum_{i} pop_{i}}$
# 
# (°) Result of functions should be rounded to 1 decimal place.

# **B. In this part, we deal with data for all years**
# 
# 7) Which country has the smallest mean life expectancy accross years?
# 
# 8) Which country has the smallest mean income per person accross years?
# 
# 9) Compute the correlation of total population between all countries accross years. Which country has the highest mean correlation with the other ones? 
# 
# 10) Compute the correlation of life expectancy between all countries accross years. Which country has the highest mean correlation of life expectancy with the other ones? 
# 
# 11) Compute the correlation of income per person between all countries accross years. Which country has the highest mean correlation of income per person with the other ones?
# 
# 12) Perform a wide to long format transformation of the total population `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for total population?
# 
# 13) Perform a wide to long format transformation of the life expectancy `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for life expectancy?
# 
# 14) Perform a wide to long format transformation of the income per person `DataFrame` object by using the `melt()` function. What is the length of the new `DataFrame` object for income per person?
# 
# 15) Perform 3 wide to long format transformations of the total population, life expectancy and income per person `DataFrame` objects by using the `melt()` function. Then perform an inner join of the 2 first `DataFrame` objects on both `geo` and `Year` by using the `merge()` function. Then perform another inner join of this `DataFrame` object and the third one. You should obtain a final `DataFrame` object with 5 columns: `geo`, `Year`, `Total Population`, `Life Expectancy` and `Income Per Person`. Remove lines with `NA` . What is the length of the final `DataFrame` object obtained?

# **Homework, out of the scope of the assignment**
# 
# - Homogenize the country names accross the different files and compare the results of the 30 exercises.
# 
# - Implement a graphics showing, for a given year, all countries positionned with their income per person on the `x` axis and their life expectancy on the `y` axis, and represented by their name, as well as, a circle which radius is linked to their total population and which color is linked to their region.

# In[1]:


# import
import numpy as np
import pandas as pd


# In[2]:


# loading the data

df_population = pd.read_csv('population_total.csv')
df_life = pd.read_csv('life_expectancy_years.csv')
df_income = pd.read_csv('income_per_person.csv')
df_country = pd.read_csv('countries_total.csv',
                           engine='python',
                           usecols=[0, 5],
                           header=0,
                           names=['geo', 'region'])


# In[3]:


df1 = df_life[["geo","2018"]].rename(columns = {"2018":"life_2018"}).replace('NaN',None)
df_lifeexpectancy = df1.dropna
df2 = df_population[["geo","2018"]].rename(columns = {"2018":"population_2018"})
df3 = df_country[["region","geo"]]
df4 = df_income[["geo","2018"]].rename(columns = {"2018":"income_2018"})

df_merged1 = pd.merge(df1, df2,
              on='geo',
              how='inner')
df_merged1 = pd.merge(df4, df_merged1,
              on='geo',
              how='inner')
df_merged2 = pd.merge(df3, df_merged1,
              on='geo',
              how='inner')

df_life2 = pd.read_csv('life_expectancy_years.csv')
df_income2 = pd.read_csv('income_per_person.csv')

df_merged2


# In[4]:


# What is the weighted average life expectancy in 2018 (°)?
def exercise_01():
    df_merged2["Weighted_LE"] = df_merged2['life_2018']*df_merged2['population_2018']
    result = df_merged2["Weighted_LE"].sum() / df_merged2['population_2018'].sum()
    return round(result, 1)


# In[5]:


# run and check
exercise_01()


# In[6]:


# What is the largest weighted average life expectancy by region in 2018 (°)?
def exercise_02():
    Largest_LE =df_merged2.groupby('region')["Weighted_LE"].sum()/df_merged2.groupby('region')["population_2018"].sum()                          
    result =Largest_LE.max()
    return round(result, 1)


# In[7]:


# run and check
exercise_02()


# In[8]:


# What is the smallest weighted average life expectancy by region in 2018 (°)?
def exercise_03():
    Smallest_LE =df_merged2.groupby('region')["Weighted_LE"].sum()/df_merged2.groupby('region')["population_2018"].sum()
    result =Smallest_LE.min()
    return round(result, 1)


# In[9]:


# run and check
exercise_03()


# In[10]:


# What is the weighted average income per person in 2018 (°)?
def exercise_04():
    df_merged2["Weighted_Income"] = df_merged2['income_2018']*df_merged2['population_2018']
    result = df_merged2["Weighted_Income"].sum() / df_merged2['population_2018'].sum()
    return round(result, 1)


# In[11]:


# run and check
exercise_04()


# In[12]:


# Which region has the largest weighted average income per person in 2018?
def exercise_05():
    Largest_IN =df_merged2.groupby('region')["Weighted_Income"].sum()/df_merged2.groupby('region')["population_2018"].sum()                          
    result = Largest_IN.idxmax()
    return result


# In[13]:


# run and check
exercise_05()


# In[14]:


# Which region has the smallest weighted average income per person in 2018?
def exercise_06():
    Smallest_IN =df_merged2.groupby('region')["Weighted_Income"].sum()/df_merged2.groupby('region')["population_2018"].sum()                          
    result = Smallest_IN.idxmin()
    return result


# In[15]:


# run and check
exercise_06()


# In[16]:


# Which country has the smallest average life expectancy accross years?
def exercise_07():
    df_life["avg"] = df_life.mean(axis=1) 
    result = df_life.groupby('geo')['avg'].sum().idxmin()
    return result


# In[17]:


# run and check
exercise_07()


# In[18]:


# Which country has the smallest average income per person accross years?
def exercise_08():
    df_income["avg"] = df_income.mean(axis=1) 
    result = df_income.groupby('geo')['avg'].sum().idxmin()
    return result


# In[19]:


# run and check
exercise_08()


# In[20]:


# Which country has the highest mean correlation of total population with other countries? 
def exercise_09():
    result = (df_population.set_index('geo').transpose()).corr().mean().idxmax()
    return result


# In[21]:


# run and check
exercise_09()


# In[22]:


# Which country has the highest mean correlation of life expectancy with other countries? 
def exercise_10():
    result = (df_life.set_index('geo').transpose()).corr().mean().idxmax()
    return result


# In[23]:


# run and check
exercise_10()


# In[24]:


# Which country has the highest mean correlation of income per person with other countries? 
def exercise_11():
    result = (df_income.set_index('geo').transpose()).corr().mean().idxmax()
    return result


# In[25]:


# run and check
exercise_11()


# In[26]:


# What is the length of the new DataFrame object for total population?
def exercise_12():
    result = len(pd.melt(df_population, id_vars= ['geo'],var_name= [(range(1800, 2018))]))
    return result


# In[27]:


# run and check
exercise_12()


# In[28]:


# What is the length of the new DataFrame object for life expectancy?
def exercise_13():
    result = len(pd.melt(df_life2, id_vars= ['geo']))
    return result


# In[29]:


# run and check
exercise_13()


# In[30]:


# What is the length of the new DataFrame object for income per person?
def exercise_14():
    result = len(pd.melt(df_income2, id_vars= ['geo']))
    return result


# In[31]:


# run and check
exercise_14()


# In[32]:


# What is the length of the DataFrame object merging total population, life expectancy and income per person in a long format?
def exercise_15():
    df5=pd.melt(df_population ,id_vars=['geo'], var_name='Year', value_name='Total Population')
    df6=pd.melt(df_life2 ,id_vars=['geo'], var_name='Year', value_name='Life Expectancy')
    df7=pd.melt(df_income2 ,id_vars=['geo'], var_name='Year', value_name='Income Per Person')
    df8 = pd.merge(df5, df6,
              on=['geo','Year'],
              how='inner')

    df9=pd.merge(df7, df8,
              on=['geo','Year'],
              how='inner')
    
    drpd_val = df9.dropna()
    result = len(drpd_val)
    return result


# In[33]:


# run and check
exercise_15()


# In[ ]:





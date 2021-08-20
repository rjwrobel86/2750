#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exploatory Data Analysis


# In[3]:


import os
directory = os.getcwd()
print(directory)


# In[1]:


#Import the Pandas library into the Python environment
#The "as pd" part renames pandas to pd, so commands take less typing
import pandas as pd


# In[7]:


#Housing Price Dataset - found on Kaggle - https://www.kaggle.com/esratmaria/house-price-dataset-with-other-information/version/1
#Load a CSV file into Python / Pandas, calling the "dataframe" df
#A dataframe is essentially a 2D data structure akin to a spreadsheet / table
df = pd.read_csv('kc_house_data.csv')


# In[31]:


#In coding, "printing" means displaying something on screen, the number in the parentheses selects how many of the top rows to display
print(df.head(5))


# In[11]:


#View the data types of each variable
info = df.info()
print(info)


# In[13]:


#Create the summary statistics (Print isn't always needed?!)
df.describe()


# In[14]:


df.info()


# In[16]:


#Store the various averages as variables
mean = df.price.mean()
median = df.price.median()
mode = df.price.mode()


# In[17]:


#Range (Max - Min)
maximum = df.floors.max() 
minimum = df.floors.min()
range_var = maximum - minimum
print(range_var)


# In[18]:


#Variance & Standard Deviation
variance = df.sqft_living.var()
standard_deviation = df.sqft_living.std()


# In[20]:


#Import visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

#Create boxplot
sns.boxplot(x="price", data = df)
plt.show()
plt.close()


# In[21]:


#Create histogram
sns.histplot(x="price", data = df)
plt.show()
plt.close()


# In[23]:


#Categorical data - Count per category
df.waterfront.value_counts()


# In[27]:


#Categorical data - Bar chart
sns.countplot(x = "waterfront", data = df)
plt.show()


# In[25]:


#Categorical data - Pie chart
df.waterfront.value_counts().plot.pie()
plt.show()


# In[28]:


#Grouping 
df.groupby('zipcode').price.mean()


# In[29]:


#Crosstabulation
pd.crosstab(df.waterfront, df.grade)


# In[30]:


#Crosstabulation - Proportions / Percentages
pd.crosstab(df.grade, df.waterfront, normalize=True)


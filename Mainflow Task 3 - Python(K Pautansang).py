#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('C:\\Study Material\\DPGITM\\Internship\\householdtask3.csv')


# In[3]:


data.head(10)


# In[4]:


#scatter plot with year against own
plt.scatter(data['year'], data['own'])

#Adding title to the plot
plt.title("Scatter plot")

#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[5]:


#Line chart with year against won
plt.plot(data['year'])
plt.plot(data['own'])

#Adding title to the plot
plt.title("Line Chart")

#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[6]:


#Bar chart or Bar plot
plt.bar(data['year'], data['own'])

#Adding title to the plot
plt.title("Bar chart")

#setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[9]:


#Histogram
plt.hist(data['income'])

#Adding title to the plot
plt.title("Histogram")

#Showing the result
plt.show()


# In[ ]:





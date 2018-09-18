
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from time import time 
from IPython.display import display
import visuals as vs


data = pd.read_csv('census.csv')


# In[4]:


data


# In[5]:


data['income']


# In[12]:


data['income']


# In[13]:


data.sort(['income'],ascending=false)


# In[14]:


data.loc[data["income"] == ">50K"]


# In[15]:


data.loc[data["income"] == ">50K"]


# In[16]:


data.loc[data["income"] == "<=50K"]


# In[17]:


data['income']


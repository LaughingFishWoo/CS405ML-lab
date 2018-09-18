#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from time import time
from IPython.display import display
import visuals as vs

get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_csv("census.csv")
display(data.head(n=1))


# In[2]:


income_raw =data['income']
features_raw = data.drop('income',axis=1)
vs.distribution(data)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





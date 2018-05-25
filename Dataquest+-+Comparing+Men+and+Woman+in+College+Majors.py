
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')
recent_grads=pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]


# In[6]:


recent_grads.head()


# In[7]:


recent_grads.tail()


# In[8]:


recent_grads.describe()


# In[9]:


raw_data_count=len(recent_grads)
raw_data_count


# In[10]:


recent_grads=recent_grads.dropna()
cleaned_data_count=len(recent_grads)
cleaned_data_count


# In[11]:


recent_grads.plot(x="Sample_size",y="Median",kind="Scatter")


# In[12]:


recent_grads.plot(x="Sample_size",y="Unemployment_rate",kind="Scatter")


# In[13]:


recent_grads.plot(x="Full_time",y="Median",kind="Scatter")


# In[14]:


recent_grads.plot(x="ShareWomen",y="Unemployment_rate",kind="Scatter")


# In[15]:


recent_grads.plot(x="Men",y="Median",kind="Scatter")


# In[16]:


recent_grads.plot(x="Women",y="Median",kind="Scatter")


# In[20]:


recent_grads["Sample_size"].hist(bins=25,range=(0,5000))


# In[61]:


recent_grads["Median"].hist(bins=10,range=(0,150000))


# In[62]:


recent_grads["Employed"].hist(bins=10,range=(0,350000))


# In[63]:


recent_grads["Full_time"].hist(bins=10,range=(0,275000))


# In[64]:


recent_grads["ShareWomen"].hist(bins=10,range=(0,1))


# In[52]:


recent_grads["Unemployment_rate"].hist(bins=25,range=(0,.2))


# In[65]:


recent_grads["Men"].hist(bins=10,range=(0,200000))


# In[66]:


recent_grads["Women"].hist(bins=10,range=(0,200000))


# In[69]:


from pandas.tools.plotting import scatter_matrix


# In[76]:


scatter_matrix(recent_grads[["Sample_size","Median"]], figsize=(6,6))


# In[77]:


scatter_matrix(recent_grads[["Sample_size","Median","Unemployment_rate"]],figsize=(6,6))


# In[85]:


recent_grads[0:10].plot.bar(x="Major",y="ShareWomen",legend=False)
recent_grads[-10:].plot.bar(x="Major",y="ShareWomen",legend=False)


# In[88]:


recent_grads[0:10].plot.bar(x="Major",y="Unemployment_rate",legend=False)
recent_grads[-10:].plot.bar(x="Major",y="Unemployment_rate",legend=False)



# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head(5)


# In[3]:


data.columns


# In[4]:


data["Do you celebrate Thanksgiving?"].value_counts()


# In[5]:


##Remove anybody that does not celebrate thanksgiving
data= data[data["Do you celebrate Thanksgiving?"] == "Yes"] 


# In[6]:


##What main dishes did people eat?
data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()


# In[7]:


##Do people pair gravy with Tofurkey?
tofurkey=data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]
tofurkey["Do you typically have gravy?"]


# In[8]:


apple_isnull=data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()
pumpkin_isnull=data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
pecan_isnull=data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()
no_pies = apple_isnull & pumpkin_isnull & pecan_isnull
no_pies.value_counts()


# In[9]:


def convert_age(age_str):  
    if pd.isnull(age_str):
        return None
    age_str = age_str.split(" ")[0]
    age_str = age_str.replace("+","")
    return int(age_str)
data["int_age"]=data["Age"].apply(convert_age)
data["int_age"].describe()


# because we have skewed the age towards the lower bound our data likely shows a younger age than what was truely represented.  Although it does show that the age groups of the responders were close to of even size.

# In[10]:


def convert_income(income_str):
    if pd.isnull(income_str):
        return None
    income_str = income_str.split(" ")[0]
    if income_str == "Prefer":
        return None
    income_str = income_str.replace("$", "")
    income_str = income_str.replace(",","")
    return int(income_str)
data["int_income"]=data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(convert_income)
data["int_income"].describe()


# Similar to age this shows the numbers skewed down because we used the lower bound of each answer.  The average income of the participants does appear to be high.

# In[14]:


data[data["int_income"]<150000]["How far will you travel for Thanksgiving?"].value_counts()


# In[15]:


data[data["int_income"]>150000]["How far will you travel for Thanksgiving?"].value_counts()


# A higher percentage of those who make over $150,000 have thanksgiving at home than those who make less than.

# In[20]:


data.pivot_table(
        index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
        columns= 'Have you ever attended a "Friendsgiving?"',
        values="int_age")


# In[21]:


data.pivot_table(
        index="Have you ever tried to meet up with hometown friends on Thanksgiving night?",
        columns= 'Have you ever attended a "Friendsgiving?"',
        values="int_income")


# Younger people are more likely to celebrate "Friendsgiving" or meet up with friends on thanksgiving.

# In[28]:


data.pivot_table(columns = "Do you typically pray before or after the Thanksgiving meal?",
                 index="US Region")


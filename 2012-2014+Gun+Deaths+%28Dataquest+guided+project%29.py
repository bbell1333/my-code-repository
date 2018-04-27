
# coding: utf-8

# In[1]:


import csv
f = open("guns.csv", "r")
data= list(csv.reader(f))
data[:5]


# In[2]:


headers = data[0]
data = data[1:]
data[:5]


# In[3]:


years = [row[1] for row in data]##extract the year from each entry in data
year_counts = {}
for year in years: ##count each gun death per year 
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
year_counts


# In[4]:


import datetime
dates = [datetime.datetime(year=int(row[1]), month=int(row[2]), day=1)for row in data]
dates


# In[5]:


date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] +=1
    else:
        date_counts[date] = 1
date_counts


# In[6]:


sex_counts = {}
sexes = [row[5] for row in data]
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex]+=1
sex_counts


# In[7]:


race_counts = {}
races = [row[7] for row in data]
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race]+=1
race_counts


# From 2012 to 2014 the number of gun deaths was consistent.  When looking deeper we see that no month really stands out with significantly more or less than any other month, although there is a slight uptick during summer months.  
# 
# Gender clearly does play a role though as almost 6 times as many men were involved than woman.  
# 
# While race looks to be a factor as well it is important to consider that over 70% of the country is white with the next largest group being black. 
# 
# More detail is needed to assess what percentage of each racial population is involved in gun deaths in the US.  

# In[8]:


f = open("census.csv", "r")
census = list(csv.reader(f))
census


# In[9]:


mapping = {"Asian/Pacific Islander":(15159516+674625),
           "Black": 40250635,
           "Hispanic": 44618105,
           "Native American/Native Alaskan": 3739506,           
           "White": 197318956
          }


# In[10]:


race_per_hundredk = {}
for race in race_counts:
    percent = race_counts[race]/mapping[race]
    race_per_hundredk[race] = percent*100000
race_per_hundredk


# In[12]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i] == "Homicide":
        homicide_race_counts[race] += 1
homicide_race_counts


# In[13]:


for race in homicide_race_counts:
    homicide_race_counts[race] = (homicide_race_counts[race]/ mapping[race])*100000
homicide_race_counts


# From the data it is clear there is a disproportionate number of homicides affecting the Black and Hispanic communities.

# Items to look into
# -  Education level vs gun death
# -  rate of suicide and other intents amongst different demographics
# -  How often a police officer was involved

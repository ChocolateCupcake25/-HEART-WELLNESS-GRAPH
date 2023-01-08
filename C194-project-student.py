#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : Ziyah")
print("We will be cleaning the big data and make a comparison to show who has a healthier heart smokers OR non smokers, uisng a line graph")
print("Also we will be deriviring which age group has the high chances of coronary heart disease in 10 years")


# # Task 1 - Plot a line graph to show the difference between heart rate of smokers and non smokers

# In[2]:


#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#read the csv
df = pd.read_csv('framingham.csv')
df


# In[3]:


#Filter and make a new dataframe for non smokers
non_smokers = df.loc[df['currentSmoker']==0]
non_smokers


# In[4]:


#Group by age column and find average heart rate at different age
group_non_smokers = non_smokers.groupby('age')['heartRate'].mean().reset_index()
print( group_non_smokers)


# In[5]:


#Filter and make a new dataframe for smokers
smokers = df.loc[df['currentSmoker']==1]
smokers


# In[6]:


#Group by age column and find average heart rate at different age
group_smokers = smokers.groupby('age')['heartRate'].mean().reset_index()
print( group_smokers)


# In[7]:


#Plot a line graph to show the heart rate of smokers vs non smokers
label1=group_non_smokers['age']
value1=group_non_smokers['heartRate']

fig = plt.subplots(figsize=(20,8))

plt.plot(label1, value1, label = "Heart rate of non smokers as per age" , linewidth=3.0)

label=group_smokers['age']
value=group_smokers['heartRate']

plt.plot(label, value, label = "Heart rate of smokers as per age" , linewidth=3.0)

plt.xlabel('AGE')
plt.xticks(rotation='vertical')

plt.ylabel('Heart Rate')

plt.title('Heart Rate of non smokers and smokers as per age', fontsize=20)

plt.legend()

plt.show()


# Conslusion - At the age of 70 the heart rate of non_smokers drop while of smokers it still stays high 

# # Task 2 - Which age group have high chances of having coronary heart disease in 10 years

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('framingham.csv')
dataframe
#Filter and make a new dataframe for those who has chances of having coronary heart disease in 10 years
coronary_heart_disease=dataframe.loc[dataframe['TenYearCHD']==1]
print(coronary_heart_disease)


# In[23]:


#Group by age column and count the rows of TenYearCHD column
group_age=coronary_heart_disease.groupby('age')['TenYearCHD'].count().reset_index()
print(group_age)


# In[24]:


#Plot a bubble graph to show total number of people having a chance of coronary heart disease in 10 years
plt.figure(figsize=(12, 8))
plt.xticks(rotation='vertical')

plt.scatter(group_age['age'], group_age['TenYearCHD'], c='green',
            label = 'TenYearCHD', alpha=0.5,s = group_age['TenYearCHD']*5)

plt.legend()
plt.xlabel("Age", size=14)
plt.ylabel("TenYearCHD", size=14)


# Conslusion - Smokers are more likely to have heart diseases from the ages of 50 to 65

# In[ ]:





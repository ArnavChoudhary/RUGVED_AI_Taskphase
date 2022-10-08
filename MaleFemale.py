#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data={'RollNo':[1,2,3,4,5,6,7,8,9,10],
      'Name':['Paul','Gotham','Peter','Nick','Scarlet','Clint','Maria','Bruce','Steve','Tony'],
      'Gender':['Male','Male','Male','Male','Female','Male','Female','Male','Male','Male'],
      'Marks1':[75,86,72,38,65,69,57,72,93,71],
      'Marks2':[72,89,56,47,67,74,39,63,89,65],
      'Marks3':[68,77,63,45,72,80,59,68,91,68],
}


# In[10]:


frame=pd.DataFrame(data)


# In[6]:


frame


# In[7]:


col_list=list(frame)


# In[11]:


col_list.remove('RollNo')


# In[12]:


frame['Total Marks']=frame[col_list].sum(axis=1)


# In[13]:


frame


# In[14]:


minimum_M1=frame['Marks1'].min()


# In[15]:


minimum_M1


# In[16]:


maximum_M2=frame['Marks2'].max()


# In[17]:


maximum_M2


# In[18]:


average_M3=frame['Marks3'].mean()


# In[19]:


average_M3


# In[20]:


frame['Average']=frame[col_list].mean(axis=1)


# In[21]:


greatest_average=frame['Average'].max()


# In[22]:


greatest_average


# In[24]:


student_greatest_average=frame.loc[frame['Average']==greatest_average,'Name'].tolist()


# In[25]:


student_greatest_average


# In[27]:


fail=frame.loc[frame['Marks2']<40]


# In[28]:


fail['Name'].count()


# In[ ]:





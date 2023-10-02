#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\Admin\\Downloads\\Diwali Sales Data.csv", encoding= 'unicode_escape')
df


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.drop(['Status','unnamed1'], axis=1, inplace=True)


# In[7]:


df.info()


# In[8]:


#drop null value
df.isnull().sum()


# In[9]:


df.dropna(inplace=True)


# In[10]:


#Change data type
df['Amount']=df['Amount'].astype('int')


# In[11]:


df['Amount'].dtype


# In[12]:


df.columns


# In[13]:


#Change the column name
df.rename(columns={'Marital_Status':'Shaadi'})


# In[14]:


#Describe use for numaric vlaue, but you can use on object datatype by df.describe(include='object')
df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis
# 
# ### Gender

# In[15]:


df.columns


# In[16]:


ax=sns.countplot(x='Gender',data=df)
for s in ax.containers:
    ax.bar_label(s)


# In[17]:


Sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
Sales_gen


# In[18]:


s=sns.barplot(x='Gender',y='Amount',data=Sales_gen)
for bar in s.containers:
    s.bar_label(bar)
    
plt.show()


# #### from above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than man.

# ## Age

# In[19]:


df.columns


# In[20]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')
for s in ax.containers:
    ax.bar_label(s)


# In[21]:


Sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
Sales_age


# In[22]:


sns.barplot(x='Age Group',y='Amount',data=Sales_age)
plt.show()


# #### from above graphs we can see that most of the buyers are of age group between 26-35 yrs female.

# ## State

# In[23]:


df.columns


# In[24]:


Sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
Sales_state


# In[25]:


sns.barplot(x='State',y='Orders',data=Sales_state)
sns.set(rc={'figure.figsize':(20,5)})
plt.show()


# In[26]:


Sales_state=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(x='State',y='Amount',data=Sales_state)
sns.set(rc={'figure.figsize':(15,5)})
plt.show()


# In[27]:


#from above graphs we can see that most of the orders and total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively


# ### Marital Status

# In[28]:


df.columns


# In[29]:


ax=sns.countplot(data=df,x='Marital_Status')
sns.set(rc={'figure.figsize':(6,5)})
for s in ax.containers:
    ax.bar_label(s)


# In[30]:


Sales_Marital_status=df.groupby(['Marital_Status'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
Sales_Marital_status


# In[31]:


sns.barplot(data=Sales_Marital_status,x='Marital_Status',y='Amount')


# #### from above graphs we can see that most of the buyers are married(women) and they have high purchasing power.

# ### Occupation

# In[32]:


df.columns


# In[33]:


ax=sns.countplot(data=df,x='Occupation')
sns.set(rc={'figure.figsize':(20,5)})
for x in ax.containers:
    ax.bar_label(x)


# In[34]:


Sales_Occupation=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
Sales_Occupation


# In[35]:


sns.barplot(data=Sales_Occupation,x='Occupation',y='Amount')
sns.set(rc={'figure.figsize':(15,5)})


# #### From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector.

# ### Product Category

# In[36]:


ax=sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(30,5)})
for a in ax.containers:
    ax.bar_label(a)


# In[37]:


Sales_Product_category=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.barplot(data=Sales_Product_category,x='Product_Category', y='Amount')



# #### From above graphs we can see that most of the sold products are from Food, Cloting and Electronics caregory.

# In[38]:


Sales_Product_ID=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.barplot(data=Sales_Product_ID,x='Product_ID',y='Orders')
sns.set(rc={'figure.figsize':(20,5)})


# #### From the above graph top 10 most sold products.

# ### Conclusion:

# ##### Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category.

# In[ ]:





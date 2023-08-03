#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[3]:


#Upload Dataset
df=pd.read_csv("Bank Customer Churn Prediction.csv")
df.head()


# # Analysis basic informations of dataset

# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


df.dtypes


# In[7]:


df.isnull().sum()


# In[8]:


df.info()


# # Exploratory Data Analysis

# # 1. Value Counts of customer on the basis of differnt coloumns of data  

# In[9]:


# Value counts of "country"
df['country'].value_counts()


# In[10]:


plt.figure(figsize=(5,3.5))
sns.countplot(x=df['country'])
plt.title("Country vs Customer Count")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()


# In[11]:


# Value counts of "gender"
df['gender'].value_counts()


# In[12]:


plt.figure(figsize=(5,3))
sns.countplot(x=df['gender'])
plt.title("Gender vs Customer Count")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()


# In[13]:


#df_m["active_member"]=pd.from_dummies(df[["active_member"]],sep=None, default_category="inactive_member")
#df_m


# # Converting dummies values into cetagorical values for the better interpretation and visualization

# In[14]:


df_m=df


# In[15]:


#Converting dummies values into cetagorical values for the better interpretation and visualization
df_m["active_member"]=df_m["active_member"].replace({0:"Inactive", 1:"Active"})
df_m["credit_card"]=df_m["credit_card"].replace({0:"Not owned", 1:"Owned"})
df_m["churn"]=df_m["churn"].replace({0:"Not churned", 1:"Churned"})
df_m


# In[16]:


# Value counts of "Active members status"
df_m["active_member"].value_counts()


# In[17]:


plt.figure(figsize=(5,3))
sns.countplot(x=df_m['active_member'],palette="rocket")
plt.title("Activity Status vs Customer Count")
plt.xlabel("Activity Status")
plt.ylabel("Count")
plt.show()


# In[18]:


# Value counts of "Credit card status"
df_m["credit_card"].value_counts()


# In[19]:


plt.figure(figsize=(5,3))
sns.countplot(x=df_m['credit_card'])
plt.title("Credit Card Status vs Customer Count")
plt.xlabel("Credit Card Status")
plt.ylabel("Count")
plt.show()


# In[20]:


# Value counts of "Churn status"
df_m["churn"].value_counts()


# In[21]:


plt.figure(figsize=(5,3))
sns.countplot(x=df_m['churn'],palette="rocket")
plt.title("Churning vs Customer Count")
plt.xlabel("Churning Status")
plt.ylabel("Count")
plt.show()


# In[22]:


# Value counts of "Tenure"
df["tenure"].value_counts()


# In[23]:


plt.figure(figsize=(5,3))
sns.countplot(x=df["tenure"])
plt.title("Custumer Tenure vs Customer Count")
plt.xlabel("Tenure(Years)")
plt.ylabel("Count")
plt.show()


# In[24]:


# Value counts of "Products number"
df["products_number"].value_counts()


# In[25]:


plt.figure(figsize=(5,3))
sns.countplot(x=df["products_number"],palette="vlag")
plt.title("Products vs Customer Count")
plt.xlabel("Product Number")
plt.ylabel("Count")
plt.show()


# 
# 

# # Analysing trend of customer on the basis of their credit score

# In[26]:


plt.figure(figsize=(5,4))
plt.hist(df["credit_score"])
plt.title("Customers credit score")
plt.xlabel("Credit Score")
plt.show()


# # Analysing trend of customer on the basis of their Age

# In[27]:


plt.figure(figsize=(5,4))
plt.hist(df["age"], color="brown")
plt.title("Customer Age")
plt.xlabel("Age(Years)")
plt.show()


# # Analysing trend of customer on the basis of their Account Balance

# In[28]:


plt.figure(figsize=(5,4))
plt.hist(df["balance"], color="purple")
plt.title("Account Balance")
plt.xlabel("Balance")
plt.show()


# # Analysing trend of customer on the basis of their Estimated salary

# In[32]:


plt.figure(figsize=(7,5))
plt.hist(df["estimated_salary"], color="green")
plt.title("Customer's estimated salary")
plt.xlabel("Estimated salary")
plt.show()


# # 2. Analysing what factors influencing churn rate

# # Analysing categorical factors

# In[30]:


plt.figure(figsize=(16,16))

plt.subplot(3,2,1)
sns.countplot(x=df['country'], hue=df["churn"], palette="copper")
plt.title("Country")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(3,2,2)
sns.countplot(x=df['gender'], hue=df["churn"],palette="pastel")
plt.title("Gender")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(3,2,3)
sns.countplot(x=df_m['active_member'],hue=df["churn"], palette="pastel")
plt.title("Activity Status")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(3,2,4)
sns.countplot(x=df_m['credit_card'],hue=df["churn"],palette="copper")
plt.title("Credit Card Status")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(3,2,5)
sns.countplot(x=df["products_number"],hue=df["churn"], palette="copper")
plt.title("Products")
plt.xlabel(None)
plt.ylabel(None)

plt.show()


# # Analysing continuous factors

# In[31]:


plt.figure(figsize=(14,14))

plt.subplot(2,2,1)
sns.histplot(x=df["age"], hue=df["churn"])
plt.title("Age")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(2,2,2)
sns.histplot(x=df["credit_score"], hue=df["churn"])
plt.title("Credit Score")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(2,2,3)
sns.histplot(x=df["balance"], hue=df["churn"])
plt.title("Account Balance")
plt.xlabel(None)
plt.ylabel(None)

plt.subplot(2,2,4)
sns.histplot(x=df["estimated_salary"], hue=df["churn"])
plt.title("Estimated Salary")
plt.xlabel(None)
plt.ylabel(None)

plt.show()


# In[ ]:





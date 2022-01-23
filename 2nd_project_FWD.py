#!/usr/bin/env python
# coding: utf-8

# # Introduction

# # Dataset Description 
# 

# This data set contains information about 10,000 movies collected from The Movie Database (TMDb),I take this data from kaggle
# ,In this analysis process i will start with wrangling the data then clean it from null values and the feature that in not important fot my analysis
# ,I will use matplotlib library to visualize the data and use seaborn to make the visualization look better and it will help me to answer the questions that i want to get from this data

# # Questions for Analysis
# 

# 1)what is the features that make more profit for the movies?
# 

# 2)Is it good to take only the popularity or vote_avg as the final judge for the movie ?
# 

# 3)what is mean of revenue and budget?
# _________________________________________________________________________________________________________________________

# In[2]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# # Data_Wrangling

# I would use pandas to read my 2 datasets and then i found that they share 2 columns so i woukd merge these 2 datasets with these 2 columns

# In[3]:


df=pd.read_csv('tmdb_5000_credits.csv')
dr=pd.read_csv('tmdb_5000_movies.csv')


# In[4]:


df.head()


# In[5]:


dr.head()


# In[6]:


df.movie_id.nunique()


# In[7]:


dr.id.nunique()


# chage name of movie_id col to id to make the 2 data sets have same name of this  col to merge them

# In[8]:


df.rename(columns={'movie_id': 'id'},inplace=True)


# In[9]:


df.head()


# In[10]:


dr.head()


# After read 2 datasets and userd merge to make it into one to help me in analysis it will be easier like that

# In[11]:


data=pd.merge(df,dr,on='id')


# In[12]:


data.head()


# checking if they megre with view the size of the new dataset I creat with these 2 datasets

# In[13]:


dr.shape


# In[14]:


df.shape


# In[15]:


data.shape


# checking the null values and the types of the data in each column

# In[16]:


data.info()


# checking the data in ['overview'] column to decide if I should drop it or not

# In[17]:


data['overview'].unique()


# # Data_Cleaning

# Here i droped the featurs that have alot of null values and not important featurs for my analysi

# In[18]:


data.drop(['homepage','tagline','keywords','title_y','release_date','overview','original_title','original_language','id','cast','crew'], axis=1, inplace=True)


# In[19]:


data.head()


# In[20]:


data.shape


# In[21]:


data.drop(['spoken_languages'],axis=1,inplace=True)


# In[22]:


data.shape


# In[23]:


data.info()


# In[24]:


data.dropna(inplace=True)


# In[25]:


data.info()


# In[26]:


data.shape


# # Exploratory_Data_Analysis

# Simple analysis decribe for each numircal column data type

# In[27]:


data.describe()


# histogram of all numerical data to see the distribution of this data and check for other information

# In[28]:


data.hist(figsize=(10,8));


# ## Checking Question 1 

# here i want to compare the budget to revenue

# In[38]:


plt.scatter(data['revenue'],data['popularity'], color ='blue',marker='*',alpha=0.25)
plt.title('The effect of popularity in revenue')
plt.xlabel('revenue')
plt.ylabel('popularity');


# here we found that the less the movie is populer the less it made porfit as you can see mont of the movies in the datasets has the same range of popularity and profit

# In[39]:


data.budget.hist(alpha=0.5, label='budget')
data.revenue.hist(alpha=0.5, label='revenue')
plt.title('comparison between budget and revenue')
plt.legend();


# After checking this hisogram I found that most of the movies have agood profit in this data so we found that this movies made abig success and the more budget u put in the movie the more revenue you will get 

# ## Checking Question 2
# 

# checking the popularity to vote_counts 

# In[104]:


data.vote_count.hist(alpha=0.5, label='vote_count')
data.popularity.hist(alpha=0.5, label='popularity')
plt.legend();


# After checking the histogram I found that this is not agood one because it can alot of people make votes and this movies is not that populer and give the movie a bad rate

# ## Checking Question 3

# ---------------------------------------------------------------------------------------------------------------------------
# Checking the mean of the budget and revenue

# In[102]:


data['budget'].mean()


# In[103]:


data['revenue'].mean()


# ------------------------------------------------------------------------------------------------------------------------------
# checking how many released movies , rumored and post production

# In[105]:


data.status.value_counts()


# #  Conclusions

# For profit of the movies the more budget you put in making the movie the more revenue you get from the movie

# the popularity does not effect the votes_avg that much there is abig gab in the scatter of them 

# there is realation between budget and revenue and it is the more budget the movie has the more revenue it will get

# the popularity also effect the revenue of the movie so the producthion companies should pay attention to make the movie more popular so it can make good renvenue

# the popularity effect the revenue of the movie the more populer the movie the more revenue it has,and most of the movies in this data have popularity in the small range and the movies that have big popularity have huge revenue
# __________________________________________________________________

# ## Limitations

# The size of the two datasets is not that big, so it may cause overfit for any conclusion we take

# Most of the movies are released so we can not use the status feature in our analysis and it has small movies number that rumored or post production

# Not all the features in the two data sets can be used in the analysis only some of them are good to make good conclusions 

# most of the movies make agood profit so we can not watch what result it will be when there is movies that did not make agood one

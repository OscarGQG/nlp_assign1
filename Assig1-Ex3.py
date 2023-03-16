#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 3 - Oscar Quispe
import pandas as pd
import re


# In[2]:


oscarq_df = pd.read_csv('Artifical_inteligence_data.csv')
oscarq_df


# In[3]:


oscarq_df = oscarq_df.drop(['user'], axis=1)
oscarq_df


# In[4]:


oscarq_df["text"] = oscarq_df["text"].str.replace(r'RT\s','',regex=True)
oscarq_df['text'] = oscarq_df['text'].str.replace(r'\@.*? ', '', regex=True)
oscarq_df['text'] = oscarq_df['text'].str.replace(r'[^A-Za-z0-9 ]+', '', regex=True)
oscarq_df.head(10)


# In[5]:


oscarq_df.shape


# In[6]:


print(oscarq_df.info())


# In[7]:


oscarq_df["sentiment"].value_counts()


# In[8]:


oscarq_df['text'] = oscarq_df['text'].str.lower()


# In[9]:


oscarq_df["tweet_len"] = oscarq_df["text"].str.count(" ") + 1
oscarq_df.head(20)


# In[10]:


pos1 = pd.read_csv("positive-words.txt",sep="\t",encoding='latin1',header=None)
neg1 = pd.read_csv("negative-words.txt",sep="\t",encoding='latin1',header=None)

pos1.columns = ["words"]
neg1.columns = ["words"]

pos_set = set(list(pos1["words"]))
neg_set = set(list(neg1["words"]))
print (len(pos_set))
print (len(neg_set))


# In[11]:


oscarq_df2 = oscarq_df[oscarq_df.tweet_len>=1]
len(oscarq_df),len(oscarq_df2)


# In[12]:


oscarq_df3 = oscarq_df2.sample(frac=0.5)
len(oscarq_df2),len(oscarq_df3)


# In[13]:


print(oscarq_df2["sentiment"].value_counts())
print(oscarq_df2["sentiment"].count())


# In[14]:


final_tag_list = []
pos_percent_list = []
neg_percent_list = []
pos_set_list = []
neg_set_list = []

for i,row in oscarq_df3.iterrows():
    
    full_txt_set = set(row["text"].split())
    tweet_len = len(full_txt_set)
    
    pos_set1 = (full_txt_set) & (pos_set)
    neg_set1 = (full_txt_set) & (neg_set)
    
    com_pos = len(pos_set1)
    com_neg = len(neg_set1)
    
    if(com_pos>0):
        pos_percent = com_pos/tweet_len
    else:
        pos_percent = 0

    
    if(com_neg>0):
        neg_percent = com_neg/tweet_len
    else:
        neg_percent =0
        
    if(pos_percent>0)|(neg_percent>0):
        if(pos_percent>neg_percent):
            final_tag = "positive"
        else:
            final_tag = "negative"
    else:
        final_tag="neutral"
    
    final_tag_list.append(final_tag)
    pos_percent_list.append(pos_percent)
    neg_percent_list.append(neg_percent)
    pos_set_list.append(pos_set1)
    neg_set_list.append(neg_set1)


# In[15]:


oscarq_df3.head(10)


# In[16]:


oscarq_df3["predicted_sentiment_score"] = final_tag_list
oscarq_df3["pos_percent"] = pos_percent_list
oscarq_df3["neg_percent"] = neg_percent_list


# In[17]:


oscarq_df3.info()


# In[18]:


oscarq_df3


# In[19]:


from sklearn.metrics import accuracy_score
print ("Accuracy score:", accuracy_score(oscarq_df3["sentiment"],oscarq_df3["predicted_sentiment_score"]))


# In[20]:


from sklearn.metrics import f1_score
print("F1 score:", f1_score(oscarq_df3["sentiment"],oscarq_df3["predicted_sentiment_score"], average='macro'))


# In[ ]:





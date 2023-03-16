#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercsie 2 OscarQuispe
import pandas as pd
import re


# In[2]:


Oscar_df = pd.read_csv('Artificial_Intelligence_mini.csv')
Oscar_df


# In[3]:


Oscar_df = Oscar_df.drop(['user'], axis=1)
Oscar_df


# In[4]:


Oscar_df["text"] = Oscar_df["text"].str.replace(r'RT\s','',regex=True)
Oscar_df['text'] = Oscar_df['text'].str.replace(r'\@.*? ', '', regex=True)
Oscar_df['text'] = Oscar_df['text'].str.replace(r'[^A-Za-z0-9 ]+', '', regex=True)
Oscar_df


# In[5]:


#lower case
n_df = Oscar_df['text'].str.lower()


# In[6]:


#removing punctuations
import string
n_df = n_df.str.translate(str.maketrans('', '', string.punctuation))


# In[7]:


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


# In[8]:


from nltk.tokenize import word_tokenize
tokenized_t1= word_tokenize(n_df.iloc[0])
print("Tokenized tweet:",tokenized_t1)
tokenized_t1_without_stopwords = [i for i in tokenized_t1 if not i in stop_words]
print("Tokenized tweet without stopwords:",tokenized_t1_without_stopwords)


# In[9]:


tokenized_t2= word_tokenize(n_df.iloc[1])
print("Tokenized tweet:",tokenized_t2)
tokenized_t2_without_stopwords = [i for i in tokenized_t2 if not i in stop_words]
print("Tokenized tweet without stopwords:",tokenized_t2_without_stopwords)


# In[10]:


tokenized_t3= word_tokenize(n_df.iloc[2])
print("Tokenized tweet:",tokenized_t3)
tokenized_t3_without_stopwords = [i for i in tokenized_t3 if not i in stop_words]
print("Tokenized tweet without stopwords:",tokenized_t3_without_stopwords)


# In[11]:


tokenized_t4= word_tokenize(n_df.iloc[3])
print("Tokenized tweet:",tokenized_t4)
tokenized_t4_without_stopwords = [i for i in tokenized_t4 if not i in stop_words]
print("Tokenized tweet without stopwords:",tokenized_t4_without_stopwords)


# In[12]:


import gensim.downloader as api
w2v_model = api.load('word2vec-google-news-300')


# In[13]:


w2v_model.most_similar('graduation')


# In[14]:


w2v_model.most_similar('villain')


# In[15]:


w2v_model.most_similar('spent')


# In[16]:


w2v_model.most_similar('projects')


# In[17]:


w2v_model.most_similar('outbreaks')


# In[18]:


w2v_model.most_similar('pandemic')


# In[19]:


w2v_model.most_similar('death')


# In[20]:


w2v_model.most_similar('closing')


# In[21]:


import nlpaug.augmenter.word as naw
get_ipython().system('pip install nlpaug==0.0.14')
from nlpaug.util import Action
import os
get_ipython().system('git clone https://github.com/makcedward/nlpaug.git')
os.environ["MODEL_DIR"] = 'nlpaug/model/'


# In[ ]:


aug = naw.WordEmbsAug(model_type='word2vec', model=w2v_model, action="insert")
augmented_text = aug.augment(t1)
print("Original:")
print(res)
print("Augmented Text:")
print(augmented_text)


# In[ ]:


aug = nac.RandomCharAug(action='substitute')
augmented_text = aug.augment(t1)
print("Original:")
print(t1)
print("Augmented Text:")
print(augmented_text)


# In[29]:


t1="sm not letting xiaojun go for his matriculation nor his brother's wedding last year is my baddie origin story he's too nice"
t2="for me it was devotes recovering from an allnighter i spent on music initiatives related to a vtuber's httpstcoHQ3LEAH1aF"
t3="954 ongoing covid19 epidemics in ontario's hospitals ltc and retirement homes every day now is a new flu pandemic high"
t4="well covid19 is once again the leading cause of murder in indiana based on average daily murders and shuttering in on aga"

ssent = {"sentiment":["positive", "negative", "positive", "negative"], "text": [t1,t2,t3,t4]}
dftw = pd.DataFrame(ssent, index=[4,5,6,7])


# In[30]:


Oscar_df_after_word_augmenter = pd.concat([Oscar_df, dftw])
Oscar_df_after_word_augmenter


# In[31]:


with open('Oscar_df_after_random_insertion.txt', mode='w') as file_object:
            print(Oscar_df_after_word_augmenter, file=file_object)


# In[32]:


Oscar_df_after_word_augmenter.to_csv('Oscar_df_after_random_insertion.csv', index=False, encoding='utf-8')


# In[ ]:





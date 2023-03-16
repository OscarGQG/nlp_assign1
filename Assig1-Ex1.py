#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Exercise 1 OscarQuispe
import requests


# In[2]:


ai_cc_url = "https://www.centennialcollege.ca/programs-courses/full-time/artificial-intelligence-fast-track/"
info_wp = requests.get(ai_cc_url)


# In[3]:


from bs4 import BeautifulSoup
info_wpsoup = BeautifulSoup(info_wp.content, 'html.parser')


# In[4]:


print(info_wpsoup.prettify())


# In[5]:


print(info_wpsoup.title)


# In[6]:


forecastpage = requests.get("https://forecast.weather.gov/MapClick.php?lat=42.35866000000004&lon=-71.05673999999993#.Y-SSlnbMK5c")
soup = BeautifulSoup(forecastpage.content, 'html.parser')
print(soup.prettify())


# In[7]:


seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())


# In[8]:


df_daye = soup.find(id="detailed-forecast")
df_itemse = df_daye.find_all(class_="row row-even row-forecast")
tonighte = df_itemse[5]
print(tonighte.prettify())


# In[9]:


df_dayo = soup.find(id="detailed-forecast")
df_itemso = df_dayo.find_all(class_="row row-odd row-forecast")
tonighto = df_itemso[5]
print(tonighto.prettify())


# In[10]:


location = soup.find(class_="smallTxt").get_text()
print(location)


# In[11]:


period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)


# In[12]:


img = tonight.find("img")
desc = img['title']
print(desc)


# In[13]:


period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods


# In[14]:


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)


# In[15]:


import pandas as pd
forecast_boston = pd.DataFrame({
    "Period": periods,
    "Short Forecast": short_descs,
    "Temperature": temps,
    "Detailed Forecast":descs
})

forecast_boston


# In[16]:


forecast_boston.to_csv('Oscar_Weather_Boston.csv', index=False, encoding='utf-8')


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import chart_studio.plotly as py


# In[3]:


from plotly import __version__
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[5]:


import cufflinks as cf


# In[6]:


init_notebook_mode(connected=True)
cf.go_offline()


# In[7]:


df = pd.read_csv('datasets_555917_1128483_Covid cases in India.csv')


# In[8]:


df.head()


# In[9]:


df[df['Active'] == df['Active'].max()]['Name of State / UT']


# In[10]:


df.iplot(kind='bar',x='Name of State / UT',y=['Deaths', 'Total Confirmed cases', 'Cured/Discharged/Migrated', 'Active'])


# In[11]:


df['Deaths'].max()


# In[12]:


df[df['Name of State / UT'] == 'Arunachal Pradesh']['Deaths']


# In[13]:


df.iplot(kind='scatter',x='Name of State / UT',y=['Deaths','Active'])


# In[14]:


df.drop(['Name of State / UT', 'S. No.'],axis=1).iplot(kind = 'ratio')


# In[15]:


df[['Total Confirmed cases','Deaths']].iplot(kind='spread')


# In[16]:


df.iplot(kind='bubble',x='Name of State / UT',y='Deaths',size='Total Confirmed cases')


# In[17]:


f, ax = plt.subplots(figsize=(12, 12))
sns.set_color_codes("pastel")
sns.barplot(x="Total Confirmed cases", y="Name of State / UT", data=df,color="red")
# sns.set_color_codes("muted")
sns.barplot(x="Deaths", y="Name of State / UT", data=df, label="Cured", color="black")
sns.barplot(x='Cured/Discharged/Migrated', y='Name of State / UT', data = df, color = 'green')
# ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 12974), ylabel="",xlabel="Cases")
sns.despine(left=True, bottom=True)


# In[18]:


df['Total Confirmed cases'].max()


# In[19]:


# import plotly.express as px
# df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
# df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
# fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()


# In[ ]:





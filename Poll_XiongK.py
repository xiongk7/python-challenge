#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import numpy as np


# In[118]:


# Save path to data set in a variable
polldata_file = "election_data.csv"


# In[119]:


# Use Pandas to read data
poll_file_df = pd.read_csv(polldata_file)
poll_file_df.head()


# In[120]:


# complete_candidate_count = poll_file_df("Candidate").sum()
# complete_candidate_count

candidates_count = poll_file_df["Candidate"].count()

candidates_count


# In[76]:


total_votes = len(poll_file_df)
total_percent_count_per_candidate = poll_file_df["Candidate"].value_counts()
total_percent_count = pd.DataFrame(round((total_percent_count_per_candidate/total_votes)*100), )
total_percent_count.head()


# In[122]:


total_count = poll_file_df["Candidate"].value_counts()
total_count.head()


# In[108]:


# # Collect a list of all the unique values in "Preferred Position"
# poll_file_df["Candidate"].unique()


# In[107]:


# poll_votes_df = poll_file_df.loc[poll_file_df["County"] == "Marsh", :]
# poll_votes_df.head()


# In[123]:


# total_votesss_df = poll_file_df["Candidate"].value_counts()

# total_votesss_df


# In[ ]:





# In[124]:


print("Election Results")

print("------------------------------------------------")

print(f"Total Votes: {candidates_count}")

print("------------------------------------------------")

print(f"{total_count})")

print("------------------------------------------------")

print(f"{total_percent_count}")

print("------------------------------------------------")
      
print(f"Winner: Khan")
print("------------------------------------------------")


# In[ ]:





# In[7]:





# In[79]:





# In[80]:





# In[10]:





# In[11]:





# In[12]:





# In[16]:





# In[ ]:





# In[25]:


total_votes = len(poll_file_df)
total_percent_count_per_candidate = poll_file_df["Candidate"].value_counts()
total_percent_count = pd.DataFrame(round((total_percent_count_per_candidate/total_votes)*100), )
total_percent_count.head()


# In[47]:


#NEWONE####################

total_count = poll_file_df["Candidate"].value_counts()
total_count


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





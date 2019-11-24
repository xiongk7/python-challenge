#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# In[33]:


# Save path to data set in a variable
data_file = "budget_data.csv"


# In[34]:


# Use Pandas to read data
budget_file_df = pd.read_csv(data_file)
budget_file_df.head()


# In[35]:


budget_file_df.describe()


# In[36]:


budget_file_df["Date"].head()


# In[37]:


# # Calculate the number of unique Months in the DataFrame
# Date_count = len(budget_file_df["Date"].unique())

# # Calculate the earliest/latest date 
# earliest_year = budget_file_df["Date"].min()
# latest_year = budget_file_df["Date"].max()

# # Hint: use the pandas' sum() method to get the sum for each row
# budget_file_df['Total Months'] = budget_file_df.iloc[:, 2:].sum(axis=1)

total_months = budget_file_df["Date"].count()

total_months


# In[38]:


# summary_table = pd.DataFrame({"Total Months": [Date_count],
#                               "Earliest Year": earliest_year,
#                               "Latest Year": latest_year})
# summary_table


# In[39]:


# The sum of Profit/Losses
profit_losses_df = budget_file_df["Profit/Losses"].sum()

profit_losses_df.sum()


# In[40]:


# The average change of the profit/losses
count = budget_file_df["Profit/Losses"].value_counts()
count


# In[41]:


#The average change of the profit/losses
budget_file_df["profit/losses"] = budget_file_df["Profit/Losses"].diff()
average_change = round(budget_file_df["profit/losses"].mean(), 2)



average_change


# In[42]:


# Calculate the earliest/latest date 
small_amount = budget_file_df["profit/losses"].min()
big_amount = budget_file_df["profit/losses"].max()


# In[43]:


# Hint: use the pandas' sum() method to get the sum for each row
big_amount_increase = budget_file_df.loc[budget_file_df["profit/losses"] == big_amount, "Date"]
small_amount_decrease = budget_file_df.loc[budget_file_df["profit/losses"] == small_amount, "Date"]


# In[44]:


big_Profit_increase = big_amount_increase.iloc[0]
small_Profit_decrease = small_amount_decrease.iloc[0]


# In[45]:


Increase_Profit = budget_file_df.loc[budget_file_df["profit/losses"] == big_amount, "Date"]
Increase_Profit


# In[46]:


Decrease_Profit = budget_file_df.loc[budget_file_df["profit/losses"] == small_amount, "Date"]
Decrease_Profit


# In[47]:


print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${profit_losses_df}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase: {big_Profit_increase} ({big_amount})")
print(f"Greatest Decrease: {small_Profit_decrease} ({small_amount})")


# In[ ]:





# In[ ]:





# In[ ]:





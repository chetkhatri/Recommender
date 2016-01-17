
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

df = pd.read_csv("family_details.csv", header=0)



# In[ ]:

def get_recommendations(firstname, middlename , lastname, df):
 
    candidate_df = df[(df['firstname'] == firstname) & (df['middlename'] == middlename) & (df['lastname'] == lastname)]
 
    if (candidate_df['gender'].values[0] == 'Male'):
        df = df[(df['gender']=='Female') & (df['age'] <= candidate_df.age.values[0].astype('int'))]
        df = df[(df.age >= candidate_df.age.values[0].astype('int') - 5 )]
    elif (candidate_df['gender'].values[0] == 'Female'):
        df = df[(df['gender']=='Male') & (df['age'] >= candidate_df.age.values[0].astype('int'))]
        df = df[(df.age <= candidate_df.age.values[0].astype('int') + 5 )]
    df = df[(df.lastname != candidate_df.lastname.values[0]) & (df.maritalStatus == 'Unmarried')]
    
    print df[:5]
    


# In[ ]:

get_recommendations("Deepali","Mansukh", "Nirmal", df)


# In[ ]:




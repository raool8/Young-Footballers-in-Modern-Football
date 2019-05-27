# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:15:36 2019

@author: Rahul
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset 
missing_values = ['na','NA','nan']                         #Assigning missing values for python to recognize
dataset = pd.read_csv('fifa19_dataset.csv', na_values = missing_values)

#Subsetting the main dataset 
df = pd.DataFrame(dataset, columns = ['ID','Name','Age','Overall','Potential','Club','Work Rate','Body Type','Height','Weight','ShortPassing','Dribbling','LongPassing','BallControl','Acceleration','SprintSpeed','Agility','Balance','Stamina','Strength','Agression','Vision','Composure'])
df.isnull().sum()                                          #find out how many nulls in each column 
df.drop('Agression', axis = 1,inplace = True)              #all values nan 
df.dropna(inplace = True)                                  #Getting rid of all nan clubs
df.drop('Work Rate',axis = 1, inplace = True)              #Useless column 

#Renaming columns to account for value conversions from string to float 
df.rename(columns = {'Body Type':'Body_Type','Height':'Height (in)','Weight': 'Weight (lbs)'},inplace = True)

#Converting height(string) to inches(float) 
def parse_ht(ht):
    # format: 7' 0.0"
    ht_ = ht.split("'")
    ft_ = float(ht_[0])
    in_ = float(ht_[1].replace("\"",""))
    return (12*ft_) + in_
df['Height'] = df['Height'].apply(lambda x:parse_ht(x))

#Converting weight(string) to weight(float)
def parse_wt(wt):
    wt_ = wt.split("l")
    a_wt = float(wt_[0])
    return a_wt
df['Weight'] = df['Weight'].apply(lambda x:parse_wt(x))


#Identifying unique values of body type to correct to withing the following 3 types: Lean, Normal & Stocky 
df['Body_Type'].unique()

#Replacing with proper body type strings: 
df['Body_Type'].replace(['Messi','C. Ronaldo','Neymar','Courtois','PLAYER_BODY_TYPE_25','Shaqiri','Akinfenwa'],['Lean','Normal','Lean','Lean','Normal','Stocky','Stocky'], inplace = True)

#Exporting dataframe to csv file for input to Tableau for data visualization 
export_csv = df.to_csv (r'D:\Data Visualization Projects\FIFA 19\newfile.csv', index = False, header=True)
    
    
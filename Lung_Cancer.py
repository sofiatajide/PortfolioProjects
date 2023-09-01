#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def read_csv():
    # Method to read the CSV file "lung_cancer_examples.csv" using pandas.
    df = pd.read_csv('lung_cancer_examples.csv')
    return df


def check_duplicates():
    df = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    duplicated_count = df.duplicated().sum()
    # Returns: The number of duplicated rows found in the DataFrame.
    return duplicated_count



def check_null_values():
    df = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    null_counts = df.isnull().sum()
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    return null_counts


def rename_column():
    # do not edit the predefined function name
    df = read_csv()
    # Rename columns 'Alkhol' to 'Alcohol'.
    df.rename(columns = {'Alkhol' : 'Alcohol'}, inplace = True)
    return df


def check_smoke_value():
    # do not edit the predefined function name
    data = rename_column()

    # Count the occurrences of each unique value in the 'Smokes' column
    smoke_counts = data['Smokes'].value_counts()

    # Return the counts of each unique smoking habit value
    return smoke_counts


# In[4]:




# Function to categorize individuals based on the number of cigarettes smoked per day
def categorize_smokers(x):
    #If x is 0, categorize the person as 'Non-Smokers'.
    if x == 0:
        return 'Non-Smokers'
    # If x is less than or equal to 2, categorize the person as 'Light Smokers'.
    elif x <= 2:
        return 'Light Smokers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Smokers'.
    elif x <= 10:
        return 'Mediocre Smokers'    
    # If x is greater than 10, categorize the person as 'Heavy Smokers'.
    else:
        return 'Heavy Smokers'
    pass




# Function to process the smoking data and add a new 'Smoking_Category' column
def smokes():
    # do not edit the predefined function name
    data = t1.rename_column()

    # Applying the 'categorize_smokers' function to each value in the 'Smokes' column
    # and storing the result in a new column 'Smoking_Category'
    data['Smoking_Category'] = data['Smokes'].apply(categorize_smokers)

    # Returning the modified dataset with the new 'Smoking_Category' column
    return data




def check_alcohol_value():
    # do not edit the predefined function name
    data = smokes()


    # Count the occurrences of each unique value in the 'Alcohol' column
    alcohol_counts = data['Alcohol'].value_counts()

    # Return the counts of each unique smoking habit value
    return alcohol_counts







# Function to categorize individuals based on the number of alcohol drinks consumed per day
def categorize_alcohol(x):

    # If x is 0, categorize the person as 'Non-Drinkers'.
    if x == 0:
        return 'Non-Drinkers'
    # If x is less than or equal to 2, categorize the person as 'Light Drinkers'.
    elif x <= 2:
        return 'Light Drinkers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Drinkers'.
    elif x <= 10:
        return 'Mediocre Drinkers'
    # If x is greater than 10, categorize the person as 'Heavy Drinkers'.
    else:
        return 'Heavy Drinkers'
    pass




# Function to process the alcohol data and add a new 'Alcohol_Category' column
def alkhol():
    # Assuming the 'smokes()' function retrieves the dataset with the 'Smokes' column and the 'Alcohol' column
    data = smokes()

    # Applying the 'categorize_alcohol' function to each value in the 'Alcohol' column
    # and storing the result in a new column 'Alcohol_Category'
    data['Alcohol_Category'] = data['Alcohol'].apply(categorize_alcohol)

    # Returning the modified dataset with the new 'Alcohol_Category' column
    return data




def export_the_dataset():
    # do not edit the predefined function name
    df = alkhol()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv('lung_cancer.csv', index=False)
    return df



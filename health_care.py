# import os
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder
#
#
# ## loading the file
# health_care = pd.read_csv('./healthcare/train_data.csv')
#
#
#
#
# """
# The columns to be pre-processed from string to numerical values are :
# 1. Hospital_type_code
# 2. Hospital_region_code
# 3. Department
# 4. Ward_Type
# 5. Ward_Facility_Code
# 6. City_Code_Patient
# 7. Type of Admission
# 8. Severity of Illness
# 9. Age
# 10. Admission_Deposit
# 11. Stay
# """
#
# ## Pre processing these columns
#
# string_columns = ['Hospital_type_code', 'Hospital_region_code', 'Department', 'Ward_Type', 'Ward_Facility_Code', 'City_Code_Patient', 'Type of Admission', 'Severity of Illness', 'Age',  'Stay' ]
# encoder = LabelEncoder()
#
# ## label_encoded data
# X_le = health_care.drop(['Stay', 'case_id', 'patientid'], axis=1)
# y_le = health_care['Stay']
#
# for column in string_columns :
#     if column == 'Stay' :
#         y_le = encoder.fit_transform(y_le)
#     else :
#         X_le[column] = encoder.fit(X_le[column]).transform(X_le[column])
#
# ## getting the inputs and labels
#
# X = X_le.values
# y = y_le


#TS_CW_draft
import os
import pandas as pd
import numpy as np
import sklearn as sk
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
%matplotlib inline


# Importing the data set
path = "healthcare"

filename_read = os.path.join(path, "train_data.csv")
df = pd.read_csv(filename_read, na_values=['NA', '?'])

print(df.shape)
print(df.columns)
df.head(10)

# Exploratory data analysis
#creating a copy of df to have an original for further manipulation
new_df = df.copy()
new_df = new_df.select_dtypes(include=["int","float"])

headers = list(new_df.columns.values)

fields = []
for field in headers:
    fields.append({
        "name":field,
        "mean":df[field].mean(),
        "var":df[field].var(),
        "sdev":df[field].std()
    })
for field in fields:
    print(field)

#????here should an analysis of columns means and st dev

#Missing Values
#checking for missing values
df.isnull().values.any()
#Checking number of NANs for each column, in order to understand how many missing values there are in a dataframe.
print("# of NaN in each columns:", df.isnull().sum(), sep='\n')

"""
To make sure we consider all the correct features to make an accurate prediction, it may be useful to create some plots to have a better understanding of our data.
We will be using the Python data visualisation library seaborn.
We could begin by visualising the length of stays by type of admissions etc., by using a countplot(), that shows the counts of observations in each categorical bin using bars.
"""

#sorting by Stay for better representation in the visualisations
df= df.sort_values(by = "Stay", ascending = True)
#visualising the length of stays by age
#plot size
plt.figure(figsize = (15,4))
#plot title
plt.title("Age", fontdict = {'fontsize':15})
ax = sns.countplot(x = "Age", hue = 'Stay', data = df)
#?? comments
"""
the age group risk - 21-80y.o.
"""

#visualising the length of stays by type of admissions
#plot size
plt.figure(figsize = (15,4))
#plot title
plt.title("Type of Admission", fontdict = {'fontsize': 15})
ax = sns.countplot(x = "Type of Admission", hue = 'Stay', data = df)
"""???? comments on the graph
Emergency and Trauma and mostly from 11 - 40 and range 51-60
Next, it may be interesting to look at the Severity of Illness segments by stay.
Again, we can use a count plot to visualise this.'
""""

#visualising the length of stays by Severity of Illness
#plot size
plt.figure(figsize = (15,4))
#plot title
plt.title("Severity of Illness", fontdict = {'fontsize':15})
ax = sns.countplot(x = "Severity of Illness", hue = 'Stay', data = df)

"""
comments on the graph:
mostly moderate and minor, and in age range 11-40 and range 51-60
"""

#visualising the length of stays by Available Extra Rooms in Hospital
#plot size
plt.figure(figsize = (20,4))
#plot title
plt.title("Available Extra Rooms in Hospital", fontdict = {'fontsize':15})
ax = sns.countplot(x = "Available Extra Rooms in Hospital", hue = 'Stay', data = df)

"""
comments on the graph
most rooms have additional 2-4 beds in the room available.
"""
#visualising the length of stays by Department
#plot size
plt.figure(figsize = (15,8))
#plot title
plt.title("Department", fontdict = {'fontsize':15})
ax = sns.countplot(x = "Department", hue = 'Stay', data = df)

"""
mostly gynecology department
"""
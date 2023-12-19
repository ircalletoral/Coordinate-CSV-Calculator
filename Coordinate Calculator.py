#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd


# In[43]:


#Obtain the CVS File for ArcGIS 
data_sheet = pd.read_csv("C:/Users/ircal/Desktop/Coding/ArcGIS Coordinates/Testing coordinates.csv", encoding='utf-8')


# In[44]:


#Coordinate Calculator for ArcGIS Model
name = input("What is the name of your location?")

#Latitude Input 
lat_d, lat_m, lat_s, y_axis = input("Please input your Latitude coordinates with a space in between, include S or N. Ex. 2 29 23 S : ").split()

lat_d = int(lat_d)
lat_m = int(lat_m)
lat_s = int(lat_s)

#Longitude Input 
long_d, long_m, long_s, x_axis = input("Please input your Longitude coordinates with a space in between, include E or W. Ex. 2 29 23 W : ").split()

long_d = int(long_d)
long_m = int(long_m)
long_s = int(long_s)

altitude = input("Please input the altitude in m")
altitude = int(altitude)


# In[45]:


#Axis Calculator Based on the Greenwich System 


# In[46]:


#Make them all uppercase to make it easier
x_axis = x_axis.upper()
y_axis = y_axis.upper()

#Calculate the variables

#Latitude value

if x_axis == "E":
    x_axis = 1
    x_axis = int(x_axis)
elif x_axis == "W":
    x_axis = -1
    x_axis = int(x_axis)
else: 
    print("Please use either E or W for your variable")
    
    
#Longitude Value

if y_axis == "N":
    y_axis = 1
    y_axis = int(y_axis)
elif y_axis == "S":
    y_axis = -1
    y_axis = int(y_axis)
else:
    print("Please use either N or S for your variable")
    




# In[47]:


#Calculator itself
#Degree to Coordinates for ArcGIS
def degree_to_coordinates(d, m, s, axis):
    d = d
    m = m / 60
    s = s / 3600
    coordinate = d + m + s
    coordinate = coordinate * axis
    return coordinate


# In[48]:


#Obtain the X and Y coordinates

x_coordinate = degree_to_coordinates(long_d, long_m, long_s, x_axis)
y_coordinate = degree_to_coordinates(lat_d, lat_m, lat_s, y_axis)


# In[49]:


#System to add the values to each column
new_data = {'Name' : [name], 'Longitude (X)' : [x_coordinate], 'Latitude (Y)' : [y_coordinate]}
new_data_df = pd.DataFrame(new_data)


# In[50]:


#Concentrate new dataframe with new data 

updated_csv_cor = pd.concat([data_sheet, new_data_df], ignore_index = True)

#import to csv sheet 

updated_csv_cor.to_csv("C:/Users/ircal/Desktop/Coding/ArcGIS Coordinates/Testing coordinates.csv", encoding='utf-8', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





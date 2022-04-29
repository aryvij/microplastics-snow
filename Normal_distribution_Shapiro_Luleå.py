from matplotlib.text import get_rotation
import pandas as pd
import matplotlib.markers as mark
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
#import Normal_distribution_Shapiro as shapiro
import warnings
warnings.filterwarnings("ignore")


from scipy.stats import norm
from scipy.stats import shapiro

#Luleå_BITUMEN_TOTAL
print ("Luleå_bitumen_total")
df = pd.read_csv('MP_Data.csv')
data_Luleå_bitumen_tot =  df [df.City == 'Lulea']  [df.Mesh_size == 5000] [df.MP_category == 'Bitumen']['Concentration']
data = data_Luleå_bitumen_tot.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå)  

#Luleå_BITUMEN_300
print ("Luleå_bitumen_300")
df = pd.read_csv('MP_Data.csv')
data_Luleå_bitumen_300 =  df [df.City == 'Lulea']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
data = data_Luleå_bitumen_300.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 

#Luleå_BITUMEN_100
print ("Luleå_bitumen_100")
df = pd.read_csv('MP_Data.csv')
data_Luleå_bitumen_100 =  df [df.City == 'Lulea']  [df.Mesh_size == 100] [df.MP_category == 'Bitumen']['Concentration']
data = data_Luleå_bitumen_100.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 


#Luleå_BITUMEN_50
print ("Luleå_bitumen_50")
df = pd.read_csv('MP_Data.csv')
data_Luleå_bitumen_50 =  df [df.City == 'Lulea']  [df.Mesh_size == 50] [df.MP_category == 'Bitumen']['Concentration']
data = data_Luleå_bitumen_50.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 

#Luleå_RUBBER_TOTAL
df = pd.read_csv('MP_Data.csv')
print ("Luleå_rubbern_total")
data_Luleå_rubber_tot =  df [df.City == 'Lulea']  [df.Mesh_size == 5000] [df.MP_category == 'Rubber']['Concentration']
data = data_Luleå_rubber_tot.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå)  

#Luleå_RUBBER_300
print ("Luleå_rubber_300")
df = pd.read_csv('MP_Data.csv')
data_Luleå_rubber_300 =  df [df.City == 'Lulea']  [df.Mesh_size == 300] [df.MP_category == 'Rubber']['Concentration']
data = data_Luleå_rubber_300.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 

#Luleå_RUBBER_100
print ("Luleå_rubber_100")
df = pd.read_csv('MP_Data.csv')
data_Luleå_rubber_100 =  df [df.City == 'Lulea']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
data = data_Luleå_rubber_100.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 


#Luleå_RUBBER_50
print ("Luleå_rubber_50")
df = pd.read_csv('MP_Data.csv')
data_Luleå_rubber_50 =  df [df.City == 'Lulea']  [df.Mesh_size == 50] [df.MP_category == 'Rubber']['Concentration']
data = data_Luleå_rubber_50.values.tolist()
print (data)
shapiro_test_Luleå = shapiro(data)
print (shapiro_test_Luleå) 



 


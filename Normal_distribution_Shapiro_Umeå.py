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

#UMEÅ_BITUMEN_TOTAL
print ("Umeå_bitumen_total")
df = pd.read_csv('MP_Data.csv')
data_Umeå_bitumen_tot =  df [df.City == 'Umea']  [df.Mesh_size == 5000] [df.MP_category == 'Bitumen']['Concentration']
data = data_Umeå_bitumen_tot.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå)  

#UMEÅ_BITUMEN_300
print ("Umeå_bitumen_300")
df = pd.read_csv('MP_Data.csv')
data_Umeå_bitumen_300 =  df [df.City == 'Umea']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
data = data_Umeå_bitumen_300.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 

#UMEÅ_BITUMEN_100
print ("Umeå_bitumen_100")
df = pd.read_csv('MP_Data.csv')
data_Umeå_bitumen_100 =  df [df.City == 'Umea']  [df.Mesh_size == 100] [df.MP_category == 'Bitumen']['Concentration']
data = data_Umeå_bitumen_100.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 


#UMEÅ_BITUMEN_50
print ("Umeå_bitumen_50")
df = pd.read_csv('MP_Data.csv')
data_Umeå_bitumen_50 =  df [df.City == 'Umea']  [df.Mesh_size == 50] [df.MP_category == 'Bitumen']['Concentration']
data = data_Umeå_bitumen_50.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 

#UMEÅ_RUBBER_TOTAL
df = pd.read_csv('MP_Data.csv')
print ("Umeå_rubbern_total")
data_Umeå_rubber_tot =  df [df.City == 'Umea']  [df.Mesh_size == 5000] [df.MP_category == 'Rubber']['Concentration']
data = data_Umeå_rubber_tot.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå)  

#UMEÅ_RUBBER_300
print ("Umeå_rubber_300")
df = pd.read_csv('MP_Data.csv')
data_Umeå_rubber_300 =  df [df.City == 'Umea']  [df.Mesh_size == 300] [df.MP_category == 'Rubber']['Concentration']
data = data_Umeå_rubber_300.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 

#UMEÅ_RUBBER_100
print ("Umeå_rubber_100")
df = pd.read_csv('MP_Data.csv')
data_Umeå_rubber_100 =  df [df.City == 'Umea']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
data = data_Umeå_rubber_100.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 


#UMEÅ_RUBBER_50
print ("Umeå_rubber_50")
df = pd.read_csv('MP_Data.csv')
data_Umeå_rubber_50 =  df [df.City == 'Umea']  [df.Mesh_size == 50] [df.MP_category == 'Rubber']['Concentration']
data = data_Umeå_rubber_50.values.tolist()
print (data)
shapiro_test_umeå = shapiro(data)
print (shapiro_test_umeå) 



 


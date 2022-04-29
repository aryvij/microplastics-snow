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

#High_traffic_intensity_BITUMEN_TOTAL
print ("High_traffic_intensity_bitumen_total")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_bitumen_tot =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 5000] [df.MP_category == 'Bitumen']['Concentration']
data = data_High_traffic_intensity_bitumen_tot.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity)  

#High_traffic_intensity_BITUMEN_300
print ("High_traffic_intensity_bitumen_300")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_bitumen_300 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
data = data_High_traffic_intensity_bitumen_300.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 

#High_traffic_intensity_BITUMEN_100
print ("High_traffic_intensity_bitumen_100")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_bitumen_100 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 100] [df.MP_category == 'Bitumen']['Concentration']
data = data_High_traffic_intensity_bitumen_100.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 


#High_traffic_intensity_BITUMEN_50
print ("High_traffic_intensity_bitumen_50")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_bitumen_50 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 50] [df.MP_category == 'Bitumen']['Concentration']
data = data_High_traffic_intensity_bitumen_50.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 

#High_traffic_intensity_RUBBER_TOTAL
df = pd.read_csv('MP_Data.csv')
print ("High_traffic_intensity_rubber_total")
data_High_traffic_intensity_rubber_tot =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 5000] [df.MP_category == 'Rubber']['Concentration']
data = data_High_traffic_intensity_rubber_tot.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity)  

#High_traffic_intensity_RUBBER_300
print ("High_traffic_intensity_rubber_300")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_rubber_300 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 300] [df.MP_category == 'Rubber']['Concentration']
data = data_High_traffic_intensity_rubber_300.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 

#High_traffic_intensity_RUBBER_100
print ("High_traffic_intensity_rubber_100")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_rubber_100 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
data = data_High_traffic_intensity_rubber_100.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 


#High_traffic_intensity_RUBBER_50
print ("High_traffic_intensity_rubber_50")
df = pd.read_csv('MP_Data.csv')
data_High_traffic_intensity_rubber_50 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 50] [df.MP_category == 'Rubber']['Concentration']
data = data_High_traffic_intensity_rubber_50.values.tolist()
print (data)
shapiro_test_High_traffic_intensity = shapiro(data)
print (shapiro_test_High_traffic_intensity) 



 


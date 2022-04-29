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

#Distance_from_intersection_D1_BITUMEN_TOTAL
print ("Distance_from_intersection_D1_bitumen_total")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_bitumen_tot =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 5000] [df.MP_category == 'Bitumen']['Concentration']
data = data_Distance_from_intersection_D1_bitumen_tot.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1)  

#Distance_from_intersection_D1_BITUMEN_300
print ("Distance_from_intersection_D1_bitumen_300")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_bitumen_300 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
data = data_Distance_from_intersection_D1_bitumen_300.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 

#Distance_from_intersection_D1_BITUMEN_100
print ("Distance_from_intersection_D1_bitumen_100")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_bitumen_100 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 100] [df.MP_category == 'Bitumen']['Concentration']
data = data_Distance_from_intersection_D1_bitumen_100.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 


#Distance_from_intersection_D1_BITUMEN_50
print ("Distance_from_intersection_D1_bitumen_50")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_bitumen_50 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 50] [df.MP_category == 'Bitumen']['Concentration']
data = data_Distance_from_intersection_D1_bitumen_50.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 

#Distance_from_intersection_D1_RUBBER_TOTAL
df = pd.read_csv('MP_Data.csv')
print ("Distance_from_intersection_D1_rubbern_total")
data_Distance_from_intersection_D1_rubber_tot =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 5000] [df.MP_category == 'Rubber']['Concentration']
data = data_Distance_from_intersection_D1_rubber_tot.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1)  

#Distance_from_intersection_D1_RUBBER_300
print ("Distance_from_intersection_D1_rubber_300")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_rubber_300 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 300] [df.MP_category == 'Rubber']['Concentration']
data = data_Distance_from_intersection_D1_rubber_300.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 

#Distance_from_intersection_D1_RUBBER_100
print ("Distance_from_intersection_D1_rubber_100")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_rubber_100 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
data = data_Distance_from_intersection_D1_rubber_100.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 


#Distance_from_intersection_D1_RUBBER_50
print ("Distance_from_intersection_D1_rubber_50")
df = pd.read_csv('MP_Data.csv')
data_Distance_from_intersection_D1_rubber_50 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 50] [df.MP_category == 'Rubber']['Concentration']
data = data_Distance_from_intersection_D1_rubber_50.values.tolist()
print (data)
shapiro_test_Distance_from_intersection_D1 = shapiro(data)
print (shapiro_test_Distance_from_intersection_D1) 



 


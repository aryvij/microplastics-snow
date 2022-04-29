from matplotlib.text import get_rotation
import pandas as pd
import matplotlib.markers as mark
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
#import Normal_distribution_Shapiro as shapiro
import warnings
from pandas.core.frame import DataFrame
from bioinfokit.analys import stat
warnings.filterwarnings("ignore")


from scipy.stats import ttest_rel

df = pd.read_csv('MP_Data.csv')
file_name = 'output_rubber_100.txt'
with open(file_name,'w') as f:

    #Rubber 100


    #1.L0CATION 

    #UMEÅ_Rubber_100
    data_Umeå_Rubber_100 =  df [df.City == 'Umea']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_1 = data_Umeå_Rubber_100.values.tolist()

    #LULEÅ_Rubber_100
    data_Luleå_Rubber_100 =  df [df.City == 'Lulea']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_2 = data_Luleå_Rubber_100.values.tolist()

    new_data = DataFrame({'Umea':data_1,'Lulea':data_2})

    res= stat()
    res.ttest(df=new_data, res=['Umea', 'Lulea'], test_type=3)

    f.write ("Comparison Umeå-Lueå-100 Rubber")
    f.write (res.summary)

    #2.TRAFFIC_INTENSITY

    #High_traffic_intensity_Rubber_100
    df = pd.read_csv('MP_Data.csv')
    data_High_traffic_intensity_Rubber_100 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_1 = data_High_traffic_intensity_Rubber_100.values.tolist()

    #Low_traffic_intensity_Rubber_100
    df = pd.read_csv('MP_Data.csv')
    data_Low_traffic_intensity_Rubber_100 =  df [df.Traffic_intensity == 'Low']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_2 = data_Low_traffic_intensity_Rubber_100.values.tolist()

    new_data = DataFrame({'High':data_1,'Low':data_2})
    res= stat()
    res.ttest(df=new_data, res=['High', 'Low'], test_type=3)

    f.write ("Comparison HT-LT-100 Rubber")
    f.write (res.summary)

    #3.DISTANCE_FROM_INTERSECTION

    #Distance_from_intersection_D1_Rubber_100
    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_intersection_D1_Rubber_100 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_1 = data_Distance_from_intersection_D1_Rubber_100.values.tolist()
    #Distance_from_intersection_D2_Rubber_100

    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_intersection_D2_Rubber_100 =  df [df.Distance_from_intersection == 'D2']  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_2= data_Distance_from_intersection_D2_Rubber_100.values.tolist()

    new_data = DataFrame({'D1':data_1,'D2':data_2})
    res= stat()
    res.ttest(df=new_data, res=['D1', 'D2'], test_type=3)

    f.write ("Comparison D1-D2-100 Rubber")
    f.write (res.summary)

    #4.DISTANCE_FROM_EDGE_OF_ROAD

    #Distance_from_edge_of_road_Rubber_100
    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_edge_point_five_Rubber_100 =  df [df.Distance_from_road == 0.5]  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_1 = data_Distance_from_edge_point_five_Rubber_100.values.tolist()

    #Distance_from_edge_2.5_Rubber_100

    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_edge_two_point_five_Rubber_100 =  df [df.Distance_from_road == 2.5]  [df.Mesh_size == 100] [df.MP_category == 'Rubber']['Concentration']
    data_2= data_Distance_from_edge_two_point_five_Rubber_100.values.tolist()

    new_data = DataFrame({'0.5':data_1,'2.5':data_2})
    res= stat()
    res.ttest(df=new_data, res=['0.5', '2.5'], test_type=3)

    f.write ("Comparison 0.5-2.5-100 Rubber")
    f.write (res.summary)
f.close()
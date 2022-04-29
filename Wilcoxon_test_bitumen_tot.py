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


from scipy.stats import wilcoxon


df = pd.read_csv('MP_Data.csv')
file_name = 'Wilcoxon_output_bitumen_tot.txt'
with open(file_name,'w') as f:

    #BITUMEN 300


    #1.L0CATION 

    #UMEÅ_BITUMEN_300
    data_Umeå_bitumen_300 =  df [df.City == 'Umea']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_1 = data_Umeå_bitumen_300.values.tolist()

    #LULEÅ_BITUMEN_300
    data_Luleå_bitumen_300 =  df [df.City == 'Lulea']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_2 = data_Luleå_bitumen_300.values.tolist()

    stat, p = wilcoxon (data_1, data_2)

    f.write ("\nComparison Umeå-Lueå-Tot bitumen")
    f.write('\nStatistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
	    f.write('\nSame distribution \n Accept noll hypothesis')
    else:
	    f.write('\nDifferent distribution \n Reject noll hypothesis')

    #2.TRAFFIC_INTENSITY

    #High_traffic_intensity_BITUMEN_300
    df = pd.read_csv('MP_Data.csv')
    data_High_traffic_intensity_bitumen_300 =  df [df.Traffic_intensity == 'High']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_1 = data_High_traffic_intensity_bitumen_300.values.tolist()

    #Low_traffic_intensity_BITUMEN_300
    df = pd.read_csv('MP_Data.csv')
    data_Low_traffic_intensity_bitumen_300 =  df [df.Traffic_intensity == 'Low']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_2 = data_Low_traffic_intensity_bitumen_300.values.tolist()

    stat, p = wilcoxon (data_1, data_2)    

    f.write ("\nComparison HT-LT-Tot bitumen")
    f.write('\nStatistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
	    f.write('\nSame distribution \n Accept noll hypothesis')
    else:
	    f.write('\nDifferent distribution \n Reject noll hypothesis')

    #3.DISTANCE_FROM_INTERSECTION

    #Distance_from_intersection_D1_BITUMEN_300
    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_intersection_D1_bitumen_300 =  df [df.Distance_from_intersection == 'D1']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_1 = data_Distance_from_intersection_D1_bitumen_300.values.tolist()
    #Distance_from_intersection_D2_BITUMEN_300

    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_intersection_D2_bitumen_300 =  df [df.Distance_from_intersection == 'D2']  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_2= data_Distance_from_intersection_D2_bitumen_300.values.tolist()

    stat, p = wilcoxon (data_1, data_2)

    f.write ("\nComparison D1-D2-Tot bitumen")
    f.write('\nStatistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
	    f.write('\nSame distribution \n Accept noll hypothesis')
    else:
	    f.write('\nDifferent distribution \n Reject noll hypothesis')
    

    #4.DISTANCE_FROM_EDGE_OF_ROAD

    #Distance_from_edge_of_road_BITUMEN_300
    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_edge_point_five_bitumen_300 =  df [df.Distance_from_road == 0.5]  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_1 = data_Distance_from_edge_point_five_bitumen_300.values.tolist()

    #Distance_from_edge_2.5_BITUMEN_300

    df = pd.read_csv('MP_Data.csv')
    data_Distance_from_edge_two_point_five_bitumen_300 =  df [df.Distance_from_road == 2.5]  [df.Mesh_size == 300] [df.MP_category == 'Bitumen']['Concentration']
    data_2= data_Distance_from_edge_two_point_five_bitumen_300.values.tolist()

    stat, p = wilcoxon (data_1, data_2)
    
    f.write ("\nComparison 0.5-2.5-Tot bitumen")
    f.write('\nStatistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
	    f.write('\nSame distribution \n Accept noll hypothesis')
    else:
	    f.write('\nDifferent distribution \n Reject noll hypothesis')

f.close()
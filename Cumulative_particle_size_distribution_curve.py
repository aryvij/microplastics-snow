from operator import index
from turtle import color
from matplotlib import colors
from matplotlib.text import get_rotation
import pandas as pd
import matplotlib.markers as mark
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
'''
df = pd.read_csv('PSD_long_data.csv')
g = sns.catplot(x="Diameter (µm)", y="Particle number (%)", hue='Sample_name', data=df, kind='point')   
ticks, labels = plt.xticks()
plt.xticks(ticks[::20], labels[::20])
#plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
#set_major_formatter('{x:9<5.1f}')
#
plt.savefig('PSD.png')
'''
df = pd.read_csv('Cumulative_curve.csv')

#sample_names = ['S1','S2','S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10','S11', 'S12', 'S13', 'S14', 'S15', 'S16']
sample_names = ['S1','S2','S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10','S11', 'S12', 'S13', 'S14', 'S15', 'S16']

fig, axes = plt.subplots(8,2, figsize=(25, 45))

for sample_name in sample_names:
        df_number = df[(df.Type == 'Number') & (df.Sample_name == sample_name)]
        df_area = df[(df.Type == 'Area') & (df.Sample_name == sample_name)]
        df_volume = df[(df.Type == 'Volume') & (df.Sample_name == sample_name)]
        # print(df_number)
        i = sample_names.index(sample_name)
       

        g = sns.lineplot(ax=axes[i % 8][int(i/8)], x="Diameter (µm)", y="Cumulative", color='black',
                        data=df_number, marker='x', label = 'Number').set(title=sample_name)
        g = sns.lineplot(ax=axes[i % 8][int(i/8)], x="Diameter (µm)", y="Cumulative", color='black',
                        data=df_area, markers='+', label = 'Area')
        g = sns.lineplot(ax=axes[i % 8][int(i/8)], x="Diameter (µm)", y="Cumulative", color='black',
                        data=df_volume, markers='v', label = 'Volume')
        
        
        g.get_legend().remove()
        g.set(xlabel=None)
        g.set(ylabel=None)
        handles, labels = g.get_legend_handles_labels()
        fig.legend(handles, labels, loc='lower right')
        fig.text(0.5,0.1, "Diameter (µm)", ha="center", va="center", size = 20)
        fig.text(0.08,0.5, "Cumulative pervcentage of particles % (number, area or volume)", ha="center", va="center", rotation=90, size = 20)
        #fig.subplots_adjust(hspace=.5)
        #fig.subplots_adjust(wspace=.1)
        #handles=[setosa, versi, virgi]
        #plt.tight_layout() 
        #plt.gcf().legend                              
        #g.get_legend
        #g.get_legend().remove()
        #ticks, labels = plt.xticks()
        g.set_xlim(0, 5000)
        #plt.text(0.5, 0.04, 'common X', ha='center')
        #plt.text(0.04, 0.5, 'common Y', va='center', rotation='vertical')
        #plt.xticks(ticks[::20], labels[::20])




#
plt.savefig('Cumulative_curve_16.png',bbox_inches='tight')

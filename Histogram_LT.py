from matplotlib.text import get_rotation
import pandas as pd
import matplotlib.markers as mark
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


import pandas as pd

def plot_histogram(fig, ax,data,MP_category,mesh_size):

    data =  data [data.Traffic_intensity == 'Low']['Concentration']
    print (data)
    counts, bins = np.histogram(data)
    ax.hist(bins[:-1], bins, weights=counts)
    
    ax.set_title(MP_category+ '_' + str(mesh_size), size = 14)
    
    
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right')
    
    plt.subplots_adjust(hspace=0.5) 

def plot_all_graphs(data):

    MP_CATEGORIES = ['Bitumen', 'Rubber']
    MESH_SIZES = [5000, 300,100,50]
    
    fig, axs = plt.subplots(2,4, sharey = False, figsize=(12,12),constrained_layout=False)  
    fig.text(0.05, 0.5, 'Number of particles/L' , va='center', rotation='vertical', size = 14)
    fig.text(0.5, 0.01, 'Sample name' , va='center', rotation='horizontal', size = 14)
    fig.text(0.25, 0.95, 'Variation in MP concentration - Luleå and Umeå' , va='center', rotation='horizontal', size = 16, weight="bold")
    #handles, labels = ax.get_legend_handles_labels()
    #fig.legend(handles, labels, loc='upper right')
    for MP_category in MP_CATEGORIES:
        i = MP_CATEGORIES.index(MP_category)
        MP_category_data = data[data['MP_category'] == MP_category]
        for mesh_size in MESH_SIZES:
            j = MESH_SIZES.index (mesh_size)
            mesh_size_data = MP_category_data[MP_category_data['Mesh_size'] == mesh_size]
            plot_histogram(fig, axs[i][j], mesh_size_data,MP_category,mesh_size)
          
    plt.savefig('Histogram_LT.png')


if __name__ == '__main__':
    df = pd.read_csv('MP_Data.csv')
    plot_all_graphs(df)
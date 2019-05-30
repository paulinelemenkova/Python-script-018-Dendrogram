#!/usr/bin/env python
# coding: utf-8
# In[101]:
# Libraries
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import os

# Data set
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
df = df.set_index('profile')
del df.index.name
df
# Calculate the distance between each sample
Z = hierarchy.linkage(df, 'average')
# Make the dendro
dendrogram(Z, labels=df.index, leaf_rotation=0, orientation="left", 
           distance_sort='ascending', )
#plt.axvline(x=1700, c='grey', lw=1, linestyle='dashed')
#plt.axvline(x=2500, c='grey', lw=1, linestyle='dashed')

plt.title('Hierarchical cluster dendrogram for the geomorphic similarity \nof the 25bathymetric profiles, Mariana Trench', fontsize=10, fontfamily='sans-serif')
plt.show()

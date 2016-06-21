# Using the magic encoding
# -*- coding: utf-8 -*-
 
from __future__ import unicode_literals
import numpy as np
import matplotlib.pylab as pl
import sys
from sklearn.manifold import TSNE
import codecs
 
listWords = ['bank', 'good', 'juice', 'google', 'apple', 'book']

listWords1 = ['book']
listWords2 = ['bank']
listWords3 = ['juice']
listWords4 = ['apple']
listWords5 = ['good']
listWords6 = ['google']
 
data = np.loadtxt("sample"+"_vec.txt")
#data = np.random.random((1000,50))
 
label=map(lambda s:s.strip(), codecs.open("sample"+"_word.txt",encoding="utf-8").readlines())
 
model = TSNE(n_components=2, random_state=0)
x, y = model.fit_transform(data).T
 
fig, ax = pl.subplots(figsize=(15, 15))
 
# nice points
#scatter = ax.scatter(x, y, alpha=0.2, color='k', facecolor='none', s=100)
 
# invisible points
scatter = ax.scatter(x, y, alpha=0.)
 
for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords1):
                              ax.text(x[i], y[i], label[i], color='red', fontsize=14)

for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords2):
                              ax.text(x[i], y[i], label[i], color='blue', fontsize=14)

for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords3):
                              ax.text(x[i], y[i], label[i], color='yellow', fontsize=14)

for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords4):
                              ax.text(x[i], y[i], label[i], color='green', fontsize=14)                                                                                          

for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords5):
                              ax.text(x[i], y[i], label[i], color='cyan', fontsize=14)   

for i in range(0, len(x)):
               if (label[i].split("_")[0] in listWords6):
                              ax.text(x[i], y[i], label[i], color='magenta', fontsize=14)                                                               
              
for i in range(0, len(x)):
               if (label[i].split("_")[0] not in listWords and np.random.rand() < 0.01):
                              ax.text(x[i], y[i], label[i].split("_")[0], alpha=0.8, color='black', fontsize=14)
 
 
ax.set_xticks([])
ax.set_yticks([])
 
pl.tight_layout()
 
pl.savefig("p1.png")
pl.show()
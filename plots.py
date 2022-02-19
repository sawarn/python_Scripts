# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:25:21 2020

@author: Rashi
"""
import matplotlib.pyplot as plt

x = [5,10,15,20,25]

y1 = [80.36,79.85,78.25,77.36,76.21,]


plt.plot(x, y1, ls = "-", label='ATWCA',color='blue')

y2 = [81.36,
80.58,
79.63,
78.36,
77.12,
]


plt.plot(x, y2,'g+', ls="--", label="ITRMR")


y3 = [88.36,
87.39,
86.14,
85.12,
84.36,
]

plt.plot(x, y3, 'c*', ls = ":", label="HMAIA")

y4 = [85.69,
84.95,
83.87,
82.12,
81.12,
]

plt.plot(x, y4, 'rx', ls = "-.", label="Image Tagging using Naïve Bayes and Ontologies")


y5 = [90.01,
89.02,
88.43,
87.42,
86.36,
]

plt.plot(x, y5, 'm^', ls = "-.", label="Image Tagging using fuzzy c-means clustering and CNN")

y6=[99.78,
98.69,
97.46,
96.32,
95.47,
]

plt.plot(x,y6 ,'bo',ls='-',label="Proposed MASSTagger")


plt.xlabel('Number of recommendations')
plt.ylabel('Recall')

plt.title('MASSTagger: Metadata Aware Semantic Strategy for Automatic Image Tagging')

plt.legend(loc="best", prop={'size': 5})

plt.show()
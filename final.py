# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:39:27 2020

@author: asuss
"""
import os
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
#پایگاه های داده وارد برنامه می گردد.

df = pd.read_csv('final.csv')
goods = pd.read_csv("goods.csv")
#ورودی ها و خروجی ها مشخص می گردند.
x = np.array(df.drop(['SP','ID'],1))
y = np.array(df['SP']) 
xn = np.array(goods.drop(['SP','ID'],1))
yn = np.array(goods['SP']) 
#مدل درخت تصمیم و k نزدیکترین همسایه اموزش داده می شود.
tree = DecisionTreeClassifier(random_state=0 , criterion="gini", ccp_alpha=0.0162 )
neigh = NearestNeighbors(n_neighbors=3)
tree.fit(x , y)
neigh.fit(xn, yn)
NearestNeighbors(n_neighbors=3)
#مقدار X1 را کاربر وارد می نماید.
x1=[[6,7,4,3,1,9,0,3,3]]
predict_tree = tree.predict(x1)
print(predict_tree)
print("")
if predict_tree<3.5:
    m = neigh.kneighbors(x1)  
    n = m[1]
    for i in n:
       print(xn[i])
       print('\r\n')

    
    
    

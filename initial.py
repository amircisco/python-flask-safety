import webbrowser
import os,time
from flask import Flask
from flask import render_template,request
from data import arr_arr
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)
@app.route('/')
def first():
    return render_template('first.html')


@app.route('/index')
def index():
    return render_template('index.html',len = len(arr_arr), arr = arr_arr)

@app.route('/handle_data',methods=['POST'])
def handle_data():
    arr_vall = []
    for i in range(0,len(arr_arr)):
        index = 'r'+str(i)        
        if index in request.form:
            arr_vall.append(int(request.form[index])) 
            
    x_0 = average([arr_vall[5] , arr_vall[6] , arr_vall[7] , arr_vall[8]]) * div(arr_vall)
    x_1 = average([arr_vall[0] , arr_vall[1] , arr_vall[2] , arr_vall[3] , arr_vall[4]]) * div(arr_vall)
    x_2 = average([arr_vall[0] , arr_vall[7] , arr_vall[9]]) * div(arr_vall)  
    x_3 = average([arr_vall[10] , arr_vall[11] , arr_vall[14] , arr_vall[15]]) * div(arr_vall)
    x_4 = average([arr_vall[16] , arr_vall[17], arr_vall[18] ]) * div(arr_vall)
    x_5 = average([arr_vall[19] , arr_vall[20] , arr_vall[21] ] ) * div(arr_vall)
    x_6 = 0
    if(arr_vall[22] == 9):
        x_6 = 1
    elif (arr_vall == 1):
        x_6 = 0     
    x_7 = average([ arr_vall[10] , arr_vall[11] , arr_vall[12] , arr_vall[13] ]) * div(arr_vall)
    x_8 = average([ arr_vall[4] , arr_vall[7] , arr_vall[15] , arr_vall[22] ]) * div(arr_vall)

    lst = [[x_0,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8]]    
    #lst = [[6,7,4,3,1,9,0,3,3]]
    result1,result2 = proc(lst)        
    res = ''
    color = ''
    result1 = result1[0]
    if result1 == 1 :
        res = "Very Low"    
        color = "red"
    elif result1 == 2 :
        res = "Low" 
        color = "orange"   
    elif result1 == 3 :
        res = "Medium"
        color = "gray"
    elif result1 == 4 :
        res = "High"
        color = "blue"
    elif result1 == 5 :
        res = "Very High"
        color = "green"

    k1 = []
    k2 = []
    k3 = []
    str_len = 0
    if result2 is None:
        k1.append('')
        k2.append('')
        k3.append('')
    else:
        k1.append(result2[0])  
        k2.append(result2[1])
        k3.append(result2[2]) 
        str_len = 9        
                 
    return render_template('results.html', itself = lst[0],lenitself = 9 , k1 = k1[0], k2 = k2[0], k3 = k3[0] ,len = str_len , res = res , color = color,result1 = result1)   
   

def average(lst):
    return sum(lst) / len(lst)    

def div(arr_vall):
    return arr_vall[9] / arr_vall[8]

def proc(x1):
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
    predict_tree = tree.predict(x1)
    #print(predict_tree)

    if predict_tree<3.5:
        arr_tmp = [] 
        m = neigh.kneighbors(x1)  
        n = m[1]
        for i in n:
            arr_tmp.append(xn[i])    
        return predict_tree,arr_tmp[0]
    else:
        return predict_tree,None       


def browser():
    url = 'http://localhost:5000'
    chrome_path = os.path.abspath('Chrome//GoogleChromePortable.exe') 
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)
    
    
   
def run_server():
    app.run(debug=True)

if __name__=="__main__" : 
    #browser()
    run_server()       
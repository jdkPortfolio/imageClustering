from flask import Flask, render_template, request
from pandas import array, read_pickle
import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

@app.route('/')
def hello_world():
##    data = read_pickle(os.path.join(basedir+'/classifier.pkl'))
    return render_template('choose.html')

@app.route('/groupMembers')
def viewMembers():
##    data = read_pickle(os.path.join(basedir+'/classifier.pkl'))
    return render_template('index.html')


@app.route('/cluster')
def clusterView():
    page_id = request.args.get("id")
    if page_id:
        clusterData = handleImages(page_id)
        # print(clusterData[0][0], clusterData[1][0])
        return render_template('choose.html', data=clusterData, id=page_id, count=0)
    else:
        return render_template('choose.html')
    
def handleImages(cluster):
    path = r"/static/evaluation/"+str(cluster)
    p = os.path.join(basedir+path)

    products = []
    with os.scandir(p) as files:
        for file in files:
            if file.name.endswith('png') or file.name.endswith('jpg'):
                products.append(file.name)

    return products

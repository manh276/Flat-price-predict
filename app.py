from flask import Flask, render_template, request,redirect,url_for
import pickle
import numpy as np
import os
import joblib

xgb = pickle.load(open('xgb.pkl', 'rb'))
lr = pickle.load(open('lr.pkl', 'rb'))
#rf = pickle.load(open('rf.pkl', 'rb'))
SGD = pickle.load(open('SGD.pkl', 'rb'))
TEMPLATE_DIR = os.path.abspath('D:/Flask_Regressor/templates')
STATIC_DIR = os.path.abspath('D:/Flask_Regressor/static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
@app.route('/')
def ma():
    return redirect(url_for('man'))
@app.route('/home')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])

def home():
    Flat_type = request.form['Flat_type']
    Storey_range = request.form['Storey_range']
    Floor_area_sqm  = request.form['Floor_area_sqm']
    Lease_commence_date = request.form['Lease_commence_date']
    Latitude = request.form['Latitude']
    Longitude = request.form['Longitude']
    Cluster = request.form['Cluster']
    arr = np.array([[Flat_type, Storey_range, Floor_area_sqm,Lease_commence_date,Latitude,Longitude,Cluster]])
    model = request.form['model']

    
    if model == 'lr':
        pred = lr.predict(np.float32(arr))
    if model == 'xgb':
        pred = xgb.predict(np.float32(arr))
    elif model == 'sgd':
        pred = SGD.predict(np.float32(arr))
    elif model == 'rf':
        pred = rf.predict(np.float32(arr))
    else:
        pred = None
    return render_template('after.html', pred=pred[0])

if __name__ == "__main__":
    app.run(debug=True)

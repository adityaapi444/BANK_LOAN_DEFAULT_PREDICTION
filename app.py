
from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
# load the built-in model 


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getdelay', methods=['POST','GET'])
def get_delay():
    result=request.form
    member_id_input=result['member_id_input']
    print(type(member_id_input))
    member_id_input=int(member_id_input)
    print(type(member_id_input))
    fT=pd.read_csv(r'C:\Users\adity\Example1\example\venv\finalTest_csv_26.csv')
    user_new_input = fT[(fT['member_id'] == member_id_input)]
    
    del user_new_input['member_id']
    log_model = joblib.load('RF_BLDP_26.pkl')
    prediction=log_model.predict(user_new_input)
    if prediction ==1:
        return render_template('result.html')
    if prediction ==0:
        return render_template('result2.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

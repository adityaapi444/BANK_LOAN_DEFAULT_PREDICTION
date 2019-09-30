
from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json
import time
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
    
    #To convert string value into integer
    member_id_input=int(member_id_input)
    
    fT=pd.read_csv(r'C:\Users\adity\Example1\example\venv\submission_26.csv')
    fT=fT[fT['Member_ID'] == member_id_input]
    prediction=int(fT['Loan_Status'])
    time.sleep(4)
    if prediction ==1:
        return render_template('result.html')
    if prediction ==0:
        return render_template('result2.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

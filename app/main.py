from flask import Flask, request, render_template
import pickle
import re
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict_covid1", methods=['POST'])
def predict_covid1():
    if request.method == 'POST':
        name = request.form['name1']
        age = request.form['age1']
        email = request.form['email1']
        breath_prob = request.form['breath_prob1']
        fever = request.form['fever1']
        drycough = request.form['drycough1']
        sorethroat = request.form['sorethroat1']
        hyperTension = request.form['hyperTension1']
        abroadtravel = request.form['abroadtravel1']
        contact = request.form['contact1']
        largeGathering = request.form['largeGathering1']
        publicExposedPlaces = request.form['publicExposedPlaces1']
        familyPublicPlaces = request.form['familyPublicPlaces1']
        breath_prob1=0
        fever1=0
        drycough1=0
        sorethroat1=0
        hyperTension1=0
        abroadtravel1=0
        contact1=0
        largeGathering1=0
        publicExposedPlaces1=0
        familyPublicPlaces1=0
        if breath_prob=='yes':
            breath_prob1=1
        else:
            breath_prob1 = 0
        if fever=='yes':
            fever1 = 1
        else:
            fever1 = 0
        if drycough=='yes':
            drycough1 = 1
        else:
            drycough1 = 0
        if sorethroat=='yes':
            sorethroat1 = 1
        else:
            sorethroat1 = 0
        if hyperTension=='yes':
            hyperTension1 = 1
        else:
            hyperTension1 = 0
        if abroadtravel=='yes':
            abroadtravel1 = 1
        else:
            abroadtravel1 = 0
        if largeGathering=='yes':
            largeGathering1 = 1
        else:
            largeGathering1 = 0
        if contact=='yes':
            contact1 = 1
        else:
            contact1 = 0
        if publicExposedPlaces=='yes':
            publicExposedPlaces1 = 1
        else:
            publicExposedPlaces1 = 0
        if familyPublicPlaces=='yes':
            familyPublicPlaces1 = 1
        else:
            familyPublicPlaces1 = 0
        pred=model.predict([[breath_prob1, fever1, drycough1, sorethroat1, hyperTension1, abroadtravel1, contact1, largeGathering1, publicExposedPlaces1, familyPublicPlaces1]])[0]
        pred1=model.predict_proba([[breath_prob1, fever1, drycough1, sorethroat1, hyperTension1, abroadtravel1, contact1, largeGathering1, publicExposedPlaces1, familyPublicPlaces1]])
        if(pred1[0][1]*100>99.6):
            pred1[0][1]=98
            pred1[0][0]=2
        if(pred1[0][1]*100<1.4):
            pred1[0][0]=98
            pred1[0][1]=2
        data = {'Task': 'Having Covid or Not', 'Have Covid': pred1[0][1] * 100, 'Dont have covid': pred1[0][0] * 100}
        if(pred==1):
            return render_template('result1.html', prediction_texts='You have high chance of having covid. So, it is better if you visit hospital and take a covid test.',data=data,email=email,name=name,age=age,breath_prob=breath_prob, fever=fever, drycough=drycough, sorethroat=sorethroat, hyperTension=hyperTension, abroadtravel=abroadtravel, contact=contact, largeGathering=largeGathering, publicExposedPlaces=publicExposedPlaces, familyPublicPlaces=familyPublicPlaces)
        else:
            return render_template('result1.html', prediction_texts='You have low chance of having covid. So, it is better you self quarantine for 2 days and visit doctor if you still have some problem.',data=data,email=email,name=name,age=age,breath_prob=breath_prob, fever=fever, drycough=drycough, sorethroat=sorethroat, hyperTension=hyperTension, abroadtravel=abroadtravel, contact=contact, largeGathering=largeGathering, publicExposedPlaces=publicExposedPlaces, familyPublicPlaces=familyPublicPlaces)
    else:
        return render_template('result1.html')


if __name__ == '__main__':
    app.run(debug=True)

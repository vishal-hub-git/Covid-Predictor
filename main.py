from flask import Flask, request, render_template
import pickle
import re
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('covid_pred.html')


@app.route("/predict_covid1", methods=['POST'])
def predict_covid1():
    if request.method == 'POST':
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
        if re.match(r'yes', breath_prob.lower()) != None:
            breath_prob1=1
        else:
            breath_prob1 = 0
        if re.match(r'yes', fever.lower()) != None:
            fever1 = 1
        else:
            fever1 = 0
        if re.match(r'yes', drycough.lower()) != None:
            drycough1 = 1
        else:
            drycough1 = 0
        if re.match(r'yes', sorethroat.lower()) != None:
            sorethroat1 = 1
        else:
            sorethroat1 = 0
        if re.match(r'yes', hyperTension.lower()) != None:
            hyperTension1 = 1
        else:
            hyperTension1 = 0
        if re.match(r'yes', abroadtravel.lower()) != None:
            abroadtravel1 = 1
        else:
            abroadtravel1 = 0
        if re.match(r'yes', largeGathering.lower()) != None:
            largeGathering1 = 1
        else:
            largeGathering1 = 0
        if re.match(r'yes', contact.lower()) != None:
            contact1 = 1
        else:
            contact1 = 0
        if re.match(r'yes', publicExposedPlaces.lower()) != None:
            publicExposedPlaces1 = 1
        else:
            publicExposedPlaces1 = 0
        if re.match(r'yes', familyPublicPlaces.lower()) != None:
            familyPublicPlaces1 = 1
        else:
            familyPublicPlaces1 = 0
        pred=model.predict([[breath_prob1, fever1, drycough1, sorethroat1, hyperTension1, abroadtravel1, contact1, largeGathering1, publicExposedPlaces1, familyPublicPlaces1]])[0]
        print(pred)
        if(pred==1):
            return render_template('covid_pred.html', prediction_texts='You have high chance of having covid. So, it is better if you visit hospital and take a covid test.')
        else:
            return render_template('covid_pred.html', prediction_texts='You have low chance of having covid. So, it is better you self quarantine for 2 days and visit doctor if you still have some problem.')
    else:
        return render_template('covid_pred.html')


if __name__ == '__main__':
    app.run(debug=True)

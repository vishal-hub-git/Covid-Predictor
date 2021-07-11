from flask import Flask,request,jsonify
import loc


app = Flask(__name__)


@app.route('/predict_covid1', methods=['POST', 'GET'])
def predict_covid1():
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
    pred=loc.covid_prediction(breath_prob, fever, drycough, sorethroat, hyperTension, abroadtravel, contact, largeGathering,publicExposedPlaces, familyPublicPlaces)
    print(pred)
    if(pred==str(1)):
        resp = jsonify({'prediction': 'You have high chance of having covid. So, it is better if you visit hospital and take a covid test.'})
    else:
        resp = jsonify({'prediction': 'You have low chance of having covid. So, it is better you self quarantine for 2 days and visit doctor if you still have some problem.'})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


if __name__ == '__main__':
    loc.load_saved_artifacts()
    app.run()

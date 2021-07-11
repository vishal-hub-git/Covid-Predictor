import json
import pickle
import re
import numpy as np
__model = None


def covid_prediction(breath_prob, fever, drycough, sorethroat, hyperTension, abroadtravel, contact, largeGathering, publicExposedPlaces, familyPublicPlaces):
    X=np.zeros(10)
    if re.match(r'yes', breath_prob.lower()) != None:
        X[0] = 1
    else:
        X[0] = 0
    if re.match(r'yes', fever.lower()) != None:
        X[1] = 1
    else:
        X[1] = 0
    if re.match(r'yes', drycough.lower()) != None:
        X[2] = 1
    else:
        X[2] = 0
    if re.match(r'yes', sorethroat.lower()) != None:
        X[3] = 1
    else:
        X[3] = 0
    if re.match(r'yes', hyperTension.lower()) != None:
        X[4] = 1
    else:
        X[4] = 0
    if re.match(r'yes', abroadtravel.lower()) != None:
        X[5] = 1
    else:
        X[5] = 0
    if re.match(r'yes', largeGathering.lower()) != None:
        X[7] = 1
    else:
        X[7] = 0
    if re.match(r'yes', contact.lower()) != None:
        X[6] = 1
    else:
        X[6] = 0
    if re.match(r'yes', publicExposedPlaces.lower()) != None:
        X[8] = 1
    else:
        X[8] = 0
    if re.match(r'yes', familyPublicPlaces.lower()) != None:
        X[9] = 1
    else:
        X[9] = 0
    return str(__model.predict([X])[0])


def load_saved_artifacts():
    global __model
    with open("model.pkl", 'rb') as f:
        __model = pickle.load(f)


if __name__ == '__main__':
    load_saved_artifacts()
    print(covid_prediction('Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes','Yes'))
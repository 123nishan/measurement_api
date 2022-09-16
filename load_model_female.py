from pickle import load
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from constant import *
import torch
from model import Model
from sklearn import preprocessing
import json
def run_model(age, height, weight, shoe_size,hourglass,inverted_triangle,rectangle,triangle):
    """
    This function is for female prediction, this load the checkpoint which than is used to predict body measurement.
    Refer to constant.py file for variables and list 
    
    parametere
    -------------
    age : float
        Age of the person
    height: Float
        Height of the person in cm
    weight: Float
        Weight of the person in kg
    shoe_size : Float
        European Shoe size of the person  
    hourglass: float 
        if hourglass body shape value will be 1 if not 0
    inverted_traingle: float
        if inverted triangle body shape value will be 1 if not 0
    rectangle: float
        if rectangle body shape value will be 1 if not 0
    triangle: Float
        if triangle body shape value will be 1 if not 0

    Return
    -------------
    Json object
        This includes all body measurement predicted from the checkpoint.
        sample {"Waist circumference (cm)": 32, "Chest circumference (cm)": 45,.....}
        

    """
    # model = torch.load("./male/model.pt")
    # print(model)

    features = torch.tensor([[age, height, weight, shoe_size,hourglass,inverted_triangle,rectangle,triangle]])
    scaler=load(open('./female/scaler.pkl','rb')) #input scaler
    scaled_data=scaler.transform(features)
    scaled_data=torch.from_numpy(scaled_data)

    model = Model(input_size=len(female_input_list),output_size= len(female_output_list),hidden_size=10,nlayers=3)
    # print(model)
    model.load_state_dict(torch.load("./female/checkpoint.pt", map_location=torch.device('cpu')))
    model.eval()

    output=model(scaled_data.float())
    output_scaler=load(open('./female/output_scaler.pkl','rb')) # loading saved output scaler 
    unscaled_output=output_scaler.inverse_transform(output.detach().numpy()) #unscale predicted measurement 


    outerInseam = np.subtract(unscaled_output[:, 7], unscaled_output[:, 10]) #substracts waist height and ankle height
    innerInseam = np.subtract(unscaled_output[:, 4], unscaled_output[:, 11]) #substracts crotch height and inner ankle height
    unscaled_output = unscaled_output.flatten() #convert 2d array to 1d
    return_dict={}
    for i  in range(len(female_output_list)): #adding to dictonary 
        feature_name=female_output_list[i].replace("(mm)","(cm)")
        return_dict[feature_name]=unscaled_output[i]/10

    return_dict[outer_inseam+" (cm)"]=outerInseam[0]/10
    return_dict[inner_inseam+" (cm)"]=innerInseam[0]/10

    json_object=json.dumps(return_dict)
    return json_object


# run_model(40.2,175.0,86.0,44.0,0,0,1,0)
# 40.2,175.0,86.0,43.0,Rectangle,1.1217481789802288,0.0,1.0,0.0
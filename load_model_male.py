from pickle import load
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from constant import *
import torch
from model import Model
from sklearn import preprocessing
import json
def run_model(age,height,weight,shoe_size,inverted_triangle,rectangle,triangle):
    
    """
        This function is for male prediction, this load the checkpoint which than is used to predict body measurement.
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

    features = torch.tensor([[age,height,weight,shoe_size,inverted_triangle,rectangle,triangle]])
    scaler=load(open('./male/scaler.pkl','rb')) #Loads scaler saved for features
    scaled_data=scaler.transform(features)
    scaled_data=torch.from_numpy(scaled_data)

    model = Model(input_size=len(male_inputs_list),output_size= len(male_output_list),hidden_size=5,nlayers=3) #initilize the model
    # print(model)
    model.load_state_dict(torch.load("./male/checkpoint.pt", map_location=torch.device('cpu')))
    model.eval()

    output=model(scaled_data.float())
    output_scaler=load(open('./male/output_scaler.pkl','rb')) #loads scaler for output of the model
    unscaled_output=output_scaler.inverse_transform(output.detach().numpy())


    outerInseam = np.subtract(unscaled_output[:, 7], unscaled_output[:, 10]) #substract waist height and ankle height to calc outer inseam
    innerInseam = np.subtract(unscaled_output[:, 4], unscaled_output[:, 11])#susbtract crotch height and inner ankle height to calc inner inseam
    unscaled_output = unscaled_output.flatten()
    return_dict={}
    for i  in range(len(male_output_list)):

        feature_name=male_output_list[i].replace("(mm)","(cm)")
        return_dict[feature_name]=unscaled_output[i]/10
    return_dict[outer_inseam+" (cm)"]=outerInseam[0]/10
    return_dict[inner_inseam+" (cm)"]=innerInseam[0]/10
    json_object=json.dumps(return_dict)
    return json_object


# run_model(40.2,175.0,86.0,44.0,0,1,0)
# 40.2,175.0,86.0,43.0,Rectangle,1.1217481789802288,0.0,1.0,0.0
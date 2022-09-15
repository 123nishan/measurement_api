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
    print("HELLO")
    # model = torch.load("./male/model.pt")
    # print(model)

    features = torch.tensor([[age, height, weight, shoe_size,hourglass,inverted_triangle,rectangle,triangle]])
    scaler=load(open('./female/scaler.pkl','rb'))
    scaled_data=scaler.transform(features)
    scaled_data=torch.from_numpy(scaled_data)

    model = Model(input_size=len(female_input_list),output_size= len(female_output_list),hidden_size=10,nlayers=3)
    # print(model)
    model.load_state_dict(torch.load("./female/checkpoint.pt", map_location=torch.device('cpu')))
    model.eval()

    output=model(scaled_data.float())
    output_scaler=load(open('./female/output_scaler.pkl','rb'))
    unscaled_output=output_scaler.inverse_transform(output.detach().numpy())


    outerInseam = np.subtract(unscaled_output[:, 7], unscaled_output[:, 10])
    innerInseam = np.subtract(unscaled_output[:, 4], unscaled_output[:, 11])
    unscaled_output = unscaled_output.flatten()
    return_dict={}
    for i  in range(len(female_output_list)):
        feature_name=female_output_list[i].replace("(mm)","(inch)")

        return_dict[feature_name]=unscaled_output[i]/25.4
    return_dict[outer_inseam+" (inch)"]=outerInseam[0]/25.4
    return_dict[inner_inseam+" (inch)"]=innerInseam[0]/25.4

    json_object=json.dumps(return_dict)
    return json_object


run_model(40.2,175.0,86.0,44.0,0,0,1,0)
# 40.2,175.0,86.0,43.0,Rectangle,1.1217481789802288,0.0,1.0,0.0
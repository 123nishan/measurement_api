from flask import Flask,request
from load_model_male import run_model
from load_model_female import run_model as run_female_model
from constant import *
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello"

# # @app.route('/male_measurement/<age>/<height>/<weight>/<shoes_size>/<inverted_traingle>/<rectangle>/<traingle>')
# def male_measurement(age,height,weight,shoes_size,inverted_traingle,rectangle,triangle):
#     return run_model(age,height,weight,shoes_size,inverted_traingle,rectangle,triangle)

# # @app.route('/male_measurement/<age>/<height>/<weight>/<shoes_size>/<inverted_traingle>/<rectangle>/<traingle>')
@app.route('/male_measurement',methods=['GET'])
def male_measurement():
    request_data=request.get_json()

    # return("WORKING")
    return run_model(
        age=request_data[age],
        height=request_data[height],
        weight=request_data[weight],
        shoe_size=request_data[shoe_size],
        inverted_triangle=request_data[inverted_triangle],
        rectangle=request_data[rectangle],
        triangle=request_data[triangle]

    )

@app.route('/female_measurement',methods=['GET'])
def female_measurement():
    request_data=request.get_json()

    # return("WORKING")
    return run_female_model(
        age=request_data[age],
        height=request_data[height],
        weight=request_data[weight],
        shoe_size=request_data[shoe_size],
        hourglass=request_data[hourglass],
        inverted_triangle=request_data[inverted_triangle],
        rectangle=request_data[rectangle],
        triangle=request_data[triangle]

    )
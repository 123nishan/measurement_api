# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from re import A
from load_model_male import run_model
from load_model_female import run_model as run_female_model

import sys


if __name__ == '__main__':
    gender=str(sys.argv[1]).lower()
    age=float(sys.argv[2])
    height=float(sys.argv[3])
    weight=float(sys.argv[4])
    shoe_size=float(sys.argv[5])
    if str(gender).lower()=="m":
        inverted_triangle=float(sys.argv[6])
        rectangle=float(sys.argv[7])
        triangle=float(sys.argv[8])
      

        json_object=run_model(
            age=age,
            height=height,
            weight=weight,
            shoe_size=shoe_size,
            inverted_triangle=inverted_triangle,
            rectangle=rectangle,
            triangle=triangle
        )     
        
    elif str(gender).lower()=="f":
        hourglass=float(sys.argv[6])
        inverted_triangle=float(sys.argv[7])
        rectangle=float(sys.argv[8])
        triangle=float(sys.argv[9])
      

        json_object=run_female_model(
            age=age,
            height=height,
            weight=weight,
            shoe_size=shoe_size,
            hourglass=hourglass,
            inverted_triangle=inverted_triangle,
            rectangle=rectangle,
            triangle=triangle
            )
    print(json_object)
        
    


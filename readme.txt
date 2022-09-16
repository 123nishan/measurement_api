Before you begin you might have to run following command:
    -python3 -m venv venv
        - this will create virutal env
    -source venv/bin/activate
        -activate the created virutal env
    -pip install -r requirements.txt
        - install necessary packages which is defined inside requirements.txt
Other note
    - All constant used in the prediction function are inside constant.py file.
    - The number of layers and number of neuron has been set after tuning the parameter while training and validation.

------Files description-------------
    -constant.py: Contains all constant
    -load_model_female.py: contains function that load checkpoint for female and which returns the predicted measurement
    -load_model_male.py: contains function that load checkpoint for male and which returns the predicted measurement
    -main.py: Main py file to run all command, it takes arguments to run
    -model.py: Neural network design class
    -female folder: Contains 3 file: 
        -checkpoint.pt: saved checkpoint for female
        -output_scaler.pkl: saved scaler function for output for female data.
        -scaler.pkl: saved scaler function for input for female data.
    -male folder: Contains 3 file: 
        -checkpoint.pt: saved checkpoint for male
        -output_scaler.pkl: saved scaler function for output for male data.
        -scaler.pkl: saved scaler function for input for femmaleale data.

-------------------For male run--------------------------
    -python main.py "gender" "age" "height in cm" "weight in kg" "european shoe size " "Inverted shape" "Rectangle shape" "Triangle Shape"
    -Sample command to run:  python main.py m 23 173 70 43 0 1 0
    -Note: 
        -Order of the argument in command must be same as line number 28
        - Enter m as gender parameter
        -all value must be in number. for body shape only one of the body shape should be 1, the one which you want to choose,
            and other should be 0.
        
        -The function returns json object, explanation of code can be found inside load_model_male.py file

        -----------sample return of male prediction-----------
            {
                "Waist Circumference, Pref (inch)": 33.10738390824926,
                "Chest Circumference (inch)": 37.34289935254675,
                "Neck Base Circumference (inch)": 18.51965956800566,
                "Hip Circumference, Maximum (inch)": 38.50753904327633,
                "Crotch Height (inch)": 31.121662770669293,
                "Thigh Circumference (inch)": 22.17965433916708,
                "Shoulder Breadth (inch)": 18.024183859036665,
                "Waist Height, Preferred (inch)": 39.834390475055365,
                "Arm Length (Shoulder to Wrist) (inch)": 24.47324737789124,
                "Chest Girth (Chest Circumference at Scye) (inch)": 38.12271478607899,
                "Ankle Ht Rt (Malleolus, Lateral) (inch)": 2.710941945473979,
                "Malleolus Med Rt (inch)": 3.2668406569112944,
                "Outer Inseam (inch)": 37.12344913032111,
                "Inner Inseam (inch)": 27.854820912278544
            }

--------------------For female run---------------------------
   -python main.py "gender" "age" "height in cm" "weight in kg" "european shoe size " "Hourglass shape" "Inverted shape" "Rectangle shape" "Triangle Shape"
   -Sample command to run:  python main.py m 23 173 70 43 0 0 1 0
   -Note:
        - Enter f as gender parameter
        -all value must be in number. for body shape only one of the body shape should be 1, the one which you want to choose,
            and other should be 0.
        Order of the argument in command must be same as line number 58
        --The function returns json object, explanation of code can be found inside load_model_female.py file

        -----------sample return of female prediction---------
                {
                    "Waist Circumference, Pref (inch)": 32.028938353531004,
                    "Chest Circumference (inch)": 38.10968834584154,
                    "Bust/Chest Circumference Under Bust (inch)": 32.24188136303519,
                    "Neck Base Circumference (inch)": 17.455969382458786,
                    "Hip Circumference, Maximum (inch)": 40.284008116234006,
                    "Crotch Height (inch)": 32.794886311208174,
                    "Thigh Circumference (inch)": 22.99527145746186,
                    "Shoulder Breadth (inch)": 16.834356353038878,
                    "Waist Height, Preferred (inch)": 42.44539996770423,
                    "Arm Length (Shoulder to Wrist) (inch)": 24.07539668045645,
                    "Chest Girth (Chest Circumference at Scye) (inch)": 36.57728780911663,
                    "Ankle Ht Rt (Malleolus, Lateral) (inch)": 2.7039721631628324,
                    "Malleolus Med Rt (inch)": 3.2855092446635092,
                    "Outer Inseam (inch)": -19.742931456077756,
                    "Inner Inseam (inch)": 37.58003535233145
                }






from flask import Flask, request, render_template
from flask_cors import cross_origin
import numpy as np
import joblib
import pickle
import pandas as pd
import logging
from multiprocessing import Process

app = Flask(__name__)

model = pickle.load(open('optimizedmodel.pkl', "rb"))
logging.info('Pickle Model Loaded')

@app.route("/")
@cross_origin()
def home():
    """
    :DESC: This is homepage Api.
    """
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    """
    :DESC: This is predict Api. It Requests inputs from user and
    predicts the approximate flight price.
    :return: Render flight.html Template
    """
    if request.method == "POST":
        logging.info('Requested Method: POST')

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        logging.info('Converted Departure Date time to Journey Day and Month')
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        logging.info('Converted Departure Date time to Departure Hour and Minutes')
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        logging.info('Converted Arrival Date time to Arrival Hour and Minutes')
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        airline=request.form['airline']
        if(airline=='Air Asia'):
            Air_Asia = 1
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0 

        elif(airline=='Jet Airways'):
            Air_Asia = 0
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif (airline=='IndiGo'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif (airline=='Air India'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0 
            
        elif (airline=='Multiple carriers'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            
        elif (airline=='SpiceJet'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0 
            
        elif (airline=='Vistara'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0

        elif (airline=='GoAir'):
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1

        else:
            Air_Asia = 0
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        
        Source = request.form["Source"]
        
        if (Source == 'Banglore'):
            s_Banglore = 1
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Delhi'):
            s_Banglore = 0
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Banglore = 0
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Banglore = 0
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Banglore = 0
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Banglore = 0
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # print(s_Banglore,
        #     s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Banglore'):
            d_Banglore = 1
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        if (Destination == 'Cochin'):
            d_Banglore = 0
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Destination == 'Delhi'):
            d_Banglore = 0
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'New_Delhi'):
            d_Banglore = 0
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            d_Banglore = 0
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Destination == 'Kolkata'):
            d_Banglore = 0
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Banglore = 0
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        # print(
        #     d_Banglore,
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        
        X=[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_min,
            Dep_hour,
            Arrival_min,
            Arrival_hour,
            dur_hour,
            dur_min,
            Air_Asia,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            s_Banglore,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Banglore,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]

        X_scaled=scaler.transform([X])

        logging.info('Standard Scaling All the Input values')

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        if (Source==Destination):
            logging.warning('Source and Destination are same')
            return render_template('home.html',prediction_text="Your Flight price is Rs. 0")

        elif (date_dep==date_arr):
            logging.warning('date time of departure and date time of arrival are same')
            return render_template('home.html',prediction_text="Your Flight price is Rs. 0")

        else:
            prediction=model.predict(X_scaled)
            logging.info('Successful Prediction')
            output=np.round(prediction[0])
            minfare= output - 500
            maxfare= output + 500
            logging.info('Output Displayed')


        return render_template('home.html',prediction_text="Your Flight price is between Rs. {} to Rs. {}".format(minfare,maxfare))
    
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)
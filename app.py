# -*- coding: utf-8 -*-
"""
Created on Wed Aug 06 02:20:31 2020
@author: Venkata N Divi
"""
import sys,streamlit as st,pickle

def predictPrice(depDate_,depTime_,arrTime_,depart_,goingTo_,stops_,airline_,randomForest_):
    try:
        departDict = {'Chennai':[1,0,0,0],'New Delhi':[0,1,0,0],'Kolkata':[0,0,1,0],'Mumbai':[0,0,0,1]}
        goingDict = {'Cochin':[1,0,0,0],'New Delhi':[0,1,0,0],'Hyderabad':[0,0,1,0],'Kolkata':[0,0,0,1]}
        airlineDict = {'Air India':[1,0,0,0,0,0,0,0,0,0,0],'GoAir':[0,1,0,0,0,0,0,0,0,0,0],'IndiGo':[0,0,1,0,0,0,0,0,0,0,0],
                       'Jet Airways':[0,0,0,1,0,0,0,0,0,0,0],'Jet Airways Business':[0,0,0,0,1,0,0,0,0,0,0],
                       'Multiple carriers':[0,0,0,0,0,1,0,0,0,0,0],'Multiple carriers Premium economy':[0,0,0,0,0,0,1,0,0,0,0],
                       'SpiceJet':[0,0,0,0,0,0,0,1,0,0,0],'Trujet':[0,0,0,0,0,0,0,0,1,0,0],'Vistara':[0,0,0,0,0,0,0,0,0,1,0],
                       'Vistara Premium economy':[0,0,0,0,0,0,0,0,0,0,1]}
        
        depDate_,depTime_,arrTime_ = str(depDate_),str(depTime_),str(arrTime_)
        depYear,depMonth,depDay = int(depDate_.split('-')[0]),int(depDate_.split('-')[1]),int(depDate_.split('-')[2])
        depHour,depMin = int(depTime_.split(':')[0]),int(depTime_.split(':')[1])
        arrHour,arrMin = int(arrTime_.split(':')[0]),int(arrTime_.split(':')[1])
        durHour,durMin = int(arrHour)-int(depHour),int(arrMin)-int(depMin)
        stops_ = 0 if stops_ == 'Non-Stop' else int(stops_)
        
        depChennai,depDelhi,depKolkata,depMumbai = departDict[depart_]
        cochin,delhi,hyd,kolkata = goingDict[goingTo_]
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11 = airlineDict[airline_]
        
        featureValues = [stops_,depYear,depMonth,depDay,depHour,depMin,arrHour,arrMin,durHour,durMin,
                         a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,depChennai,depDelhi,depKolkata,depMumbai,
                         cochin,delhi,hyd,kolkata]
        st.write(featureValues)
        airFarePrice = randomForest_.predict([featureValues])
        st.title("The Flight Price for your Journey Details will be approximately **"+str("{:.2f}".format(airFarePrice[0]))+" INR**")
    except Exception as e:
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno),Exception, e)
        
def selectOptions():
    try:
        mlModel = open('FlightFarerForest.pkl','rb')
        randomForest_ = pickle.load(mlModel)
        depDate_ = st.date_input("Departure Date")
        depTime_ = st.time_input("Departure Time")
        arrTime_ = st.time_input("Arrival Time")
        depart_ = st.selectbox("Depart From",('Select','New Delhi','Mumbai','Kolkata','Chennai'))
        goingTo_ = st.selectbox("Going To",('Select','Cochin','Hyderabad','New Delhi','Kolkata'))
        stops_ = st.selectbox("No. of Stops",('Select','Non-Stop','1','2','3','4'))
        airline_ = st.selectbox("Airline",('Select','Air India','GoAir','IndiGo','Jet Airways','Jet Airways Business','Multiple carriers','Multiple carriers Premium economy','SpiceJet','Trujet','Vistara','Vistara Premium economy'))
        
        if st.button('Get Flight Price'):
            if depart_ == goingTo_:
                st.warning('Source and Destination should not be the same!!!')
            else:
                st.success('Getting the Price For You...')
                predictPrice(depDate_,depTime_,arrTime_,depart_,goingTo_,stops_,airline_,randomForest_)
    except Exception as e:
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno),Exception, e)
        
def main():
    try:
        selectOptions()
    except Exception as e:
        print ('Error on line {}'.format(sys.exc_info()[-1].tb_lineno),Exception, e)
    
if __name__ == '__main__':
    st.write('<!DOCTYPE html><html lang="en">   <head>      <meta charset="UTF-8">      <meta name="viewport" content="width=device-width, initial-scale=1.0">      <meta http-equiv="X-UA-Compatible" content="ie=edge">      <title>Responsive Navigation Bar - W3jar.Com</title>      <style>*,*::before,*::after {  box-sizing: border-box;  -webkit-box-sizing: border-box;}body {  font-family: sans-serif;  margin: 0;  padding: 0;}.container {  height: 80px;  background-color: #052252;  display: -webkit-box;  display: -ms-flexbox;  display: flex;  -ms-flex-wrap: wrap;  flex-wrap: wrap;  -webkit-box-align: center;  -ms-flex-align: center;  align-items: center;  overflow: hidden;}.container .logo {  max-width: 250px;  padding: 0 10px;  overflow: hidden;}.container .logo a {  display: -webkit-box;  display: -ms-flexbox;  display: flex;  -ms-flex-wrap: wrap;  flex-wrap: wrap;  -webkit-box-align: center;  -ms-flex-align: center;  align-items: center;  height: 60px;}.container .logo a img {  max-width: 100%;  max-height: 60px;}@media only screen and (max-width: 650px) {  .container {    -webkit-box-pack: justify;    -ms-flex-pack: justify;    justify-content: space-between;  }  .container .logo {    -webkit-box-flex: 1;    -ms-flex: 1;    flex: 1;  }}.body {  max-width: 700px;  margin: 0 auto;  padding: 10px;} .h1 { color:#FEFEFE; position: center; top: 10px; font-size:135px;font-family:verdana;    margin-top:0px;    margin:0px; line-height:50px; }</style>   </head>   <body>      <div class="container">      <div class="logo">    <a href="#"><img src="https://cdn.iconscout.com/icon/free/png-512/aeroplane-airplane-plane-air-transportation-vehicle-pessanger-people-emoj-symbol-30708.png" alt="logo"></a>    </div> </body></html>', unsafe_allow_html=True)
    st.title("Flight Price Prediction")
    st.markdown("You want to travel from one place to another place and want to know how much cost your flight ticket is? **Try our Service!!!**")
    main()

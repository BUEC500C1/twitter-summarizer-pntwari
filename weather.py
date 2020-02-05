#!/home/ece-student/anaconda3/bin/python
#chmod 755 splitargs
# -*- coding: utf-8 -*-


# Created by: Pat Rick Ntwari
# Homework 1, EC500


# Pulling City 

import requests
import json

def cityCall(city):
  #API KEY
  api_key = "3e69fdf9f225f1150776ca92ff196256" 
  current = "http://api.openweathermap.org/data/2.5/weather?"
  current_url = current + "appid=" + api_key + "&q=" + city
  cresponse = requests.get(current_url).json()
  forecast = "http://api.openweathermap.org/data/2.5/forecast?"
  forecast_url = forecast + "appid=" + api_key + "&q=" + city
  fresponse = requests.get(forecast_url).json()

  if cresponse["cod"] != "404" and fresponse["cod"] != "404": 
    ### Current Temperature
    temp = cresponse['main']["temp"]
    tempF = (temp-273.15)*(9/5)+32
    pres = cresponse['main']["pressure"] 
    wind = cresponse['wind']["speed"] 
    weather = cresponse['weather'][0]["description"]
    
    print("The current temperature is: %.0f deg F" % (tempF))
    print("The current wind speed is: %.0f m/s" %(wind))
    print("Generally ", weather)


    ### Forecast Temperature
    #print(fresponse)
    ftime = fresponse['list'][6]["dt_txt"]
    ftemp = fresponse['list'][6]['main']["temp"]
    ftempF = (ftemp-273.15)*(9/5)+32
    fpres = fresponse['list'][6]['main']["pressure"] 
    fwind = fresponse['list'][6]['wind']["speed"] 
    fweather = fresponse['list'][6]['weather'][0]["description"]

    print("on %s the weather will be:" %(ftime))
    print("The temperature will be: %.0f deg F" % (ftempF))
    print("The wind speed is: %.0f m/s" %(fwind))
    print("Generally %s " %(fweather))
    return "Found"

  else: 
    print("The city does not exist")
    return "Error"

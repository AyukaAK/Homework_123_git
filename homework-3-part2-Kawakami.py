# Ayuka Kawakami
# June 14, 2022
# Homework 3, Part 2

# On Terminal => open the file => python => exec(open('homework-3-part2-Kawakami.py').read())

# Q1. Documentation
#url = https://www.weatherapi.com/docs/
#api key = 976685a7f4594f9c90b191549221406

# Q2. Make a request for the current weather where you are born, or somewhere you've lived.
import requests
response = requests.get("http://api.weatherapi.com/v1/current.json?key=976685a7f4594f9c90b191549221406&q=Reykjavik&aqi=no")
print(response)
data = response.json()
print (data)

# Q3. Print out the country this location is in.
print(data["location"]["country"])

    # Iceland

# Q4. Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

print(data.keys())
print(data["current"])
print(data["current"].keys())

print(data["current"]["feelslike_c"])
print(data["current"]["temp_c"])

if data["current"]["feelslike_c"] > data["current"]["temp_c"]:
    print ("It feels", data["current"]["feelslike_c"], "degrees warmer")
elif data["current"]["feelslike_c"] < data["current"]["temp_c"]:
    print ("It feels", data["current"]["feelslike_c"], "degrees colder")

# Q5. What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
# url = https://www.weatherapi.com/api-explorer.aspx#forecast
# iata:LHR

response_LHR = requests.get("http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=iata:LHR&days=3&aqi=no&alerts=no")
print(response_LHR)
data_LHR = response_LHR.json()

print (data_LHR)
print (data_LHR.keys())
print (data_LHR ["current"])
print (data_LHR ["current"].keys())
print (data_LHR ["current"]['temp_c'])

    # 14c degree

# Q6. What URL would I use to request a 3-day forecast at Heathrow?
#url = http://api.weatherapi.com/v1/forecast.json?key=976685a7f4594f9c90b191549221406&q=iata:LHR&days=3&aqi=no&alerts=no

# Q7. Print the date of each of the 3 days you're getting a forecast for.

print (data_LHR ["forecast"])
print (data_LHR ["forecast"].keys())
print (data_LHR ["forecast"]["forecastday"])

#print each dictionary in the list of dictionary. each dictionary in new line "\n"
for forecast_LHR in data_LHR ["forecast"]["forecastday"]:
    print(forecast_LHR, "\n\n\n")

#explore the data
print (data_LHR ["forecast"]["forecastday"][0].keys())
print (data_LHR ["forecast"]["forecastday"][0]["day"])
print (data_LHR ["forecast"]["forecastday"][0]["day"].keys())

#Forecast Dates
for forecast_date in data_LHR ["forecast"]["forecastday"]:
    print (forecast_date["date"])

#Q8. Print the maximum temperature of each of the days.

# Each forecasted date's max temperature
print (data_LHR ["forecast"]["forecastday"][0]["day"]["maxtemp_c"])

# Each date
print (data_LHR ["forecast"]["forecastday"][0]["date"])

#with for loops
for forecast_LHR in data_LHR ["forecast"]["forecastday"]:
    print ("On", forecast_LHR["date"], "the max temp is", forecast_LHR ["day"]["maxtemp_c"])

#with manual print
print ("On", data_LHR ["forecast"]["forecastday"][0]["date"], "the average temp is", data_LHR ["forecast"]["forecastday"][0]["day"]["maxtemp_c"])
print ("On", data_LHR ["forecast"]["forecastday"][1]["date"], "the average temp is", data_LHR ["forecast"]["forecastday"][1]["day"]["maxtemp_c"])
print ("On", data_LHR ["forecast"]["forecastday"][2]["date"], "the average temp is", data_LHR ["forecast"]["forecastday"][2]["day"]["maxtemp_c"])

#Q9. Print the day with the highest maximum temperature.

#list comprehension for making the list of three days max temp
maxTemp = max( [Temp["day"]["maxtemp_c"] for Temp in data_LHR ["forecast"]["forecastday"]])

for TempTemp in data_LHR ["forecast"]["forecastday"]:
    if TempTemp["day"]["maxtemp_c"] == maxTemp:
        print (TempTemp["date"])










# Ayuka Kawakami
# June 11, 2022
#Homework 2, Part 2

#Lists
countries = ["Greenland", "Tanzania", "USA", "Japan", "Brazil", "Iceland"]

for country in countries:
    print (country)

countries.sort()
print(countries)

print (countries [0])

print (countries [-2])

countries.remove("USA")
print (countries)

print([x.upper() for x in countries])

#Dictionaries
#'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. 

tree = {
    "name" : "Dobera Glabra",
    "Species" : "D. Glabra",
    "age": 100,
    "location_name" : "Nairobi, Kenya",
    "latitude": -1.2928,
    "longitude" : 36.8219,
}
# with f format
print(f'{tree["name"]} is a {tree ["age"]} year old tree that is in {tree["location_name"]}')
# with comma
print (tree["name"], "is a", tree ["age"], "year old tree that is in", tree["location_name"] )

NYC = {
    "latitude": 40.7128,
    "longitude" : -74.0059
}

if tree["latitude"] < NYC ["latitude"]:
    print (tree["name"], "in", tree["location_name"], "is south of NYC")
else:
    print (tree["name"], "in", tree["location_name"], "is north of NYC")

User_Age = int(input ("How old are you?"))

if User_Age > tree ["age"]:
    print ("You are",  User_Age-tree ["age"], "years older than", tree["name"])
elif User_Age < tree ["age"]:
    print ("You are",  tree ["age"]-User_Age, "years younger than", tree["name"])

places = [
    {
        "name" : "Moscow",
        "latitude" : 55.7558,
        "longitude" : 37.6173
    },
    {
        "name" : "Tehran",
        "latitude" : 35.7219,
        "longitude" : 51.3347
    },
    {
        "name" : "Falkland_Islands",
        "latitude" : -51.7963,
        "longitude" : -59.5236
    },
    {
        "name" : "Seoul",
        "latitude" : 37.5665,
        "longitude" : 126.9780
    },
    {
        "name" : "Santiago",
        "latitude" : -33.4489,
        "longitude" : -70.6693
    }
]

for place in places:
    if place ["latitude"] > 0 and place ["name"] != "Falkland_Islands" :
        print (place ["name"], "is above the equator")
    elif place ["latitude"] < 0 and place ["name"] != "Falkland_Islands" :
        print (place ["name"], "is below the equator")
    if place ["name"] == "Falkland_Islands" and place ["latitude"] < 0:
        print (place ["name"], "is below the equator and is a biogeographical part of the mild Antarctic zone" )
    elif place ["name"] == "Falkland_Islands" and place ["latitude"] > 0:
        print (place ["name"], "is above the equator and is a biogeographical part of the mild Antarctic zone" )         

for place in places:
    if place ["latitude"] > tree ["latitude"] :
        print (place ["name"], "is north of", tree ["name"])
    elif place ["latitude"] < tree ["latitude"] :
        print (place ["name"], "is south of", tree ["name"])
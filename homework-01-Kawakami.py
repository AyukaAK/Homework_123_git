# Ayuka Kawakami
# June 7, 2022
# Homework 1

# User's Year of Birth
from datetime import datetime


Birth_Year = int(input ("What's your year of birth?"))
This_Year = datetime.now().year

# Q1. How old the user is 
Age = This_Year - int(Birth_Year)
print (Age)

# Q2. How many times the user's heart has beaten
Heart_Year = 60*24*365
#Heart rate per minute
Heart_PM = 65
#Numbers of beats of a user
Heart_R = Heart_PM * Heart_Year * Age
print (Heart_R)
print(f"Your heart has beaten {Heart_R: ,} times")

# Q3. How many time a blue whale's heart has beaten
#Heart rate of BW per minute
Blue_PM = 11
#Blue what's lifetime beats
Blue_R = Blue_PM * Heart_Year * Age
print (Blue_R)
print(f"Blue Whale's heart has beaten {Blue_R: ,} times")

# Q4. How many time a rabbit's heart has beaten (if stressed)
Rabbit_PM = 300
Rabbit_R = Rabbit_PM * Heart_Year * Age
print (Rabbit_R)
print(f"Rabbit's heart has beaten {Rabbit_R:,} times")

# Q5. If the answer to rabbit heartbeats is more than a million, say "XXX million"
if Rabbit_R > 1000000:
    print (Rabbit_R // 1000000, "million")

# Q6. How old they are in Venus
Venus_Year = 365/225
Venus_HAge = Age * Venus_Year
print(Venus_HAge)

# Q7. How old they are in Neptune
Neptune_Year = 365/165
Neptune_HAge = Age * Neptune_Year
print(Neptune_HAge)

# Q8. Wether they are the same age as you, older, younger?
# Q9. If older or younger, how many years difference
# Compare with the blue whale
My_Age = 36
if Age > My_Age:
    print (Age-My_Age, "older")
elif Age < My_Age:
    print (My_Age-Age, "younger")
elif Age == My_Age:
    print ("Same")

# Q10. If they were born in an even or odd year
if Birth_Year % 2 ==0:
    print ("even")
else: 
    print ("odd")

# Q11. How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
presidents= {
    "Kennedy" : [1961, "D"], 
    "Johnson" : [1963, "D"],
    "Nixon" : [1969, "R"],
    "Ford" : [1974, "R"],
    "Carter" : [1977, "D"],
    "Reagan" : [1981, "R"],
    "Bush" : [1989, "R"],
    "Clinton" : [1993, "D"],
    "Bush" : [2001, "R"],
    "Obama" : [2009, "D"],
    "Trump" : [2017, "R"],
    "Biden" : [2021, "D"],
}
presidents_count = 0
for value in presidents.values():
    if value[0]>Birth_Year: 
        if value[1] == "D":
            presidents_count = presidents_count+1

print(presidents_count)
             
# Q12. Which US President was in office when they were born ?

Years_list = []
for key, value in presidents.items():
    if value[0]<Birth_Year:
        Years_list.append(value[0])

President_year = max(Years_list)

for key, value in presidents.items():
    if value[0] == President_year:
        print(key)






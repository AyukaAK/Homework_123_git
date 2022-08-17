# Ayuka Kawakami
# June 8, 2022
# Homework 2, Part 1

from statistics import mean, median

# List Questions
my_list = [22, 90, 0, -10, 3, 22, 48]

print (my_list)

print (my_list [3])

my_list [1] + my_list [3]

sorted_list = sorted (my_list)
print(sorted_list[-2])

print (my_list[-1])

#listing comprehension
divided_list = [x/2 for x in my_list]
print (divided_list)

print (sum(divided_list))

if median(my_list) > mean(my_list):
    print("median is higher than median")
elif median(my_list) == mean(my_list):
    print("they are the same")
else:
    print("mean is higher than median")

# Dictionaries Questions

movie = {
    "title" : "Frozen II",
    "director" : "Chris Buck",
    "year" : 2019
}

print ( "my favorite movie is", (movie["title"]), "which was released in", (movie["year"]), "and directed by", (movie ["director"]))

movie ["budget"] = 150
movie ["revenue"] = 1450

print (movie ["revenue"] - movie ["budget"])

if movie ["revenue"] < movie ["budget"]:
    print ("That was a bad investment")
elif movie ["revenue"] >= movie ["budget"] * 5:
    print ("That was a great investemnt")
else: 
    print("That was an okay investment")

pop = {
    "Manhattan" : 1600,
    "Brooklyn" : 2600,
    "Bronx" : 1400,
    "Queens" : 2300,
    "Staten Island" : 470
}

print (pop["Brooklyn"])

print (pop["Manhattan"]+ pop["Brooklyn"]+ pop["Bronx"]+ pop["Queens"]+ pop["Staten Island"])

total_pop = (pop["Manhattan"]+ pop["Brooklyn"]+ pop["Bronx"]+ pop["Queens"]+ pop["Staten Island"])

print (round(pop["Manhattan"]/total_pop * 100), "percent of NYC's population lives in Manhattan")







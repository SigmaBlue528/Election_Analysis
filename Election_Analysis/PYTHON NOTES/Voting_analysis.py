# Methods for determining votes by county
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#    print(counties_dict[county])

#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(county, voters)

#Dictionaries in a list of dictionaries
    #voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
    #                {"county":"Denver", "registered_voters": 463353},
    #                {"county":"Jefferson", "registered_voters": 432438}]

    #for county_dict in voting_data:
    #    print(county_dict)

# Get values from a List of Dictionaries
    #for county_dict in voting_data:
    #    for value in county_dict.values():
    #        print(value)

# print statement for the loop
    #for county_dict in voting_data:
    #    print(county_dict['county'])

# F- STRINGS
    #ORIGINAL
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

    #MODIFIED
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# F-STRINGS W. DICTIONARIES
    #ORIGINAL
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#   print(county + " county has " + str(voters) + " registered voters.")

    #MODIFIED
        #counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
            #for county, voters in counties_dict.items():
            #    print(f"{county} county has {voters} registered voters.")

# Multiple F-strings
    #candidate_votes = int(input("How many votes did the candidate get in the election? "))
    #total_votes = int(input("What is the total number of votes in the election? "))
    #message_to_candidate = (
        #    f"You received {candidate_votes} number of votes. "
        #    f"The total number of votes in the election was {total_votes}. "
                #f"You received {candidate_votes / total_votes * 100}% of the total votes.")
        #    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
        #print(message_to_candidate)

#format floating -point decimals
    #f'{value:{width}.{precision}}'

#SKILL DRILL
    #counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    #for county, voters in counties_dict.items():
    #    print(f"{county} county has {voters} registered voters.")

#SKILL DRILL 2
    #counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    #voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
    #for county, voters in counties_dict.items():
        #    print(f"{county} county has {voters} registered voters.")
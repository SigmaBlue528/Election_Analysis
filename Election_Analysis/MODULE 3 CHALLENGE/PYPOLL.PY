# THE DATA WE NEED TO RETREIVE
#1. THE TOTLA NUMBER OF VOTES CAST
#2. A COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES
#3. THE PERCENTAGE OF VOTES EACH CANDIDATE WON
#4. THE TOTAL NUMBER OF VOTES EACH CANDIDATE WON
#5. THE WINNER OF THE ELECTION BASED ON POPULAR VOTE

#TIME NOTES
#METHOD 1
    # Import the datetime class from the datetime module.
        #import datetime
    # Use the now() attribute on the datetime class to get the present time.
        #now = datetime.datetime.now()
    # Print the present time.
       #print("The time right now is ", now)

#METHOD 2
    # Import the datetime class from the datetime module.
        #import datetime as dt
    # Use the now() attribute on the datetime class to get the present time.
        #now = dt.datetime.now()
    # Print the present time.
        #print("The time right now is ", now)

#TO OPEN THE CSV

    # Assign a variable for the file to load and the path.
        #file_to_load = 'Resources/election_results.csv'
    # Open the election results and read the file.
        #election_data = open(file_to_load, 'r')

    # To do: perform analysis.

    # Close the file.
        #election_data.close()

#DIRECT PATH
    # Open the election results and read the file
        #file_to_load = 'Resources/election_results.csv'
        #with open(file_to_load) as election_data:

        # To do: perform analysis.
            #print(election_data)

# INDIRECT METHOD
#import csv
#import os
 #Assign a variable for the file to load and the path.
#file_to_load = os.path.join("Resources", "election_results.csv")
 #Open the election results and read the file.
#with open(file_to_load) as election_data:
 # Print the file object.
#    print(election_data)


#3.4.3 STARTS HERE ORIGINAL
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()


#3.4.3 CLEANER VERSION
# Create a filename variable to a direct or indirect path to the file.
#    file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the txt file.
#    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson") 


#DIRECT METHOD WAS SELECTED
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

      # Print the header row.
    headers = next(file_reader)
    print(headers)







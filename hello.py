#NOTES:
# print "hello" #python 2
#print("hello") #python3

#goals: Alex's Moodie Foodie Log
# 0 onboarding - reserve first line w/ my name and a nice greeting
# 1 take input - food item (string), mood (sad, neutral, happy)
# 2 save input to csv 
    #2.5(so that every time script is run it will load csv file), 
# 3 analyze score for the day, then week
    #3.5 make graph
# 4  save

import csv
#CHECK IF USER INFO CSV FILE EXISTS THEN PULL DATA FROM user_info.CSV, use conditionals (if elses)
# USE IF ELSE if detects csv file; use str from csv; COPY READ BLOCK 
with open('user_info.csv', 'r') as user_info:
    #first line says i want to open this file and make it available as "user_info"
    user_info_reader = csv.reader(user_info)
    user_name = None
    #^defining user_name variable as none/false value = empty
    for row in user_info_reader:
        user_name = (', '.join(row))
        #take this ', '  
    if user_name:
        print ("Hello, M'lady -tips fedora-, " + user_name)
    else:
        print ('Enter your name:')
        user_name = input ()
        print ("Hello M'lady, " + user_name) 
# if user_name is not an empty string
    # go ahead and print "hello " {user_name}
# else ask the user for their name

#get the name from input and save to csv

with open('user_info.csv', 'w' ) as user_info:
    #open - open the file named ('user_info.csv', 'w' - writing in the file vs 'r' read file) 
        # as csvfile - opening the file and saving it as VARIABLE NAME "user_info"
    user_info_writer = csv.writer(user_info,
         #writer, what is used to write to the file
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    user_info_writer.writerow([user_name])
        #[] = an array, writerow takes in arrays instead of strings; above puts a string (user_name) intro an array []
    
# with open('user_info.csv', 'r') as user_info:
#     #first line says i want to open this file and make it available as "r_user_info"
#     user_info_reader = csv.reader(user_info)
#     for row in user_info_reader:
#         user_name = (', '.join(row))
#         #take this ', ' 


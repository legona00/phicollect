from excuses import *
from mailing import *
from attendance import *
from sanctions import *
import pandas as pd
import xlsxwriter

#Dictionary with the emails of each bro
EMAILS = {'Don Yanez':'legona00@gmail.com', 'Don Pachuco':'marcocastaneda10@gmail.com'}

#Get the current excuse/sanction totals for each brother
#FORMAT:
#Don Name, Balance, Remaining Excuses
master_list = list_of_bros()

#FORMAT:
#Don Name, Submission Date, Event Date
excuse_responses = excuse_response()
print("EXCUSE RESPONSES")
print(excuse_responses)

#----------------Validate Excuse----------------
#First check if they have any excuses remaining
for response in excuse_responses:
    for brother in master_list:
        #Now that we found the correct brother, check if they have any excuses remaining
        if(brother[0] == response[0] and int(brother[2]) > 0):
            #Now validate the date submission
            if(date_before(response[1], response[2])):
                #Excuse has been validated, append the date of the event to the bro,
                #Will use this later to verify attendance for events
                print(response[2])
                brother.append(response[2])
                #Now decrement # of excuses by 1
                brother[2] = str(int(brother[2]) - 1)
            else:
                print()
                print(brother[0], 'submitted an invalid excuse, the date is not before the event')
        elif brother[0] == response[0] and int(brother[2]) <= 0:
            print(brother[0], 'does not have any excuses remaining')

#Now that the excuse is validated, we now need to check attendance for the event
#---- attendance.txt
# TODO: take input from google form for attendance


#format file so first line is date, second line is event name, next line has each brother's name
#
file = open('attendance.txt', 'r')


attendance_list = []
#Remove hanging newline character
#YYYY-MM-DD
date = file.readline()[0:-1]
event_name = file.readline()[0:-1]
for line in file:
    attendance_list.append(line[0:-1])
#Attendance list now has each bro who attended


#These bros need to be sanctioned, they do not have a valid excuse and they missed the event
#This only works for one event at a time
#This only has the name of bros
sanctionBros = noExcuses(master_list, attendance_list, date)
print(sanctionBros)
sanction_amt = int(input("What is the sanction amount: "))

#--------------EMAIL------------------------------------
#use event-name from previous to create the body of the email
body = 'Saludos,\n\nUnfortunately we failed to receive an excuse for your absence(s). You have been sanctioned in the amount of $'
body += str(sanction_amt)
body += '.\nBelow you will find the reasoning for your sanction, date and its price.\n- '
body += event_name
body += ' (' + date + ')'
body += ' : '
body += str(sanction_amt)
body += '$\n\nPlease pay all fees through Venmo @Leo-Gonzalez-89 CashApp $LeoG2002 or by cash by the first meeting of the upcoming month.\n\n'
body += 'If you have any questions or concerns, feel free to contact me.\n\nSPSJ\n--\nLeo Gonzalez\nVP of Standards\ntamufiastandards@gmail.com (972)536-3310' 
#print(body)

#Send email to each brother in sanctionBros
#good, just need to update EMAILS to include all brothers email addresses

send_email(body, 'legona00@gmail.com')
#for brother in sanctionBros:
#    send_email(body, EMAILS[brother])

#--------------SANCTIONS--------------------------------
#Now need to update the sanction amount for each bro


#This works, now that we have this, we can make a new csv with
#all the updated values
update_sanctions(master_list, sanctionBros, sanction_amt)

workbook = xlsxwriter.Workbook('updated.xlsx')
worksheet = workbook.add_worksheet()


worksheet.write('A1', 'Brother')
worksheet.write('B1', 'Sanction Total ($)')
worksheet.write('C1', 'Remaining Excuses')
worksheet.write('D1', 'Used Excuses')

row = 1
col = 0
for brother in master_list:
    col = 0
    for item in brother:
        if col == 1: 
            #Sanction Balance
            worksheet.write_number(row, col, int(item))
        elif col == 2:
            #Excuses left
            worksheet.write_number(row, col, int(item))
        else:
            #Brother Names and Dates
            worksheet.write_string(row, col, item)
        col += 1
    row += 1

workbook.close()
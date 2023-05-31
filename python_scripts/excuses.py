#Get master sheet w/ totals for sanctions and excuses
#Get list of all events and make sure there is actually an event
#First check submissions for each event make sure they are submitted 24 hrs before
#Check if brothers have enough excuses left
import gspread as gs
import pandas as pd
 

def list_of_bros():
    excel = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vRSmOMQeO88rWQZrVNWYXeL2DuEjOl-kf98AM1_bbitUaqxDRPWRirzqzQ761OsuEt3NTPWGnypvn3N/pub?output=xlsx')

    excel = excel.to_string()
    excel = excel.split('\n')
    #print(excel)
    del excel[0]
    #Each line contains each brother and their info, need to split into list of list with each list containing:
    # NAME, BALANCE, EXCUSE 1-5
    #Need to combine don and brother name, currently split up bc of space
    list_of_bros = []
    for index, line in enumerate(excel):
        line.strip()
        line_list = line.split()
        del line_list[0]
        name = line_list[0] + ' ' + line_list[1]
        del line_list[0]
        line_list[0] = name
        list_of_bros.append(line_list)

    return list_of_bros

#We now have a list with the update values for each bro
#We now can check the excuses response to see if anyone has submitted, Check the calendar and make sure there is an event on the date from the excuse


#TODO: Change so it does not append responses that have already been used
#Handle this by deleting the entries once they have been used by the program
#Also need to be able to verify that the event date is correct, so people dont lie
def excuse_response():
    responses = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vRzjbimzwf81IHeYHMlDwCO7_4aEyEOLHZwp4NCflKvGQxBsI91dqeup3ZX3H416n4fEnm0B5f8Hqhl/pub?output=xlsx')
    responses = responses.to_string().split('\n')
    #Always delete the first line, it is just a header
    del responses[0]
    response_data = []
    #Next we only need the date of submission, date of the event, and bro name
    for line in responses:
        #First make sure the response line is not empty, empty = NaN
        line = line.split()
        #Only work with the response if it is not blank
        if line[1] != "NaT":
            submit_date = line[1]
            name = line[3] + ' ' + line[4]
            event_date = line[6]
            line = []
            #NAME | SUBMISSION DATE | EVENT DATE
            line.append(name)
            line.append(submit_date)
            line.append(event_date)
            response_data.append(line)

    return response_data


#Inputs in format of 'YYYY-MM-DD'
#Return true if the submission is at least one day before the date
def date_before(submission, date):
    submission_list = submission.split('-')
    date_list = date.split('-')
    #First check the months
    if(int(submission_list[1]) < int(date_list[1])):
        return True
    #Then check the days
    if(int(submission_list[2]) < int(date_list[2])):
        return True
    return False
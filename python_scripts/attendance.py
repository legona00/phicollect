#Everything is validated, each brother has a list of the events they 
#submitted excuses for at the end of their 'list'

#Need to check each event's attendance and check with full roster
#Bros not in attendance, check if they have an excuse submitted for the event

#This function will return a list of bros that missed an event and do not have
# an excuse, each function call should have the date of the event we are 
#checking an excuse for
#Parameters: list of active bros, list of bros who attended event
#DATE: YYYY-MM-DD
def noExcuses(brotherList, attendanceList, date):
    didNotAttend = []
    for brother in brotherList:
        #If the bro did not atend, add to didNotAttend
        if brother[0] not in attendanceList:
            didNotAttend.append(brother)

    ##Now check if any of the brothers in didNotAttend have a valid excuse
    for brother in didNotAttend:
        for info in brother:
            if(info == date):
                didNotAttend.remove(brother)

    nameList = []

    for brother in didNotAttend:
        #We only need the don name
        nameList.append(brother[0])

    return nameList
    
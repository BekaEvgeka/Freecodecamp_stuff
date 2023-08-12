def add_time(starttime, time_to_add, startday = None):

    if startday is not None:
        if startday.lower() == "monday":
            startday = 1
        elif startday.lower() == "tuesday":
            startday = 2
        elif startday.lower() == "wednesday":
            startday = 3
        elif startday.lower() == "thrursday":
            startday = 4
        elif startday.lower() == "friday":
            startday = 5
        elif startday.lower() == "saturday":
            startday = 6
        elif startday.lower() == "sunday":
            startday = 7

    print(startday)

    time = starttime.split()
    timetoconvert = time[0]
    hours = timetoconvert.split(':')[0]
    minutes = int(timetoconvert.split(':')[1])

    if time[1] == "AM":
        hours = int(hours)
    else:
        hours = int(hours) + 12
    
    addhours = int(time_to_add.split(':')[0])
    addminutes = int(time_to_add.split(':')[1])

    finalhours = hours + addhours
    finalminutes = minutes + addminutes

    finalhours = finalhours + (finalminutes // 60)
    finalminutes = finalminutes % 60
    if finalminutes < 10:
        finalminutes = "0" + str(finalminutes)

    dayspassed = finalhours // 24
    finalhours = finalhours % 24
    if finalhours > 12:
        finalhours = finalhours - 12
        if startday == None:
            if dayspassed == 1:
                print(str(finalhours) + ":" + str(finalminutes) + " PM"+ " " + "(one day)" )
            elif dayspassed > 1:
                print(str(finalhours) + ":" + str(finalminutes) + " PM" + " " + "(" +  str(dayspassed) + " days later)" )
            else:
                print(str(finalhours) + ":" + str(finalminutes) + " PM")
        else:
            endday = startday + dayspassed
            while endday >= 7:
                endday -= 7
            if endday == 1:
                endday = "Monday"
            elif endday == 2:
                endday = "Tuesday"
            elif endday == 3:
                endday = "Wednesday"
            elif endday == 4:
                endday = "Thursday"
            elif endday == 5:
                endday = "Friday"
            elif endday == 6:
                endday = "Saturday"
            elif endday == 7:
                endday = "Sunday"
            elif endday == 0:
                endday = "Sunday"
            if dayspassed == 1:
                print(str(finalhours) + ":" + str(finalminutes) + " PM, " + endday + " " + "(one day)" )
            elif dayspassed > 1:
                print(str(finalhours) + ":" + str(finalminutes) + " PM, " + endday + " " + "(" +  str(dayspassed) + " days later)" )
            else:
                print(str(finalhours) + ":" + str(finalminutes) + " PM, " + endday)

    elif finalhours <= 12:
        if startday == None:
            if dayspassed == 1:
                print(str(finalhours) + ":" + str(finalminutes) + " AM"+ " " + "(one day)" )
            elif dayspassed > 1:
                print(str(finalhours) + ":" + str(finalminutes) + " AM" + " " + "(" +  str(dayspassed) + " days later)" )
            else:
                print(str(finalhours) + ":" + str(finalminutes) + " AM")
        else:
            endday = startday + dayspassed
            while endday >= 7:
                endday -= 7
            if endday == 1:
                endday = "Monday"
            elif endday == 2:
                endday = "Tuesday"
            elif endday == 3:
                endday = "Wednesday"
            elif endday == 4:
                endday = "Thursday"
            elif endday == 5:
                endday = "Friday"
            elif endday == 6:
                endday = "Saturday"
            elif endday == 7:
                endday = "Sunday"
            elif endday == 0:
                endday = "Sunday"
            
            if dayspassed == 1:
                print(str(finalhours) + ":" + str(finalminutes) + " AM, " + endday + " " + "(one day)" )
            elif dayspassed > 1:
                print(str(finalhours) + ":" + str(finalminutes) + " AM, " + endday + " " + "(" +  str(dayspassed) + " days later)" )
            else:
                print(str(finalhours) + ":" + str(finalminutes) + " AM, " + endday)




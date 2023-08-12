def add_time(starttime, time_to_add, startday = None):
    time = starttime.split()
    timetoconvert = time[0]
    # print(timetoconvert)
    hours = timetoconvert.split(':')[0]
    minutes = int(timetoconvert.split(':')[1])

    if time[1] == "AM":
        hours = int(hours)
    else:
        hours = int(hours) + 12
    
    print (hours)
    print (minutes)

    to_add = time_to_add
    addhours = int(time_to_add.split(':')[0])
    addminutes = int(time_to_add.split(':')[1])

    finalhours = hours + addhours
    finalminutes = minutes + addminutes

    finalhours = finalhours + (finalminutes // 60)
    finalminutes = finalminutes % 60
    
    
    print(str(finalhours) + ":" + str(finalminutes) )

    # if time[1] == "AM":
    #     timetoconvert = time[0]
    # elif time[1] == "PM":
    #     timetoconvert = time[0] + 


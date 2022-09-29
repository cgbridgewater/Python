miliTime= ()

def timeConvert():
    miliTime = int(input("Enter a time in hh:mm (military) format: "))
    miliTime.split(":")
    if len(miliTime) == 3:
        hours = miliTime[0]
        minutes = miliTime[2]
        if hours < 0:
            print("Hours can't be less than 0.")
    elif len(miliTime) == 4:
        if miliTime[0:2] >= 10:
            hours = militime[0:2]
            minutes = militime[3]
            if minutes < 0:
                print("Minutes can't be less than 0.")
            if minutes < 10:
                minutes = 0 + minutes
        else:
            hours = miliTime[0]
            minutes = militime[2:]
            if minutes >= 60:
                print("Too big of a number for minutes.")
    else:
        hours = miliTime[0:2]
        minutes = miliTime[3:]
    setting = AM
    if hours > 12:
        setting = PM
        hours -= 12
    # print(hours + ":" + minutes + setting)
print(("%02d:%02d" + setting) % (hours, minutes))


timeConvert()
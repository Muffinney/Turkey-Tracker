cookTim = []
def convertTim():
    if min >= 60:
        hour = (min-(min%60))/60
        min = min%60
        if hour >= 24:
            day = (hour-(hour%24))/24
            hour = hour%24
            if day >= 7:
                week = (day-(day%7))/7
                day = day%7
while True:
    min = 0
    hour = 0
    day = 0
    week = 0
    # ask number of turkeys
    numTur = int(input("Number of turkeys: "))
    for i in range(numTur):
        # ask for weight and method of cooking
        weight = int(input("How many pounds does your turkey weigh? "))
        method = input("How do you want to cook the turkey? (roast, grill, fry, smoke, or boil) ")
        # calculate cooking time based on method of cooking
        if method == "roast":
            indivTim = weight * 14
        elif method == "grill":
            indivTim = weight * 12
        elif method == "fry":
            indivTim = weight * 4
        elif method == "smoke":
            indivTim = weight * 35
        elif method == "boil":
            indivTim = weight * 13
        else:
            print("That method of cooking is not supported by this program")
            # ask if user wants to run program again
            question = input("Would you like to calculate the cooking time of more turkeys? (y/n) ")
            again = question == "y"
            if again:
                continue
            else:
                break
        cookTim.append(indivTim)
    for i in range(numTur):
        min = cookTim[i]
        convertTim()
        if week > 0:
            print("Turkey " +  is " + str(week) + " weeks, " + str(day) + " days, " + str(hour) + " hours, " + str(min) + " minutes")
        elif day > 0:
            print("Your total cooking time is " + str(day) + " days, " + str(hour) + " hours, " + str(min) + " minutes")
        elif hour > 0:
            print("Your total cooking time is " + str(hour) + " hours, " + str(min) + " minutes")
        else:
            print("Your total cooking time is " + str(min) + " minutes")
        min = 0
        hour = 0
        day = 0
        week = 0
    # sum individual cook times
    min = sum(cookTim)
    convertTim()
    # print total cook time
    if week > 0:
        print("Your total cooking time is " + str(week) + " weeks, " + str(day) + " days, " + str(hour) + " hours, " + str(min) + " minutes")
    elif day > 0:
        print("Your total cooking time is " + str(day) + " days, " + str(hour) + " hours, " + str(min) + " minutes")
    elif hour > 0:
        print("Your total cooking time is " + str(hour) + " hours, " + str(min) + " minutes")
    else:
        print("Your total cooking time is " + str(min) + " minutes")
    # ask if user wants to run program again
    question = input("Would you like to calculate the cooking time of more turkeys? (y/n) ")
    stop = question != "y"
    if stop:
        break
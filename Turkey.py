while True:
    hour = 0
    day = 0
    min = 0
    # ask number of turkeys
    numTur = int(input("Number of turkeys: "))
    for i in range(numTur):
        # ask for weight and method of cooking
        weight = int(input("How many pounds does your turkey weigh? "))
        method = input("How do you want to cook the turkey? (roast, grill, fry, smoke, or boil) ")
        # calculate cooking time based on method of cooking
        if method == "roast":
            min += weight * 14
        elif method == "grill":
            min += weight * 12
        elif method == "fry":
            min += weight * 4
        elif method == "smoke":
            min += weight * 35
        elif method == "boil":
            min += weight * 13
        else:
            print("That method of cooking is not supported by this program")
            # ask if user wants to run program again
            question = input("Would you like to calculate the cooking time of more turkeys? (y/n) ")
            again = question == "y"
            if again:
                continue
            else:
                break
    # convert minutes to hours and days
    if min > 60:
        hour = (min-min%60)/60
        min = min%60
        if hour > 24:
            day = (hour-hour%24)/24
            hour = hour%24
    # print times
    if day > 0:
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
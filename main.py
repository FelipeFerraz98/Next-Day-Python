day = int(input("Enter the day "))
month = int(input("Enter the month "))
year = int(input("Enter the year "))
trade = 0
february = 0

#Months with 31 days
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day == 31:
      day = 1
      month = month + 1
      trade = 1
    
    else:
      day = day + 1
    
#Months with 30 days
if month == 4 or month == 6 or month == 9 or month == 11 and trade == 0:
    if day == 30:
      day = 1
      month = month + 1
      trade = 1
    
    else:
      day = day + 1
    
  

#February
if month == 2 and trade == 0:

    if day == 28 or day == 29:
    
    #Leap year analysis
        if year % 400 == 0 or year % 4 == 0:
            if day == 29:
                day = 1
                month = month + 1
                trade = 1

            else:
                day = day + 1
                trade = 1
      
        
    #If the year is not a leap year
    if day == 28 or day == 29 and trade == 0:
        if day == 29:
            day = 1
            month = month + 1
            trade = 1
            print("The year is not a leap year, so there is no day 29, the next day after the 28 will be: {}/{}/{}".format(month, day, year))
            february = 1
            #Day 29 does not exist so the program ends here showing the possible next day

        else:
            day = 1
            month = month + 1
            trade = 1
      

    #Normal day
    if day < 28 and trade == 0:
        day = day + 1

        

#December
if month == 12 and trade == 0:
    if day == 31:
        day = 1
        year = year + 1
        month = 1

    else:
        day = day + 1


if february == 0:
    print("The next day: {}/{}/{}".format(month, day, year))

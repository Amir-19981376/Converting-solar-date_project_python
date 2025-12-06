def converter (day , month , year ) :
    if month > 10 or day >10 and month ==10 :
        birthday =year +622
    else :
        birthday =year +621

    print(f"The birthday is {birthday}")

day = int (input("Enter the day"))
month = int (input("Enter the month"))
year = int (input("Enter the year"))

converter (day,month,year)
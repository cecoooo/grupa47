while(True):    
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    if month > 12 or month < 1:
        raise Exception('Invalid data')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30 or day < 1:
            raise Exception('Invalid data')
        elif day == 30:
            day = 1
            month += 1
        else:
            day+=1
    elif month == 2:
        if year % 4 == 0:
            if day > 29 or day < 1:
                raise Exception('Invalid data')
            elif day == 29:
                day = 1
                month = 3
            else:
                day+=1
        else:
            if day > 28 or day < 1:
                raise Exception('Invalid data')
            elif day == 28:
                day = 1
                month = 3
            else:
                day+=1
    else:
        if day > 31 or day < 1:
            raise Exception('Invalid data')
        elif day == 31:
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1
            day = 1
        else:
            day+=1
    print(f"{year}:{month:02d}:{day:02d}")
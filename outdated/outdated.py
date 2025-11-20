cal={
    "January" : '01',
    "February": '02',
    "March" : '03',
    "April" : '04',
    "May" : '05',
    "June" : '06',
    "July" : '07',
    "August" : '08',
    "September" : '09',
    "October" : '10',
    "November" : '11',
    "December" : '12'
}

while True:
    try:
        date = input('Date: ').strip()
        if '/' in date:
            month,day,year = date.split('/')
            if len(year)!=4:
                raise Exception
            month = int(month)
            day = int(day)
            if not 1<= month <=12 or day >31:
                raise Exception

            if month in [1,2,3,4,5,6,7,8,9]:
                month = str(month)
                month= '0' + month
            break
        elif ',' in date:
            date = date.replace(',','')
            month,day,year = date.split(' ')
            month = month.lower().title()
            day = int(day)
            if not month in cal or day>31:
                raise Exception
            month = cal[month]
            break
        else:
            raise Exception
    except ValueError:
        pass
    except Exception:
        pass


if day in [1,2,3,4,5,6,7,8,9]:
    day = str(day)
    day = '0' + day
print(year,month,day,sep='-')



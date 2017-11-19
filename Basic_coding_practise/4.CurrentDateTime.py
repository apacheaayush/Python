import datetime
print(datetime.datetime.now())
print('Current date & time is: ')
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

now = datetime.datetime.now()
print('Current date & time is: %r' %now.strftime('%Y-%m-%d %H:%M:%S'))


"""
About datetime module:
dir(datetime)

Main classes inside datetime are:
(i) date - date class is for working with dates
(ii) time - time class is for working with times
(iii) datetime - combination of both date and time classes

help(datetime.date)
help(datetime.time)
help(datetime.datetime)

Making a date:
date1 = datetime.date(1956, 6, 2)
type(date1)
print(date1.year)
print(date1.month)
print(date1.day)

'timedelta' class - lets you add or substract number of days from a date
Suppose you want to know the date after 100 days from date1
Create a timedelta object by passing the number of days:
delta = datetime.timedelta(100) (A positive number will increase the date and a negative number will decrease the date)
print(date1 + delta)

Notice that the default date format is 'yyyy-mm-dd'
But you can always change the format.
for example:
to print date1 in format # Day-name, Month-name Day#, Year
print(date1.strftime("%A, %B %d, %Y"))

datetime class:
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0) (hour, minute, second)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
access different components
print(launch_date.year)
print(launch_date.hour)
print(launch_date.minute)

Current date:
now = datetime.dateime.today()
print(now)
print(now.microsecond)

Convert strings into datetimes:
Module - datetime
Class - datetime
Method - strptime()
moon_landing = '7/20/1969'
moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m/%d/%Y')
print(moon_landing_date)
type(moon_landing_date)




"""

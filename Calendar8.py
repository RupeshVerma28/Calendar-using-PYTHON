import calendar

year = int(input("Enter year: "))
month = int(input("Ente month: "))

cal = calendar.month(year,month)
print(cal)
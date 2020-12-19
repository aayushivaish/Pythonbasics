import datetime
today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")
d2 = today.strftime("%B %d %Y")
current = datetime.datetime.now()
print(current)
current_str = current.strftime("%d %m %Y %H %M %S")
print(current_str)



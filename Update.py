import DB
import CustomerFile
import datetime

from DB import ReadData as DBReadData, WriteData as DBWriteData, SelectData as DBSelectData
from CustomerFile import Customer
from datetime import date, datetime

def FixLastSeen(date, name):
    default = "UPDATE Customer SET LastSeen = '"
    unique = FixLastSeenDate(date) + "' WHERE CustName = '" + name + "'"
    DB.WriteData(default + unique)

def FixLastSeenDate(date):
    date = '2015' if date == "" else date
    return date + '-05-03'

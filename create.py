import DB
import CustomerFile
import datetime

from DB import ReadData as DBReadData, WriteData as DBWriteData, SelectData as DBSelectData
from CustomerFile import Customer



def AddTransaction(deal,dealCustomer):
        if IsNotPresent(deal.custID):
           mrHyde = dealCustomer
           AddCustomer(mrHyde)
        AddToTheORDER(deal)   
def AddToTheORDER(deal):
        default = "INSERT INTO theORDER(OrderID,oTimeStamp,oStatus,PayInfo,Subtotal,Total,BasketSize,CustID,OrderListID) VALUES"
        unique = "('"+deal.orderID+"','"+ToGoodDate(deal.oTimeStamp)+"','"+deal.oStatus+"','"+deal.payInfo+"',"+str(deal.subTotal)+","+str(deal.total)+","+str(deal.basketSize)+","+str(deal.custID)+","+str(deal.orderListID)+")"
        DBWriteData(default + unique)
def IsNotPresent(custID):
        query = 'SELECT COUNT(*) FROM Customer Where CustID = ' + str(custID)
        temp = DBReadData(query)
        present = True if temp == 0 else False
        return present
def AddCustomer(johnDoe):
        print ('anything?')
        AddtoCustomer(johnDoe)
        print ('check 1')
        AddToCustomerListID(johnDoe)
        print ('check 2')
        AddToEmail(johnDoe)
def AddtoCustomer(johnDoe):
        default = 'INSERT INTO Customer(CustID, CustName, CustStatus, JoinDate, Birthday) VALUES'
        unique = "("+str(johnDoe.custID) +",'"+johnDoe.custName+"','"+johnDoe.custStatus+"','"+str(johnDoe.created)+"','"+str(johnDoe.birthday)+"')"
        print (default + unique)
        query = default + unique
        DB.SelectData('SELECT * FROM Customer')
        DBWriteData(query)

def AddToCustomerListID(johnDoe):#this shit broke
    d1 = datetime.date(2015,1,1)
    d2 = datetime.date(2016,1,1)
    d3 = datetime.date(2017,1,1)
    d4 = datetime.date(2018,1,1)
    d5 = datetime.date(2019,1,1)
    custListID = 102015 if d1 <= johnDoe.created < d2 else 102016 if d2 <= johnDoe.created < d3 else 102017 if d3 <= johnDoe.created < d4 else 102018 if d4 <= johnDoe.created < d5 else 102019
    query = 'INSERT INTO Customer_ListID(CustListID, CustID) VALUES (' + str(custListID) + ',' + str(johnDoe.custID)+')'
    DBWriteData(query)

def AddToEmail(johnDoe):
    default = 'INSERT INTO Customer_Emails(CustID, Email) VALUES '
    for email in johnDoe.emails.emails:        
        DBWriteData(default + '(' + str(johnDoe.custID) + ",'"+ email +"')")

def ToGoodDate(date):
        temp = str(date).split('.')
        return temp[0]

# def ToAcceptableDate(temp):
#         if temp == '':
#                 temp = 41721.0
#         return str(datetime.fromordinal(datetime(1900,1,1).toordinal()+int(temp) - 2))[0:10] if temp > 2000 else FixLastSeenDate(temp)

# def FixLastSeenDate(date):
#     date = '2015' if date == "" else date
#     return date + '-05-03'

# def TwoDig(number):
#          return str(number) if number >= 10 else '0'+str(number)
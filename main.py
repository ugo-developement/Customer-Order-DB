import create
import datetime
import CustomerFile
import transactionFile

from CustomerFile import Customer, CustomerEmails
from transactionFile import Transaction
from create import AddCustomer, AddTransaction, ToGoodDate


def __main__():
    name = 'francisco'
    ident = 11222007
    created = datetime.date(2017,5,5)
    bday = datetime.date(1998,8,11)
    stat = 'Active'
    emails ={'test@test.com'}
    emailList = CustomerEmails(ident,emails)
    drJekyll = Customer(ident,created,stat,name,bday,emailList)
    
    #AddCustomer(drJekyll)

    oID = 'testdatabrah'
    oTS = datetime.datetime.now()
    oStat = 'complete'
    payFo = 'cash'
    subTo = 10
    to = 10.9
    bask = 1
    cus = 11222007
    orList = 111111
    dimeBag = Transaction(oID,oTS,oStat,payFo,subTo,to,bask,cus,orList)

    AddTransaction(dimeBag,drJekyll)
    # try:
    #     AddCustomer(drJekyll)
    #     print('did it')
    # except:
    #     print('nada')
    



if __name__ == "__main__":
    __main__()
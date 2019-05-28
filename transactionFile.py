class Transaction:
    def __init__(self,orderID,oTimeStamp,oStatus,payInfo,subTotal,total,basketSize,custID,orderListID):
        self.orderID = orderID
        self.oTimeStamp = oTimeStamp
        self.oStatus = oStatus
        self.payInfo = payInfo
        self.subTotal = subTotal
        self.total = total
        self.basketSize = basketSize
        self.custID = custID
        self.orderListID = orderListID
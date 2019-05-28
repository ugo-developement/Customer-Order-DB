
class Customer:
    def __init__(self, custID, created, custStatus, custName, birthday, emails):
        self.custID = custID
        self.created = created
        self.custStatus = custStatus
        self.custName = custName
        self.birthday = birthday
        self.emails = emails


class CustomerEmails:
    def __init__(self, custID, emails):
        self.custID = custID
        self.emails = emails


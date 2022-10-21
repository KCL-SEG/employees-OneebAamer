"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, hourly, hours, commision, bonus, contracts):
        self.name = name
        self.pay = pay
        self.hours = hours
        self.hourly = hourly
        self.commission = commision
        self.bonus = bonus
        self.contracts = contracts

    def get_pay(self):
        totalPay = self.pay
        if self.hourly:
            totalPay *= self.hours
        totalCommission = self.commission
        if not self.bonus:
            totalCommission *= self.contracts
        return totalCommission + totalPay

    def __str__(self):
        message = self.name + " works on a"
        if self.hourly:
            message += " contract of " + str(self.hours) + " hours at " + str(self.pay) + "/hour"
        else:
            message += " monthly salary of " + str(self.pay)
        if self.commission > 0:
            if self.bonus:
                message += " and receives a bonus commission of " + str(self.commission) + "."
            else:
                message += " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.commission) + "/contract."
        else:
            message += "."
        message += " Their total pay is " + str(self.get_pay()) + "."
        return message


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,False,0,0,True,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25,True,100,0,True,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,False,0,200,False,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,True,150,220,False,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,False,0,1500,True,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,True,120,600,True,0)

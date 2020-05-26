class Bank:
    bank_funds=0
    bank_customers={}
    Number_of_customers=0
    def __init__(self,first,last,date_of_birth):
        self.first=first
        self.last=last
        self.DOB=date_of_birth
        self.account_number=first[0].upper()+last[0].upper()+date_of_birth
        self.account_balance=0
        Bank.Number_of_customers+=1
        Bank.bank_customers[self.account_number]=self.account_balance

    def deposit_fund(self,amount):
        self.account_balance+=amount
        Bank.bank_funds+=amount
        Bank.bank_customers[self.account_number]+=amount
        print(self.first,self.last,'has deposited', amount, 'Rs in his account. Available balance is',self.account_balance)
    def withdraw_fund(self,amount):
        if self.account_balance>=amount and Bank.bank_funds>=amount:
            self.account_balance-=amount
            Bank.bank_funds-=amount
            Bank.bank_customers[self.account_number]-=amount
            print(self.first,self.last,'withdrew', amount, 'Rs from his account. Available balance is',self.account_balance)
        else:
            print ('Can not withdraw money because of low available balance')

nk=Bank('nand','kishor','7292')
test=Bank('test','user','1111')
john=Bank('john','wyck','7777')
nk.deposit_fund(2000)
nk.withdraw_fund(1200)
test.deposit_fund(400)
nk.withdraw_fund(500)
test.deposit_fund(2000)
nk.deposit_fund(1000)
john.withdraw_fund(5000)
print(nk.__dict__)
print(Bank.__dict__)


print('\nCustomer, Account Balance:',Bank.bank_customers)

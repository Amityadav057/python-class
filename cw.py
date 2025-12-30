class BankAccount():
    def __init__(self,account_number,acc_name,acc_type,balance):
        self.acc_num = account_number
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.balance = balance
        
    def check_balance(self):
        if self.balance == 0:
            return f'{self.acc_name}, your balance is zero'
        return f'{self.acc_name}, your balance is {self.balance}'     
    
obj = BankAccount(122, "amit", "saving", 123)
print(obj.check_balance())  
    
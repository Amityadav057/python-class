# class A():
#     __a = 100
#     __api_key = "12m,123487"
#     b =0
#     def __data(self):
#         return self.__api_key
    
# class B(A):
#     c = 100
#     def test(self):
#         return self.__a
    
# obj = A()
# # print(obj.__a)
# print(obj.__data())






class BankAccount():
    
    __account_number = "76774551790981"
    __balance = 0.0
    
    def deposite(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
    def withdrawl(self,amount):
            self.__balance = self.__balance + amount
            return self.__balance

    
    def get_balance(self):
            return self.__balance

class SavingAccount(BankAccount):
    __interest_rate = 5.0
    
    def add_interest(self):
        data = (self.get_balance() *1*self.__interest_rate)/100
        self.deposite(data)
        return self.__balance
        
        
        
    def get_account_info():
        return self.__balance
        
obj = SavingAccount()
obj.deposite(6000)
obj.withdrawl(600)

    
class bankdetail:
    def   __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance #protected

    def get_balance(self): #getter
        return self.__balance
    
    def set_balance(self,newbalance):
        self.__balance =newbalance


user1=bankdetail("rahul",1000)
user1.set_balance(2000)

print(user1.name,user1._bankdetail__balance)

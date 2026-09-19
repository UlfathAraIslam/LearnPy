class Card:
    def __init__(self,balance):
        self.__balance = balance
    
    def withdraw(self,amount):
        if amount> self.__balance:
            print("Denied: insufficient balance.")
            return False
        self.__balance += amount
        print(f"Dispensed ¥{amount}. Remaining: ¥{self.__balance}")
        return True

    def check_balance(self):
        return self.__balance
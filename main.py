class Account:
                def __init__(self, name, account_number, balance):
                    self.name = name
                    self.account_number = account_number
                    self.balance = balance
                def deposit(self, amount):
                  self.balance += amount
                  
                  print(f"{self.name} Deposited {amount} $. Current"
                        f" balance is {self.balance} $.") 
                  def withdraw(self, amount):
                    if self.balance >= amount:
                        self.balance -= amount
                        print(f"{self.name} Withdrew {amount} $. Current" 
                          f" balance is: {self.balance}")
                    else:
                        print("You don't have enough funds to withdraw.") 

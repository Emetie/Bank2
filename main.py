class Sam:
  def __init__(self):
      self.name = "Sam"
      self.bank_name = "Fictional Bank"

  def welcome(self):
      return f"Welcome to {self.bank_name}, {self.name}! How can I help you today?"

  def account_balance(self, acc):
      return f"{self.name}: Account {acc} balance: $100,000."

  def transaction_history(self, acc):
      return f"{self.name}:Recent transactions for {acc}:\n- Deposit: +$1,000\n-WD:-$90"

  def customer_support(self):
      return f"{self.name}: Customer support available 24/7. How can we assist you?"

sam = Sam()
print(sam.welcome())
print(sam.account_balance("123456"))
print(sam.transaction_history("123456"))
print(sam.customer_support())

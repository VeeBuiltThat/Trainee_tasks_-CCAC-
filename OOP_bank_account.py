""" Create a class BankAccount with:

  Attributes (set in __init__):
    - owner (string)
    - balance (float, default 0.0)

  Methods:
    - deposit(amount) — adds money, prints confirmation
    - withdraw(amount) — removes money, prints error if insufficient
    - get_balance() — returns current balance
    - __str__() — returns a readable summary

Test it:
  acc = BankAccount("Māris")
  acc.deposit(500)
  acc.withdraw(200)
  print(acc) """

class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)

    def adjust_interest_rate(self, new_rate):
        if new_rate < 0:
            print("Interest rate cannot be negative.")
        else:
            self.interest_rate = float(new_rate)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be greater than zero.")
        else:
            self.amount += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be greater than zero.")
        elif amount > self.amount:
            print("Insufficient funds.")
        else:
            self.amount -= amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Annual Interest Rate: {self.interest_rate:.2f}%\n"
                f"Interest for 30 Days: ${self.calculate_interest(30):.2f}")


def test_bank_acct():
    account = BankAcct("John Smith", "100245", 1000, 5)

    print("ORIGINAL ACCOUNT")
    print(account)

    print("\nAFTER DEPOSITING $500")
    account.deposit(500)
    print(f"Balance: ${account.get_balance():.2f}")

    print("\nAFTER WITHDRAWING $200")
    account.withdraw(200)
    print(f"Balance: ${account.get_balance():.2f}")

    print("\nAFTER CHANGING INTEREST RATE TO 4%")
    account.adjust_interest_rate(4)
    print(f"Interest for 90 Days: ${account.calculate_interest(90):.2f}")

    print("\nTESTING INSUFFICIENT FUNDS")
    account.withdraw(2000)

    print("\nFINAL ACCOUNT")
    print(account)


if __name__ == "__main__":
    test_bank_acct()

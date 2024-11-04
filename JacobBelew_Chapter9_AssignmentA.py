##Create a BankAcct Class that contains at least the following state information:
##name, account number, amount and interest rate. In addition to an __init__ method, the class
##should support methods for adjusting the interest rate, for withdrawing and depositing,
##and for giving a balance. You should also include a method to calculate the interest based
##on the number of days. Use the __str__ method to display balances and interest amounts.
##Create a test function to test the different methods in the BankAcct Class.

##The class and test function should be in one .py file.

#Create Bankacct class
class BankAcct:
    def __init__(self, name, acct_num, amount, int_rt):
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.int_rt = int_rt

    #Function for adjusting rates
    def adjust_rate(self, new_rt):
        self.int_rt = new_rt

    #Function for withdrawing funds
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds!")
        else:
            self.amount -= amount

    #Function for depositing funds
    def deposit(self, amount):
        self.amount += amount

    #Function to tell current balance
    def balance(self):
        return self.amount

    #Function to calculate interest
    def calculate_int(self, days):
        return (self.amount * self.int_rt * days) / 365

    #Display the account credentials
    def __str__(self):
        return f"Name: {self.name}, Account Number: {self.acct_num}, Balance: {self.amount}, Interest Rate: {self.int_rt}"

#Test function to test the BankAcct class methods

def test_bank_acct():
    print("Make Account")
    acct = BankAcct("Jacob Belew", 123456789, 1000, 3.5)
    print(acct)
    print("Deposit 1000 into the account:")
    acct.deposit(1000)
    print(acct)
    print ("Withdraw 500 from the account:")
    acct.withdraw(500)
    print(acct)
    print("Adjust the interest rate:")
    acct.adjust_rate(.073)
    print(acct)
    print("Calculate interest rate over a period of time:")
    interest = acct.calculate_int(23)
    print(f"Interest for 23 consecutive days: {interest}")

#Close test bank account function
def main():
    test_bank_acct()

if __name__ == '__main__':
    main()

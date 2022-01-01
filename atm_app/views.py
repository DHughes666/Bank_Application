from .models import Account as AC, CheckingAccount as CK, SavingsAccount as SA, BusinessAccount as BA 

class ATM(AC):

    def __init__(self, name, balance):
        super().__init__(name, balance)
        print('Welcome {}'.format(self.name))
        print('Please enter your 4-digit number:\n****')
        input()

    def accBalance(self):
        super().accBalance()

    def action(self):
        check = CK(self.name, self.balance).acc_type()

        menu = ('CHECK_BALANCE DEPOSIT WITHDRAW TRANSFER AIRTIME END').split()
        options = int(input(
            'Choose action: \n1-Check balance\n2-Deposit \n3-Withdraw \n4-Transfer \n5-Airtime \n6-End\n\n'))
        if check == 'BUSINESS ACCOUNT':

            if options == 1:
                print(menu[0])
                BA(self.name, self.balance).accBalance()
            elif options == 2:
                print(menu[1])
                Damt = int(input('Deposit amount: '))
                BA(self.name, self.balance).deposit(Damt)
            elif options == 3:
                print(menu[2])
                amt = int(input('Withdrawal amount: '))
                BA(self.name, self.balance).withdraw(amt)
            elif options == 4:
                print(menu[3])
                print("Transfer protocol initiated")
            elif options == 5:
                print(menu[4])
                print('Airtime protocol initiated')
            elif options == int(6):
                print(menu[5])
                print('Take your card')

        elif check == 'SAVINGS ACCOUNT':

            if options == 1:
                print(menu[0])
                SA(self.name, self.balance).accBalance()
            elif options == 2:
                print(menu[1])
                amt = int(input('Deposit amount: '))
                SA(self.name, self.balance).deposit(amt)
            elif options == 3:
                print(menu[2])
                amount = int(input('Withdrawal amount: '))
                SA(self.name, self.balance).withdraw(amount)
            elif options == 4:
                print(menu[3])
                print("Transfer protocol initiated")
            elif options == 5:
                print(menu[4])
                print('Airtime protocol initiated')
            elif options == int(6):
                print(menu[5])
                print('Take your card')


#Yunus = ATM('Ezra', 5678)
#Yunus.action()

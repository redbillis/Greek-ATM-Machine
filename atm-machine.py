class Account:
    def __init__(self, name, balance, withdraw, deposit):
        self.name = name
        self.balance = balance
        self.withdraw = withdraw
        self.deposit = deposit

    def erwtisi_ypol(self):
        print("\nΤο υπόλοιπό σας είναι / Your Balance is: ", self.balance, "\n")

    def analypsi(self):
        if self.withdraw in [10, 20, 40, 60, 80, 100] and self.withdraw <= self.balance:
            self.balance = self.balance - self.withdraw
            print("\nΤο υπόλοιπό σας είναι / Your Balance is: ", self.balance, "\n")

    def katathesi(self):
        self.balance += self.deposit
        print("\nΤο υπόλοιπό σας είναι / Your Balance is: ", self.balance, "\n")




name = input("Παρακαλώ γράψτε το όνομά σας / Please enter your name: ")
withdraw = 0
deposit = 0
bank = Account(name, 700, withdraw, deposit)
print("Καλώς ήρθες / Welcome ", bank.name)
run = True
while run:
    print("\nΕπιλέξτε 1 για Ερώτηση Υπολοίπου / Choose 1 to check your Account Balance")
    print("Επιλέξτε 2 για Ανάληψη / Choose 2 to Withdraw money")
    print("Επιλέξτε 3 για Κατάθεση / Choose 3 to Deposit money")
    print("Επιλέξτε 4 για Έξοδος /  Choose 4 to Exit\n")

    option = int(input("Ποια ενέργεια θα θέλατε να εκτελέσετε; / Which option would you like to execute? "))

    if option == 1:
        bank.erwtisi_ypol()
    elif option == 2:
        print("Επιλογές ανάληψης / Withdrawal options\n10, 20, 40, 60, 80, 100.")
        bank.withdraw = float(input("Ποσό ανάληψης / Withdrawal amount: "))
        bank.analypsi()
    elif option == 3:
        bank.deposit = float(input("Ποσό κατάθεσης / Deposit amount: "))
        bank.katathesi()
    elif option == 4:
        run = False
    else:
        print("\n!!!!!!Λάθος εντολή / Not Existing Option!!!!!!")
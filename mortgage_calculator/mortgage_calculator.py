import math

class MortgageCalculator():
    months_in_years = 12
    percent = 100
    
    def __init__(self, principal_amount, annual_interest_rate, years_to_pay_mortgage):
        self.pincipal_amount = principal_amount
        self.annual_interest_rate = annual_interest_rate
        self.years_to_pay_mortgage = years_to_pay_mortgage



    def enter_principal_amount(self):
        self.principal_amount = int(input("Enter your intial sum: "))
        
    def monthly_interest_rate(self):
        self.annual_interest_rate = int(input("Enter annual interest rate in %: "))
        self.monthly_interest_rate = self.annual_interest_rate / self.percent / self.months_in_years
       
    def number_of_payments(self):
        self.years_to_pay_mortgage = int(input("Enter in how many years you would like to pay mortgage: "))
        self.number_of_payments = self.years_to_pay_mortgage * self.months_in_years
    
    def increased_interest_rate (self, new_interest_rate):
        self.annual_interest_rate = new_interest_rate
        self.monthly_interest_rate = self.annual_interest_rate / self.percent / self.months_in_years

   
    def payment_schedule(self):
        monthly_interest = self.monthly_interest_rate
        principal = self.principal_amount
        number_of_payments = self.number_of_payments
        monthly_payment = principal*(monthly_interest * math.pow(1 + monthly_interest, number_of_payments)) / (math.pow( 1 - monthly_interest, number_of_payments) - 1)
        print("Payment Schedule")
        print("Month\tPayment\t\tInteres\tPrincipal\tBalance")
        balance = principal
        for i in range(1, number_of_payments+1):
            interest = balance*monthly_interest
            principal_paid = monthly_payment - interest
            balance = balance - principal_paid
            print(f"{i}\t${monthly_payment:.2f}\t${interest:.2f}\t${principal_paid:.2f}\t${balance:.2f}")
    
    

calculator = MortgageCalculator(0, 0, 0)
calculator.enter_principal_amount()
calculator.monthly_interest_rate()
calculator.number_of_payments()
mortgage = calculator.principal_amount - float(input("Enter down payment: "))
print("Mortgagr: $", mortgage)
calculator.increased_interest_rate(5)
calculator.payment_schedule()





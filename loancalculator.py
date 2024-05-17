#Input
money_owed = float(input("How much do you want as the loan amount?\n")) # $10000
apr = float(input("What is the rate?\n")) #3%
monthly_payment = float(input("How much do you want to pay monthly?\n")) # $500
months = int(input("In How many months do you want to complete the loan?\n")) #21

monthly_interest_percent = apr/100/12

for i in range(months):
    monthly_interest = money_owed * monthly_interest_percent
    money_owed = money_owed + monthly_interest
    if (money_owed - monthly_payment < 0):
        print("The last payment is", round(money_owed,2), end=' ')
        print("You paid the loan in", i+1, "months")
        break
    money_owed = money_owed - monthly_payment
    print("Paid amount",round(monthly_payment,2), "of which the interst is", round(monthly_interest,2), "amount owed", round(money_owed,2))

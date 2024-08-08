count_pers=int(input("How many people do you have?"))
percentage=int(input("Percentage?"))
amount=pers=int(input("Amount?"))
to_pay=(((percentage/100)*amount)+amount)/count_pers

print("\nYou have to pay",to_pay,"people")
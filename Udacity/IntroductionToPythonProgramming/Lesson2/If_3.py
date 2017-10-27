#change the age to experiment with the pricing
age = 35

#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message)

class Garage():
    tickets = 60
    parkingSpaces = 60
    currentTicket = {'paid' : False}
    payment = 0

    def takeTicket(self):
        # - This should decrease the amount of tickets available by 1
        # - This should decrease the amount of parkingSpaces available by 1
        self.tickets -= 1
        self.parkingSpaces -= 1
        print('Heres your ticket.')


    def payForParking(self):
        # - Display an input that waits for an amount from the user and store it in a variable
        # - If the payment variable is not empty then (meaning the ticket has been paid) -> display 
        # a message to the user that their ticket has been paid and they have 15mins to leave
        # - This should update the "currentTicket" dictionary key "paid" to True
        try:
            self.payment = int(input('Enter Your Payment: '))
            if self.payment == 0:
                self.payForParking()
            else:
                print("You have 15 minutes to leave the parking structure.")
                self.currentTicket['paid'] = True
        except:
            print('Enter a number')
            self.payForParking()




    def leaveGarage(self):
        # - If the ticket has been paid, display a message of "Thank You, have a nice day"
        # - If the ticket has not been paid, display an input prompt for payment
        # - Once paid, display message "Thank you, have a nice day!"
        # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # - Update tickets list to increase by 1 (meaning add to the tickets list)
        if self.payment == 0:
            try:
                self.payment = int(input('Enter Your Payment: '))
                if self.payment == 0:
                    self.leaveGarage()
                else:
                    print("Thank you have a nice day.")
                    self.currentTicket['paid'] = True
                    self.tickets -= 1
                    self.parkingSpaces -= 1
            except:
                print('Enter a number')
                self.leaveGarage()
        else:
            print("Thank you have a nice day.")
        self.payment = 0
        self.tickets -= 1
        self.parkingSpaces -= 1

customer = Garage()
while True:
    ticket = input("Need a ticket? (Yes/No) ")
    if ticket.lower() == "yes":
        customer.takeTicket()
        print('Time passes...')
        ticket = input('Would you like to pay for your ticket yet? (yes/other)')
        if ticket.lower() == 'yes':
            customer.payForParking()
            ticket = input('Head to exit? (yes/other)')
            if ticket.lower() == 'yes':
                customer.leaveGarage()
            else:
                print('To bad your leaving.')
                customer.leaveGarage()
        else:
            ticket = input('Head to exit? (yes/other)')
            if ticket.lower() == 'yes':
                customer.leaveGarage()
            else:
                print('Time passes...')
                print('Parking structure is closing down.')
                customer.leaveGarage()
    elif ticket.lower() == 'no':
        print("See you another time.")
        break

def ticket_sale(
    total_tickets=20,
    max_tickets=4
):
    buyer_count = 0 #Initialize buyer_count in the function
    while total_tickets > 0:
        while True: # Ensure the input is in the correct format between 1-4
            try:
                requested_tickets = int(input('How many tickets would you like to purchase? (1-4): '))
                if 1 <= requested_tickets <= max_tickets:
                    #Stop loop if input is valid
                    break
                else:
                    print('Please enter a number between 1 and 4.')
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 4')

        #If statement to ensure there are enough tickets to purchase
        if requested_tickets <= total_tickets:
            total_tickets = total_tickets - requested_tickets
            buyer_count = buyer_count + 1 #Accumulator for buyer count
            print(f'Purchase successful! You bought {requested_tickets} tickets(s).')
        else:
            print(f'Sorry, only {total_tickets} ticket(s) remaining.')

        #Prints remaining tickets left to purchase
        print(f'Remaining tickets: {total_tickets}\n')

    #Print total number of buyers after all tickets are sold
    print(f'All tickets shave been sold! Total number of buyers: {buyer_count}')

#Call the function to run ticket sale
ticket_sale()



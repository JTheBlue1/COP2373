##Write a program asking the user for a list of their monthly expenses.
##When asking the user for their expenses, ask for the type of expense and the amount.
##Use the reduce method to analyze the expenses and display the total expense,
##the highest expense and the lowest expense.
##Label what the highest and lowest expense is.

from functools import reduce

def get_user_expenses():

    #Intialize the list of expenses
    expenses = []
    while True:

        #Prompt user for expense types
        expense_types = input('What is the type of expense? (If finished type "complete"): ').strip()
        if expense_types.lower() == 'complete':
            #Exit the loop if user wishes to quit listing expenses
            break
        while True:
            try:

                #Prompt user for the expense amount
                expense_amount = float(input(f'What is the amount for {expense_types}? '))
                expenses.append((expense_types, expense_amount))

                #Create exception handler (non-numeric input)
                break
            except ValueError:
                print("Wrong input. Enter a valid numerical value.")

    #Return list of expenses
    return expenses

def get_expense_totals(expenses):

    #Calculate the total, highest, and lowest expenses whilst using the reduce method

    total_expenses = reduce(lambda acc, expense: acc + expense[1], expenses, 0)
    highest_expenses = reduce(lambda acc, expense: max(acc, expense[1]), expenses, float('-inf'))
    lowest_expenses = reduce(lambda acc, expense: min(acc, expense[1]), expenses, float('inf'))

    #Return the calculated expenses
    return total_expenses, highest_expenses, lowest_expenses

def expense_analyzer(expense):
    #Get the total, highest, and lowest expenses
    total_expenses, highest_expenses, lowest_expenses = get_expense_totals(expense)

   #Display the total expenses
    print('\nExpense Analyzer:')
    print('******************')
    print(f'Total Expense: ${total_expenses:.2f}')

    #Identify types of expenses for highest/lowest amounts
    highest_expense_types = [expense[0] for expense in expense if expense[1] == highest_expenses]
    lowest_expense_types = [expense[0] for expense in expense if expense[1] == lowest_expenses]

    print(f'Highest expense: ${highest_expenses:.2f} (for {', '.join(highest_expense_types)})')
    print(f'Lowest expense: ${lowest_expenses:.2f} (for {', '.join(lowest_expense_types)})')

def main():
    print('Hello!, Welcome to the Expense Analyzer Machine!')
    print('---------------------------------------------------')

    #Get expenses from the user
    expense = get_user_expenses()

    #Analyze and display the user's expenses
    expense_analyzer(expense)

 #Run the main function
if __name__ == '__main__':
    main()



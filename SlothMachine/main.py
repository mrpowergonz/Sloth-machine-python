import random

#constant value
MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3
#create what each column and row is going to contain ("Baraja de cartas por ejemplo")
#dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
#multiplier in case it wins
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []

    for line in range(lines):
        symbols_in_line = [column[line] for column in columns]
        if len(set(symbols_in_line)) == 1:  # Check if all symbols in the line are the same
            symbol = symbols_in_line[0]
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

#Storing the columns    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # copy all symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)  # add the value to the column
        columns.append(column)  # append the column to columns list
    return columns
            



def print_slot_machine(columns, rows_to_print=3):
    items_per_row = 3
    total_rows = min(rows_to_print, max(len(column) for column in columns))

    for row in range(total_rows):
        count = 0
        for column in columns:
            print(column[row], end=" | ")
            count += 1

            if count % items_per_row == 0:
                print()  # Move to the next row

        if count % items_per_row != 0:
            print()  # Move to the next row if the count isn't a multiple of items_per_row


def deposit():
    #ask player to enter deposit amount
    while True:
        amount = input("What would you like to deposit $?")
        #amount has to be a positive number
        if amount.isdigit():
           amount = int(amount)
           #Check if is greater than 0
           if amount > 0:
               break
           else:
               print("Amount must be greater than 0.")
        #needs to be a number       
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        #add number of max lines in to the string
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        
        if lines.isdigit():
           lines = int(lines)
            #if lines are greater or equal to one or less than MAX_LINES
           if 1 <= lines <= MAX_LINES:
               break
           else:
               print("Enter a valid number of lines.")
          
        else:
            print("Please enter a number.")
    return lines

#amount I want to bet on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line $?")
        #amount has to be a positive number
        if amount.isdigit():
           amount = int(amount)
           #Check if is greater than 0
           if MIN_BET <= amount <= MAX_BET :
               break
           else:
               print(f"Amount must be between ${MIN_BET}  - ${MAX_BET}.")
        #needs to be a number       
        else:
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} !")
        else:
            break
    
    print(f"You are betting $ {bet} one {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS ,symbol_count)
    print_slot_machine(slots, 3)
    winnings, winning_lines = check_winnings(slots, lines , bet , symbol_value )
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)#passs every winning line to this print function
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

  

main()


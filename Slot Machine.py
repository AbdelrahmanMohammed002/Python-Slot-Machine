import random

# Constants
MAX_LINES = 3         # Maximum number of lines the user can bet on
MAX_BET = 200         # Maximum bet allowed per line
MIN_BET = 10          # Minimum bet allowed per line

REEL_ROWS = 3         # Number of rows on the slot machine (height)
REEL_COLS = 3         # Number of columns on the slot machine (width)

# Symbols and their respective counts and values
symbol_count = {
    'A': 2,  # Symbol 'A' appears twice per reel
    'B': 4,  # Symbol 'B' appears four times per reel
    'C': 6,  # Symbol 'C' appears six times per reel
    'D': 8   # Symbol 'D' appears eight times per reel
}

symbol_value = {
    'A': 5,  # Symbol 'A' has the highest value of 5
    'B': 4,  # Symbol 'B' has a value of 4
    'C': 3,  # Symbol 'C' has a value of 3
    'D': 2   # Symbol 'D' has the lowest value of 2
}

def get_slot_machine_spin(rows, cols, symbols):
    """
    Simulates a slot machine spin. It randomly selects symbols for each column based on their frequency.

    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Dictionary containing symbols and their respective counts.

    Returns:
        list: A list of lists where each sublist represents a column of the slot machine.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)  # Create a list with the appropriate number of symbols

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)  # Randomly select symbols for each column
        columns.append(column)
    return columns

def print_slot_machine(columns):
    """
    Prints the slot machine's current state in a user-friendly format.

    Args:
        columns (list): A list of columns containing symbols.
    """
    for row in range(len(columns[0])):  # Iterate over each row
        row_symbols = [column[row] for column in columns]
        print(" | ".join(row_symbols))

def check_winnings(columns, lines, bet, values):
    """
    Checks for winning lines and calculates the total winnings based on the bet and winning symbols.

    Args:
        columns (list): A list of columns from the slot machine spin.
        lines (int): Number of lines the user bet on.
        bet (int): The bet amount per line.
        values (dict): Dictionary containing symbols and their values.

    Returns:
        tuple: The total winnings and a list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]  # The symbol in the first column of the current line
        if all(column[line] == symbol for column in columns):  # Check if the same symbol appears across the line
            winnings += values[symbol] * bet  # Calculate winnings based on symbol value and bet
            winning_lines.append(line + 1)  # Store the winning line (1-based index)

    return winnings, winning_lines

def deposit():
    """
    Prompts the user to deposit an amount of money.

    Returns:
        int: The deposited amount.
    """
    while True:
        amount = input("Please enter the amount of money to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Invalid input! Please enter a positive number.")

def get_number_of_lines():
    """
    Prompts the user to select the number of lines to bet on.

    Returns:
        int: The number of lines chosen by the user.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print(f"Invalid input! Please enter a number between 1 and {MAX_LINES}.")

def get_bet():
    """
    Prompts the user to enter a bet amount per line.

    Returns:
        int: The bet amount chosen by the user.
    """
    while True:
        bet = input(f"Enter your bet per line (${MIN_BET}-${MAX_BET}): ")
        if bet.isdigit() and MIN_BET <= int(bet) <= MAX_BET:
            return int(bet)
        print(f"Invalid input! Bet must be between ${MIN_BET} and ${MAX_BET}.")

def spin(user_balance):
    """
    Handles a single spin of the slot machine, calculates winnings, and adjusts the user's balance.

    Args:
        user_balance (int): The current balance of the user.

    Returns:
        int: The net result (winnings minus total bet).
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > user_balance:
            print(f"Insufficient balance! Your current balance is ${user_balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
    slots = get_slot_machine_spin(REEL_ROWS, REEL_COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("No winning lines.")

    return winnings - total_bet  # Net profit or loss

def main():
    """
    The main game loop where the user can continue playing or quit.
    """
    user_balance = deposit()
    while True:
        print(f"Current balance: ${user_balance}")
        if input("Press Enter to play (or 'q' to quit): ").lower() == 'q':
            break
        user_balance += spin(user_balance)

    print(f"You left with ${user_balance}.")

if __name__ == "__main__":
    main()

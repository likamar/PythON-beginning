import calculations.deposit_future_value


def ask_for_numeric_value(message):
    input_value = input(message)
    return float(input_value)


initial_capital = ask_for_numeric_value("Initial calital: ")
interest_rate = ask_for_numeric_value("Interes rate: ")
term_years = ask_for_numeric_value("Deposite term in years: ")

user_deposite_future_value = calculations.deposit_future_value.calculate_deposite_future_value(initial_capital, interest_rate, term_years)

print(f"Your deposit value after {term_years:.0f} yeras wll be: {user_deposite_future_value:.2f} USD")
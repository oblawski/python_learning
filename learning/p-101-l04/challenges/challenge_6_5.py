# challange: track your investments

def invest(amount, rate, years):
    """Display year-on-year growth of an initial investment"""
    for i in range(years):
        amount = amount + (amount * rate)
        print(f"year {i + 1}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an annual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)

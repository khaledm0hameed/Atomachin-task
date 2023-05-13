from datetime import date

def calculate_days_between_dates(start_date, end_date):
    days = (end_date - start_date).days
    print(f"There are {days} days between {start_date} and {end_date}.")



from datetime import date

def calculate_days_to_birthday(birthdate):
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)

    if today > next_birthday:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

    days_left = (next_birthday - today).days
    print(f"There are {days_left} days left until your next birthday.")

# Example usage
birthdate = date(1990, 6, 15)
calculate_days_to_birthday(birthdate)

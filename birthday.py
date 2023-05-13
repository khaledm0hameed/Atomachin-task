from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year

   
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    print(f"You are {age} years old.")



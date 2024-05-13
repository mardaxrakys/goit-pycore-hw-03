from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримання поточної дати
    today = datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження у форматі рядка у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначення дати народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, розглядаємо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначення різниці між днем народження та поточним днем
        delta_days = (birthday_this_year - today).days

        # Перенесення дати привітання на наступний понеділок, якщо день народження припадає на вихідний
        if delta_days <= 7 and birthday_this_year.weekday() >= 5:
            delta_days += (7 - birthday_this_year.weekday()) + 1

        # Додавання інформації про привітання у список, якщо день народження випадає на наступний тиждень
        if 0 <= delta_days <= 7:
            congratulation_date = today + timedelta(days=delta_days)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

# ім'я та дата
users = [
    {"name": "перший", "birthday": "1995.05.16"},
    {"name": "другий", "birthday": "1995.05.12"},  
    {"name": "третій", "birthday": "1995.05.11"}

]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
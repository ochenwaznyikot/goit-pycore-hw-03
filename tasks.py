import datetime
import random
import re

#TASK 1

def get_days_from_today(date):
    object = datetime.datetime.strptime(date, "%Y.%m.%d")
    today = datetime.datetime.today()
    return object - today

print(get_days_from_today("2010.05.10").days)


#TASK 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        print('Incorrect input')
    else:
        gen = random.sample(range(min, max), quantity)
    return sorted(gen)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


#TASK 3
def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    if phone_number.startswith("380"):
        phone_number = "+" + phone_number
    elif phone_number.startswith("+"):
        pass
    else:
        phone_number = "+38" + phone_number

    return phone_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#TASK 4

from datetime import datetime, timedelta, date


def _birthday_in_year(birthday: date, year: int) -> date:
    """Return the birthday in the given year (Feb 29 falls back to Mar 1 in non-leap years)."""
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = _birthday_in_year(birthday, today.year)

        # Already passed this year -> use next year's date
        if birthday_this_year < today:
            birthday_this_year = _birthday_in_year(birthday, today.year + 1)

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            # Saturday (5) -> +2 days, Sunday (6) -> +1 day, so both land on Monday
            if congratulation_date.weekday() >= 5:
                congratulation_date += timedelta(days=7 - congratulation_date.weekday())

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming



users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
]
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
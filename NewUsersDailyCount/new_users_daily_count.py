import datetime

class NewUsersDailyCounter:
    def __init__(self):
        self._daily_counts = {}

    def add_user(self, registration_date_str):
        try:
            registration_date = datetime.datetime.strptime(registration_date_str, '%Y-%m-%d').date()
            self._daily_counts[registration_date] = self._daily_counts.get(registration_date, 0) + 1
        except ValueError:
            pass # Silently ignore invalid date formats as per strict output requirements (no print statements)

    def get_daily_counts(self):
        sorted_counts = dict(sorted(self._daily_counts.items()))
        return sorted_counts

    def get_total_new_users(self):
        return sum(self._daily_counts.values())

if __name__ == "__main__":
    counter = NewUsersDailyCounter()

    counter.add_user("2023-01-01")
    counter.add_user("2023-01-02")
    counter.add_user("2023-01-01")
    counter.add_user("2023-01-03")
    counter.add_user("2023-01-02")
    counter.add_user("2023-01-05")
    counter.add_user("2023-01-03")
    counter.add_user("2023-01-01")
    counter.add_user("2023-01-04")
    counter.add_user("invalid-date") # This will be ignored

    daily_counts = counter.get_daily_counts()
    for date, count in daily_counts.items():
        print(f"{date.strftime('%Y-%m-%d')}: {count}")

    print(f"Total: {counter.get_total_new_users()}")

    counter.add_user("2023-02-01")
    counter.add_user("2023-02-01")
    counter.add_user("2023-01-01")

    updated_daily_counts = counter.get_daily_counts()
    for date, count in updated_daily_counts.items():
        print(f"{date.strftime('%Y-%m-%d')}: {count}")

    print(f"Updated Total: {counter.get_total_new_users()}")

    empty_counter = NewUsersDailyCounter()
    print(f"Empty Counter Daily Counts: {empty_counter.get_daily_counts()}")
    print(f"Empty Counter Total Users: {empty_counter.get_total_new_users()}")
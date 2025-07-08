def get_daily_max_transactions(transactions: list[tuple[str, int]]) -> dict[str, int]:
    daily_max = {}
    for date, amount in transactions:
        daily_max[date] = max(daily_max.get(date, -float('inf')), amount)
    return daily_max
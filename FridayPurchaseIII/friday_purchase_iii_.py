import sys

def calculate_total_cost(prices):
    if not prices:
        return 0
    prices.sort(reverse=True)
    total_cost = 0
    for i in range(len(prices)):
        if (i + 1) % 3 != 0:
            total_cost += prices[i]
    return total_cost

if __name__ == '__main__':
    try:
        input_line = sys.stdin.readline().strip()
        if input_line:
            prices_str = input_line.split()
            prices = [int(p) for p in prices_str]
        else:
            prices = []
    except ValueError:
        prices = []
    except Exception:
        prices = []

    result = calculate_total_cost(prices)
    sys.stdout.write(str(result) + '\n')
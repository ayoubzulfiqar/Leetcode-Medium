import sys
import math

def find_most_expensive_unbuyable(costs):
    if not costs:
        return -1

    costs = sorted(list(set(costs)))

    if 1 in costs:
        return 0

    current_gcd = costs[0]
    for i in range(1, len(costs)):
        current_gcd = math.gcd(current_gcd, costs[i])
        if current_gcd == 1:
            break

    if current_gcd > 1:
        return -1

    max_cost = costs[-1]
    MAX_SUM = max_cost * max_cost + max_cost

    dp = [False] * (MAX_SUM + 1)
    dp[0] = True

    for cost in costs:
        for i in range(cost, MAX_SUM + 1):
            if dp[i - cost]:
                dp[i] = True

    for i in range(MAX_SUM, 0, -1):
        if not dp[i]:
            return i

    return 0

def main():
    line = sys.stdin.readline().strip()
    if not line:
        print(-1)
        return

    try:
        costs_str = line.split()
        costs = [int(x) for x in costs_str]
    except ValueError:
        print(-1)
        return

    result = find_most_expensive_unbuyable(costs)
    print(result)

if __name__ == '__main__':
    main()
import sys


def max_profit(prices):
    min_price = sys.maxsize
    max_profit_value = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit_value:
            max_profit_value = prices[i] - min_price
    return max_profit_value


# sample: [7, 1, 5, 3, 6, 4]
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter the Elements : ")))
print(max_profit(arr))

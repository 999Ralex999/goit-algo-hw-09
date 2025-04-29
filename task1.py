import timeit

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі суми монетами.
    Завжди обирає найбільший доступний номінал монети.

    Args:
        amount (int): сума для видачі

    Returns:
        dict: словник монет і їх кількість
    """
    coins_result = {}

    for coin in COINS:
        count = amount // coin
        if count:
            coins_result[coin] = count
            amount -= coin * count

    return coins_result


def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для мінімальної кількості монет.

    Args:
        amount (int): сума для видачі

    Returns:
        dict: словник монет і їх кількість
    """
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in COINS:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    result = {}
    current = amount
    while current > 0:
        coin = last_coin[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


def measure_execution_time(func, amount):
    """
    Вимірює час виконання функції.

    Args:
        func (callable): функція для тестування
        amount (int): сума для видачі

    Returns:
        float: час виконання у секундах
    """
    start_time = timeit.default_timer()
    func(amount)
    end_time = timeit.default_timer()
    return end_time - start_time


def run_tests():
    """
    Запускає тести на різних сумах і виводить результати.
    """
    test_amounts = [113, 1013, 1000033]

    print("Тестування find_coins_greedy:")
    for amount in test_amounts:
        time_spent = measure_execution_time(find_coins_greedy, amount)
        print(f"Сума {amount}: {time_spent:.6f} секунд")

    print("\nТестування find_min_coins:")
    for amount in test_amounts:
        time_spent = measure_execution_time(find_min_coins, amount)
        print(f"Сума {amount}: {time_spent:.6f} секунд")


if __name__ == "__main__":
    amount = 113

    print("Результат жадібного алгоритму:")
    print(find_coins_greedy(amount))

    print("\nРезультат алгоритму динамічного програмування:")
    print(find_min_coins(amount))

    print("\nПорівняння часу виконання:")
    run_tests()

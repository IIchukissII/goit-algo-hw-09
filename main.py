import timeit
import matplotlib.pyplot as plt


def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - coin * count
    stop = timeit.default_timer()
    return count_coins


def find_min_coins_dynamic(sum_):
    # Тут індекс це сума
    min_coins_required = [0] + [float("inf")] * sum_  # мінімальна кілкість монет
    last_coin_used = [0] * (sum_ + 1)  # остання монета для цієї суми

    for s in range(1, sum_ + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin
    return count_coins


def plot_results(time_data):
    x = [x[0] for x in time_data]
    y1 = [x[1] for x in time_data]
    y2 = [x[2] for x in time_data]

    # Create subplots stacked vertically
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Plot data on the first subplot
    plt.sca(ax1)
    plt.plot(x, y1, label="Greedy")
    plt.xlabel("Sum")
    plt.ylabel("Time")
    plt.legend()
    plt.grid()

    # Plot data on the second subplot
    plt.sca(ax2)
    plt.plot(x, y2, label="Dynamic")
    plt.legend()
    plt.xlabel("Sum")
    plt.ylabel("Time")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    time_data = []
    for i in range(1, 20000, 34):
        time_data.append(
            (
                i,
                timeit.timeit(lambda: find_coins_greedy(i), number=20),
                timeit.timeit(lambda: find_min_coins_dynamic(i), number=20),
            )
        )
    plot_results(time_data)

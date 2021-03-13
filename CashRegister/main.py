# -*- coding: utf-8 -*-

CHANGE_COINS = {
    2: "2€",
    1: "1€",
    0.5: "50 Cent",
    0.1: "10 Cent",
    0.05: "5 Cent",
    0.02: "2 Cent",
    0.01: "1 Cent",
}


def calculate_change(change_value: float):
    change_list = []
    while change_value > 0.00:
        # Round because of internal representation of floating-point numbers (Having numbers like 0.00000006)
        # It also ensures that the input only consists of two decimal places
        change_value = round(change_value, 2)
        # Check how many coins of every type fit in
        for coin_value, coin_description in CHANGE_COINS.items():
            coins_in_value = change_value // coin_value
            if coins_in_value > 0:
                change_list.append(f"{coins_in_value}x {coin_description}")
                change_value = change_value - coins_in_value * coin_value
    return change_list


if __name__ == "__main__":
    print(calculate_change(9.56))

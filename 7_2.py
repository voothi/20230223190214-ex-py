# 7.2

# [ ]
# [ ]

def get_order_amount(price_of_portion_of_ice_cream: int,
                     price_of_bottle_of_soda: int,
                     number_of_portion_of_ice_cream: int,
                     number_of_bottle_of_soda: int):
    return \
        price_of_portion_of_ice_cream * number_of_portion_of_ice_cream + \
        price_of_bottle_of_soda * number_of_bottle_of_soda


def get_analyse_summary(sum_order_stefania, sum_order_michailo):
    if sum_order_stefania < sum_order_michailo:
        print("Стефания потратила - "
              + str(sum_order_stefania)
              + ", что меньше, чем Михайло - "
              + str(sum_order_michailo))
    elif sum_order_stefania > sum_order_michailo:
        print("Стефания потратила - "
              + str(sum_order_stefania)
              + ", что больше, чем Михайло - "
              + str(sum_order_michailo))
    else:
        print("Стефания потратила - "
              + str(sum_order_stefania)
              + ", что столько же, сколько Михайло - "
              + str(sum_order_michailo))

# Тестирование
sum_order_stefania = get_order_amount(1, 4, 3, 2)
sum_order_michailo = get_order_amount(1, 4, 2, 3)
get_analyse_summary(sum_order_stefania, sum_order_michailo)

sum_order_stefania = get_order_amount(1, 4, 3, 2)
sum_order_michailo = get_order_amount(1, 4, 3, 2)
get_analyse_summary(sum_order_stefania, sum_order_michailo)

sum_order_stefania = get_order_amount(1, 4, 2, 3)
sum_order_michailo = get_order_amount(1, 4, 3, 2)
get_analyse_summary(sum_order_stefania, sum_order_michailo)
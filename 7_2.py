# 7.2

# [ ] 20230223214336 Сделать консольный ввод

def get_order_amount(price_of_portion_of_ice_cream: int,
                     price_of_bottle_of_soda: int,
                     number_of_portion_of_ice_cream: int,
                     number_of_bottle_of_soda: int):
    return \
        price_of_portion_of_ice_cream * number_of_portion_of_ice_cream + \
        price_of_bottle_of_soda * number_of_bottle_of_soda


def print_result_of_compare_orders(order_amount_stefania, order_amount_michailo):
    if order_amount_stefania < order_amount_michailo:
        print("Стефания потратила - "
              + str(order_amount_stefania)
              + ", что меньше, чем Михайло - "
              + str(order_amount_michailo))
    elif order_amount_stefania > order_amount_michailo:
        print("Стефания потратила - "
              + str(order_amount_stefania)
              + ", что больше, чем Михайло - "
              + str(order_amount_michailo))
    else:
        print("Стефания потратила - "
              + str(order_amount_stefania)
              + ", что столько же, сколько Михайло - "
              + str(order_amount_michailo))


# Тестирование
order_amount_stefania = get_order_amount(1, 4, 3, 2)
order_amount_michailo = get_order_amount(1, 4, 2, 3)
print_result_of_compare_orders(order_amount_stefania, order_amount_michailo)

order_amount_stefania = get_order_amount(1, 4, 3, 2)
order_amount_michailo = get_order_amount(1, 4, 3, 2)
print_result_of_compare_orders(order_amount_stefania, order_amount_michailo)

order_amount_stefania = get_order_amount(1, 4, 2, 3)
order_amount_michailo = get_order_amount(1, 4, 3, 2)
print_result_of_compare_orders(order_amount_stefania, order_amount_michailo)

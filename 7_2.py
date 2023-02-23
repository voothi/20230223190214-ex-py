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


sum_order_stefania = get_order_amount(1, 4, 3, 2)
sum_order_michailo = get_order_amount(1, 4, 2, 3)



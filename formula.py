import numpy as np
from constant import platform_fee

def trading_fee_malaysia(value):
    total_pricing = calculate_clearing_fee(value) + \
        platform_fee + calculate_stamp_duty(value)

    return total_pricing

def calculate_stamp_duty(transaction_value):
    if transaction_value % 1000 != 0:
        return (transaction_value // 1000) + 1
    else:
        return transaction_value // 1000
    
def calculate_clearing_fee(transaction_value):
    return (transaction_value * 0.0003)


# def custom_round(number):
#     # Check the third decimal place
#     third_precision = int((number * 1000) % 10)

#     # Round up if the third decimal is greater than 0
#     if third_precision > 0:
#         return round(number + 0.01, 2)
#     else:
#         return round(number, 2)

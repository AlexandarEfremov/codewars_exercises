from decimal import Decimal

def series_sum(n):
    division = Decimal('4')
    total_sum = Decimal('1')
    current_working_number = Decimal('1')

    for _ in range(n - 1):
        new_division = current_working_number / division
        new_division = Decimal(str(new_division))
        division += Decimal('3')
        total_sum += new_division

    total_sum = Decimal(str(total_sum))
    if n == 0:
        total_sum = "0.00"
    elif total_sum == Decimal('1'):
        total_sum = "1.00"
    else:
        total_sum = f"{total_sum:.2f}"
    return total_sum

print(series_sum(3))

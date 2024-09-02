def Decimal_To_Binary(decimal_number):
    if decimal_number == 0:
        return 0

    binary = []

    having_negative = False
    if decimal_number < 0:
        decimal_number = abs(decimal_number)
        having_negative = true

    while decimal_number > 0:
        r = decimal_number % 2
        binary.append(str(r))
        decimal_number //= 2

    binary.reverse()
    binary_number = "".join(binary)

    if having_negative:
        return "-" + binary_number
    else:
        return binary_number
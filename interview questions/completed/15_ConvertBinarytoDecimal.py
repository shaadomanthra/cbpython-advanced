def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

def binaryToDecimal2(n):
    return int(n,2)

print(binaryToDecimal2('100'))
print(binaryToDecimal2('101'))
print(binaryToDecimal2('1001'))
# Convert Binary to Decimal
def BinarytoDecimal(num):
        temp = num
        sum , i = 0, 0
        while(num):
            lastdigit = num % 10
            sum  = sum + lastdigit * pow(2,i)
            num = num//10
            i = i +1
        return sum

def BinarytoDecimal2(num):
    return int(num,2)

print(BinarytoDecimal2('11011'))


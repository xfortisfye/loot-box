"""
create empty nested list
"""

lst = [[] for _ in range(3)]
print(lst)

"""
print numbers in decimal places without rounding up or down
"""
def div_percent(dividend, divisor):
    if dividend != 0 and divisor != 0:
        return str(truncate(dividend/divisor*100, 2))
    elif dividend == 0:
        return 0.00
    elif divisor == 0:
        return 100.00
      
def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n

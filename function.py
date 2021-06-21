# return Max value between Two different values
def max(value1, value2):
    if value1 > value2:
        return value1
    elif value2 > value1:
        return value2
value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))
print(max(value1,value2))

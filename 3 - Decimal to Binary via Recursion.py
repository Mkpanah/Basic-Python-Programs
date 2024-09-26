def convert(num):
    if num == 0:
        return 0
    else:
        return (num % 2 + 10 * convert(num//2))

number = int(input("Enter a Decimal Integer Number: "))
print(f"The Binary format of {number} is {convert(num=number)}.")

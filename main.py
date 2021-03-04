let_num = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
}


def s_to_n(num):
    try:
        return int(num)
    except ValueError:
        return let_num[num.upper()]


def n_to_s(target):
    for let, num in let_num.items():
        if num == target:
            return let
    return target


def to_dec(init_base: int, num: str) -> int:
    res = 0
    rev_num = num[::-1]
    for power, digit in enumerate(rev_num):
        print(f"{res} + {s_to_n(digit)} * {init_base}^{power}")
        res += s_to_n(digit) * pow(init_base, power)
    return res


def from_dec(dest_base: int, num: int) -> str:
    dest_num = []
    while num != 0:
        print(f"{num}/{dest_base} - > {num % dest_base}")
        dest_num.append(n_to_s(num % dest_base))
        num = int(num / dest_base)
    dest_num = dest_num[::-1]
    dest_num = list(map(str, dest_num))
    return "".join(dest_num)


def convert(to_base: int, from_base: int, num_to_convert: str) -> str:
    return from_dec(to_base, to_dec(from_base, num_to_convert))


def any_base_convert():
    from_base, to_base = map(int, input("Enter base to convert from and base to convert to: ").split(" "))
    num_to_convert = input("Enter number to convert: ")
    print(f"{num_to_convert} base {from_base} to base {to_base}: {convert(to_base, from_base, num_to_convert)}")


def operation_with_any_numbers():
    num1_base, num1, num2_base, num2 = map(int, input("Enter base number base number: ").split(" "))
    num1_dec = convert(10, num1_base, str(num1))
    num2_dec = convert(10, num2_base, str(num2))
    operator = input(f"Enter operator ({num1} -> {num1_dec}_10) [operator here] ({num2} -> {num2_dec}_10): ")
    res = eval(num1_dec + operator + num2_dec)
    if res < 0:
        print(f"\n***** Result was negative the number needs to be negated *****\n    Number base 10: {res} \n")
        res = abs(res)
    return convert(num1_base, 10, str(res))


while True:
    option = input("Choose option: \n   1. Convert\n   2. Add, subtract, etc.\n ")
    if option == "1":
        check1 = "y"
        while check1 == "y":
            any_base_convert()
            check1 = input("Continue(y/n): ")
    elif option == "2":
        check2 = "y"
        while check2 == "y":
            print(operation_with_any_numbers())
            check2 = input("Continue(y/n): ")
    else:
        print("Wrong option.")
        break

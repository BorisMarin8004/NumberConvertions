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
    return str(target)


def to_dec(init_base: int, num: str) -> int:
    res = 0
    num_whole, *num_partial = num.split(".")
    num_partial = "".join(num_partial)
    rev_num_whole = num_whole[::-1]
    for power, digit in enumerate(rev_num_whole):
        if show_operations:
            print(f"{res} + {s_to_n(digit)} * {init_base}^{power}")
        res += s_to_n(digit) * pow(init_base, power)
    for power, digit in enumerate(num_partial):
        if show_operations:
            print(f"{res} + {s_to_n(digit)} * {init_base}^{-(power+1)}")
        res += s_to_n(digit) * pow(init_base, -(power+1))
    return res


def from_dec(dest_base: int, num: float) -> str:
    dest_num = ""
    num_whole = int(num)
    num_partial = num % 1
    while True:
        if show_operations:
            print(f"{num_whole}/{dest_base} - > {num_whole % dest_base}")
        dest_num += n_to_s(num_whole % dest_base)
        num_whole = int(num_whole / dest_base)
        if num_whole == 0:
            break
    dest_num = dest_num[::-1]
    if num_partial % 1 != 0:
        dest_num += "."
        while True:
            if show_operations:
                print(f"{num_partial} * {dest_base} - > {num_partial*dest_base}")
            num_partial *= dest_base
            dest_num += str(int(num_partial))
            num_partial %= 1
            if num_partial % 1 == 0:
                break
    return dest_num


def convert(to_base: int, from_base: int, num_to_convert: str) -> str:
    if from_base == to_base:
        return num_to_convert
    if from_base == 10:
        return from_dec(to_base, float(num_to_convert))
    if to_base == 10:
        return str(to_dec(from_base, num_to_convert))
    return from_dec(to_base, to_dec(from_base, num_to_convert))


def negate(base: int, num: str) -> str:
    num_neg = ""
    for i in num:
        num_neg += n_to_s(base - s_to_n(i) - 1)
    num_neg = convert(base, 10, str(eval(convert(10, base, num_neg) + "+1")))
    return num_neg


def any_base_convert() -> None:
    from_base, to_base = map(int, input("Enter base to convert from and base to convert to: ").split(" "))
    num_to_convert = input("Enter number to convert: ")
    print(f"{num_to_convert} base {from_base} to base {to_base}: {convert(to_base, from_base, num_to_convert)}")


def operation_with_any_numbers() -> str:
    num1_base, num1, num2_base, num2 = input("Enter base number base number: ").split(" ")
    num1_dec = convert(10, int(num1_base), num1)
    num2_dec = convert(10, int(num2_base), num2)
    operator = input(f"Enter operator ({num1} -> {num1_dec}_10) [operator here] ({num2} -> {num2_dec}_10): ")
    res = eval(num1_dec + operator + num2_dec)
    if res < 0:
        print(f"\n***** Result was negative the number needs to be negated *****\n    Number base 10: {res} \n")
        res = convert(int(num1_base), 10, str(abs(res)))
        return "(1)" + negate(int(num1_base), res)
    return convert(int(num1_base), 10, str(res))


while True:
    # Set to False if you do not want to see operations
    show_operations = True
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

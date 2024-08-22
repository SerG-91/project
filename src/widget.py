from src.hw9_1 import get_mask_account, get_mask_card_number


def mask_account_card(my_string: str) -> str:
    """Функция маскировки карты и счета"""
    numb = my_string.split()
    if numb[0] == "Счет":
        return get_mask_account(numb[-1])
    else:
        card_number = get_mask_card_number(numb[-1])
        return f"{" ".join(numb[:-1])}  {card_number}"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_data(data: str) -> str:
    """Функция преобразования даты к нужному формату"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


print(get_data("2024-03-11T02:26:18.671407"))

def get_mask_card_number(card: str) -> str:
    """Функция маскировки номера карты типа хххх хх** **** хххх"""

    if len(card) == 16 and card.isdigit():
        return card[:4] + " " + card[4:6] + "**" + " **** " + card[12:]
    else:
        return "Не корректно введен номер карты"


number_card = input("Введите номер карты: ")
print(get_mask_card_number(number_card))


def get_mask_account(card: str) -> str:
    """Функция маскировки номера счета типа **хххх"""
    if card.isdigit():
        return "**" + card[-4:]
    else:
        return "Не корректно введен номер счета"


number_account = input("Введите номер счета:")
print(get_mask_account(number_account))

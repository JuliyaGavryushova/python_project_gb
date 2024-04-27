"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""
import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


def check_multiplicity(amount):
    if amount % MULTIPLICITY != 0:
        print("Сумма должна быть кратной 50 у.е.")


def deposit(amount):
    check_multiplicity(amount)
    if amount % MULTIPLICITY == 0:
        global bank_account, count
        bank_account += amount
        count += 1
        operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")


def withdraw(amount):
    check_multiplicity(amount)
    global bank_account, count
    tax = (amount * PERCENT_REMOVAL).normalize()
    if tax < MIN_REMOVAL:
        tax = MIN_REMOVAL
    elif tax > MAX_REMOVAL:
        tax = MAX_REMOVAL
    if amount + tax > bank_account:
        operations.append(f"Недостаточно средств. Сумма с комиссией {(amount + tax).normalize()} у.е. На карте {bank_account} у.е.")
    else:
        bank_account -= amount + tax.normalize()
        count += 1
        operations.append(f"Снятие с карты {amount} у.е. Процент за снятие {tax} у.е.. Итого {bank_account} у.е.")


def exit():
    global bank_account, count
    if bank_account >= RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT
        operations.append(f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {round((bank_account * RICHNESS_PERCENT),4)} у.е. Итого {round((bank_account - bank_account * RICHNESS_PERCENT), 4)} у.е.")
        operations.append(f"Возьмите карту на которой {round((bank_account - tax), 4)} у.е.")
    else:
        operations.append(f"Возьмите карту на которой {bank_account} у.е.")


deposit(1000)
withdraw(200)
exit()

print(operations)
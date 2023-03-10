import requests
from datetime import datetime


def get_data(url):
    """Функция, которая получает данные в формате .json и если они получены конвертирует их в формат для работы
    в python, если данные не получены то программа сообщает по какой причине"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно\n"
        return None, f"INFO: ОШИБКА status_code{response.status_code}\n"
    except requests.exceptions.ConnectionError:
        return None, "INFO: ОШИБКА requests.exceptions.ConnectionError\n"
    except requests.exceptions.JSONDecodeError:
        return None, "INFO: ОШИБКА requests.exceptions.JSONDecodeError\n"
    return


def get_operations_executed(data):
    """Функция, возвращающая только те транзакции в которых есть необходимые ключи и значения"""
    operation_ex = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operation_ex.append(operation)
    operations_with_from = []
    for operation in operation_ex:
        if 'from' in operation:
            operations_with_from.append(operation)
    return operations_with_from


def get_last_five_operations(operations_executed, num_of_operations):
    """Функция возвращающая последних 5 уже отсортированных транзакций (от новых к старым)"""
    operations_sort = sorted(operations_executed, key=lambda operation: operation["date"], reverse=True)
    last_five = operations_sort[0:num_of_operations]
    return last_five


def get_operations_formatted(last_five_operations):
    """Функция которая в форме списка выводит информацию о транзакции в заданном формате"""
    operations_formatted_lst = []
    for operation in last_five_operations:
        date = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = operation["description"]
        payer_info, payment_method = "", ""
        if "from" in operation:
            payer = operation["from"].split()
            payment_method = payer.pop(-1)
            if payer[0] == 'Счет':
                payment_method_from = f"**{payment_method[-4:]}"
            else:
                payment_method_from = f"{payment_method[:4]} {payment_method[4:6]}** **** {payment_method[-4:]}"
            payer_info = " ".join(payer)
        recipient = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        operations_formatted_lst.append(
            f"{date} {description}\n{payer_info} {payment_method_from}->{recipient}\n{operation_amount}")
    return operations_formatted_lst
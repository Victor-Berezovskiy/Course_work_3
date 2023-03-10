import pytest


@pytest.fixture
def test_url():
    """Фикстура с адресом для получения первоначальных данных (в данном случае, я для удобства перенес их на jsonkeeper,
    но я понимаю, что это может быть любой подходящий URL)"""
    return "https://www.jsonkeeper.com/b/VK9M"


@pytest.fixture
def test_data():
    """Фикстура с ограниченным набором данных для тестирования
    в 1-м словаре нет 'execute' во 2-м нет 'from' итого 3 соответствующих условиям функции get_operations_executed
    во 2-й функции дата изменена на 2020 год"""
    return [{'date': '2019-08-26T10:50:58.294041',
             'description': 'Перевод организации',
             'from': 'Maestro 1596837868705199',
             'id': 441945886,
             'operationAmount': {'amount': '31957.58',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},

             'to': 'Счет 64686473678894779589'},
            {'date': '2020-07-03T18:35:29.512364',
             'description': 'Перевод организации',
             'from': 'MasterCard 7158300734726758',
             'id': 41428829,
             'operationAmount': {'amount': '8221.37',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 35383033474447895560'},
            {'date': '2018-06-30T02:08:58.425572',
             'description': 'Перевод организации',

             'id': 939719570,
             'operationAmount': {'amount': '9824.07',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 11776614605963066702'},
            {'date': '2019-04-04T23:20:05.206878',
             'description': 'Перевод со счета на счет',
             'from': 'Счет 19708645243227258542',
             'id': 142264268,
             'operationAmount': {'amount': '79114.93',
                                 'currency': {'code': 'USD', 'name': 'USD'}},
             'state': 'EXECUTED',
             'to': 'Счет 75651667383060284188'},
            {'date': '2019-03-23T01:09:46.296404',
             'description': 'Перевод со счета на счет',
             'from': 'Счет 44812258784861134719',
             'id': 873106923,
             'operationAmount': {'amount': '43318.34',
                                 'currency': {'code': 'RUB', 'name': 'руб.'}},
             'state': 'EXECUTED',
             'to': 'Счет 74489636417521191160'}]

from develop import utils


def test_get_data(test_url):
    """Проверка получения данных по URL"""
    assert len(utils.get_data(test_url)[0]) > 0
    assert utils.get_data("https://www.wrong.url.com")[0] is None
    assert utils.get_data("https://www.google.com")[0] is None
    assert utils.get_data("https://www.google.com/123")[0] is None


def test_get_operations_executed(test_data):
    """Проверка отбора транзакций с подходящими ключами и значениями"""
    assert len(utils.get_operations_executed(test_data)) == 3


def test_get_last_five_operations(test_data):
    """Проверка получения заданного числа транзакций"""
    assert utils.get_last_five_operations(test_data, 4)[0]['date'] == '2020-07-03T18:35:29.512364'
    assert len(utils.get_last_five_operations(test_data, 4)) == 4


def test_get_operations_formatted(test_data):
    """Проверка получения данных в необходимом формате"""
    assert utils.get_operations_formatted(test_data) == [
        '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199->Счет **9589\n31957.58 руб.',
        '03.07.2020 Перевод организации\nMasterCard 7158 30** **** 6758->Счет **5560\n8221.37 USD',
        '30.06.2018 Перевод организации\n 7158 30** **** 6758->Счет **6702\n9824.07 USD',
        '04.04.2019 Перевод со счета на счет\nСчет **8542->Счет **4188\n79114.93 USD',
        '23.03.2019 Перевод со счета на счет\nСчет **4719->Счет **1160\n43318.34 руб.']
    # data = utils.get_operations_formatted(test_data)
    # print(data)
from develop import utils


def main():
    """Функция запускающая программу"""
    OPERATIONS_URL = "https://www.jsonkeeper.com/b/VK9M"
    num_of_operations = 5

    data, info = utils.get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(info)

    operations_executed = utils.get_operations_executed(data)
    last_five_operations = utils.get_last_five_operations(operations_executed, num_of_operations)
    operations_formatted = utils.get_operations_formatted(last_five_operations)

    for string in operations_formatted:
        print(f"{string}\n")


if __name__ == "__main__":
    main()


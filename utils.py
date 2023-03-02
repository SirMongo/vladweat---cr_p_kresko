def get_private_keys() -> list:
    try:
        with open("_setup\private_keys.txt", "r") as file:
            keys = file.read().splitlines()
        return keys

    except Exception as e:
        return e

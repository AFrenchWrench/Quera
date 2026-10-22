# link https://quera.org/problemset/21205


def check_registration_rules(**kwargs):
    valid_users = []

    for username, password in kwargs.items():
        is_username_invalid = username in ["quera", "codecup"]
        is_username_short = len(username) < 4
        is_password_weak = len(password) < 6 or password.isdigit()

        is_valid = not any((is_username_invalid, is_username_short, is_password_weak))

        valid_users.append(username) if is_valid else ...

    return valid_users

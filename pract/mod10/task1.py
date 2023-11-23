import re
import doctest


def check_password(password):
    """
    :param password: string
    :return: bool

    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    """
    if not re.match("(?=.*[0-9])", password):
        return False
    if re.search(r"(.)\1\1", password):
        return False
    if not re.match(".{6,}$", password):
        return False
    if not re.match("^(?=.*[A-Z].*[A-Z])", password):
        return False
    if not re.match("(?=.*[^A-Za-z0-9].*[^A-Za-z0-9])", password):
        return False
    return True


doctest.testmod()

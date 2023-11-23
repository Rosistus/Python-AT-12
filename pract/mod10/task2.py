import re
import doctest


def check_color(color):
    """
    :param color: string
    :return: bool

    >>> check_color("#21f48D")
    True
    >>> check_color("#888")
    True
    >>> check_color("rgb(255, 255,255)")
    True
    >>> check_color("rgb(10%, 20%, 0%)")
    True
    >>> check_color("hsl(200,100%,50%)")
    True
    >>> check_color("hsl(0, 0%, 0%)")
    True
    >>> check_color("#2345")
    False
    >>> check_color("ffffff")
    False
    >>> check_color("rgb(257, 50, 10)")
    False
    >>> check_color("hsl(20, 10, 0.5)")
    False
    >>> check_color("hsl(34%, 20%, 50%)")
    False
    """
    # rgb
    if re.match(r'^(rgb\(\s*((25[0-5]|2[0-4]\d|1\d{2}|\d{1,2}%)\s*,\s*){2}(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2}%)\s*\))$', color):
        return True
    # hex
    elif re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', color):
        return True
    # hsl
    elif re.match(r'^hsl\(\s*(\d{1,3})\s*,\s*(\d{1,3}%)\s*,\s*(\d{1,3}%)\s*\)$', color):
        return True
    else:
        return False


doctest.testmod()

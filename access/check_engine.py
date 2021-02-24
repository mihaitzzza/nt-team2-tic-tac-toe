import re


def string_check(word: str):
    """Returns None or string according with condition:
    string must contain low letters, numbers, minimum
     6 characters, at least 1 letter and 1 number
     : param: word type string
     : returns: string according to condition above
     """
    result = re.match('^(?=.*[a-z])(?=.*[0-9])[a-z,0-9]{6,}$', word)
    if result is not None:
        return result.group(0)
    else:
        return result


def character_check(word: str):
    """Returns None or string according with condition:
    string must contain letters , minimum
     1 character
     : param: word type string
     : returns: string according to condition above
     """
    result = re.match('^[a-z,A-Z]+$', word)
    if result is not None:
        return result.group(0)
    else:
        return result


def email_string_check(word: str):
    """Returns None or string according with condition:
    string must have email format
     : param: word type string
     : returns: string according to condition above
     """
    result = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', word)
    if result is not None:
        return result.group(0)
    else:
        return result

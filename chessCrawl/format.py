FLOAT_VALUE_LIST = ["score", "rank", "winrate"]


def formatChessValue(valueStr):
    dicMoveValue = {}
    secs = valueStr.split(",")
    for sec in secs:
        key, value = tuple(sec.split(":"))
        if key in FLOAT_VALUE_LIST:
            dicMoveValue[key] = getScore(value)
        elif key == "move":
            dicMoveValue[key] = value
    return dicMoveValue


def formatChessValues(valuesStr):
    values = []
    secUnits = valuesStr.split("|")
    for valueStr in secUnits:
        value = formatChessValue(valueStr)
        values.append(value)
    return values


def getScore(scoreStr):
    try:
        return int(scoreStr.split()[0])
    except Exception as e:
        # print(scoreStr)
        return 10000


def toCodeMove(fenStr):
    ret = ""
    for i in range(0, len(fenStr)):
        number = None
        if i % 2 == 0:
            char = fenStr[i]
            number = ord(char) - 97
        else:
            number = 9 - int(fenStr[i])
        ret += str(number)
    return ret


def toFenMove(moveStr):
    ret = ""
    for i in range(0, len(moveStr)):
        char = None
        number = int(moveStr[i])
        if i % 2 == 0:
            char = chr(number + 97)
        else:
            char = str(9 - number)
        ret += char
    return ret

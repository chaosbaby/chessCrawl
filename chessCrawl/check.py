import re


def GetValidDateList(strDate):
    if strDate is None:
        return []
    dateList = list(map(int, re.findall(r"\d+", strDate)))
    if len(dateList) == 0:
        return []
    while len(dateList) < 3:
        dateList.append(1)
    year = dateList[0]
    if year > 9999:
        dateList[0] = int(str(year)[:4])
    for i in range(0, len(dateList)):
        if dateList[i] == 0:
            dateList[i] = 1
    return dateList


def FindBWH(BWHStr, char):
    reStr = r"(?<=%s)(\d+)" % char
    pattern = re.compile(reStr)
    ret = pattern.findall(BWHStr)
    if ret is not None and len(ret) > 0:
        return ret[0]
    else:
        return None


def strNumberIsBigger(strA, strB):
    return changeStrToNumber(strA) > changeStrToNumber(strB)


def changeStrToNumber(strA):
    pureNumber = strA
    if strA[-1] == "万":
        pureNumber = strA[:-1]
        return float(pureNumber) * 10000
    else:
        return float(pureNumber)


def subNotWord(s):
    subs = re.sub(r"[^\w]", "", s)
    return subs


def isContentChinese(t):
    zhModel = re.compile("[\u4e00-\u9fa5]")  # 检查中文
    # zhModel = re.compile(u'[^\u4e00-\u9fa5]')   #检查非中文
    match = zhModel.search(t)
    if match:
        return True
    else:
        return False


def isContent(containStr, keyWord, ignoreCase=True):
    if ignoreCase is True:
        return containStr.lower().find(keyWord.lower()) >= 0
    else:
        return containStr.find(keyWord) >= 0


def getNumberOutStr(s):
    ret = re.findall(r"\d+", s)
    if ret is not None and len(ret) == 1:
        return ret[0]
    else:
        return None


VOLUME_DIC = {
    "k": 10**-3,
    "K": 10**-3,
    "m": 1,
    "M": 1,
    "g": 10**3,
    "G": 10**3,
}


def strVolumeToNumber(s):
    scale = "g"
    chars = re.findall(r"[gmkGMK]", s)
    if len(scale) > 0:
        scale = chars[0]
    number = 0
    numbers = re.findall(r"\d+\.?\d*", s)
    if len(numbers) > 0:
        number = float(numbers[0])
    return number * VOLUME_DIC[scale]


# def getDesignation(s):
#     # it = re.search(r"([A-Za-z]{3,5}[-]?[0-9]{3,4})[A-G]?\.(mp4|avi|wmv|mkv|m2ts|rm|rmvb)$", s)
#     it = re.search(r"([A-Za-z0-9]{2,6}[-]?[0-9]{3,4})[A-G]?", s)
#     dis = None
#     if it:
#         dis = it.group(1)
#     else:
#         return
#     joinerPos = dis.find('-')
#     if joinerPos > 0:
#         pass
#     else:
#         m = next(re.finditer(r"[0-9]+", dis))
#         disPos = m.start()
#         dis = (dis[:disPos] + '-' + dis[disPos:])
#     return dis.upper()


def getDesignation(s):
    # it = re.search(r"([A-Za-z]{3,5}[-]?[0-9]{3,4})[A-G]?\.(mp4|avi|wmv|mkv|m2ts|rm|rmvb)$", s)
    # retList = re.findall(r"([A-Za-z0-9]{2,6}[-]?[0-9]{3,4})[A-G]?", s)
    # retList = re.findall(r"([A-Za-z]{2,5}|[0-9]{6})([-]?[0-9]{3,4})[A-G]?", s)
    retList = re.findall(r"[^A-Za-z]([A-Za-z]{2,6}[-]?|[0-9]{6}-)([0-9]{3,4})[A-G]?", s)
    if retList:
        retList = ["".join(x) for x in retList]
    retDesList = []
    if retList:
        for possibleDes in retList:
            des = possibleDes.upper()
            joinerPos = des.find("-")
            if joinerPos > 0:
                pass
            elif des.isnumeric():
                continue
            elif des.isalnum():
                m = next(re.finditer(r"[0-9]+", des))
                desPos = m.start()
                des = des[:desPos] + "-" + des[desPos:]
            retDesList.append(des)
    return list(set(retDesList))

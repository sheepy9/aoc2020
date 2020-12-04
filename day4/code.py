import re

def checkbyr(val):
    if type(re.search("^[0-9]{4}$",val)) == type(None):
        return False
    if int(val) < 1920 or int(val) > 2002:
        return False
    return True

def checkiyr(val):
    if type(re.search("^[0-9]{4}$",val)) == type(None):
        return False
    if int(val)<2010 or int(val) > 2020:
        return False
    return True

def checkeyr(val):
    if type(re.search("^[0-9]{4}$",val)) == type(None):
        return False
    if int(val) < 2020 or int(val) > 2030:
        return False
    return True

def checkhgt(val):
    if type(re.search("^[0-9]+cm",val)) == type(None) and \
        type(re.search("^[0-9]+in",val)) == type(None):
        return False

    if type(re.search("^[0-9]+cm",val)) != type(None):
        hgt = int(val.split("cm")[0])
        if hgt < 150 or hgt > 193:
            return False

    if type(re.search("^[0-9]+in",val)) != type(None):
        hgt = int(val.split("in")[0])
        if hgt < 59 or hgt > 76:
            return False
    return True

def checkhcl(val):
    if type(re.search("^#[0-9a-f]{6}$",val)) == type(None):
        return False
    return True

def checkecl(val):
    colorSet = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if not val in colorSet:
        return False
    return True

def checkpid(val):
    if type(re.search("^[0-9]{9}$",val)) == type(None):
        return False
    return True

def checkcid(val):
    return True

f = open("passports")
passports = f.read().split("\n\n")

validatePass = {"byr":checkbyr,"iyr":checkiyr, "eyr":checkeyr, 
                "hgt":checkhgt, "hcl":checkhcl, "ecl":checkecl, 
                "pid":checkpid, "cid":checkcid}

cnt = 0;
for passport in passports:
    dataList = re.split("[ \n]", passport)
    if dataList[-1] == "":
        dataList.pop()

    if len(dataList) < 7 or (len(dataList) == 7 and passport.find("cid") != -1):
        continue

    passValid = True
    for data in dataList:
        keyValue = data.split(":")
        if(not validatePass[keyValue[0]](keyValue[1])):
            passValid = False
            break
    
    if passValid:
        cnt = cnt + 1

print(cnt)

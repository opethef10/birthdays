from datetime import date, timedelta
BUGÜN = date.today()

def doğumGünleri(dic):
    result = ""
    for kişi, doğumGünü in dic.items():
        günler = (BUGÜN-doğumGünü).days
        yaş = age(doğumGünü)
        result += f"{kişi:<10} {doğumGünü:%d/%m/%Y %a} {günler:>6} days {yaş:>6.2f} years\n"
    return result

def onBin(dic,günler=10000):
    result = f"{günler} Days:\n"
    for kişi, doğumGünü in dic.items():
        onBin = doğumGünü + timedelta(günler)
        result += f"{kişi:<10} {onBin:%d %b %Y} in {(onBin-BUGÜN).days:>6} days\n"
    return result
    
def dateParser(dct):
    for k, v in dct.items():
        dct[k] = date.fromisoformat(v)
    return dct

def dayofyear(tarih):
    return (tarih - date(tarih.year, 1, 1) + timedelta(1)).days

def _dayofyear2(tarih):
    equinox = date(tarih.year, 3, 21)
    if tarih < equinox:
        equinox = date(tarih.year - 1, 3, 21)
    return (tarih - equinox + timedelta(1)).days

def fixedCal(tarih):
    aylar = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", 
             "Sol", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    if tarih.month==2 and tarih.day==29:
        return "29 Sol"
    if tarih.month==12 and tarih.day==31:
        return "29 Dec"
    
    yıl = tarih.year
    ay, gün = divmod(dayofyear(tarih), 28)
    if yıl%4==0 and tarih >= date(yıl, 3, 1):
        gün -= 1
    if gün <= 0:
        ay -= 1
        gün += 28
    return f"{gün} {aylar[ay]} {yıl}"

def _fixedCal2(tarih):
    aylar = "ABCDEFGHIJKLM"
    ay, gün = divmod(_dayofyear2(tarih), 28)
    return f"{gün}/{ay+1}{aylar[ay]}"

def march21(tarih):
    aralıklar = 31, 30, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30
    gün = _dayofyear2(tarih)
    yıl = tarih.year
    if tarih < date(yıl, 3, 21):
        yıl-=1
    
    for ay, aralık in enumerate(aralıklar, 1):
        if gün > aralık:
            gün -= aralık
        else:
            return f"{gün:02}/{ay:02}/{yıl}"

def age(birth):
    bday = birth.replace(year = BUGÜN.year) 
    return BUGÜN.year - birth.year + ((BUGÜN - bday) / timedelta(365))
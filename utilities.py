from datetime import date, timedelta

march21Margins = 31, 30, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30
fixedMonths = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Sol", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
)

def doğumGünleri(kişi, doğumGünü, today):
    günler = (today - doğumGünü).days
    hafta = günler // 7
    yaş = age(doğumGünü, today)
    return f"{kişi:<10} {doğumGünü:%d/%m/%Y %a} {günler:>6} days {hafta:>5} weeks {yaş:>6.2f} years"

def onBin(kişi, doğumGünü, today, günler = 10000):
    onBin = doğumGünü + timedelta(günler)
    return f"{kişi:<10} {onBin:%d %b %Y} in {(onBin-today).days:>6} days"

def dateParser(dct):
    for k, v in dct.items():
        dct[k] = date.fromisoformat(v)
    return dct
    
###########################
    
def age(birth, today):
    bday = birth.replace(year = today.year) 
    return today.year - birth.year + ((today - bday) / timedelta(365))

def dayOfYear(tarih):
    return (tarih - date(tarih.year, 1, 1) + timedelta(1)).days

def dayOfYear21March(tarih):
    equinox = date(tarih.year, 3, 21)
    if tarih < equinox:
        equinox = date(tarih.year - 1, 3, 21)
    return (tarih - equinox + timedelta(1)).days

def fixedCal(tarih):
    if tarih.month==2 and tarih.day==29:
        return "29 Sol"
    
    if tarih.month==12 and tarih.day==31:
        return "29 Dec"
    
    yıl = tarih.year
    ay, gün = divmod(dayOfYear(tarih), 28)
    if yıl%4==0 and tarih >= date(yıl, 3, 1):
        gün -= 1
    
    if gün <= 0:
        ay -= 1
        gün += 28
    
    return f"{gün} {fixedMonths[ay]} {yıl}"

def march21(tarih):
    d = dayOfYear21March(tarih)
    y = tarih.year
    if tarih < date(y, 3, 21):
        y -= 1
    
    for m, margin in enumerate(march21Margins, 1):
        if d > margin:
            d -= margin
        else:
            return f"{d:02}/{m:02}/{y}"

"""Some utility functions that are useful to make date and calendar calculations"""
from datetime import date, timedelta

MARCH_21_MARGINS = 31, 30, 31, 31, 31, 31, 30, 30, 30, 30, 30, 30
FIXED_MONTHS = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
    "Sol", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
)

def doğumGünleri(name: str, birthdate: date, today: date) -> str:
    days: int = (today - birthdate).days
    weeks: int = days // 7
    current_age: float = _age(birthdate, today)
    return f"{name:<10} {birthdate:%d/%m/%Y %a} {days:>6} days {weeks:>5} weeks {current_age:>6.2f} years"

def onBin(name: str, birthdate: date, today: date, milestone: int = 10000) -> str:
    tenThousandthDay: date = birthdate + timedelta(milestone)
    daysUntilTenThousandth: timedelta = tenThousandthDay-today
    return f"{name:<10} {tenThousandthDay:%d %b %Y} in {daysUntilTenThousandth.days:>6} days"

def dateParser(json_data: dict[str, str]) -> dict[str, date]:
    return {k: date.fromisoformat(v) for k, v in json_data.items()}
    
###########################
    
def _age(birthdate: date, today: date) -> float:
    """Calculate the age of someone with floating point precision"""
    birthday: date = birthdate.replace(year = today.year)
    return today.year - birthdate.year + ((today - birthday) / timedelta(days=365))

def dayOfYear(today: date) -> int:
    """Return which day of the year today's date is"""
    firstDayOfYear: date = date(today.year, 1, 1)
    return (today - firstDayOfYear + timedelta(1)).days

def _dayOfYear21March(today: date) -> int:
    """Return which day of the year today's date is relative to March 21"""
    equinox: date = date(today.year, 3, 21)
    if today < equinox:
        equinox = equinox.replace(year=today.year - 1)
    return (today - equinox + timedelta(days=1)).days

def fixedCal(today: date) -> str:
    """Get International Fixed Calendar representation of the given date"""
    year: int = today.year
    if today.month==2 and today.day==29:
        return f"29 Sol {year}"
    
    if today.month==12 and today.day==31:
        return f"29 Dec {year}"
    
    month, day = divmod(dayOfYear(today), 28)
    march1: date = date(year, 3, 1)
    
    if year % 4 == 0 and today >= march1:
        # Leap year edge case
        day -= 1
    
    if day <= 0:
        # In case the divmod or leap year calculation result makes the day 0 or less
        month -= 1
        day += 28

    return f"{day} {FIXED_MONTHS[month]} {year}"

def march21(today: date) -> str:
    """Get the date representation of the calendar that starts with March 21"""
    day: int = _dayOfYear21March(today)
    year: int = today.year
    equinox: date = date(year, 3, 21)
    if today < equinox:
        year -= 1
    
    for month, margin in enumerate(MARCH_21_MARGINS, 1):
        if day > margin:
            day -= margin
        else:
            return f"{day:02}/{month:02}/{year}"


import json
from pathlib import Path
from datetime import date
from utilities import dateParser, dayOfYear, fixedCal, march21, doğumGünleri, onBin

BUGÜN = date.today()
JSON_PATH = Path(__file__).parent / "birthdays.json"
with JSON_PATH.open(encoding="utf-8") as jsonFile:
    birthdays = json.load(jsonFile, object_hook = dateParser)

print(f"Today: {BUGÜN:%d/%m/%Y %A} - Day {dayOfYear(BUGÜN)} of year")
print(f"{BUGÜN.year} Doomsday: {date(BUGÜN.year,10,31):%A}")
print(f"Fixed Calendar: {fixedCal(BUGÜN)}")
print(f"March 21 Calendar: {march21(BUGÜN)}")
print()
for kişi, doğumGünü in birthdays.items():
    print(doğumGünleri(kişi, doğumGünü, BUGÜN))
print() 
print("10000 Days:") 
for kişi, doğumGünü in birthdays.items():
    print(onBin(kişi, doğumGünü, BUGÜN))

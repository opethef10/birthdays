#! python -i -B
import json
from pathlib import Path
from datetime import date
from utilities import dateParser, dayofyear, fixedCal, march21, doğumGünleri, onBin

#comment again

BUGÜN = date.today()
JSON_PATH = Path(__file__).parent / "birthdays.json"
with JSON_PATH.open(encoding="utf-8") as jsonFile:
    birthdays = json.load(jsonFile, object_hook=dateParser)

print(f"Today: {BUGÜN:%d/%m/%Y %A} - Day {dayofyear(BUGÜN)} of year")
print(f"{BUGÜN.year} Doomsday: {date(BUGÜN.year,10,31):%A}")
print(f"Fixed Calendar: {fixedCal(BUGÜN)}")
print(f"March 21 Calendar: {march21(BUGÜN)}")
print()
print(doğumGünleri(birthdays))
print(onBin(birthdays))

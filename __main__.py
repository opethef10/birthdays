#! /usr/bin/env python3
"""
This program takes a JSON input of name-birthdate pairs and gives information
about how many days, week and years old. Additionally it gives an information
about how many days these people are close to their 10000th day in their lives.
"""

# Standard library imports
import argparse
from datetime import date
import json
from pathlib import Path

# Local imports
from utilities import dateParser, dayOfYear, fixedCal, march21, doğumGünleri, onBin

TODAY = date.today()
MAIN_DIRECTORY = Path(__file__).parent
DEFAULT_JSON_FILE_NAME = "birthdays.json"


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Display birthday information of the people"
    )
    parser.add_argument(
        "-t",
        "--tenThousand",
        action="store_true",
        help="Display 10000th day data of the players",
    )
    parser.add_argument(
        "-f", "--file", type=str, help="Path of JSON file with birthday data"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    # Use the specified file if provided
    # Otherwise fallback to the default path
    file_name = args.file if args.file else DEFAULT_JSON_FILE_NAME
    json_path = MAIN_DIRECTORY / file_name
    if not json_path.exists():
        if args.file:
            raise SystemExit(
                f"FileNotFoundError: No such file or directory: '{json_path}'"
            )
        raise SystemExit(
            f"FileNotFoundError: No such file or directory: '{json_path}'\n"
            f"Either add a file named '{DEFAULT_JSON_FILE_NAME}'"
            f"(preferably copying from '{DEFAULT_JSON_FILE_NAME}.example')"
            f"or enter a valid path using the -f command line option."
        )
    with json_path.open(encoding="utf-8") as jsonFile:
        birthdays = json.load(jsonFile, object_hook=dateParser)

    print(f"Today: {TODAY:%d/%m/%Y %A} - Day {dayOfYear(TODAY)} of year")
    print(f"{TODAY.year} Doomsday: {date(TODAY.year, 10, 31):%A}")
    print(f"Fixed Calendar: {fixedCal(TODAY)}")
    print(f"March 21 Calendar: {march21(TODAY)}")
    print()
    for person, birthdate in birthdays.items():
        print(doğumGünleri(person, birthdate, TODAY))

    if args.tenThousand:
        print()
        print("10000 Days:")
        for person, birthdate in birthdays.items():
            print(onBin(person, birthdate, TODAY))

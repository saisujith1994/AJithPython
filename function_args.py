import csv
import re
from datetime import datetime

input_file = "students_dataset.csv"
output_file = "students_cleaned.csv"

missing_values = ["", "NULL", "NaN", "???", "@@@"]

cleaned_rows = []
seen = set()

print("Ready to start!!!")

# function to replace the missing values with None
def clean_missing(row):
    for key, value in row.items():
        if value in missing_values:
            row[key] = None
def parse_date(date_str):
    if not date_str:
        return None
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%d %b %Y",
        "%b-%Y",
        "%m/%Y",
        "%Y/%m/%d"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue

    return None

def clean_month(month):
    if month is None:
        return None

    month_map = {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    if isinstance(month, str):
        month = month.strip()

    if month and month.isdigit():
        return str(int(month))

    return month_map.get(month)
def name_clean(row,column):
    first_name = row.get(column)
    if first_name and not re.match(r"^[A-Za-z]+$", first_name):
        return None
    else:
        return first_name
def numbers_clean(row,column):
    value= row.get(column)
    if value and not re.match(r"^[0-9]+$", value):
        return None
    else:
        return value
#lets open the file
with open(input_file) as csvfile:
    reader = csv.DictReader(csvfile)
    columns = reader.fieldnames
    print(columns)
    for i in reader:
        clean_missing(i)
        i["date_of_birth"] = parse_date(i["date_of_birth"])
        i["class_ending_month"]=clean_month(i["class_ending_month"])
        i["first_name"]=name_clean(i,"first_name")
        i["last_name"]=name_clean(i,"last_name")
        i["class_ending_year"]=numbers_clean(i,"class_ending_year")
        print(i)

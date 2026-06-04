import csv
import re
from datetime import datetime

input_file = "students_dataset.csv"
output_file = "students_cleaned.csv"

missing_values = {"", "NULL", "NaN", "???", "@@@"}

cleaned_rows = []
seen = set()

# # =========================
# # 4. MONTH CLEANING
# # =========================
# def clean_month(month):
#     if month is None:
#         return None
#
#     month_map = {
#         "January": "1",
#         "February": "2",
#         "March": "3",
#         "April": "4",
#         "May": "5",
#         "June": "6",
#         "July": "7",
#         "August": "8",
#         "September": "9",
#         "October": "10",
#         "November": "11",
#         "December": "12"
#     }
#
#     if isinstance(month, str):
#         month = month.strip()
#
#     if month and month.isdigit():
#         return str(int(month))
#
#     return month_map.get(month)
#

# =========================
# MAIN PIPELINE
# =========================
with open(input_file, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # STEP 1: clean all fields
        row = clean_row(row)

        #
        # # STEP 4: validate first name
        # first_name = row.get("first_name")
        # if first_name and not re.match(r"^[A-Za-z]+$", first_name):
        #     row["first_name"] = None
        #
        # # STEP 5: deduplication
        # row_key = tuple(sorted(row.items()))
        # if row_key in seen:
        #     continue
        #
        # seen.add(row_key)
        # cleaned_rows.append(row)


# =========================
# SAFETY CHECK
# =========================
if not cleaned_rows:
    print("No valid data after cleaning.")
    exit()


# =========================
# WRITE OUTPUT
# =========================
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=cleaned_rows[0].keys())
    writer.writeheader()
    writer.writerows(cleaned_rows)


print("Done")
print("rows:", len(cleaned_rows))
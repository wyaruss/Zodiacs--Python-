from calendar import month
from tokenize import String

month = 0
day = 0
sign = "null"

month = int(input("Enter the month of your birth: "))
while  month < 1 or month > 12: 
    month = int(input("Enter the month of your birth: "))

if month == 1: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 19: 
        sign = "Capricorn, the Goat"
    if day >= 20: 
        sign = "Aquarius, the Water Bearer"

if month == 2: 
    day = int(input("Enter the day of your birth (1 - 29): "))
    while day < 1 or day > 29:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 29): "))
    if day <= 18: 
        sign = "Aquarius, the Water Bearer"
    if day >= 19: 
        sign = "Pisces, the Fishes"

if month == 3: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 20: 
        sign = "Pisces, the Fishes"
    if day >= 21: 
        sign = "Aries, the Ram"

if month == 4: 
    day = int(input("Enter the day of your birth (1 - 30): "))
    while day < 1 or day > 30:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 30): "))
    if day <= 19: 
        sign = "Aries, the Ram"
    if day >= 20: 
        sign = "Taurus, the Bull"

if month == 5: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 20: 
        sign = "Taurus, the Bull"
    if day >= 21: 
        sign = "Gemini, the Twins"

if month == 6: 
    day = int(input("Enter the day of your birth (1 - 30): "))
    while day < 1 or day > 30:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 30): "))
    if day <= 21: 
        sign = "Gemini, the Twins"
    if day >= 22: 
        sign = "Cancer, the Crab"

if month == 7: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 22: 
        sign = "Cancer, the Crab"
    if day >= 23: 
        sign = "Leo, the Lion"

if month == 8: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 22: 
        sign = "Leo, the Lion"
    if day >= 23: 
        sign = "Virgo, the Virgin"

if month == 9: 
    day = int(input("Enter the day of your birth (1 - 30): "))
    while day < 1 or day > 30:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 30): "))
    if day <= 22: 
        sign = "Virgo, the Virgin"
    if day >= 23: 
        sign = "Libra, the Balance"

if month == 10: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 23: 
        sign = "Libra, the Balance"
    if day >= 24: 
        sign = "Scorpio, the Scorpion"

if month == 11: 
    day = int(input("Enter the day of your birth (1 - 30): "))
    while day < 1 or day > 30:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 30): "))
    if day <= 22: 
        sign = "Scorpio, the Scorpion"
    if day >= 23: 
        sign = "Saggitarius, the Archer"

if month == 12: 
    day = int(input("Enter the day of your birth (1 - 31): "))
    while day < 1 or day > 31:
        print("That's not a valid day for this month.")
        day = int(input("Enter the day of your birth (1 - 31): "))
    if day <= 21: 
        sign = "Saggitarius, the Archer"
    if day >= 22: 
        sign = "Capricorn, the Goat"

print("Your sign is", sign, "!")
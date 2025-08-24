months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

"""
05/27/2004
May 27, 2004
"""

prompt = input()

if len(prompt.split("/")) == 3:
    month, day, year = prompt.split("/")
    
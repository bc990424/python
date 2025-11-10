import re

par = re.compile(r"\d{2}/[a-zA-Z]{3}/\d{4}")

korMonth = {
    "JAN": "1", "FEB": "2", "MAR": "3", "APR": "4", "MAY": "5", "JUN": "6",
    "JUL": "7", "AUG": "8", "SEP": "9", "OCT": "10", "NOV": "11", "DEC": "12"
}

temp = input("Enter a date (e.g., 12/Jan/2024): ")
pos = par.search(temp)
print(pos)
date = pos.group().split("/")

result = temp[:pos.start() ] +date[2] +"년" +korMonth[date[1].upper()] + "월" + date[0] + "일" + temp[pos.end():]
print(result)

class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(" ")
        monthConverter = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        month_converted = monthConverter[month]
        if len(day) == 4:
            day_converted = day[:2]
        else:
            day_converted = "0" + day[0]
        return year + "-" + month_converted + "-" + day_converted
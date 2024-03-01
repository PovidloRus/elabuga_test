from dataclasses import dataclass


class Date:

    def __init__(self, year: int, month: int, day: int, hour: int, minutes: int, sec: int):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minutes = minutes
        self.sec = sec


class Calc():
    days_in_mont = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def calc_years_difference(self, date1, date2):
        if date2.year != date1.year:
            return date2.year * 365 - date1.year * 365
        else:
            return 0

    def calc_months_difference(self, date1, date2):
        days_count = 0
        if date2.month == date1.month:
            days_count = date2.day - date1.day
        elif date2.month > date1.month:
            days_count += self.days_in_mont[date1.month] - date1.day
            for i in range(date1.month + 1, date2.month):
                days_count += self.days_in_mont[i]
            days_count += date2.day
        elif date2.month < date1.month:
            days_count += self.days_in_mont[date1.month] - date1.day
            for i in range(date1.month + 1, 12 + 1):
                days_count += self.days_in_mont[i]
            for i in range(1, date2.month):
                days_count += self.days_in_mont[i]
            days_count += date2.day

        return days_count - 1

    def calc_hourse_second_difference(self, date1: Date, date2: Date) -> int:
        if date2.day == date1.day and date2.month == date1.month and date2.year == date1.year:
            seconds = (date2.hour - date1.hour) * 60 * 60 + ((59 - date1.minutes) + date2.minutes) * 60 + (
                    59 - date1.sec + date2.sec)
        else:
            seconds = (23 - date1.hour + date2.hour) * 60 * 60 + (
                    59 - date1.minutes + date2.minutes) * 60 + (59 - date1.sec + date2.sec)
        return seconds + 1

    def start(self, date1, date2):
        a = self.calc_years_difference(date1, date2)
        b = self.calc_months_difference(date1, date2)
        seconds = self.calc_hourse_second_difference(date1, date2)
        days = a + b
        if seconds > 24 * 60 * 60:
            days = days + 1
            seconds = seconds - 24 * 60 * 60
        return days, seconds


# date1 = Date(1001, 5, 20, 14, 15, 16)
# date2 = Date(9009, 9, 11, 12, 21, 11)
# date3 = Date(980, 2, 12, 10, 30, 1)
# date4 = Date(980, 3, 1, 10, 31, 37)

if __name__ == '__main__':
    date1_input = str(input()).split()
    date2_input = str(input()).split()
    date1_input = list(map(int, date1_input))
    date2_input = list(map(int, date2_input))
    date1 = Date(date1_input[0], date1_input[1], date1_input[2], date1_input[3], date1_input[4], date1_input[5])
    date2 = Date(date2_input[0], date2_input[1], date2_input[2], date2_input[3], date2_input[4], date2_input[5])
    calc = Calc()
    days, seconds = calc.start(date1,date2)
    print(days, seconds)
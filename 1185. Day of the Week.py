class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isleap(year: int) -> bool:
            if year % 4 == 0:
                if year % 100 == 0:
                    return year % 400 == 0
                return True
            return False

        dayNames = ['Saturday', 'Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        # from Jan to Dec
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # days since 1/1/1971, which is a Friday
        def daySinceStart(day: int, month: int, year: int) -> int:
            numDays = 0
            for y in range(1971, year):
                numDays += 366 if isleap(y) else 365
            for mon in range(1, month):
                numDays += daysInMonth[mon - 1]
                # check leap year, then Feb has 29 days
                if (month == 2 and isleap(year)):
                    numDays += 1
            numDays += day
            print(f'Number of days: {numDays}')
            return numDays


        num_days_from_start = daySinceStart(day, month, year)

        return dayNames[(num_days_from_start + 5)%7]


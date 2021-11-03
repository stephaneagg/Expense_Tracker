class Date:

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __str__ (self):
        return self.toString()

    def __repr__(self):
        result = ""
        result += self.month
        result += self.day
        result += self.year
        return result

    def __eq__(self, other):
        if (self.month == other.get_month()
        and self.day == other.get_day()
        and self.year == other.get_year()):
            return True
        else:
            return False

    def get_month():
        return self.month

    def set_month(month):
        self.month = month

    def get_day():
        return self.day

    def set_day(day):
        self.day = day

    def get_year():
        return self.year

    def set_year(year):
        self.year = year

    def toString(self):
        if (self.month == "01"):
            result = "January "
        if (self.month == "02"):
            result = "February "
        if (self.month == "03"):
            result = "March "
        if (self.month == "04"):
            result = "April "
        if (self.month == "05"):
            result = "May "
        if (self.month == "06"):
            result = "June "
        if (self.month == "07"):
            result = "July "
        if (self.month == "08"):
            result = "August "
        if (self.month == "09"):
            result = "September "
        if (self.month == "10"):
            result = "October "
        if (self.month == "11"):
            result = "November "
        if (self.month == "12"):
            result = "December "
        result += self.day + " " + self.year
        return result

    def isBefore(self, other):
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return False
                if self.day > other.day:
                    return False
                if self.day < other.day:
                    return True
            if self.month > other.month:
                return False
            if self.month < other.month:
                return True
        if self.year > other.year:
            return False
        if self.year < other.year:
            return True

    def isValid(self):
        try:
            if (int(self.month) > 12 or int(self.month) < 0):
                return False
            if (int(self.day) > 31 or int(self.month) < 0):
                return False
            int(self.year)
        except ValueError:
            return False
        return True

import datetime
class Student:
    name = ""
    year = 2000
    group = 1
    average_mark = 11
    def __init__(self, name = "", year = 2000, group = 1, average_mark = 11):
        self.name = name
        self.year = year
        self.group = group
        self.average_mark = average_mark
    def __str__(self):
        return f"-[{self.name}]-\n" \
               f"Year -> {self.year}\n" \
               f"Group -> {self.group}\n" \
               f"Average Mark -> {self.average_mark}\n" \
               f"{self.get_age()}\n"


    def get_age(self):
        return f"Age -> {datetime.date.today().year - self.year}"

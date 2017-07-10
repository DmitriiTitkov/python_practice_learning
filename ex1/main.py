from datetime import datetime
from dateutil.relativedelta import relativedelta


class User:
    def __init__(self, name="", age=None, had_birthday_this_year=None):
        if name != "" :
            self.name = name
        else :
            self.set_name()

        if age is not None:
            self.age = age
        else:
            self.set_age()

        if had_birthday_this_year is not None:
            self.had_birthday_this_year = had_birthday_this_year
        else:
            self._set_birthday_this_year()

    def _set_birthday_this_year(self):
        answer = input("Did you have a birthday this year? [Y/N]:")
        if answer == "Y" :
            self.had_birthday_this_year = True
        elif answer == "N":
            self.had_birthday_this_year = False
        else:
            raise Exception("The input data is not in correct format")

    def set_age(self):
        age = input("How old are you: ")
        if int(age):
            self.age = int(age)
        else:
            return False

    def set_name(self):
        name = input("What's you name: ")
        self.name = str(name)

    def year_calc(self):
        if isinstance(self.age, int):
            today = datetime.now()
            if self.had_birthday_this_year is True:
                current_year_birthday = 0
            else:
                current_year_birthday = 1
            calculated_year = (today + relativedelta(years=(100 - self.age - current_year_birthday))).year
            return calculated_year

        else:
            raise Exception("Age is not in correct format")


user = User()
print("In {} you will be 100 years".format(user.year_calc()))

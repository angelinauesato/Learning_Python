from datetime import date
# pytest -v


class Employee:

    def __init__(self, name, dbirth, salary):
        self._name = name
        self._dbirth = dbirth
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        split_year_dbith = self._dbirth.split('/')[-1]
        current_year = date.today().year
        return current_year - int(split_year_dbith)

    def last_name(self):
        full_name = self._name.strip()
        last_name = full_name.split(' ')
        return last_name[-1]

    def _check_director(self):
        last_names = ['Braga', 'Windsor', 'Bourbon', 'Yamato', 'Higa', 'Tudor', 'Stark']
        return self._salary >= 100000 and (self.last_name() in last_names)

    def decrease_salary(self):
        if self._check_director():
            decrease = self._salary * 0.1
            self._salary -= decrease

    def calc_bonus(self):
        amount = self._salary * 0.1
        if amount > 1000:
            raise Exception('Salary is too high to receive a bonus.')
        return amount

    def __str__(self):
        return f'Employee({self._name}, {self._dbirth}, {self._salary})'

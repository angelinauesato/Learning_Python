class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def format_dada(self):
        print(f"{self.day}/{self.month}/{self.year}")

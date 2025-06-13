from datetime import datetime

class Transaction:
    def __init__(self, t_type, category, amount, date):
        self.type = t_type
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.type},{self.category},{self.amount},{self.date.strftime('%Y-%m-%d')}"

    @staticmethod
    def from_string(line):
        t_type, category, amount, date_str = line.strip().split(",")
        return Transaction(t_type, category, float(amount), datetime.strptime(date_str, '%Y-%m-%d').date())
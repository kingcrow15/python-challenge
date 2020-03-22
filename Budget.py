import os
import csv
from datetime import datetime
from dateutil import relativedelta
from collections import defaultdict

file_path = os.path.join(os.path.expanduser("~"), "Documents", "GitHub", "python-challenge", "budget_data_copy.csv")


def get_date(date):
    try:
        return datetime.strptime(date, '%b-%y')  # https://stackabuse.com/converting-strings-to-datetime-in-python/
    except ValueError:
        pass


def get_budget_stats(file_path):
    with open(file_path) as csvfile:
        rows = csv.reader(csvfile)
        total = 0
        first_date = None
        last_date = None
        count = 0
        largest_increase = 0
        increase_date = None
        largest_decrease = 0
        decrease_date = None
        current_value = None
        last_value = None

        for row in rows:
            if not first_date:
                first_date = get_date(row[0])
            last_date = get_date(row[0])
            try:
                last_value = current_value
                current_value = int(row[1])
                if last_value:
                    difference = current_value - last_value
                    if difference > largest_increase:
                        largest_increase = difference
                        increase_date = row[0]
                    if difference < largest_decrease:
                        largest_decrease = difference
                        decrease_date = row[0]
                total += int(current_value)
                count += 1
            except ValueError:
                pass

        print("profit/loss total is ... " + str(total))
        print("First date: {}".format(first_date))
        print("Last date: {}".format(last_date))
        print(last_date - first_date)
        difference = relativedelta.relativedelta(last_date, first_date)
        months = 12 * difference.years + difference.months
        print("Number of months: {}".format(months))
        print("Average profit/loss: {}".format(total / count))
        print("Largest increase was {} on {}".format(largest_increase, increase_date))
        print("Largest decrease was {} on {}".format(largest_decrease, decrease_date))

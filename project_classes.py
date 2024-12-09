import csv
from tabulate import tabulate


class HorizontalTable:
    def __init__(self, csv_file):
        self.csv_file = csv_file


    def csv_to_list(self):
        script = []
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                script.append(row)
        return script


    def save_csv(self, script):
        with open(self.csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(script)


    def add_column(self):
        script = self.csv_to_list()
        col_name = input("Insert new column's name: ")
        col_index = len(script[0]) -1

        script[0].insert(col_index, col_name)
        for line in script[1:]:
            line.insert(col_index, "0")

        self.save_csv(script)
        print("")
        print("\033[33mColumn added!\033[0m")
        print("")


    def del_column(self):
        script = self.csv_to_list()
        col_name = input("Name of the column to delete: ")
        if col_name in script[0]:
            col_index = script[0].index(col_name)
            for col in script:
                col.pop(col_index)
            self.save_csv(script)
            print("")
            print("\033[33mColumn deleted!\033[0m")
            print("")
        else:
            print("The column doesn't exist")


    def insert_payment(self):
        month = (((input("Select month: ")).lower()).capitalize())[:3]
        acc = ((input("Account: ")).lower()).capitalize()
        value = input("Value: ")
        script = self.csv_to_list()
        acc_index = script[0].index(acc)

        for line in script:
            if line[0] == month:
                line[acc_index] = value
        self.save_csv(script)
        print("")
        print("\033[33mValue modified!\033[0m")
        print("")


    def print_csv(self):
        print(tabulate(self.csv_to_list(), headers='firstrow', tablefmt="github"))


    def total_sum(self):
        script = self.csv_to_list()
        row_length = len(script[0])
        for line in script[1:]:
            line[row_length - 1] = sum(float(value) for value in line[1:(row_length - 1)])
        self.save_csv(script)


    def month_total(self):
        script = self.csv_to_list()
        month = (((input("Select month: ")).lower()).capitalize())[:3]
        for line in script:
            if line[0] == month:
                total_paid = line[(len(line)) - 1]
                print("")
                print(f"\033[32mTotal in {month}: {total_paid}\033[0m")


class VerticalTable:
    def __init__(self, csv_file):
        self.csv_file = csv_file


    def csv_to_list(self):
        script = []
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                script.append(row)
        return script

    def print_csv(self):
        print(tabulate(self.csv_to_list(), headers='firstrow', tablefmt="github"))


    def save_csv(self, script):
        with open(self.csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(script)

    def new_row(self):
        script = self.csv_to_list()
        line = script[-2]
        line_2 = script[-3]
        x = any(n != '0.0' for n in line[1:])
        if x is True:
            new_row = [(int(line_2[0]) + 2),'0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0']
            script.insert(-1, new_row)
            self.save_csv(script)
        else:
            pass


    def insert_value(self):

        def val_month():
            while True:
                month = (((input("Select month: ")).lower()).capitalize())[:3]
                if month in script[0]:
                    return month
                else:
                    print("")
                    print("\033[31mInvalid month, try again!\033[0m")
                    print("")
                    pass


        def val_value():
            while True:
                try:
                    value = float(input("Value: "))
                    return value
                except ValueError:
                    print("")
                    print("\033[31mValue must be a number, try again!\033[0m")
                    print("")
                    pass


        script = self.csv_to_list()
        month = val_month()
        if month:
                value = val_value()
        if month in script[0]:
            month_index = (script[0]).index(month)
        for line in script[1:-1]:
            if line[month_index] == "0.0":
                line[month_index] = value
                break
        self.save_csv(script)


    def sum_total(self):
        script = self.csv_to_list()
        script_2 = script[1:-1]
        total_row = script[len(script) - 1]
        col_qty = len(script[0]) - 1
        total_values = [0.0] * col_qty
        for line in script_2:
            for month_index, value in enumerate(line[1:], start=1):
                total_values[month_index - 1] += float(value)
        total_row[1:] = total_values
        self.save_csv(script)


    def month_total(self):
        script = self.csv_to_list()
        month = (((input("Select month: ")).lower()).capitalize())[:3]
        month_index = 0
        for line in script[0]:
            month_index += 1
            if line == month:
                total_paid = (script[-1])[month_index - 1]
                print("")
                print(f"\033[32mTotal in {month}: {total_paid}\033[0m")


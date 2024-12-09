import cowsay
import csv
from project_classes import HorizontalTable, VerticalTable


def main():
     print("")
     print("\033[34m------------------------------------------\033[0m")
     print("\033[34m Welcome to your personal finance program \033[0m")
     print("\033[34m------------------------------------------\033[0m")

     while True:
            print("")
            print("\033[33m------------\033[0m")
            print("\033[33m Main menu: \033[0m")
            print("\033[33m------------\033[0m")
            print("")
            print("1) Home accounts")
            print("2) Incomes")
            print("3) Variable expenses")
            print("4) Monthly balance")
            print("5) Saving projection")
            print("0) Quit program")
            print("")
            option = input("Select an option: ")
            if option == "1":
                 home_accounts_menu()
            elif option == "2":
                 incomes_menu()
            elif option == "3":
                 var_exp_menu()
            elif option == "4":
                 month = (((input("Select month: ")).lower()).capitalize())[:3]
                 ha_script = csv_to_list("home_accounts.csv")
                 in_script = csv_to_list("incomes.csv")
                 ve_script = csv_to_list("var_expenses.csv")
                 ha_total = float(month_total(ha_script, month))
                 in_total = float(month_total(in_script, month))
                 ve_total = float(month_total2(ve_script, month))

                 print("")
                 print(f"\033[32m-------- Balance --------\033[0m")
                 print(f"\033[32mIncomes: {in_total}\033[0m")
                 print(f"\033[32mHome accounts: {ha_total}\033[0m")
                 print(f"\033[32mVariable expenses: {ve_total}\033[0m")
                 print(f"\033[32m-------------------------\033[0m")
                 bal = round(monthly_balance(in_total, ha_total, ve_total), 2)
                 print(f"\033[32mTotal: {bal}\033[0m")

                 ha_per, ve_per, sav_per = monthly_distribution(in_total, ha_total, ve_total)
                 print("")
                 print(f"\033[32mHome accounts represent {ha_per}%.\033[0m")
                 print(f"\033[32mVariable expenses represent {ve_per}%.\033[0m")
                 print("")
                 print(f"\033[32mTotal savings: {sav_per}%.\033[0m")
                 while True:
                    print("")
                    option = input("Insert 0 to go back to the main menu: ")
                    if option == "0":
                         break
                    else:
                         print("Invalid option")
                         pass

            elif option == "5":
                 month = (((input("Select month: ")).lower()).capitalize())[:3]
                 ha_script = csv_to_list("home_accounts.csv")
                 in_script = csv_to_list("incomes.csv")
                 ve_script = csv_to_list("var_expenses.csv")
                 ha_total = float(month_total(ha_script, month))
                 in_total = float(month_total(in_script, month))
                 ve_total = float(month_total2(ve_script, month))
                 bal = round(monthly_balance(in_total, ha_total, ve_total), 2)
                 mon_num = int(input("Number of months for projection: "))
                 amount = round((saving_projection(bal, mon_num)), 2)
                 print("")
                 print(f"\033[32mTotal saving in {mon_num} months: {amount}\033[0m")
                 while True:
                    print("")
                    option = input("Insert 0 to go back to the main menu: ")
                    if option == "0":
                         break
                    else:
                         print("Invalid option")
                         pass

            elif option == "0":
                 cowsay.cow("Goodbye!")
                 break
            else:
                 print("Invalid option")
                 pass

# ---------------------------------------------------------
def csv_to_list(csv_file):
        script = []
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                script.append(row)
        return script


def month_total(script, month):
        for line in script:
            if line[0] == month:
                total_paid = line[(len(line)) - 1]
                return total_paid


def month_total2(script, month):
        month_index = 0
        for line in script[0]:
            month_index += 1
            if line == month:
                total_paid = (script[-1])[month_index - 1]
                return total_paid


def monthly_balance(inc, ha, ve):
     bal = (inc - ha - ve)
     return bal


def monthly_distribution(inc, ha, ve):
     ha_per = round((float((ha * 100) / inc)), 2)
     ve_per = round((float((ve * 100) / inc)), 2)
     sav_per = round((float(100 - ha_per - ve_per)), 2)
     return (ha_per, ve_per, sav_per)


def saving_projection(bal, num):
     balance = bal
     return balance * num

# -------------- Main table menus -------------------------

def var_exp_menu():
     var_exp = VerticalTable("var_expenses.csv")
     print("--------------------")
     print("\033[34mVariable expenses\033[0m")
     print("")
     var_exp.sum_total()
     var_exp.print_csv()
     print("")
     print("Options: 1) Insert value 0) Main menu")
     print("")

     while True:
            option = input("Select an option: ")
            if option == "1":
                 var_exp.new_row()
                 var_exp.insert_value()
                 print("")
                 var_exp.sum_total()
                 var_exp.print_csv()
                 print("")
                 print("1) Insert value 0) Main menu")
                 print("")
            elif option == "0":
                 break
            else:
                 print("Invalid option")
                 pass


def incomes_menu():
     incomes = HorizontalTable("incomes.csv")
     print("--------------------")
     print("\033[34mIncomes\033[0m")
     print("")
     incomes.print_csv()
     print("")
     print("Options: 2) Insert/modify value 3) Add column 4) Delete column 0) Main menu")
     print("")

     while True:
            option = input("Select an option: ")
            if option == "2":
                 incomes.insert_payment()
                 incomes.total_sum()
                 incomes.print_csv()
                 print("Options: 2) Insert/modify value 3) Add column 4) Delete column 0) Main menu")
                 print("")
            elif option == "3":
                 incomes.add_column()
                 incomes.print_csv()
                 print("Options: 2) Insert/modify value 3) Add column 4) Delete column 0) Main menu")
                 print("")
            elif option == "4":
                 incomes.del_column()
                 incomes.total_sum()
                 incomes.print_csv()
                 print("Options: 2) Insert/modify value 3) Add column 4) Delete column 0) Main menu")
                 print("")
            elif option == "0":
                 break
            else:
                 print("Invalid option")
                 pass


def home_accounts_menu():
    home_acc = HorizontalTable("home_accounts.csv")
    home_acc.total_sum()

    print("--------------------")
    print("\033[34mHome accounts\033[0m")
    print("")
    home_acc.print_csv()
    print("")
    print("Options: 2) Insert/modify payment 3) Add column 4) Delete column 0) Main menu")
    print("")


    while True:
            option = input("Select an option: ")
            if option == "2":
                 home_acc.insert_payment()
                 home_acc.total_sum()
                 home_acc.print_csv()
            elif option == "3":
                 home_acc.add_column()
                 home_acc.print_csv()
                 print("Options: 2) Insert/modify payment 3) Add column 4) Delete column 0) Main menu")
                 print("")
            elif option == "4":
                 home_acc.del_column()
                 home_acc.total_sum()
                 home_acc.print_csv()
                 print("Options: 2) Insert/modify payment 3) Add column 4) Delete column 0) Main menu")
                 print("")
            elif option == "0":
                 break
            else:
                 print("\033[33m \033[0m")
                 print("\033[33mInvalid option, try again!\033[0m")
                 print("\033[33m \033[0m")
                 pass


if __name__ == "__main__":
    main()


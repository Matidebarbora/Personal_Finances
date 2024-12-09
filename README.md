# PERSONAL FINANCE PROGRAM

#### Video Demo:  <URL HERE>

#### Description:

The program’s primary goal is to help users calculate a monthly balance and manage related financial functions with ease.
To organize the data, the program uses three customizable tables: Incomes, Home Accounts, and Variable Expenses.

These tables are stored as CSV files, ensuring simplicity and portability.

With the exception of the menus, all the numbers that the user is able to use can be decimals.

### Main features:

The following menu will appear when the program starts and everytime the user quit a sub-menu.
To enter the sub-menus, the user should enter the corresponding number with the keyboard.

 Main menu:

1) Home accounts
2) Incomes
3) Variable expenses
4) Monthly balance
5) Saving projection
0) Quit program

If the number entered is not correct or even if it's not a number, the program prints "Invalid option" and asks for another try until it gets it correct.

### Option 1: Home Accounts Table

This section allows users to input and manage their **utility bill values**.
It also supports adding or removing accounts (located in columns) dynamically, with the total amounts displayed in the final column for quick reference.

| Month   |   Rent |   Electricity |   Water |   Phone |   Total |
|---------|--------|---------------|---------|---------|---------|
| Jan     | 678    |         23.67 |  100    |  100    |  901.67 |
| Feb     | 678    |         24    |    2.56 |   67    |  771.56 |
| Mar     | 701    |        400    |  150    |   56.98 | 1307.98 |
| Apr     | 699    |        100    |   34    |   12.67 |  845.67 |
| May     | 678    |         90    |   12    |   55    |  835    |
| Jun     | 710    |         30.28 |   60.13 |   10    |  810.41 |
| Jul     | 777    |         67    |  110    |    5    |  959    |
| Aug     | 650.65 |         67    |   75    |   14    |  806.65 |
| Sep     | 600    |         92    |   84.32 |   12    |  788.32 |
| Oct     | 700    |         65    |   68    |   98.23 |  931.23 |
| Nov     | 600    |         93    |   45    |   88    |  826    |
| Dec     | 500    |         92    |   78    |   45.7  |  715.7  |

Options: 2) Insert/modify payment 3) Add column 4) Delete column 0) Main menu

Following the given options, the user can modify the table.
All the new columns will be located automatically before the column "Total".

| Month   |   Rent |   Electricity |   Water |   Phone |   new_column |   Total |
|---------|--------|---------------|---------|---------|--------------|---------|
| Jan     | 678    |         23.67 |  100    |  100    |            0 |  901.67 |
| Feb     | 678    |         24    |    2.56 |   67    |            0 |  771.56 |
| Mar     | 701    |        400    |  150    |   56.98 |            0 | 1307.98 |
| Apr     | 699    |        100    |   34    |   12.67 |            0 |  845.67 |
| May     | 678    |         90    |   12    |   55    |            0 |  835    |
| Jun     | 710    |         30.28 |   60.13 |   10    |            0 |  810.41 |
| Jul     | 777    |         67    |  110    |    5    |            0 |  959    |
| Aug     | 650.65 |         67    |   75    |   14    |            0 |  806.65 |
| Sep     | 600    |         92    |   84.32 |   12    |            0 |  788.32 |
| Oct     | 700    |         65    |   68    |   98.23 |            0 |  931.23 |
| Nov     | 600    |         93    |   45    |   88    |            0 |  826    |
| Dec     | 500    |         92    |   78    |   45.7  |            0 |  715.7  |

If the user wants to delete a column, the program will ask for the name of the column in order to alow delete any besides of the last.
By selecting the option 0, the user go back to the main menu.

### Option 2: Incomes Table

Similar to the Home Accounts table, this editable section organizes all income sources by categories, making it easy to track **personal incomes**.

| Month   |   Salary |   Extra 1 |   Extra 2 |   Total |
|---------|----------|-----------|-----------|---------|
| Jan     |     3000 |         0 |         0 |    3000 |
| Feb     |     3000 |         0 |         0 |    3000 |
| Mar     |     3000 |        56 |       156 |    3212 |
| Apr     |     3000 |         0 |         0 |    3000 |
| May     |     3000 |         0 |         0 |    3000 |
| Jun     |     3000 |       900 |        12 |    3912 |
| Jul     |     3000 |        78 |         0 |    3078 |
| Aug     |     3000 |         0 |         0 |    3000 |
| Sep     |     3250 |       123 |         0 |    3373 |
| Oct     |     3250 |       145 |         0 |    3395 |
| Nov     |     3250 |       356 |         0 |    3606 |
| Dec     |     3250 |         0 |         0 |    3250 |

Options: 2) Insert/modify value 3) Add column 4) Delete column 0) Main menu

The options behavior is equal to the previous table since they are managed for the same internal class.

By selecting the option 0, the user go back to the main menu.

### Option 3: Variable Expenses Table

Unlike the first two tables, this section is structured vertically, accommodating a potentially large number of entries.
This format ensures better readability and usability for tracking irregular expenses.

In the first two tables, the user has the possibility of deleting an entry by replacing it with a 0, whereas in this case it is necessary to add another value but in negative, this was thought like this to keep the trace of all the entries.

| Month   |    Jan |    Feb |    Mar |    Apr |    May |    Jun |    Jul |   Aug |   Sep |   Oct |   Nov |   Dec |
|---------|--------|--------|--------|--------|--------|--------|--------|-------|-------|-------|-------|-------|
| 1       |  89    |  98    |  56    |   7    |  34.7  |  89.1  |  34    |    92 |   6.8 |  37.4 |     5 |    90 |
| 2       |  13.3  |  67.23 |   4.98 |  23    |  45.78 |  45    |  67.23 |     0 |   0   |   0   |    -5 |     0 |
| 3       |  89.12 |   9    |   6    |  78.45 |  98    |  67    |   6.7  |     0 |   0   |   0   |     0 |     0 |
| 4       |  10    |   6.98 |  12.5  | 347    |   7.99 |   7.24 |  98.25 |     0 |   0   |   0   |     0 |     0 |
| 5       | 167    |   5.99 | 155    |   9.1  |   7.99 |  78.98 |  45    |     0 |   0   |   0   |     0 |     0 |
| 6       |   0    |   3.5  |  43.25 |  12    |  12.5  |  34.6  |   0    |     0 |   0   |   0   |     0 |     0 |
| 7       |   0    |  12.2  |  89.12 |  12.5  |  23    |   0    |   0    |     0 |   0   |   0   |     0 |     0 |
| 8       |   0    |   0    |   0    |   0    |  12.5  |   0    |   0    |     0 |   0   |   0   |     0 |     0 |
| 9       |   0    |   0    |   0    |   0    |   0    |   0    |   0    |     0 |   0   |   0   |     0 |     0 |
| Total   | 368.42 | 202.9  | 366.85 | 489.05 | 242.46 | 321.92 | 251.18 |    92 |   6.8 |  37.4 |     0 |    90 |

Options: 1) Insert value 0) Main menu

In the following, we'll see how the program manage a typo when the user inserts the month:
Select an option: 2
Select month: jlu

Invalid month, try again!

The program handles the invalid inputs, prompting the user for another input until it gets it correct.
This kind of error handling is used in all the functions to ensure the correct performance of the program.

By selecting the option 0, the user go back to the main menu.

### Option 4: Monthly Balance

This feature summarizes the **user’s financial status** for a selected month. It’s designed to give an at-a-glance view of their income, expenses, and overall balance.

|Balance                              |
|-------------------------------------|
|Incomes: 3000.0                      |
 Home accounts: 901.67
 Variable expenses: 368.42
 Total: 1729.91
 Home accounts represent 30.06%
 Variable expenses represent 12.28%
 Total saving: 57.66%

By selecting the option 0, the user go back to the main menu.

### Option 5: Savings Projection

Based on the balance of a chosen month, this function helps users project their savings, allowing them to plan for future purchases, investments, and other financial goals.

|Select month: feb                  |
|-----------------------------------|
|Number of months for projection: 4 |

**Total saving in 4 months: 8102.16**

By selecting the option 0, the user go back to the main menu.

### Option 0: quit program

The user can exit the program by selecting option 0 in the main menu, and in order to give the user a nice greeting, a lovely cow says goodbye.

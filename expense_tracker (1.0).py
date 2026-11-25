"""
EXPENSE TRACKER  (Beginner-friendly version)
--------------------------------------------
Features:
  1. Add income / expense (amount, date, category, description)
  2. Edit and delete transactions
  3. View history, search and filter
  4. Total income, total expenses, balance
  5. Set budgets (overall monthly + per category) and see remaining budget
  6. Reports: daily, weekly, monthly
  7. Charts (matplotlib if installed, otherwise text bars)

Data is saved in a file called  expense_data.json  so nothing is lost
when the program closes.
"""

import json
import os
from datetime import datetime, timedelta

FILE_NAME = "expense_data.json"

CATEGORIES = ["Food", "Transportation", "Shopping", "Bills",
              "Entertainment", "Education", "Healthcare", "Other"]

# These two variables hold all our data while the program runs
transactions = []   # list of dictionaries, one per transaction
budgets = {}        # e.g. {"Total": 30000, "Food": 6000}


# ---------------------------------------------------------------
# PART 1: SAVING AND LOADING DATA
# ---------------------------------------------------------------
def load_data():
    """Read saved data from the file (if it exists)."""
    global transactions, budgets
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
        transactions = data["transactions"]
        budgets = data["budgets"]


def save_data():
    """Write our data to the file."""
    data = {"transactions": transactions, "budgets": budgets}
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------------------------------
# PART 2: HELPER FUNCTIONS (safe input)
# ---------------------------------------------------------------
def get_amount(message="Enter amount (Rs.): "):
    """Keep asking until the user types a valid positive number."""
    while True:
        try:
            amount = float(input(message))
            if amount > 0:
                return amount
            print("  Amount must be greater than 0.")
        except ValueError:
            print("  Please enter a number.")


def get_date(message="Enter date (YYYY-MM-DD) or press Enter for today: "):
    """Keep asking until the user types a valid date."""
    while True:
        text = input(message).strip()
        if text == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")   # checks the format
            return text
        except ValueError:
            print("  Wrong format. Example: 2026-11-24")


def choose_category():
    """Show the category list and let the user pick one."""
    print("\nCategories:")
    for number, name in enumerate(CATEGORIES, start=1):
        print(f"  {number}. {name}")
    while True:
        choice = input("Choose category number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("  Invalid choice, try again.")


def new_id():
    """Give each transaction a unique number."""
    if len(transactions) == 0:
        return 1
    return max(t["id"] for t in transactions) + 1


def print_table(rows):
    """Print a list of transactions as a neat table."""
    if len(rows) == 0:
        print("\n  No transactions found.")
        return
    print(f"\n{'ID':<4} {'Date':<11} {'Type':<8} {'Category':<15} {'Amount':>10}  Description")
    print("-" * 70)
    for t in rows:
        print(f"{t['id']:<4} {t['date']:<11} {t['type']:<8} {t['category']:<15} "
              f"{t['amount']:>10.2f}  {t['description']}")


# ---------------------------------------------------------------
# PART 3: ADD / EDIT / DELETE / VIEW
# ---------------------------------------------------------------
def add_transaction(kind):
    """kind is either 'Income' or 'Expense'."""
    print(f"\n--- Add {kind} ---")
    amount = get_amount()
    date = get_date()
    if kind == "Income":
        category = "Income"
    else:
        category = choose_category()
    description = input("Description: ")

    transaction = {
        "id": new_id(),
        "type": kind,
        "amount": amount,
        "date": date,
        "category": category,
        "description": description,
    }
    transactions.append(transaction)
    save_data()
    print(f"  {kind} added successfully!")

    if kind == "Expense":
        check_budget_warning(category, date)


def view_history():
    print("\n--- All Transactions ---")
    print_table(sorted(transactions, key=lambda t: t["date"]))


def find_by_id(tid):
    for t in transactions:
        if t["id"] == tid:
            return t
    return None


def edit_transaction():
    view_history()
    if len(transactions) == 0:
        return
    tid = input("\nEnter the ID to edit: ")
    if not tid.isdigit() or find_by_id(int(tid)) is None:
        print("  ID not found.")
        return
    t = find_by_id(int(tid))
    print("Press Enter to keep the old value.")

    new_amount = input(f"Amount [{t['amount']}]: ")
    if new_amount != "":
        try:
            t["amount"] = float(new_amount)
        except ValueError:
            print("  Invalid number, amount not changed.")

    new_date = input(f"Date [{t['date']}]: ")
    if new_date != "":
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            t["date"] = new_date
        except ValueError:
            print("  Invalid date, date not changed.")

    new_desc = input(f"Description [{t['description']}]: ")
    if new_desc != "":
        t["description"] = new_desc

    if t["type"] == "Expense":
        if input("Change category? (y/n): ").lower() == "y":
            t["category"] = choose_category()

    save_data()
    print("  Transaction updated!")


def delete_transaction():
    view_history()
    if len(transactions) == 0:
        return
    tid = input("\nEnter the ID to delete: ")
    if not tid.isdigit() or find_by_id(int(tid)) is None:
        print("  ID not found.")
        return
    t = find_by_id(int(tid))
    if input("Are you sure? (y/n): ").lower() == "y":
        transactions.remove(t)
        save_data()
        print("  Transaction deleted.")


# ---------------------------------------------------------------
# PART 4: SEARCH AND FILTER
# ---------------------------------------------------------------
def search_transactions():
    print("\n--- Search / Filter ---")
    print("1. By category")
    print("2. By date")
    print("3. By amount range")
    print("4. By keyword in description")
    choice = input("Choose: ")

    if choice == "1":
        category = choose_category()
        result = [t for t in transactions if t["category"] == category]
    elif choice == "2":
        date = get_date("Enter date (YYYY-MM-DD): ")
        result = [t for t in transactions if t["date"] == date]
    elif choice == "3":
        low = get_amount("Minimum amount: ")
        high = get_amount("Maximum amount: ")
        result = [t for t in transactions if low <= t["amount"] <= high]
    elif choice == "4":
        word = input("Keyword: ").lower()
        result = [t for t in transactions if word in t["description"].lower()]
    else:
        print("  Invalid choice.")
        return
    print_table(result)


# ---------------------------------------------------------------
# PART 5: BALANCE AND TOTALS
# ---------------------------------------------------------------
def calculate_totals(rows):
    """Return (total_income, total_expense, balance) for a list of transactions."""
    income = sum(t["amount"] for t in rows if t["type"] == "Income")
    expense = sum(t["amount"] for t in rows if t["type"] == "Expense")
    return income, expense, income - expense


def show_balance():
    income, expense, balance = calculate_totals(transactions)
    print("\n--- Balance Summary ---")
    print(f"  Total Income     : Rs. {income:.2f}")
    print(f"  Total Expenses   : Rs. {expense:.2f}")
    print(f"  Remaining Balance: Rs. {balance:.2f}")


def spending_by_category(rows):
    """Return a dictionary like {'Food': 6000, 'Bills': 7000}."""
    result = {}
    for t in rows:
        if t["type"] == "Expense":
            cat = t["category"]
            result[cat] = result.get(cat, 0) + t["amount"]
    return result


# ---------------------------------------------------------------
# PART 6: BUDGETS
# ---------------------------------------------------------------
def set_budget():
    print("\n--- Set Budget (monthly limit) ---")
    print("1. Overall monthly budget")
    print("2. Category budget")
    choice = input("Choose: ")
    if choice == "1":
        budgets["Total"] = get_amount("Monthly budget (Rs.): ")
    elif choice == "2":
        category = choose_category()
        budgets[category] = get_amount(f"Monthly budget for {category} (Rs.): ")
    else:
        print("  Invalid choice.")
        return
    save_data()
    print("  Budget saved!")


def month_rows(month):
    """All transactions whose date starts with 'YYYY-MM'."""
    return [t for t in transactions if t["date"].startswith(month)]


def view_budget():
    month = datetime.now().strftime("%Y-%m")
    rows = month_rows(month)
    spent = spending_by_category(rows)
    total_spent = sum(spent.values())

    print(f"\n--- Budget Status for {month} ---")
    if len(budgets) == 0:
        print("  No budgets set yet. Use 'Set budget' first.")
        return

    for name, limit in budgets.items():
        used = total_spent if name == "Total" else spent.get(name, 0)
        remaining = limit - used
        status = "OK" if remaining >= 0 else "OVER BUDGET!"
        print(f"  {name:<15} Limit: {limit:>9.2f}  Spent: {used:>9.2f}  "
              f"Left: {remaining:>9.2f}  {status}")


def check_budget_warning(category, date):
    """After adding an expense, warn the user if a budget is crossed."""
    rows = month_rows(date[:7])
    spent = spending_by_category(rows)
    if category in budgets and spent.get(category, 0) > budgets[category]:
        print(f"  WARNING: You crossed your {category} budget!")
    if "Total" in budgets and sum(spent.values()) > budgets["Total"]:
        print("  WARNING: You crossed your overall monthly budget!")


# ---------------------------------------------------------------
# PART 7: REPORTS
# ---------------------------------------------------------------
def print_report(title, rows):
    income, expense, balance = calculate_totals(rows)
    print(f"\n===== {title} =====")
    print(f"  Income  : Rs. {income:.2f}")
    print(f"  Expenses: Rs. {expense:.2f}")
    print(f"  Balance : Rs. {balance:.2f}")
    spent = spending_by_category(rows)
    if spent:
        print("  Expenses by category:")
        for cat, amount in spent.items():
            print(f"    {cat:<15} Rs. {amount:.2f}")


def generate_report():
    print("\n--- Reports ---")
    print("1. Daily")
    print("2. Weekly (last 7 days)")
    print("3. Monthly")
    choice = input("Choose: ")

    if choice == "1":
        date = get_date("Enter date (YYYY-MM-DD) or press Enter for today: ")
        rows = [t for t in transactions if t["date"] == date]
        print_report(f"Daily Report: {date}", rows)
    elif choice == "2":
        today = datetime.now()
        start = (today - timedelta(days=6)).strftime("%Y-%m-%d")
        end = today.strftime("%Y-%m-%d")
        rows = [t for t in transactions if start <= t["date"] <= end]
        print_report(f"Weekly Report: {start} to {end}", rows)
    elif choice == "3":
        month = input("Enter month (YYYY-MM) or press Enter for this month: ").strip()
        if month == "":
            month = datetime.now().strftime("%Y-%m")
        print_report(f"Monthly Report: {month}", month_rows(month))
    else:
        print("  Invalid choice.")


# ---------------------------------------------------------------
# PART 8: CHARTS
# ---------------------------------------------------------------
def show_chart():
    spent = spending_by_category(transactions)
    if len(spent) == 0:
        print("\n  No expenses to show yet.")
        return

    # Always show a simple text chart (works everywhere)
    print("\n--- Spending by Category (text chart) ---")
    total = sum(spent.values())
    for cat, amount in spent.items():
        bar = "#" * int(amount / total * 40)
        print(f"  {cat:<15} {bar} Rs. {amount:.0f} ({amount / total * 100:.1f}%)")

    # Try a real chart if matplotlib is installed
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n  (Install matplotlib with 'pip install matplotlib' for graphs.)")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    ax1.pie(spent.values(), labels=spent.keys(), autopct="%1.1f%%")
    ax1.set_title("Expenses by Category")
    ax2.bar(spent.keys(), spent.values(), color="steelblue")
    ax2.set_title("Amount Spent per Category (Rs.)")
    ax2.tick_params(axis="x", rotation=45)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------
# PART 9: MAIN MENU
# ---------------------------------------------------------------
def show_menu():
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print(" 1. Add income")
    print(" 2. Add expense")
    print(" 3. View transaction history")
    print(" 4. Edit a transaction")
    print(" 5. Delete a transaction")
    print(" 6. Search / filter")
    print(" 7. Show balance")
    print(" 8. Set budget")
    print(" 9. View budget status")
    print("10. Reports (daily/weekly/monthly)")
    print("11. Charts")
    print(" 0. Exit")


def main():
    load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_transaction("Income")
        elif choice == "2":
            add_transaction("Expense")
        elif choice == "3":
            view_history()
        elif choice == "4":
            edit_transaction()
        elif choice == "5":
            delete_transaction()
        elif choice == "6":
            search_transactions()
        elif choice == "7":
            show_balance()
        elif choice == "8":
            set_budget()
        elif choice == "9":
            view_budget()
        elif choice == "10":
            generate_report()
        elif choice == "11":
            show_chart()
        elif choice == "0":
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("  Invalid choice, please try again.")


# This line makes the program start when you run the file
if __name__ == "__main__":
    main()

💰 Expense Tracker – Personal Finance Management System

A Python-based Expense Tracker application that helps users record, manage, monitor, and analyze their daily income and expenses. It provides budget management, transaction history, financial reports, and graphical representations of spending patterns.

📌 Project Overview

Managing personal finances manually can be difficult and time-consuming. People often spend money on different categories but fail to maintain accurate records.

The Expense Tracker is designed to simplify personal financial management by allowing users to record income and expenses, organize transactions into categories, calculate their remaining balance, set monthly budgets, and generate financial reports.

The application uses Python and JSON file handling to store transaction data permanently.

✨ Key Features

- Add Income: Record income with amount, date, and description.
- Add Expenses: Record expenses with amount, date, category, and description.
- Edit Transactions: Update previously recorded transactions.
- Delete Transactions: Remove unwanted transactions.
- Transaction History: View all recorded financial transactions.
- Search and Filter: Search transactions by category, date, amount range, and description keyword.
- Balance Summary: Automatically calculate total income, total expenses, and remaining balance.
- Budget Management: Set overall monthly and category-wise budgets.
- Budget Monitoring: Check remaining budgets and receive warnings when spending limits are exceeded.
- Financial Reports: Generate daily, weekly, and monthly reports.
- Expense Charts: Display spending patterns using text-based charts and optional graphical charts.

🛠️ Technologies Used

- Programming Language: Python
- Data Storage: JSON
- Modules: "json", "os", "datetime", "timedelta"
- Optional Library: Matplotlib (for graphical charts)
- Code Editor: Visual Studio Code
- Version Control: Git and GitHub

📂 Project Structure

Expense-Tracker/
│
├── expense_tracker.py
├── expense_data.json
├── README.md
└── .gitignore

Note: "expense_data.json" is automatically created when the application saves data for the first time.

⚙️ Requirements

- Python 3.8 or later
- Visual Studio Code or any Python-supported editor
- No external package installation is required for the basic application.
- Matplotlib is optional for graphical charts.

▶️ How to Run the Project

Step 1: Clone the Repository

git clone YOUR_REPOSITORY_URL

Step 2: Open the Project Folder

Open the downloaded project folder in Visual Studio Code.

Step 3: Run the Python Program

python expense_tracker.py

Step 4: Select an Option

Choose an option from the menu to manage your income, expenses, budgets, reports, and charts.

📋 Application Menu

========================================
             EXPENSE TRACKER
========================================
1. Add income
2. Add expense
3. View transaction history
4. Edit a transaction
5. Delete a transaction
6. Search / filter
7. Show balance
8. Set budget
9. View budget status
10. Reports (daily/weekly/monthly)
11. Charts
0. Exit

📊 Example Calculation

Suppose a user has the following financial details:

Description| Amount
Monthly Income| ₹40,000
Food| ₹6,000
Transportation| ₹3,000
Shopping| ₹5,000
Bills| ₹7,000
Entertainment| ₹2,000
Total Expenses| ₹23,000
Remaining Balance| ₹17,000

Formula:

Remaining Balance = Total Income − Total Expenses

💾 Data Storage

The project uses Python's built-in JSON module to store transaction and budget information in "expense_data.json".

- Existing data is loaded when the program starts.
- New transactions are saved automatically.
- Updated and deleted transactions are reflected in the saved file.
- Data remains available after closing and reopening the application.

🧠 Python Concepts Demonstrated

- Variables and data types
- Conditional statements ("if", "elif", "else")
- Loops ("for" and "while")
- Lists and dictionaries
- Functions and return values
- Lambda functions
- List comprehensions
- Sorting and filtering
- Exception handling ("try", "except")
- File handling
- JSON data processing
- Date and time operations

🚀 Future Improvements

- Develop a graphical user interface (GUI).
- Add user login and authentication.
- Export financial reports to PDF and Excel.
- Add more advanced financial charts.
- Improve budget analysis and notifications.
- Introduce permanent database storage.

🎯 Project Objectives

1. Maintain an accurate record of income and expenses.
2. Organize expenses into different categories.
3. Monitor monthly spending habits.
4. Calculate available balance automatically.
5. Set and monitor spending budgets.
6. Generate financial reports.
7. Improve financial awareness and budgeting decisions.

👨‍💻 Author

Name: Your Name

Course: Bachelor of Computer Applications (BCA)

Semester: Your Semester

Institution: Your University

GitHub: Your GitHub Profile URL

---

⭐ If you find this project useful, consider giving the repository a star!

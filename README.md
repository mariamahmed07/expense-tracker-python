# 💰 Expense Tracker

A simple command-line expense tracker built with Python. It helps users record daily expenses, organize spending by category, manage a budget, and save their data locally using JSON.

## ✨ Features

- **Add Expenses:** Record an amount, category, and optional description.
- **View Transactions:** Display all recorded expenses with dates and details.
- **Budget Management:** Set or update a budget in EGP.
- **Budget Summary:** View total spending, remaining budget, and budget usage percentage.
- **Category Breakdown:** Calculate spending totals for each category.
- **Persistent Storage:** Save and reload data using a JSON file.
- **Input Validation:** Reject invalid amounts, negative expenses, and empty categories.
- **Automated Tests:** Test calculations, validation, and data persistence.

## 🛠️ Technologies

- Python 3
- JSON
- `unittest`
- Standard Python libraries

## 📂 Project Structure

```text
expense-tracker-python/
├── main.py
├── test_expense_tracker.py
├── expenses.json       # Generated when data is saved
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mariamahmed07/expense-tracker-python.git
cd expense-tracker-python
```

### 2. Run the application

Make sure Python 3 is installed, then run:

```bash
python main.py
```

### 3. Run the automated tests

```bash
python -m unittest -v test_expense_tracker.py
```

## 📖 How to Use

1. Choose an option from the main menu.
2. Set your budget.
3. Add expenses with an amount and category, such as Food, Transport, or Study.
4. View all transactions or check the budget summary.
5. Review spending totals by category.
6. Exit the application; saved data will be stored in `expenses.json`.

## 🧪 Testing

The test suite covers:

- Adding expenses
- Rejecting negative expenses
- Rejecting empty categories
- Calculating total spending
- Calculating category totals
- Calculating the remaining budget
- Rejecting negative budgets
- Saving and loading data
- Handling a missing data file

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Functions and modular programming
- Lists and dictionaries
- Input validation and exception handling
- File handling and JSON serialization
- Aggregation and basic financial calculations
- Automated testing with `unittest`

## 🔮 Future Improvements

- Edit and delete expenses
- Filter transactions by date
- Monthly reports
- Export transactions to CSV
- Add a graphical user interface
- Create charts to visualize spending

## ⚠️ Notes

This is an educational project. Data is stored locally in a JSON file and is not synchronized or backed up automatically. Avoid storing sensitive financial information in shared repositories.

## 👩‍💻 Author

**Mariam Ahmed**

- GitHub: [@mariamahmed07](https://github.com/mariamahmed07)

---

*Built as part of the 30 Projects in 30 Days challenge.*

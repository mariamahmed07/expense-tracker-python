
import unittest
import os
import tempfile

from main import (
    add_expense,
    set_budget,
    get_total_expenses,
    get_category_totals,
    get_remaining_budget,
    save_data,
    load_data,
)


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.data = {
            "budget": 300.0,
            "expenses": []
        }

    def test_add_expense(self):
        add_expense(self.data, 40, "Food", "Breakfast")
        self.assertEqual(len(self.data["expenses"]), 1)
        self.assertEqual(self.data["expenses"][0]["amount"], 40.0)

    def test_reject_negative_expense(self):
        with self.assertRaises(ValueError):
            add_expense(self.data, -10, "Food")

    def test_reject_empty_category(self):
        with self.assertRaises(ValueError):
            add_expense(self.data, 20, "  ")

    def test_total_expenses(self):
        add_expense(self.data, 40, "Food")
        add_expense(self.data, 15, "Transport")
        self.assertEqual(get_total_expenses(self.data), 55.0)

    def test_category_totals(self):
        add_expense(self.data, 40, "Food")
        add_expense(self.data, 20, "Food")
        add_expense(self.data, 15, "Transport")

        totals = get_category_totals(self.data)

        self.assertEqual(totals["Food"], 60.0)
        self.assertEqual(totals["Transport"], 15.0)

    def test_remaining_budget(self):
        add_expense(self.data, 75, "Study")
        self.assertEqual(get_remaining_budget(self.data), 225.0)

    def test_reject_negative_budget(self):
        with self.assertRaises(ValueError):
            set_budget(self.data, -100)

    def test_save_and_load_data(self):
        add_expense(self.data, 35, "Food", "Lunch")

        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "test_expenses.json")

            save_data(self.data, file_path)
            loaded_data = load_data(file_path)

        self.assertEqual(loaded_data["budget"], 300.0)
        self.assertEqual(len(loaded_data["expenses"]), 1)
        self.assertEqual(
            loaded_data["expenses"][0]["category"],
            "Food"
        )

    def test_empty_file_path_returns_default_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = os.path.join(temp_dir, "missing.json")
            loaded_data = load_data(file_path)

        self.assertEqual(loaded_data["budget"], 0.0)
        self.assertEqual(loaded_data["expenses"], [])


if __name__ == "__main__":
    unittest.main()

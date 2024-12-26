### README for Expense Tracker CLI Application

---

## Expense Tracker CLI Application

This application is a simple Command-Line Interface (CLI) tool to manage expenses. It allows users to add, list, delete, and summarize expenses in a JSON file. The application is implemented in Python and designed for personal financial tracking.

---

### Features

- **Add Expenses**: Record a new expense with details like description and amount.
- **List Expenses**: View all recorded expenses.
- **Delete Expenses**: Remove an expense by its unique ID.
- **Summary**: Summarize expenses for analysis.

---

### Requirements

- **Python**: Version 3.7 or higher
- **Dependencies**: No additional dependencies; uses Python's standard library.

---

### Usage

Run the application from the command line using the following syntax:

```bash
python script.py <action> [arguments]
```

#### Actions and Arguments

1. **`add`**  
   Add a new expense. Requires `--description` and `--amount` arguments.

   ```bash
   python script.py add --description "Lunch" --amount 15
   ```

   Example Output:

   ```
   Expense added successfully ID: <unique-id>
   ```

2. **`list`**  
   Display all recorded expenses.

   ```bash
   python script.py list
   ```

   Example Output:

   ```
   [
     {
       "id": "123e4567-e89b-12d3-a456-426614174000",
       "created_at": "2024-12-26",
       "description": "Lunch",
       "amount": 15
     }
   ]
   ```

3. **`delete`**  
   Remove an expense by its unique ID.

   ```bash
   python script.py delete <expense-id>
   ```

4. **`summary`**  
   Display a summary of expenses (e.g., total, average).
   ```bash
   python script.py summary
   ```

---

### Files

- **`expenses.json`**  
  Stores all expense data in JSON format. It is automatically created in the working directory if it doesn't exist.

---

### Error Handling

- Invalid or missing fields trigger descriptive error messages.
- Actions not permitted will prompt a valid list of options.

---

### Developer Notes

The following improvements are suggested for future versions:

- Implement the `list`, `delete`, and `summary` actions.
- Add data validation for non-empty descriptions.
- Enhance the summary functionality with filtering options (e.g., by date or category).

---

### License

This application is open-source and available under the MIT License.

---

### Contribution

Feel free to contribute by submitting a pull request or raising issues on the repository.

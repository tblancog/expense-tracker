### README for Expense Tracker CLI Application

---

## Expense Tracker CLI Application

This application is a simple Command-Line Interface (CLI) tool to manage expenses. It allows users to add, list, delete, and summarize expenses stored in a JSON file. The application is implemented in Python and designed for personal financial tracking.

---

### Features

- **Add Expenses**: Record a new expense with details like description and amount.
- **List Expenses**: View all recorded expenses in a tabular format.
- **Delete Expenses**: Remove an expense by its unique ID.
- **Summary**: Summarize expenses for a specified month (e.g., total expenses).

---

### Requirements

- **Python**: Version 3.7 or higher.
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
   Display all recorded expenses in a tabular format.

   ```bash
   python script.py list
   ```

   Example Output:

   ```
   # ID                Date                Description         Amount
   # 123e4567-e89b-12d3-a456-426614174000  2024-12-26          Lunch               $15
   ```

3. **`delete`**
   Remove an expense by its unique ID. Use `--id` to specify the expense ID.

   ```bash
   python script.py delete --id <expense-id>
   ```

   Example Output:

   ```
   Expense deleted: <expense-id>
   ```

4. **`summary`**
   Display a summary of expenses for a specific month (format: `YYYY-MM`). Requires `--date` argument.

   ```bash
   python script.py summary --date 2024-12
   ```

   Example Output:

   ```
   Total expenses: $45 for 2024-12
   ```

---

### Files

- **`expenses.json`**
  Stores all expense data in JSON format. It is automatically created in the working directory if it doesn't exist.

---

### Error Handling

- Invalid or missing fields trigger descriptive error messages.
- Invalid actions prompt a list of permitted options.
- Errors with argument types or missing arguments provide clear feedback.

---

### Developer Notes

The following improvements are suggested for future versions:

- **Enhance `add` validation**: Ensure descriptions are non-empty strings.
- **Extend `summary` functionality**: Add filtering options by category or range of dates.
- **Support for categories**: Allow tagging expenses with categories (e.g., Food, Travel).
- **Improved output formatting**: Make the tabular output cleaner and support alignment.
- **Unit Tests**: Add tests for individual functions and edge cases.
- **Refactor Code**: Modularize further for better maintainability.

---

### License

This application is open-source and available under the MIT License.

---

### Contribution

Feel free to contribute by submitting a pull request or raising issues on the repository.

---

### Code Example

Below is a snippet of how the main logic integrates actions:

```python
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough arguments provided")
        print("Usage: python script.py <action> [arguments]")
        sys.exit(1)

    action = sys.argv[1]
    if action not in PERMITTED_ACTIONS:
        print(f"Action not valid, should be one of: {', '.join(PERMITTED_ACTIONS)}")
        sys.exit(1)

    ACTIONS = {
        'add': add_action,
        'list': list_action,
        'delete': delete_action,
        'summary': summary_action,
    }

    try:
        ACTIONS[action](sys.argv)
    except Exception as e:
        print(f"Error: {e}")
```

### Project URL

https://roadmap.sh/projects/expense-tracker

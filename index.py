import sys
import uuid
import json
import os
from datetime import datetime

PERMITTED_ACTIONS = {
    'add', 'list', 'delete', 'summary'
  }
EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses_list):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(expenses_list, f, indent=2)

def check_field(field, value):
  permitted_fields = {
    '--description': str, '--amount': int
  }
  if field not in permitted_fields:
    raise Exception("Field not valid, should be either --description or --amount with correspondent value, example --description \"Lunch\"")
  if value is None:
    raise Exception("Value cannot be None")
  if field == '--amount':
     try:
       value = int(value)
     except ValueError:
       raise Exception("Amount should be a number")
     
  if not isinstance(value, permitted_fields[field]):
    raise Exception(f"Value for {field} must be of type {permitted_fields[field].__name__}")
  return value

def check_permitted_actions(action):
  if action not in PERMITTED_ACTIONS:
    raise Exception(f"Action not valid, should be one of:", "|".join(PERMITTED_ACTIONS))

def add_action(args):
  if len(args) < 4:
      print("Not enough arguments provided for \"add\" operation")
      return
  expense = {
    'id': str(uuid.uuid4()),
    'created_at': datetime.now().strftime("%Y-%m-%d")
  }
  for i in range(2, len(args)-1, 2):
    if args[i] is None and args[i+1] is None:
      print(f"Argument pair missing {args[i]} missing")
      return
    field = args[i]
    value = args[i+1]
    validated_value = check_field(field, value)
    expense[field[2:]] = validated_value

  # Load existing expenses
  expenses_list = load_expenses()
  
  # Add new expense to the list
  expenses_list.append(expense)
  
  # Save updated expenses list
  save_expenses(expenses_list)

  print(f"Expense added successfully ID: {expense['id']}")

  return

def list_action():
  expenses = load_expenses()
  if len(expenses) > 0:
    print(f"# ID                Date                Description         Amount")
    for expense in expenses:
      print(f"# {expense['id'][-6:]}            {expense['created_at']}          {expense['description']}              ${expense['amount']}")
  return
def delete_action():
  return
def summary_action():
  return


def main():
  if(len(sys.argv) < 2):
    print("Not enough arguments provided")
    print("Usage: python script.py <action> [arguments]")
    return
  
  current_action = sys.argv[1]
  check_permitted_actions(current_action)

  ACTIONS = {
    'add': add_action,
    'list': list_action,
    'delete': delete_action,
    'summary': summary_action,
  }

  # Triggerer
  ACTIONS[current_action](sys.argv)

if __name__ == '__main__':
  main()
import sys
import uuid
import json
import os
from datetime import datetime


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
  permitted_actions = {
    'add', 'list', 'delete', 'summary'
  }
  if action not in permitted_actions:
    raise Exception(f"Action not valid, should be one of:", "|".join(permitted_actions))


def main():
  if(len(sys.argv) < 2):
    print("Not enough arguments provided")
    print("Usage: python script.py <action> [arguments]")
    return
  
  action = sys.argv[1]
  check_permitted_actions(action)

  if action == 'add':
    if len(sys.argv) < 4:
      print("Not enough arguments provided for \"add\" operation")
      return
    
    expense = {
      'id': str(uuid.uuid4()),
      'created_at': datetime.now().strftime("%Y-%m-%d")
    }
    for i in range(2, len(sys.argv)-1, 2):
      if sys.argv[i] is None and sys.argv[i+1] is None:
        print(f"Argument pair missing {sys.argv[i]} missing")
        return
      field = sys.argv[i]
      value = sys.argv[i+1]
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
  if action == 'list':
    return
  if action == 'delete':
    return
  if action == 'summary':
    return



if __name__ == '__main__':
  main()
print("[DEBUG] tracker.py loaded ✅")

import json, os
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "expenses.json")

def load_data():
    print(f"[DEBUG] Loading from: {DATA_FILE}")
    if not os.path.exists(DATA_FILE):
        print("[DEBUG] File does not exist, creating new.")
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(DATA_FILE) as f:
            data = json.load(f)
            print(f"[DEBUG] Loaded data: {data}")
            return data
    except json.JSONDecodeError:
        print("[DEBUG] JSON decode error - returning empty list.")
        return []

def save_data(expenses):
    print(f"[DEBUG] Saving to: {DATA_FILE}")
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def handle_command(args):
    expenses = load_data()

    if args.command == "add":
        expense = {
            "id": len(expenses) + 1,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "description": args.description,
            "amount": args.amount
        }
        expenses.append(expense)
        save_data(expenses)
        print(f"Expense added successfully (ID: {expense['id']})")

    elif args.command == "list":
        if not expenses:
            print("# No expenses found.")
        else:
            print("# ID    Date        Description    Amount")
            for e in expenses:
                print(f"# {e['id']}    {e['date']}    {e['description']}    ${e['amount']}")
    
    elif args.command == "summary":
        if args.month:
            total = sum(e['amount'] for e in expenses if datetime.strptime(e['date'], "%Y-%m-%d").month == args.month)
            print(f"# Total expenses for {datetime(1900, args.month, 1).strftime('%B')}: ${total}")
        else:
            total = sum(e['amount'] for e in expenses)
            print(f"# Total expenses: ${total}")
    
    elif args.command == "delete":
        expenses = [e for e in expenses if e['id'] != args.id]
        save_data(expenses)
        print(f"# Expense deleted successfully.")
    
    elif args.command == "update":
        for e in expenses:
            if e['id'] == args.id:
                if args.description:
                    e['description'] = args.description
                if args.amount:
                    e['amount'] = args.amount
                print(f"# Expense updated successfully.")
        save_data(expenses)